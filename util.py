#pip install numpy
#pip install scikit-learn==0.22.2.post1
#pip install pickle
#pip install jsonlib

import datetime
import pickle
import json
import numpy as np

_data_columns, _model = None, None


def avail_period(avail_date):
  if avail_date in ['Ready To Move', 'Immediate Possession']:
    return 0
  year = 2000 + int(avail_date.split(sep='-')[0])
  month = avail_date.split(sep='-')[1]
  months = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun', 'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
  
  end_date = datetime.datetime(year, months.index(month) + 1, 1)
  start_date = datetime.datetime(2014, 1, 1)

  num_months = (end_date.year - start_date.year) * 12 + (end_date.month - start_date.month)
  return num_months

def predict_price(area_type,availability,location,size,society,sqft,bath,balcony):
  
  mod_area_type = area_type[:-5]+ '  Area'
  loc_1 = _data_columns.index(mod_area_type)
  loc_2 = _data_columns.index(location)
    
  x = np.zeros(len(_data_columns))
  
  x[0] = avail_period(availability)
  x[1] = size.split()[0]
  x[2] = sqft
  x[3] = bath
  x[4] = balcony
  
  x[loc_1] = 1 
  x[loc_2] = 1

  return _model.predict([x])[0]
    
def load_artifacts():
    print("Loading Artifacts info.....")
    global _data_columns, _model

    with open("./columns.json",'r') as f:
        _data_columns = json.load(f)['data_columns']

    if _model is None:
        with open('./Bengaluru_Housing_Price_Predictor.pickle','rb') as f:
            _model = pickle.load(f)

def get_data_columns():
    return _data_columns

load_artifacts()
print(get_data_columns())
#print(predict_price('Super built-up  Area', '19-Dec', 'Electronic City Phase II', '2 BHK', 'Coomee', 1056, 2.0, 1.0))

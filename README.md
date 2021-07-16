# Housing price predictor Web App
This project involves developing a Linear regression model for the given *Bengaluru housing price dataset* (Link to the dataset: https://www.kaggle.com/amitabhajoy/bengaluru-house-price-data). The model is further saved as a .pickle file and deployed as a web app using Flask. HTML and CSS were used for web development tasks.

**_Tech Stack: Python, Linear Regress, Pandas, Scikit-learn, Flask, HTML, CSS._**

## File Description
* *app* : This folder contains files needed for web development.
  * *app.css*: CSS code to design webpage.
  * *app.html*: HTML code for developing webpage.
  * *house_bg.jpg*: background image for the webapge. 
* *Bengaluru Housing Price Data Processed.csv*: Dataset obtained after pre-processing stage.
* *Bengaluru Housing Price Data.csv*: Dataset in CSV format.
* *Bengaluru_Housing_Price_Predictor.pickle*: Model saved as .pickle file.
* *Group2_Mishael,Saurav.ipynb*: This notbook contains the model developed, trained and tested using [Google Colab](https://colab.research.google.com).
* *columns.json*: Column names in dataset in JSON format.
* *server.py*: This python file contains the code to set up a local server using Flask.
* *util.py*: This python file utilizes the model and predicts the housing price.

## Results

Algorithm | Training Data Score (%) | Testing Data Score (%)
---------------|-------------------------|-----------------------
Linear Regression | 80.599 | 82.353
Random Forest | 84.982 | 77.995
Decision Tree | 83.756 | 77.356

## Webpage

![Webapp](/Web_App.jpg)

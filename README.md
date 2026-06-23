# 🚗 Car MPG Prediction Using Multiple Linear Regression

## 📌 Project Overview

This project predicts a car's **Miles Per Gallon (MPG)** using a **Multiple Linear Regression (MLR)** model. The model takes four input features:

* Horse Power (HP)
* Volume (VOL)
* Speed (SP)
* Weight (WT)

  The application is built using Python, Scikit-learn, and Streamlit, and is deployed as an interactive web application.

🔗 Live Demo

Streamlit App:https://carsmpgprediction-mh7d2pnzodqytrap2ngyqs.streamlit.app/

The application is built using **Python**, **Scikit-learn**, and **Streamlit**, and is deployed as an interactive web application.

---

## 🎯 Objective

To build a machine learning model that predicts a car's fuel efficiency (MPG) based on its specifications and provide predictions through a user-friendly web interface.

---

## 📂 Dataset Features

| Feature | Description                        |
| ------- | ---------------------------------- |
| HP      | Horse Power of the car             |
| VOL     | Engine Volume                      |
| SP      | Speed of the car                   |
| WT      | Weight of the car                  |
| MPG     | Miles Per Gallon (Target Variable) |

---

## 🛠️ Technologies Used

* Python
* Pandas
* NumPy
* Scikit-learn
* Streamlit
* Pickle

---

## 🔍 Machine Learning Model

**Algorithm:** Multiple Linear Regression

The model learns the relationship between the independent variables:

X = [HP, VOL, SP, WT]

and predicts the dependent variable:

Y = MPG

---

## 🚀 Project Workflow

1. Load the dataset
2. Perform data preprocessing
3. Select input and output variables
4. Train the Multiple Linear Regression model
5. Save the trained model using Pickle
6. Build a Streamlit web application
7. Deploy the application online

---

## ▶️ How to Run the Project

### Clone the Repository

```bash
git clone https://github.com/your-username/cars_mpg_prediction.git
cd cars_mpg_prediction
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Run the Application

```bash
streamlit run app.py
```

---

## 📁 Project Structure

cars_mpg_prediction/
├── app.py
├── mlr.pkl
├── Cars.csv
├── requirements.txt
└── Car_MPG_Prediction.ipynb

---

## 💻 Application Features

* Accepts HP, VOL, SP, and WT as inputs
* Predicts the MPG of a car
* Simple and interactive web interface
* Deployed using Streamlit Cloud

---

## 📈 Future Enhancements

* Add data visualizations and charts
* Improve UI design
* Compare multiple machine learning algorithms
* Add model evaluation metrics such as R² Score, MAE, and MSE

---

## 👨‍💻 Author

**Balasubramani**
B.Tech – Information Technology
Passionate about Machine Learning, Data Analytics, and Software Development.

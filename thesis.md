# Integration of a Machine Learning Model with an Application

## Abstract

Machine Learning is widely used to make predictions and solve real-world problems. However, a machine learning model is not very useful to normal users unless it is connected to an application. This project focuses on integrating a trained ML model with a simple web application using Python and Streamlit.

## Introduction

In this project, the ML model is first trained using a dataset. The data is cleaned and prepared before training. After selecting and training the model, it is saved using Joblib. The saved model can then be loaded and used inside a Streamlit application.

## Method

The main steps are collecting the dataset, preprocessing the data, training the machine learning model, testing its performance, and saving the trained model using Joblib.

After training, the saved model is loaded into a Streamlit application. The application collects input from the user, performs the required preprocessing, and sends the input to the ML model. The model generates a prediction, which is displayed through the Streamlit interface.

**User Input → Streamlit Application → Preprocessing → ML Model → Prediction → Result**

## Technologies Used

* **Python** — main programming language
* **Pandas** — data processing
* **NumPy** — numerical operations
* **Scikit-learn** — machine learning
* **Joblib** — saving and loading the trained model
* **Streamlit** — web application
* **GitHub** — source-code management and sharing

## Result

The integrated application allows users to enter the required information and receive a prediction without directly working with Python code. This makes the machine learning model easier and more convenient to use.

## Conclusion

Integrating a machine learning model with an application is an important step in making ML solutions practical. Using Python and Streamlit, a trained model can be connected to a simple user interface and used easily by users. The complete project can be maintained, version-controlled, and shared through GitHub.

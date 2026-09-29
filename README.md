# 🏠 AI House Price Prediction

A Machine Learning project that predicts the **median house value of a housing area** using housing and geographic characteristics.

## 📌 Project Overview

The objective of this project is to build a complete Machine Learning pipeline, from data exploration to model deployment.

The project includes:

* Data exploration and visualization
* Feature analysis
* Train/test split
* Regression model comparison
* Hyperparameter tuning
* Model evaluation
* Model saving
* Interactive Streamlit application

## 🎯 Objectives

The main objectives are:

* Understand the characteristics of the dataset
* Identify relationships between features and house values
* Compare several regression algorithms
* Optimize the best-performing model
* Evaluate the final model on an independent test set
* Build an interactive application for predictions

## 📊 Dataset

The project uses the **California Housing dataset** provided by Scikit-learn.

The dataset contains **20,640 observations** and **8 input features**.

### Features

| Feature      | Description                 |
| ------------ | --------------------------- |
| `MedInc`     | Median income               |
| `HouseAge`   | Median house age            |
| `AveRooms`   | Average number of rooms     |
| `AveBedrms`  | Average number of bedrooms  |
| `Population` | Population of the area      |
| `AveOccup`   | Average household occupancy |
| `Latitude`   | Geographic latitude         |
| `Longitude`  | Geographic longitude        |

### Target

`MedHouseVal`

The target represents the **median house value of a housing area**, expressed in units of $100,000.

## 🔎 Exploratory Data Analysis

Several analyses were performed to understand the dataset:

* Dataset structure and data types
* Descriptive statistics
* Target distribution
* Feature-target relationships
* Correlation analysis
* Correlation heatmap
* Outlier analysis
* Geographic visualization

One important observation was the strong positive correlation between `MedInc` and `MedHouseVal`:

**Correlation ≈ 0.69**

Geographic features were also important because house values vary depending on location.

## 🤖 Models Tested

Several regression algorithms were compared:

1. Linear Regression
2. Random Forest Regressor
3. Gradient Boosting Regressor

The models were evaluated using:

* MAE
* RMSE
* R²

The methodology was:

> J'ai comparé plusieurs algorithmes de régression afin d'identifier celui qui généralisait le mieux sur les données de test.

## 📈 Model Comparison

| Model             |    MAE |   RMSE |     R² |
| ----------------- | -----: | -----: | -----: |
| Linear Regression | 0.5332 | 0.7456 | 0.5758 |
| Random Forest     | 0.3277 | 0.5060 | 0.8046 |
| Gradient Boosting | 0.3716 | 0.5422 | 0.7756 |

Random Forest achieved the strongest performance among the tested models.

## ⚙️ Model Optimization

Random Forest hyperparameters were optimized using `GridSearchCV`.

The optimized configuration was:

```text
n_estimators = 300
max_depth = 25
min_samples_split = 2
```

The final model was evaluated on a test set that was kept separate from the training and validation process.

### Final Test Results

| Metric | Result |
| ------ | -----: |
| MAE    | 0.3266 |
| RMSE   | 0.5041 |
| R²     | 0.8061 |

The final R² means that approximately **80.6% of the variance in the test target values** is explained by the model predictions.

The MAE corresponds to an average error of approximately **$32,700** in the target's original dollar scale.

## 🔄 Machine Learning Pipeline

```text
Dataset
   ↓
Data Exploration
   ↓
Feature Analysis
   ↓
Train / Test Split
   ↓
Model Training
   ↓
Model Comparison
   ↓
Hyperparameter Tuning
   ↓
Final Evaluation
   ↓
Model Saving
   ↓
Streamlit Application
```

## 🌐 Streamlit Application

An interactive web application was developed using **Streamlit**.

The user can enter:

* Median income
* House age
* Average rooms
* Average bedrooms
* Population
* Average occupancy
* Latitude
* Longitude

The application then uses the trained Random Forest model to generate a predicted median house value.

## 🏗️ Project Structure

```text
AI HOOUSE PREDICTION/
│
├── app/
│   └── app.py
│
├── models/
│   └── house_price_model.pkl
│
├── notebooks/
│   └── 01_exploration.ipynb
│
├── .venv/
│
├── README.md
└── test.py
```

## 🛠️ Technologies

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-learn
* Jupyter Notebook
* Streamlit
* Joblib
* Git / GitHub

## 🚀 How to Run

### 1. Clone the repository

```bash
git clone <YOUR_GITHUB_REPOSITORY_URL>
cd AI-HOUSE-PREDICTION
```

### 2. Create and activate the virtual environment

```bash
python -m venv .venv
```

Windows:

```bash
.venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

### 4. Run the Streamlit application

```bash
streamlit run app/app.py
```

The application will open in your browser.

## ⚠️ Limitations

This project uses the California Housing dataset.

Therefore:

* It is limited to California housing areas.
* The target represents the median value of a housing area, not the exact selling price of an individual house.
* The model should therefore be considered an educational Machine Learning project rather than a professional real-estate valuation system.

A future version could use a larger real-estate dataset containing individual properties, cities, surface area, number of bedrooms, bathrooms and other property-level information.

## 📚 What I Learned

Through this project, I practiced:

* Data cleaning and exploration
* Data visualization
* Correlation analysis
* Regression
* Train/test splitting
* Cross-validation
* Hyperparameter tuning
* Model evaluation
* Model persistence with Joblib
* Building a Machine Learni

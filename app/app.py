import streamlit as st
import joblib
import pandas as pd
from pathlib import Path

# ==========================================
# PAGE CONFIGURATION
# ==========================================

st.set_page_config(
    page_title="AI House Price Prediction",
    page_icon="🏠",
    layout="centered"
)

# ==========================================
# LOAD THE MODEL
# ==========================================

BASE_DIR = Path(__file__).resolve().parent.parent
model_path = BASE_DIR / "models" / "house_price_model.pkl"

model = joblib.load(model_path)

# ==========================================
# SIDEBAR
# ==========================================

with st.sidebar:

    st.header("📊 Project Information")

    st.write("**Dataset**")
    st.write("California Housing")

    st.write("**Model**")
    st.write("Random Forest Regressor")

    st.write("**Test R²**")
    st.write("0.806")

    st.write("**Test MAE**")
    st.write("0.327")

    st.divider()

    st.write("### ⚠️ Limitation")

    st.write(
        "The model predicts the median value of a "
        "housing area. It does not predict the exact "
        "selling price of an individual house."
    )

    st.divider()

    st.caption(
        "Machine Learning Portfolio Project"
    )

# ==========================================
# TITLE
# ==========================================

st.title("🏠 AI House Price Prediction")

st.write(
    "Enter the characteristics of a housing area "
    "to estimate its median house value."
)

st.info(
    "The model uses the California Housing dataset "
    "and a trained Random Forest Regressor."
)

# ==========================================
# INPUTS
# ==========================================

st.subheader("🏡 Housing Characteristics")

col1, col2 = st.columns(2)

with col1:

    med_inc = st.number_input(
        "Median Income (× $10,000)",
        min_value=0.5,
        max_value=15.0,
        value=3.5,
        help="Median household income in tens of thousands of dollars."
    )

    house_age = st.number_input(
        "House Age (years)",
        min_value=1.0,
        max_value=52.0,
        value=20.0,
        help="Median age of houses in the area."
    )

    ave_rooms = st.number_input(
        "Average Rooms",
        min_value=0.8,
        max_value=15.0,
        value=5.0,
        help="Average number of rooms per household."
    )

    ave_bedrms = st.number_input(
        "Average Bedrooms",
        min_value=0.3,
        max_value=10.0,
        value=1.0,
        help="Average number of bedrooms per household."
    )

with col2:

    population = st.number_input(
        "Population (people)",
        min_value=1.0,
        max_value=40000.0,
        value=1000.0,
        help="Total population of the area."
    )

    ave_occup = st.number_input(
        "Average Occupancy",
        min_value=0.5,
        max_value=20.0,
        value=3.0,
        help="Average number of people per household."
    )

    latitude = st.number_input(
        "Latitude",
        min_value=32.0,
        max_value=42.0,
        value=35.0,
        help="Geographic latitude of the area."
    )

    longitude = st.number_input(
        "Longitude",
        min_value=-125.0,
        max_value=-114.0,
        value=-119.0,
        help="Geographic longitude of the area."
    )

# ==========================================
# PREDICTION
# ==========================================

st.subheader("🔍 Prediction")

if st.button("Predict House Price", type="primary"):

    input_data = pd.DataFrame([{
        "MedInc": med_inc,
        "HouseAge": house_age,
        "AveRooms": ave_rooms,
        "AveBedrms": ave_bedrms,
        "Population": population,
        "AveOccup": ave_occup,
        "Latitude": latitude,
        "Longitude": longitude
    }])

    prediction = model.predict(input_data)[0]

    predicted_price = prediction * 100000

    st.success("Prediction completed!")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "Estimated Median Value",
            f"${predicted_price:,.0f}"
        )

    with col2:
        st.metric(
            "Value in $1000s",
            f"{prediction:.2f}"
        )

    st.caption(
        "Estimated median value for this housing area."
    )

    st.warning(
        "⚠️ This is an ML estimate, not the exact selling "
        "price of an individual house."
    )

# ==========================================
# ABOUT THE MODEL
# ==========================================

st.divider()

with st.expander("📊 About the Model"):

    st.write(
        "The application uses a Random Forest Regressor "
        "trained on the California Housing dataset."
    )

    st.write("**Model performance on the test set:**")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.metric("R²", "0.806")

    with col2:
        st.metric("MAE", "0.327")

    with col3:
        st.metric("RMSE", "0.504")

    st.write(
        "**R²:** approximately 80.6% of the variation "
        "in the target values is explained by the model."
    )

    st.write(
        "**MAE:** the average prediction error is "
        "approximately $32,700."
    )

    st.write(
        "**RMSE:** this metric gives more weight to "
        "larger prediction errors."
    )

    st.write(
        "The model was compared with Linear Regression "
        "and Gradient Boosting before selecting Random Forest."
    )
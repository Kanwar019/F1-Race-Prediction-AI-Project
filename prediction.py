import streamlit as st
import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.linear_model import Lasso  
from sklearn.metrics import mean_squared_error
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Load data
data_constructor = pd.read_csv(r'ConstructorPrediction.csv')
comparison_df    = pd.read_csv(r'regression_comparison.csv')

def predict_points(data):
    # --- Page-specific CSS styling ---
    st.markdown("""
    <style>
    .stContainer { background-color: rgba(0,0,0,0.6)!important; border-radius:10px; padding:20px; }
    table.dataframe { background-color: rgba(0,0,0,0.8)!important; color:white; border-radius:8px; }
    .note-box { background-color: rgba(0,0,0,0.8); border-radius:8px; padding:10px; margin:10px 0; color:white; }
    .stButton>button { background-color:#b30000; color:white; border-radius:8px; padding:8px 16px; }
    .stButton>button:hover { background-color:#900000; transform:scale(1.02); }
    </style>
    """, unsafe_allow_html=True)

    st.header('Prediction: F1 Driver Points for 2024 Season')

    # Prepare features & target
    X = data[['driverRating','carRating','constructorStrategy','2021_points','2022_points']]
    y = data['2024_points']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

    # Scale
    scaler = StandardScaler()
    X_train_s = scaler.fit_transform(X_train)
    X_test_s  = scaler.transform(X_test)
    X_all_s   = scaler.transform(X)

    # Train Lasso
    model = Lasso(alpha=0.1)
    model.fit(X_train_s, y_train)

    # Test MSE
    preds_test = model.predict(X_test_s)
    st.write(f"**MSE:** {mean_squared_error(y_test, preds_test):.2f}")

    # Predict for all drivers, round & clip >=0
    raw_preds = model.predict(X_all_s)
    rounded  = np.round(raw_preds)
    clipped  = np.clip(rounded, 0, None)
    data['predicted_2024_points'] = clipped.astype(int)
    data = data.sort_values('predicted_2024_points', ascending=False)

    # Display table
    df_html = data[['driverRef','2021_points','2022_points','2023_points','predicted_2024_points']] \
                .to_html(index=False, classes='dataframe', border=0)
    st.markdown(df_html, unsafe_allow_html=True)

    # Bar chart
    plt.figure(figsize=(10,4), facecolor='none')
    ax = plt.axes()
    ax.set_facecolor('none')
    bars = plt.bar(data['driverRef'], data['predicted_2024_points'], color='#b30000')
    plt.xlabel('Driver', color='white')
    plt.ylabel('Predicted 2024 Points', color='white')
    plt.title('Driver Predictions', color='white')
    plt.xticks(rotation=90, color='white')
    plt.yticks(color='white')
    for b in bars:
        plt.text(b.get_x()+0.1, b.get_height()+0.5, int(b.get_height()), color='white')
    plt.tight_layout()
    st.pyplot(plt)

    # Context image & notes
    st.image(
        "https://media-cldnry.s-nbcnews.com/image/upload/t_fit-1500w,f_auto,q_auto:best/rockcms/2022-10/221010-Max-Verstappen-ew-1132a-276412.jpg",
        use_container_width=True
    )
    st.markdown('<div class="note-box">Predicting sports isn’t always accurate—this uses Lasso on the last 3 seasons, driver & car ratings, and strategy.</div>',
                unsafe_allow_html=True)
    st.markdown('<div class="note-box">As it turned out, Verstappen won the championship!</div>',
                unsafe_allow_html=True)

    # Divider
    st.markdown('---')
    st.header('Prediction: F1 Constructor Points for 2024 Season')

    # Constructors table & chart
    df2_html = data_constructor[['Constructor','2021_Points','2022_Points','2023_Points','Predicted_2024_Points']] \
                 .to_html(index=False, classes='dataframe', border=0)
    st.markdown(df2_html, unsafe_allow_html=True)

    plt.figure(figsize=(10,4), facecolor='none')
    ax = plt.axes()
    ax.set_facecolor('none')
    bars2 = plt.bar(data_constructor['Constructor'], data_constructor['Predicted_2024_Points'], color='#b30000')
    plt.xlabel('Constructor', color='white')
    plt.ylabel('Predicted 2024 Points', color='white')
    plt.title('Constructor Predictions', color='white')
    plt.xticks(rotation=90, color='white')
    plt.yticks(color='white')
    for b in bars2:
        plt.text(b.get_x()+0.1, b.get_height()+0.5, int(b.get_height()), color='white')
    plt.tight_layout()
    st.pyplot(plt)

    st.image(
        "https://www.racefans.net/wp-content/uploads/2024/12/racefansdotnet-7728889_HiRes.jpg",
        use_container_width=True
    )
    st.markdown('<div class="note-box">This constructor data is based on driver predictions; AlphaTauri is now Racing Bulls.</div>',
                unsafe_allow_html=True)

    # Model comparison
    st.subheader('Why Linear Regression')
    comp_html = comparison_df[['Model','R2 Value']].to_html(index=False, classes='dataframe', border=0)
    st.markdown(comp_html, unsafe_allow_html=True)


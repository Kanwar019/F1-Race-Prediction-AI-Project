import streamlit as st
from analysis import analyze_pitstop_duration, lap_analysis
from prediction import predict_points
from visualization import tableau_viz
from constructor_analysis import constructor_analysis
from Historical import historical
from TrackInfo import tracks
import pandas as pd
from PIL import Image
from drivers_analysis import drivers
from yearanalysis import yearanalysis
from About import about
from references import references

# Load app icon and set page config
img = Image.open(r'formula1projectlogo.jfif')
st.set_page_config(page_title='Formula 1 AI Project', page_icon=img, layout="wide")

# === GLOBAL STYLES (background, font, tables) ===
st.markdown("""
    <style>
    /* Use a modern sans-serif everywhere */
    html, body, .stApp {
      font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
      background: url("https://www.wsupercars.com/wallpapers-regular/Formula-1/Scuderia-Ferrari/2025-Formula1-Ferrari-SF-25-001-2160.jpg") no-repeat center center fixed;
      background-size: cover;
    }
    /* Semi-transparent backdrop for panels */
    .stContainer, .stSidebar {
      background-color: rgba(0, 0, 0, 0.6) !important;
      border-radius: 10px;
      padding: 20px;
    }
    /* Headings */
    h1, .stHeader h1 {
      color: #e10600 !important;
      text-shadow: 1px 1px 2px #000;
    }
    h2, h3 {
      color: #fff !important;
    }
    /* Paragraph text */
    p, .stText, .track-info {
      color: #ddd !important;
    }
    /* Horizontal rules */
    hr {
      border-top: 1px solid #444;
    }
    /* Buttons (global) – darker red shades */
    .stButton>button {
      background-color: #8f1717;
      color: white;
      border-radius: 8px;
      padding: 8px 16px;
      font-size: 16px;
      transition: background-color 0.2s ease, transform 0.1s ease;
    }
    .stButton>button:hover {
      background-color: #900000;
      transform: scale(1.02);
    }
    /* LINKS */
    a {
      color: #ff6f61 !important;
      text-decoration: none !important;
    }
    a:hover {
      text-decoration: underline !important;
    }

    /* Darken HTML-generated tables */
    table.dataframe {
    background-color: rgba(0, 0, 0, 0.6) !important;  /* darker than 0.8 */
    color: white;
    border-radius: 8px;
    overflow: hidden;
}
    /* Darken native st.table / st.dataframe outputs */
    [data-testid="stTable"] table {
      background-color: rgba(0, 0, 0, 0.6) !important;
    }
    [data-testid="stTable"] th,
    [data-testid="stTable"] td {
      background-color: rgba(0, 0, 0, 0.6) !important;
      color: white !important;
    }

    /* Card for home page content */
    .home-card {
        background-color: rgba(0, 0, 0, 0.6);
        border-radius: 10px;
        padding: 30px;
        margin-bottom: 20px;
    }

    </style>
""", unsafe_allow_html=True)

# === SIDEBAR NAVIGATION ===
with st.sidebar:
    st.title("🏁 Navigation")
    about_button            = st.button('About F1')
    tracks_button           = st.button('Track Info')
    prediction_button       = st.button("Predict Points")
    drivers_button          = st.button("Drivers")
    analysis_button         = st.button("Pitstop & Lap Analysis")
    tableau_viz_button      = st.button('Tableau Dashboard')
    constructor_button      = st.button('Constructor Analysis')
    historical_button       = st.button('Historical Analysis')
    yearlyanalysis_button   = st.button('2023 Analysis')
    references_button       = st.button('References')

button_clicked = False
data = pd.read_csv(r'DriverPrediction.csv')

# === PAGE LOGIC ===
if analysis_button:
    button_clicked = True
    st.button("← Home")
    analyze_pitstop_duration()
    lap_analysis()

elif tracks_button:
    button_clicked = True
    st.button("← Home")
    tracks()

elif prediction_button:
    button_clicked = True
    st.button("← Home")
    predict_points(data)

elif tableau_viz_button:
    button_clicked = True
    st.button("← Home")
    tableau_viz()

elif constructor_button:
    button_clicked = True
    st.button("← Home")
    constructor_analysis()

elif historical_button:
    button_clicked = True
    st.button("← Home")
    historical()

elif drivers_button:
    button_clicked = True
    st.button("← Home")
    drivers()

elif yearlyanalysis_button:
    button_clicked = True
    st.button("← Home")
    yearanalysis()

elif about_button:
    button_clicked = True
    st.button("← Home")
    about()

elif references_button:
    button_clicked = True
    st.button("← Home")
    references()

# === HOME SCREEN ===
if not button_clicked:
    st.header("🏎️ F1 Analysis and Predictions 🏎️")

    # Home page wrapped in a card
    st.markdown(""" 
                    <div class="home-card">
        <h2>Welcome to the F1 AI Project!</h2>
        <p>Dive into pit-stop times, lap analyses, driver stats, constructor trends, and predictive models—all in one place.</p>
        <hr style='border: 0; border-top: 1px solid #555; margin: 20px 0;' />
        <h3 style='color: #e10600;'>Submitted by –</h3>
        <ul style='color: #ccc; font-size: 16px;'>
            <li><strong>102317209</strong> – Mayank Bajaj</li>
            <li><strong>102317223</strong> – Kanwarajaybir Singh</li>
            <li><strong>102317226</strong> – Advait Gautam</li>
        </ul>
    </div>
    """, unsafe_allow_html=True)

    
    st.markdown("---")

    # Home page buttons
    col1, col2, col3 = st.columns(3)
    with col1:
        latest_news = st.button("Latest News")
    with col2:
        show_drivers = st.button("Driver Standings")
    with col3:
        show_teams = st.button("Team Standings")

    # Conditionally display sections
    if latest_news:
        st.subheader("📢 Latest News")

        # Provide a link to the Formula 1 latest news webpage
        st.markdown("""
        <div class="home-card">
            <p>Stay up-to-date with the very latest from the paddock on <a href="https://www.formula1.com/en/latest/all" target="_blank">Formula 1 Latest News</a>.</p>
        </div>
        """, unsafe_allow_html=True)

    if show_drivers:
        st.subheader("🏆 Driver Standings")
        standings_df = pd.read_csv(r'CurrentStanding.csv')
        st.table(standings_df[['Position','Driver','Points']])

    if show_teams:
        st.subheader("🏁 Team Standings")
        standings_df2 = pd.read_csv(r'CurrentStanding2.csv')
        st.table(standings_df2[['Position','Constructor','Points']])

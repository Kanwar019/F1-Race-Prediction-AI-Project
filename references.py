import streamlit as st

def references():
    # CSS styling for cards
    st.markdown("""
        <style>
            .info-card {
                background-color: rgba(0, 0, 0, 0.6);
                padding: 20px;
                border-radius: 15px;
                color: white;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.4);
                margin-bottom: 20px;
                font-family: 'Segoe UI', sans-serif;
                line-height: 1.6;
            }
            .info-card a {
                color: #1f77b4;
                text-decoration: none;
            }
            .info-card a:hover {
                text-decoration: underline;
            }
            ul {
                padding-left: 20px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.subheader('References')
    st.markdown("""
        <div class="info-card">
            We have used various data sources including 
            <a href="https://www.kaggle.com/datasets/rohanrao/formula-1-world-championship-1950-2020" target="_blank">this Kaggle dataset</a> 
            as the main source of historical race and driver data. I’ve also directly or indirectly utilized the 
            <a href="https://www.formula1.com/" target="_blank">Formula 1 official website</a> for current and factual updates. 
            Additionally, multiple royalty-free images were sourced from online repositories. We have taken care to respect copyright and usage policies.
        </div>
    """, unsafe_allow_html=True)

    st.subheader('Technology')
    st.markdown("""
        <div class="info-card">
            We have used the following technology stack:
            <ul>
                <li>Python (3.10.2)</li>
                <li>Streamlit (1.33.0)</li>
                <li>Visual Studio Code</li>
                <li>Jupyter Notebook</li>
                <li>Tableau Public (for exploratory visualization)</li>
                <li>Libraries: Pandas, NumPy, Matplotlib, Plotly, PIL, Math</li>
            </ul>
        </div>
    """, unsafe_allow_html=True)

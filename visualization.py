import streamlit as st

def tableau_viz():
    st.markdown("""
        <h2 style='text-align: center; color: white;'>🏎️ Constructor Performance Dashboard</h2>
        <div style='
            background-color: #1E1E1E;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 0px 12px rgba(0, 0, 0, 0.5);
            margin-bottom: 40px;
        '>
            <div style='text-align: center;'>
                <iframe src="https://public.tableau.com/views/F1Analysis_17030682058580/Dashboard1?:showVizHome=no&:embed=true" 
                        width="100%" 
                        height="600" 
                        style="border: none; border-radius: 8px;">
                </iframe>
            </div>
        </div>
    """, unsafe_allow_html=True)

    st.markdown("""
        <h2 style='text-align: center; color: white;'>👨‍✈️ Driver Performance Dashboard</h2>
        <div style='
            background-color: #1E1E1E;
            padding: 20px;
            border-radius: 12px;
            box-shadow: 0px 0px 12px rgba(0, 0, 0, 0.5);
        '>
            <div style='text-align: center;'>
                <iframe src="https://public.tableau.com/shared/2MK69P83C?:showVizHome=no&:embed=true" 
                        width="100%" 
                        height="600" 
                        style="border: none; border-radius: 8px; width: 100%;">
                </iframe>
            </div>
        </div>
    """, unsafe_allow_html=True)

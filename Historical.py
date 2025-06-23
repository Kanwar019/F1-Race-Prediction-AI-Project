import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
unlucky_df=pd.read_csv(r'unlucky_driver.csv')
youngwin_df=pd.read_csv(r'youngest_race_win.csv')
oldwin_df=pd.read_csv(r'oldest_race_win.csv')
nowin_df=pd.read_csv(r'MostRaceWithoutWin.csv')
def historical():

    st.subheader('Youngest Driver to Win Race')
    data_to_show4 = youngwin_df[['Driver','Age', 'Race']].to_html(index=False, classes='dataframe',border=0)
    styled_html4 = f'<style>table.dataframe{{background-color:black; color:white; padding:10px;}}</style>{data_to_show4}'
    st.write(styled_html4, unsafe_allow_html=True)

    st.subheader('Oldest Driver to Win Race')
    data_to_show5 = oldwin_df[['Driver','Age', 'Race']].to_html(index=False, classes='dataframe',border=0)
    styled_html5 = f'<style>table.dataframe{{background-color:black; color:white; padding:10px;}}</style>{data_to_show5}'
    st.write(styled_html5, unsafe_allow_html=True)
    
    st.subheader('Driver With Most Races Without Win')
    data_to_show6 = nowin_df[['Driver','Entries']].to_html(index=False, classes='dataframe',border=0)
    styled_html6 = f'<style>table.dataframe{{background-color:black; color:white; padding:10px;}}</style>{data_to_show6}'
    st.write(styled_html6, unsafe_allow_html=True)

    st.subheader('Unlucky Driver Data (Mechanical Failure Rate)')
    st.markdown('<img src="https://i.pinimg.com/originals/82/63/2f/82632f58a4e3367bb6a62641df799ffd.gif" width="1000" height="500" />', unsafe_allow_html=True)
    st.markdown('')
    # Plotting
    plt.figure(figsize=(10, 4),facecolor='#463F41')
    ax = plt.axes()
    ax.set_facecolor("#463F41")
    plt.bar(unlucky_df['Driver'], unlucky_df['Failure Percent'],color='#E11433')
    plt.xlabel('Driver name',color='white')
    plt.ylabel('Machine Failure Percentage',color='white')
    plt.title('Unlucky Drivers (Mechanical Failure Rate)',color='white')
    plt.xticks(rotation=90,color='white')
    plt.yticks(color='white')
    st.pyplot(plt,use_container_width=True)

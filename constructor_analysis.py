import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

def style_card(content_html):
    return f"""
    <div style="
        background-color: rgba(0, 0, 0, 0.6);
        padding: 15px;
        border-radius: 10px;
        margin-bottom: 30px;
        box-shadow: 0 4px 10px rgba(0,0,0,0.5);
    ">
        <span style="color: white; font-size: 16px; line-height: 1.6;">{content_html}</span>
    </div>
    """

def display_team(name, image_url, details):
    st.markdown(f"### {name}")
    st.image(image_url, use_container_width=True)
    st.markdown(style_card(details), unsafe_allow_html=True)

def plot_pie_chart(data, column, title, threshold=0, fig_size=(4, 4), color='black'):
    if threshold:
        data = data[data[column] >= threshold]
        others_sum = data[column].sum()
        others = pd.DataFrame({'Constructor': ['Other'], column: [others_sum]})
        data = pd.concat([data, others])

    labels = [f"{c} ({v})" for c, v in zip(data['Constructor'], data[column])]
    with plt.style.context({'axes.facecolor': color, 'figure.facecolor': 'white'}):
        fig, ax = plt.subplots(figsize=fig_size)
        ax.pie(data[column], labels=labels, textprops={'color': 'black'})
        ax.add_artist(plt.Circle((0, 0), 1.0, edgecolor='black', linewidth=2, fill=False))
        ax.set_title(title, fontsize=12)
        st.pyplot(fig)

def constructor_analysis():
    st.title('🏎️ F1 Constructor Analysis Dashboard')

    constructor_details = [
        {
            "name": "Oracle Red Bull Racing",
            "img": "https://www.oracle.com/a/pr/img/rc24-orbr.jpg",
            "info": "Started: 2005<br>Engine: Honda<br>Tyres: Pirelli<br>Race Wins: 116<br>Championships: 6"
        },
        {
            "name": "Scuderia Ferrari",
            "img": "https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/t_16by9Centre/f_auto/q_auto/fom-website/2025/Ferrari/Ferrari%20SF-25%20launch%20renders/F677_still_02_v11_169",
            "info": "Started: 1950<br>Engine: Ferrari<br>Tyres: Pirelli<br>Race Wins: 243<br>Championships: 16"
        },
        {
            "name": "Mercedes-AMG Petronas",
            "img": "https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/t_16by9Centre/f_auto/q_auto/fom-website/2023/Mercedes/W15%20launch/Mercedes-AMG%20W15%20E%20PERFORMANCE%20-%20Lewis%20Hamilton%20-%20Front%20Quarter",
            "info": "Started: 2010<br>Engine: Mercedes<br>Tyres: Pirelli<br>Race Wins: 125<br>Championships: 8"
        },
        {
            "name": "McLaren F1 Team",
            "img": "https://www.topgear.com/sites/default/files/2024/01/1-McLaren-MCL38-2024-F1-livery.jpg?w=1784&h=1004",
            "info": "Started: 1966<br>Engine: Mercedes<br>Tyres: Pirelli<br>Race Wins: 183<br>Championships: 8"
        },
        {
            "name": "Aston Martin Aramco",
            "img": "https://www.astonmartin.com/-/media/models---amr25/heros/amr25_hero_desktop.jpg?mw=1920&rev=1dc4bd480a3d49fd92e45f025b68f624&extension=webp&hash=673364FA515C7C1999282F22BF897605",
            "info": "Started: 2021<br>Engine: Mercedes<br>Tyres: Pirelli<br>Race Wins: 0<br>Championships: 0"
        },
        {
            "name": "BWT Alpine F1 Team",
            "img": "https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/f_auto/q_auto/content/dam/fom-website/manual/Misc/2023manual/Pre-season/February/Alpine%202",
            "info": "Started: 2021<br>Engine: Renault<br>Tyres: Pirelli<br>Race Wins: 21<br>Championships: 2 (as Renault)"
        },
        {
            "name": "Williams Racing",
            "img": "https://www.f1authentics.com/cdn/shop/files/1_Williams-FW45-Show-Car-3200px_72fd1aa1-602a-4859-9603-57dc9167baba.jpg?v=1728897949&width=2000",
            "info": "Started: 1977<br>Engine: Mercedes<br>Tyres: Pirelli<br>Race Wins: 114<br>Championships: 9"
        },
        {
            "name": "Kick Sauber (formerly Alfa Romeo)",
            "img": "https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/t_16by9Centre/f_auto/q_auto/fom-website/2023/Kick%20Sauber/C44_ST-Front-left_Stake_ZHO_16-9",
            "info": "Started: 1993 (as Sauber)<br>Engine: Ferrari<br>Tyres: Pirelli<br>Race Wins: 1<br>Championships: 0"
        },
        {
            "name": "RB Racing (formerly AlphaTauri)",
            "img": "https://a.espncdn.com/combiner/i?img=%2Fphoto%2F2024%2F0209%2Fr1288800_1296x518_5%2D2.jpg&w=920&h=368&scale=crop&cquality=80&location=origin&format=jpg",
            "info": "Started: 2006 (as Toro Rosso)<br>Engine: Honda<br>Tyres: Pirelli<br>Race Wins: 1<br>Championships: 0"
        },
        {
            "name": "Haas F1 Team",
            "img": "https://cdn-2.motorsport.com/images/amp/YEQnVvKY/s1200/formula-1-haas-f1-launch-2023--2.webp",
            "info": "Started: 2016<br>Engine: Ferrari<br>Tyres: Pirelli<br>Race Wins: 0<br>Championships: 0"
        }
    ]

    for team in constructor_details:
        display_team(team["name"], team["img"], team["info"])

    st.markdown("---")
    st.subheader('🏆 Constructor Standings – Podium Finishes')
    constructor_2023 = pd.read_csv('Constructor_Championship_2023.csv')
    constructor_2022 = pd.read_csv('Constructor_Championship_2022.csv')
    constructor_2021 = pd.read_csv('Constructor_Championship_2021.csv')

    col1, col2, col3 = st.columns(3)
    with col1:
        plot_pie_chart(constructor_2023[constructor_2023['podium'] > 1], 'podium', '2023 Podiums')
    with col2:
        plot_pie_chart(constructor_2022[constructor_2022['podium'] > 1], 'podium', '2022 Podiums')
    with col3:
        plot_pie_chart(constructor_2021[constructor_2021['podium'] > 1], 'podium', '2021 Podiums')

    st.subheader('🥇 Wins Comparison')
    col1, col2, col3 = st.columns(3)
    with col1:
        plot_pie_chart(constructor_2023[constructor_2023['wins'] > 0], 'wins', '2023 Wins')
    with col2:
        plot_pie_chart(constructor_2022[constructor_2022['wins'] > 0], 'wins', '2022 Wins')
    with col3:
        plot_pie_chart(constructor_2021[constructor_2021['wins'] > 0], 'wins', '2021 Wins')

    st.subheader('📊 Points Analysis')
    col1, col2, col3 = st.columns(3)
    with col1:
        plot_pie_chart(constructor_2023, 'Points', '2023 Points', threshold=160)
    with col2:
        plot_pie_chart(constructor_2022, 'Points', '2022 Points', threshold=160)
    with col3:
        plot_pie_chart(constructor_2021, 'Points', '2021 Points', threshold=160)

    st.subheader("🥇 Constructor Championships")
    cons_titles = pd.read_csv('Constructor_Titles.csv')
    plot_pie_chart(cons_titles, 'Titles', 'All-Time Constructor Titles', fig_size=(6, 6))

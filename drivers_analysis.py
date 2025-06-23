import streamlit as st

def drivers():
    st.markdown("""
    <style>
      .driver-container {
        display: flex;
        flex-wrap: wrap;
        gap: 30px;
        justify-content: center;
      }
      .driver-card {
  background-color: rgba(0,0,0,0.6);
  border-radius: 12px;
  width: 960px;            
  padding: 20px;
  text-align: center;
  margin-bottom: 30px;    /* ← add this */
}
      .driver-card img {
        border-radius: 8px;
        width: 100%;
        height: 500px;           /* made taller */
        object-fit: cover;
      }
      .driver-name {
        font-size: 40px;         /* slightly larger */
        font-weight: 900;
        margin-top: 16px;
        color: #e10600;
      }
      .driver-info {
        font-size: 17px;         /* slightly larger */
        line-height: 1.5;
        color: #fff;
        margin-top: 12px;
      }
    </style>
    """, unsafe_allow_html=True)

    st.subheader("🏎️ F1 Drivers")

    drivers = [
        ("Max Verstappen", "https://gpticketstore.vshcdn.net/uploads/images/12172/teams-lineups-f1-max-verstapen.jpg",
         "Nationality: Netherlands<br>Team: Red Bull<br>Age: 26<br>First Race: 2015 Australian GP<br>Wins: 63<br>Titles: 4"),
        ("Sergio Perez", "https://www.autohebdo.fr/app/uploads/2021/07/DPPI_00124025_1324.jpg",
         "Nationality: Mexico<br>Team: Red Bull<br>Age: 34<br>First Race: 2011 Australian GP<br>Wins: 6<br>Titles: 0"),
        ("Lewis Hamilton", "https://cdn-4.motorsport.com/images/amp/0k7er3A0/s1200/formula-1-styrian-gp-2021-lewi-2.webp",
         "Nationality: British<br>Team: Mercedes<br>Age: 39<br>First Race: 2007 Australian GP<br>Wins: 105<br>Titles: 7"),
        ("George Russell", "https://images.contentstack.io/v3/assets/blte77f57883ea46be1/blt94b1f0981ad85f4b/67d53fb4b97a517532c386df/M439025.jpg",
         "Nationality: British<br>Team: Mercedes<br>Age: 26<br>First Race: 2019 Australian GP<br>Wins: 3<br>Titles: 0"),
        ("Charles Leclerc", "https://motorcyclesports.net/wp-content/uploads/2025/02/2024122024-11-30T134157Z_1402530913_UP1EKBU121VS0_RTRMADP_3_MOTOR-F1-QATAR-scaled-1.jpg",
         "Nationality: Monégasque<br>Team: Ferrari<br>Age: 26<br>First Race: 2018 Australian GP<br>Wins: 8<br>Titles: 0"),
        ("Carlos Sainz", "https://lastwordonsports.com/motorsports/wp-content/uploads/sites/12/2024/11/4317448c-8eff-4e14-91d1-932b5abf6adc-1.jpg",
         "Nationality: Spanish<br>Team: Ferrari<br>Age: 29<br>First Race: 2015 Australian GP<br>Wins: 4<br>Titles: 0"),
        ("Lando Norris", "https://ichef.bbci.co.uk/ace/standard/965/cpsprodpb/edcf/live/ae067fc0-b4b0-11ef-8cd5-a537f1bb7c47.jpg",
         "Nationality: British<br>Team: McLaren<br>Age: 24<br>First Race: 2019 Australian GP<br>Wins: 4<br>Titles: 0"),
        ("Oscar Piastri", "https://www.autohebdo.fr/app/uploads/2022/06/DPPI_00124024_667.jpg",
         "Nationality: Australian<br>Team: McLaren<br>Age: 23<br>First Race: 2023 Bahrain GP<br>Wins: 2<br>Titles: 0"),
        ("Fernando Alonso", "https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/t_16by9Centre/f_auto/q_auto/trackside-images/2023/F1_Grand_Prix_of_Brazil___Previews/1771000913",
         "Nationality: Spanish<br>Team: Aston Martin<br>Age: 42<br>First Race: 2001 Australian GP<br>Wins: 32<br>Titles: 2"),
        ("Lance Stroll", "https://images.ps-aws.com/c?url=https%3A%2F%2Fd3cm515ijfiu6w.cloudfront.net%2Fwp-content%2Fuploads%2F2023%2F05%2F31135942%2Flance-stroll-aston-martin-monaco-planet-f1-2023.jpg",
         "Nationality: Canadian<br>Team: Aston Martin<br>Age: 25<br>First Race: 2017 Australian GP<br>Wins: 0<br>Titles: 0"),
        # Add the rest here...
    ]

    st.markdown('<div class="driver-container">', unsafe_allow_html=True)
    for name, img_url, info in drivers:
        st.markdown(f'''
            <div class="driver-card">
                <img src="{img_url}" alt="{name}">
                <div class="driver-name">{name}</div>
                <div class="driver-info">{info}</div>
            </div>
        ''', unsafe_allow_html=True)
    st.markdown('</div>', unsafe_allow_html=True)

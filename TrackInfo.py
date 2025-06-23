import streamlit as st

def tracks():
    st.markdown("""
        <style>
            .track-card {
                background-color: rgba(0, 0, 0, 0.7);
                border-radius: 12px;
                padding: 20px;
                margin-bottom: 30px;
                box-shadow: 0 4px 20px rgba(0,0,0,0.3);
                transition: transform 0.3s ease;
            }

            .track-card:hover {
                transform: scale(1.02);
            }

            .track-title {
                font-size: 22px;
                font-weight: bold;
                color: white;
                margin-bottom: 15px;
            }

            .track-image {
                display: block;
                margin: 0 auto 15px auto;
                max-width: 100%;
                height: auto;
                border-radius: 8px;
            }

            .track-info {
                background-color: rgba(0, 0, 0, 0.7);
                border-radius: 12px;
                padding: 20px;
                font-size: 18px;
                line-height: 1.6;
                color: white;
                box-shadow: 0 4px 20px rgba(0,0,0,0.3);
            }

            hr {
                margin-top: 20px;
                margin-bottom: 30px;
            }
        </style>
    """, unsafe_allow_html=True)

    st.subheader('Racing Track Information')
    st.markdown('<div class="track-info">All images are from the official Formula 1 website (Monaco from McLaren official site).<br>Data is accurate up to February 2024.</div>', unsafe_allow_html=True)
    st.markdown('<hr>', unsafe_allow_html=True)

    def render_track(title, image_url, info_text):
        st.markdown(f"""
            <div class="track-card">
                <div class="track-title">{title}</div>
                <img class="track-image" src="{image_url}">
                <div class="track-info">{info_text}</div>
            </div>
        """, unsafe_allow_html=True)

    # Now call render_track(...) as in your original code
    # Example:
    render_track("Bahrain - Sakhir Circuit",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Bahrain_Circuit.png.transform/9col/image.png",
                 """Country: Bahrain<br>
                    Length of Circuit: 5.412 km<br>
                    First Race: 2004<br>
                    Number of Laps: 57<br>
                    Lap Record: 1:31.447 - De la Rosa (2005)<br>
                    Most Wins Driver: Lewis Hamilton (5)<br>
                    Most Wins Constructor: Ferrari (7)""")

     # Saudi Arabia
    render_track("Jeddah Corniche Circuit",
                 "https://media.formula1.com/image/upload/f_auto/q_auto/v1677244985/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Saudi_Arabia_Circuit.png.transform/7col/image.png",
                 """Country: Saudi Arabia<br>
                    Length of Circuit: 6.174 km<br>
                    First Race: 2021<br>
                    Number of Laps: 50<br>
                    Lap Record: 1:30.734 - Lewis Hamilton (2021)<br>
                    Most Wins Driver: Max Verstappen (2)<br>
                    Most Wins Constructor: Red Bull (3)""")

    # Australia
    render_track("Melbourne Grand Prix Circuit",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Australia_Circuit.png.transform/9col/image.png",
                 """Country: Australia<br>
                    Length of Circuit: 5.278 km<br>
                    First Race: 1996<br>
                    Number of Laps: 58<br>
                    Lap Record: 1:24.125 - Michael Schumacher (2004)<br>
                    Most Wins Driver: Michael Schumacher (4)<br>
                    Most Wins Constructor: Ferrari (6)""")

    # Azerbaijan
    render_track("Baku City Circuit",
                 "https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/f_auto/q_auto/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Baku_Circuit",
                 """Country: Azerbaijan<br>
                    Length of Circuit: 6.003 km<br>
                    First Race: 2016<br>
                    Number of Laps: 51<br>
                    Lap Record: 1:43.009 - Max Verstappen (2021)<br>
                    Most Wins Driver: Lewis Hamilton (3)<br>
                    Most Wins Constructor: Mercedes (4)""")

    # Canada
    render_track("Circuit Gilles Villeneuve",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Canada_Circuit.png.transform/9col/image.png",
                 """Country: Canada<br>
                    Length of Circuit: 4.361 km<br>
                    First Race: 1978<br>
                    Number of Laps: 70<br>
                    Lap Record: 1:13.078 - Michael Schumacher (2004)<br>
                    Most Wins Driver: Michael Schumacher (7)<br>
                    Most Wins Constructor: Ferrari (13)""")

    # France
    render_track("Circuit Paul Ricard",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/France_Circuit.png.transform/9col/image.png",
                 """Country: France<br>
                    Length of Circuit: 5.842 km<br>
                    First Race: 1971<br>
                    Number of Laps: 53<br>
                    Lap Record: 1:32.740 - Lewis Hamilton (2019)<br>
                    Most Wins Driver: Lewis Hamilton (5)<br>
                    Most Wins Constructor: Mercedes (6)""")

    # Austria
    render_track("Red Bull Ring",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Austria_Circuit.png.transform/9col/image.png",
                 """Country: Austria<br>
                    Length of Circuit: 4.318 km<br>
                    First Race: 2014<br>
                    Number of Laps: 71<br>
                    Lap Record: 1:05.619 - Max Verstappen (2021)<br>
                    Most Wins Driver: Max Verstappen (5)<br>
                    Most Wins Constructor: Red Bull (8)""")

    # United Kingdom
    render_track("Silverstone Circuit",
                 "https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/f_auto/q_auto/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Great_Britain_Circuit",
                 """Country: United Kingdom<br>
                    Length of Circuit: 5.891 km<br>
                    First Race: 1950<br>
                    Number of Laps: 52<br>
                    Lap Record: 1:27.369 - Max Verstappen (2020)<br>
                    Most Wins Driver: Lewis Hamilton (8)<br>
                    Most Wins Constructor: Ferrari (10)""")

    # Hungary
    render_track("Hungaroring",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Hungary_Circuit.png.transform/9col/image.png",
                 """Country: Hungary<br>
                    Length of Circuit: 4.381 km<br>
                    First Race: 1986<br>
                    Number of Laps: 70<br>
                    Lap Record: 1:16.627 - Lewis Hamilton (2009)<br>
                    Most Wins Driver: Lewis Hamilton (8)<br>
                    Most Wins Constructor: Ferrari (8)""")

    # Belgium
    render_track("Circuit de Spa-Francorchamps",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Belgium_Circuit.png.transform/9col/image.png",
                 """Country: Belgium<br>
                    Length of Circuit: 7.004 km<br>
                    First Race: 1950<br>
                    Number of Laps: 44<br>
                    Lap Record: 1:46.286 - Valtteri Bottas (2018)<br>
                    Most Wins Driver: Michael Schumacher (6)<br>
                    Most Wins Constructor: Ferrari (9)""")

    # Netherlands
    render_track("Circuit Zandvoort",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Netherlands_Circuit.png.transform/9col/image.png",
                 """Country: Netherlands<br>
                    Length of Circuit: 4.259 km<br>
                    First Race: 2021<br>
                    Number of Laps: 72<br>
                    Lap Record: 1:11.097 - Max Verstappen (2021)<br>
                    Most Wins Driver: Max Verstappen (2)<br>
                    Most Wins Constructor: Red Bull (2)""")

    # Italy
    render_track("Autodromo Nazionale Monza",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Italy_Circuit.png.transform/9col/image.png",
                 """Country: Italy<br>
                    Length of Circuit: 5.793 km<br>
                    First Race: 1950<br>
                    Number of Laps: 53<br>
                    Lap Record: 1:21.046 - Michael Schumacher (2004)<br>
                    Most Wins Driver: Michael Schumacher (5)<br>
                    Most Wins Constructor: Ferrari (19)""")

    # Russia
    render_track("Sochi Autodrom",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Russia_Circuit.png.transform/9col/image.png",
                 """Country: Russia<br>
                    Length of Circuit: 5.848 km<br>
                    First Race: 2014<br>
                    Number of Laps: 53<br>
                    Lap Record: 1:35.761 - Lewis Hamilton (2019)<br>
                    Most Wins Driver: Lewis Hamilton (5)<br>
                    Most Wins Constructor: Mercedes (7)""")

    # Singapore
    render_track("Marina Bay Street Circuit",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Singapore_Circuit.png.transform/9col/image.png",
                 """Country: Singapore<br>
                    Length of Circuit: 5.063 km<br>
                    First Race: 2008<br>
                    Number of Laps: 61<br>
                    Lap Record: 1:41.905 - Daniel Ricciardo (2018)<br>
                    Most Wins Driver: Sebastian Vettel (5)<br>
                    Most Wins Constructor: Red Bull (4)""")

    # Japan
    render_track("Suzuka Circuit",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Japan_Circuit.png.transform/9col/image.png",
                 """Country: Japan<br>
                    Length of Circuit: 5.807 km<br>
                    First Race: 1987<br>
                    Number of Laps: 53<br>
                    Lap Record: 1:23.881 - Michael Schumacher (2004)<br>
                    Most Wins Driver: Michael Schumacher (6)<br>
                    Most Wins Constructor: Ferrari (10)""")
    
        # USA - Circuit of the Americas
    render_track("Circuit of the Americas",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/manual/2023/Circuit-maps/USA_Circuit.png.transform/9col/image.png",
                 """Country: United States<br>
                    Length of Circuit: 5.513 km<br>
                    First Race: 2012<br>
                    Number of Laps: 56<br>
                    Lap Record: 1:36.169 - Charles Leclerc (2019)<br>
                    Most Wins Driver: Lewis Hamilton (5)<br>
                    Most Wins Constructor: Mercedes (6)""")

    # Mexico
    render_track("Autódromo Hermanos Rodríguez",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Mexico_Circuit.png.transform/9col/image.png",
                 """Country: Mexico<br>
                    Length of Circuit: 4.304 km<br>
                    First Race: 1963<br>
                    Number of Laps: 71<br>
                    Lap Record: 1:17.774 - Valtteri Bottas (2021)<br>
                    Most Wins Driver: Max Verstappen (4)<br>
                    Most Wins Constructor: Red Bull (5)""")

    # Brazil
    render_track("Interlagos Circuit (São Paulo GP)",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Brazil_Circuit.png.transform/9col/image.png",
                 """Country: Brazil<br>
                    Length of Circuit: 4.309 km<br>
                    First Race: 1973<br>
                    Number of Laps: 71<br>
                    Lap Record: 1:10.540 - Valtteri Bottas (2018)<br>
                    Most Wins Driver: Alain Prost (6)<br>
                    Most Wins Constructor: McLaren (12)""")

    # Abu Dhabi
    render_track("Yas Marina Circuit",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Abu_Dhabi_Circuit.png.transform/9col/image.png",
                 """Country: United Arab Emirates<br>
                    Length of Circuit: 5.281 km<br>
                    First Race: 2009<br>
                    Number of Laps: 58<br>
                    Lap Record: 1:26.103 - Max Verstappen (2021)<br>
                    Most Wins Driver: Lewis Hamilton (5)<br>
                    Most Wins Constructor: Mercedes (6)""")

    # Spain
    render_track("Circuit de Barcelona-Catalunya",
                 "https://media.formula1.com/image/upload/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Spain_Circuit.png.transform/9col/image.png",
                 """Country: Spain<br>
                    Length of Circuit: 4.657 km<br>
                    First Race: 1991<br>
                    Number of Laps: 66<br>
                    Lap Record: 1:18.149 - Max Verstappen (2021)<br>
                    Most Wins Driver: Michael Schumacher (6)<br>
                    Most Wins Constructor: Ferrari (12)""")

    # Monaco
    render_track("Circuit de Monaco",
                 "https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Monaco_Circuit",
                 """Country: Monaco<br>
                    Length of Circuit: 3.337 km<br>
                    First Race: 1950<br>
                    Number of Laps: 78<br>
                    Lap Record: 1:12.909 - Lewis Hamilton (2021)<br>
                    Most Wins Driver: Ayrton Senna (6)<br>
                    Most Wins Constructor: McLaren (15)""")

    # Qatar
    render_track("Lusail International Circuit",
                 "https://media.formula1.com/image/upload/f_auto/q_auto/v1677244985/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Qatar_Circuit.png.transform/4col/image.png",
                 """Country: Qatar<br>
                    Length of Circuit: 5.419 km<br>
                    First Race: 2021<br>
                    Number of Laps: 57<br>
                    Lap Record: 1:24.319 - Max Verstappen (2023)<br>
                    Most Wins Driver: Max Verstappen (2)<br>
                    Most Wins Constructor: Red Bull (2)""")

    # Miami
    render_track("Miami International Autodrome",
                 "https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Miami_Circuit",
                 """Country: United States<br>
                    Length of Circuit: 5.412 km<br>
                    First Race: 2022<br>
                    Number of Laps: 57<br>
                    Lap Record: 1:29.708 - Max Verstappen (2023)<br>
                    Most Wins Driver: Max Verstappen (2)<br>
                    Most Wins Constructor: Red Bull (2)""")

    # Las Vegas
    render_track("Las Vegas Street Circuit",
                 "https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Las_Vegas_Circuit",
                 """Country: United States<br>
                    Length of Circuit: 6.201 km<br>
                    First Race: 2023<br>
                    Number of Laps: 50<br>
                    Lap Record: 1:35.490 - Oscar Piastri (2023)<br>
                    Most Wins Driver: Max Verstappen (1)<br>
                    Most Wins Constructor: Red Bull (1)""")

    # Imola
    render_track("Imola - Autodromo Enzo e Dino Ferrari",
                 "https://media.formula1.com/image/upload/f_auto,c_limit,q_auto,w_1320/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/Emilia_Romagna_Circuit",
                 """Country: Italy<br>
                    Length of Circuit: 4.909 km<br>
                    First Race: 1980<br>
                    Number of Laps: 63<br>
                    Lap Record: 1:15.484 - Lewis Hamilton (2020)<br>
                    Most Wins Driver: Michael Schumacher (7)<br>
                    Most Wins Constructor: Ferrari (8)""")

    # China
    render_track("Shanghai International Circuit",
                 "https://media.formula1.com/image/upload/f_auto,c_limit,w_960,q_auto/f_auto/q_auto/content/dam/fom-website/2018-redesign-assets/Circuit%20maps%2016x9/China_Circuit",
                 """Country: China<br>
                    Length of Circuit: 5.451 km<br>
                    First Race: 2004<br>
                    Number of Laps: 56<br>
                    Lap Record: 1:32.238 - Michael Schumacher (2004)<br>
                    Most Wins Driver: Lewis Hamilton (6)<br>
                    Most Wins Constructor: Mercedes (6)""")

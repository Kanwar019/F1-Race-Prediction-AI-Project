import streamlit as st

def about():
    st.markdown(
        """
        <style>
            .card {
                background-color: rgba(0, 0, 0, 0.6);
                padding: 20px;
                border-radius: 12px;
                box-shadow: 0 4px 12px rgba(0, 0, 0, 0.3);
                margin-bottom: 25px;
            }
            .card-title {
                font-size: 24px;
                font-weight: bold;
                color: #ffffff;
                margin-bottom: 12px;
            }
            .card-content {
                color: #dddddd;
                font-size: 17px;
                line-height: 1.6;
            }
            .card img {
                width: 100%;
                border-radius: 8px;
                margin-top: 15px;
            }
        </style>
        """,
        unsafe_allow_html=True
    )

    def render_section(title, content, image_url):
        st.markdown(f"""
            <div class="card">
                <div class="card-title">{title}</div>
                <div class="card-content">{content}</div>
                <img src="{image_url}" />
            </div>
        """, unsafe_allow_html=True)

    render_section("Sensors", """
        Formula 1 cars use around <b>300 sensors</b> to collect live data on <b>temperature, pressure, speed, torque, inertia, displacement</b> and more.
        These sensors are connected via <b>analog systems</b> or <b>ECUs (Electronic Control Units)</b>. 
        Although data collected during a weekend can reach <b>terabytes</b>, the actionable telemetry is often just <b>30–60 megabytes</b>.
    """, "https://www.autoracing1.com/wp-content/uploads/2023/f1/misc/f1carcross-section.jpg")

    render_section("Steering", """
        The Formula 1 steering wheel is a complex control unit with buttons for <b>gear shifts, engine modes, DRS</b>, and more. 
        It includes an information display, <b>LED shift lights</b>, <b>haptic feedback</b>, and a <b>quick-release</b> mechanism for safety.
    """, "https://www.ontheroadtrends.com/wp-content/uploads/2021/02/volante-F1-TW-ENG.jpg")

    render_section("Telemetry", """
        Telemetry allows teams to wirelessly track key metrics like <b>speed, RPM, throttle, brake force, DRS status</b>, and more — often in real time. 
        The x-axis of the telemetry graph usually represents the <b>length of the track</b>.
    """, "https://miro.medium.com/v2/resize:fit:2000/1*4iys-zDXVIWoeiLOsLovfw.png")

    render_section("Flags", """
        Common F1 flags include:<br>
        <b>Red flag</b>: Stops the race for safety.<br>
        <b>Yellow flag</b>: Indicates danger, drivers must slow.<br>
        <b>Green flag</b>: Track is clear, normal racing resumes.<br>
        <b>Checkered flag</b>: Race completed.
    """, "https://d3cm515ijfiu6w.cloudfront.net/wp-content/uploads/2022/05/04141242/Chequered-flag-waved-at-Red-Bull-Ring-Austria-2020-planetf1.jpg")

    render_section("Safety (Halo)", """
        The <b>halo</b> is a titanium safety device introduced in <b>2018</b> to protect the driver's head from debris and crashes. 
        It has proven effective in many real-world incidents.
    """, "https://i.ytimg.com/vi/3-3gIAkYEX8/maxresdefault.jpg")

    render_section("DRS (Drag Reduction System)", """
        DRS is a system that <b>reduces aerodynamic drag</b> by opening the rear wing flap. 
        Drivers can activate DRS in <b>designated zones</b> when within <b>1 second</b> of the car ahead, helping overtaking.
    """, "https://cdn.racingnews365.com/_975xAUTO_fit_center-center_85_none/9255618/DRS-F1-RacingNews-365.webp?v=1679583308")

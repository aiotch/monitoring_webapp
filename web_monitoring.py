import streamlit as st
from firebase import firebase
import plotly.graph_objs as go
from plotly.subplots import make_subplots

def main():
    st.set_page_config(page_title="Moniotrinng", layout="wide")
    st.markdown(""" <style> .font {
            font-size:35px ; font-family: 'Cooper Black'; color: #FF9633;}
            </style> """, unsafe_allow_html=True)

    st.markdown('<p class="font">Monitoring Web App</p>', unsafe_allow_html=True)

    st.markdown("""
    <style>
    div.stButton > button:first-child {width:80pt
    }
    </style>""", unsafe_allow_html=True)


    myDB = firebase.FirebaseApplication("https://monitoring-system-e57cd-default-rtdb.firebaseio.com/", None)
    get_Data_set_point_now = myDB.get('Data/Data_set_point_now', None)
    st.write("Set Point Sekarang: " + str(get_Data_set_point_now))
    
    input = -1
    myDB.put('Data',"Data_new_set_point", int(input))
    
    input = st.text_input("Set Point Baru")
    try:
        myDB.put('Data',"Data_new_set_point", int(input))
    except:
        pass
    col2, col3 = st.columns([0.1, 0.9])

    with col2:
        # st.markdown("#")
        if (st.button("ON")):
            try:
                myDB.put('Data', "Data_ON_OFF", 1)
            except:
                pass
        else:
            pass

    with col3:
        # st.markdown("#")
        if (st.button("OFF")):
            try:
                myDB.put('Data', "Data_ON_OFF", 0)
            except:
                pass
        else:
            pass

    col4, col5, col6 = st.columns([0.33, 0.33, 0.33])
    with col4:
        placeholder1 = st.empty()
    with col5:
        placeholder2 = st.empty()
    with col6:
        placeholder3 = st.empty()

    while True:
        get_Data_Open_Valve = myDB.get('Data/Data_Open_Valve', None)
        with col4:
            placeholder1.empty()
            with placeholder1.container():
                open_value = go.Indicator(mode="gauge+number", value=get_Data_Open_Valve,
                                          gauge={'axis': {'range': [None, 100]}},
                                          domain={'row': 1, 'column': 1}, delta={'reference': 100},
                                          title={'text': "Open Valve"})

                fig_1= make_subplots(
                    rows=1,
                    cols=1,
                    specs=[[{'type' : 'indicator'}]],
                    )

                fig_1.append_trace(open_value, row=1, col=1)
                st.plotly_chart(fig_1, use_container_width=True)

        get_Data_Flow = myDB.get('Data/Data_Flow', None)
        with col5:
            placeholder2.empty()
            with placeholder2.container():
                flow = go.Indicator(mode="gauge+number", value=get_Data_Flow,
                                    gauge={'axis': {'range': [None, 100]}},
                                    domain={'row': 1, 'column': 1}, delta={'reference': 100}, title={'text': "Flow"})

                fig_2 = make_subplots(
                    rows=1,
                    cols=1,
                    specs=[[{'type' : 'indicator'}]],
                    )

                fig_2.append_trace(flow, row=1, col=1)
                st.plotly_chart(fig_2, use_container_width=True)

        get_Data_Pressure = myDB.get('Data/Data_Pressure', None)
        with col6:
            placeholder3.empty()
            with placeholder3.container():
                pressure = go.Indicator(mode="gauge+number", value=get_Data_Pressure,
                                            gauge={'axis': {'range': [None, 100]}},
                                            domain={'row': 1, 'column': 1}, delta={'reference': 100}, title={'text': "Pressure"})

                fig_3 = make_subplots(
                    rows=1,
                    cols=1,
                    specs=[[{'type' : 'indicator'}]],
                    )

                fig_3.append_trace(pressure, row=1, col=1)
                st.plotly_chart(fig_3, use_container_width=True)

main()

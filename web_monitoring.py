import streamlit as st
from firebase import firebase
import plotly.graph_objs as go
import matplotlib.pyplot as plt
import time

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
   
    placeholder0 = st.empty()
    
    input = st.text_input("Set Point Baru")
    try:
        myDB.put('Data',"Data_new_set_point", int(input))
        myDB.put('Data',"triger", int(1))
    except:
        pass
    col2, col3 = st.columns([0.1, 0.9])

    with col2:
        # st.markdown("#")
        if (st.button("ON")):
            try:
                myDB.put('Data', "Data_ON_OFF", 1)
            except:
                myDB.put('Data', "Data_ON_OFF", 0)
        else:
            pass

    with col3:
        # st.markdown("#")
        if (st.button("OFF")):
            try:
                myDB.put('Data', "Data_ON_OFF", 0)
            except:
                myDB.put('Data', "Data_ON_OFF", 1)
        else:
            pass
    

    while True:
        with placeholder0.container():
            get_Data_set_point_now = myDB.get('Data/Data_set_point_now', None)   
            st.write("Set Point Sekarang: " + str(get_Data_set_point_now))
        
        get_Data_Open_Valve = myDB.get('Data/Data_Open_Valve', None)
        get_Data_Flow = myDB.get('Data/Data_Flow', None)
        get_Data_Pressure = myDB.get('Data/Data_Pressure', None)
        
        fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3)

        x_valve = (1)
        y_valve = get_Data_Open_Valve
        ax1.bar(x_valve, 100.2, alpha = 1, color = 'white', edgecolor = "black")
        ax1.bar(x_valve, y_valve, color = 'green', edgecolor = "black")
        if y_velve >= 95:
            ax1.annotate(y_valve, (1, y_valve - 5), ha='center')
        else:
            ax1.annotate(y_valve, (1, y_valve + 2), ha='center')


        ax1.set_ylim([0, 100.2])
        ax1.xaxis.set_visible(False)
        ax1.yaxis.set_visible(False)
        ax1.spines['top'].set_visible(False)
        ax1.spines['right'].set_visible(False)
        ax1.spines['bottom'].set_visible(False)
        ax1.spines['left'].set_visible(False)

        x_flow = (2)
        y_flow = get_Data_Flow
        ax2.bar(x_flow, 100.2, alpha = 1, color = 'white', edgecolor = "black")
        ax2.bar(x_flow, y_flow, color = 'green', edgecolor = "black")
        if y_flow >= 95:
            ax2.annotate(y_flow, (2, y_flow - 5), ha='center')
        else:
            ax2.annotate(y_flow, (2, y_flow + 2), ha='center')

        ax2.set_ylim([0, 100.2])
        ax2.xaxis.set_visible(False)
        ax2.yaxis.set_visible(False)
        ax2.spines['top'].set_visible(False)
        ax2.spines['right'].set_visible(False)
        ax2.spines['bottom'].set_visible(False)
        ax2.spines['left'].set_visible(False)

        x_pressure = (3)
        y_pressure = get_Data_Pressure
        ax3.bar(x_pressure, 100.2, alpha = 1, color = 'white', edgecolor = "black")
        ax3.bar(x_pressure, y_pressure, color = 'green', edgecolor = "black")
        if y_pressure >= 95:
            ax3.annotate(y_pressure, (3, y_pressure - 5), ha='center')
        else:
            ax3.annotate(y_pressure, (3, y_pressure + 2), ha='center')

        ax3.set_ylim([0, 100.2])
        ax3.xaxis.set_visible(False)
        ax3.yaxis.set_visible(False)
        ax3.spines['top'].set_visible(False)
        ax3.spines['right'].set_visible(False)
        ax3.spines['bottom'].set_visible(False)
        ax3.spines['left'].set_visible(False)

        st.plotly_chart(fig, use_container_width=True)
main()

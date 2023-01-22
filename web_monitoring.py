import streamlit as st
from firebase import firebase
from matplotlib import pyplot as plt
import time
from PIL import Image
import streamlit as st
    
def run_1(kode):
    placeholder_kode_1 = st.empty()
    placeholder_kode_0 = st.empty()
    
    placeholder_kode_1.empty()
    placeholder_kode_0.empty()
    
    st.markdown(""" <style> h1 {
    font-family: "Source Sans Pro", sans-serif;
    font-weight: 700;
    padding: 0rem 0px rem;
    margin: 0px;
    line-height: 0;
    } </style> """, unsafe_allow_html=True)
    
    st.markdown("""<style>.css-18e3th9 {
    flex: 1 1 0%;
    width: 100%;
    padding: 2rem 1rem 10rem;
    min-width: auto;
    max-width: initial;
    } </style> """, unsafe_allow_html=True)
    
    st.markdown(""" <style>.font {font-size:40px ; font-family: 'Cooper Black'; color: #FF9633; line-height: 1.2;} </style> """, unsafe_allow_html=True)
    st.markdown(""" <style> div.stButton > button:first-child {width:60pt}</style>""", unsafe_allow_html=True)
    
    if kode == 0:
        with placeholder_kode_0.container():  

            st.markdown('<p class="font">PT. MARABUNTA BERKARYA CEPERINDO</p>', unsafe_allow_html=True)
            #st.write('<p class="font">Monitoring</p>', unsafe_allow_html=True)
            st.title('Monitoring')

            myDB = firebase.FirebaseApplication("https://monitoring-b94b2-default-rtdb.asia-southeast1.firebasedatabase.app/", None)
            
            placeholderinfo = st.empty()
            placeholderinfo.empty()
            with placeholderinfo:
                get_Data_set_point_now = myDB.get('Data/Data_set_point_now', None)          
                st.write("Set Point Sekarang: " + str(get_Data_set_point_now))  
           
            placeholder = st.empty()
            
            while True:
                placeholder.empty()
                with placeholder.container():
                    get_Data_Open_Valve = myDB.get('Data/Data_Open_Valve', None)
                    get_Data_Flow = myDB.get('Data/Data_Flow', None)
                    get_Data_Pressure = myDB.get('Data/Data_Pressure', None)

                    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 4))
                    fig.tight_layout()
                    
                    x_valve = (1)
                    y_valve = get_Data_Open_Valve
                    ax1.bar(x_valve, 100.2, alpha = 1, color = 'white', edgecolor = "black")
                    ax1.annotate("Valve", (1, 100 + 5), ha='center') 
                    if y_valve > 100:
                        ax1.annotate(y_valve, (1, 100 - 5), ha='center')      
                        ax1.bar(x_valve, 100, color = 'green', edgecolor = "black")
                    elif y_valve >= 95:
                        ax1.annotate(y_valve, (1, y_valve - 5), ha='center')
                        ax1.bar(x_valve, y_valve, color = 'green', edgecolor = "black")
                    else:
                        ax1.annotate(y_valve, (1, y_valve + 2), ha='center')
                        ax1.bar(x_valve, y_valve, color = 'green', edgecolor = "black")
                    
                    ax1.set_ylim([0, 105.2])
                    ax1.xaxis.set_visible(False)
                    #ax1.yaxis.set_visible(False)
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['bottom'].set_visible(False)
                    ax1.spines['left'].set_visible(False)

                    x_flow = (3)
                    y_flow = get_Data_Flow
                    ax2.bar(x_flow, 100.2, alpha = 1, color = 'white', edgecolor = "black")
                    ax2.annotate("Flow", (3, 100 + 5), ha='center')
                    if y_flow > 100:
                        ax2.annotate(y_flow, (3, 100 - 5), ha='center')
                        ax2.bar(x_flow, 100, color = 'green', edgecolor = "black")
                    elif y_flow >= 95:
                        ax2.annotate(y_flow, (3, y_flow - 5), ha='center')
                        ax2.bar(x_flow, y_flow, color = 'green', edgecolor = "black")
                    else:
                        ax2.annotate(y_flow, (3, y_flow + 2), ha='center')
                        ax2.bar(x_flow, y_flow, color = 'green', edgecolor = "black")

                    ax2.set_ylim([0, 105.2])
                    ax2.xaxis.set_visible(False)
                    #ax2.yaxis.set_visible(False)
                    ax2.spines['top'].set_visible(False)
                    ax2.spines['right'].set_visible(False)
                    ax2.spines['bottom'].set_visible(False)
                    ax2.spines['left'].set_visible(False)

                    x_pressure = (5)
                    y_pressure = get_Data_Pressure
                    ax3.bar(x_pressure, 10.02, alpha = 1, color = 'white', edgecolor = "black")
                    ax3.annotate("Pressure", (5, 10 + 0.5), ha='center')
                    if y_pressure >= 10:
                        ax3.annotate(y_pressure, (5, 10 - 0.5), ha='center')
                        ax3.bar(x_pressure, 10, color = 'green', edgecolor = "black")
                    elif y_pressure >= 9.5:
                        ax3.annotate(y_pressure, (5, y_pressure - 0.5), ha='center')
                        ax3.bar(x_pressure, y_pressure, color = 'green', edgecolor = "black")
                    else:
                        ax3.annotate(y_pressure, (5, y_pressure + 0.2), ha='center')
                        ax3.bar(x_pressure, y_pressure, color = 'green', edgecolor = "black")


                    ax3.set_ylim([0, 10.52])
                    ax3.xaxis.set_visible(False)
                    #ax3.yaxis.set_visible(False)
                    ax3.spines['top'].set_visible(False)
                    ax3.spines['right'].set_visible(False)
                    ax3.spines['bottom'].set_visible(False)
                    ax3.spines['left'].set_visible(False)
                    
                    #fig.patch.set_alpha(0)
                    st.pyplot(fig)
                    plt.close(fig)
                    
    if kode == 1:
        with placeholder_kode_1.container():  
            st.markdown('<p class="font">PT. MARABUNTA BERKARYA CEPERINDO</p>', unsafe_allow_html=True)
            #st.write('<p class="font">Monitoring</p>', unsafe_allow_html=True)
            st.title('Monitoring')
            myDB = firebase.FirebaseApplication("https://monitoring-b94b2-default-rtdb.asia-southeast1.firebasedatabase.app/", None)
            
            placeholderinfo = st.empty()
            placeholder_input = st.empty()
                   
            col5, col6, col7 = st.columns([0.1, 0.1, 0.8])          
            
           
            placeholderinfo.empty()
            with placeholderinfo:
                get_Data_set_point_now = myDB.get('Data/Data_set_point_now', None)          
                st.write("Set Point Sekarang: " + str(get_Data_set_point_now))  
                
            with placeholder_input.container():
                input = st.text_input("Set Point Baru")
                        
            if input: 
                placeholderinfo.empty()                
                with placeholderinfo.container():   
                    st.write("Set Point Sekarang: " + str(input))
                
                myDB.put('Data',"Data_new_set_point", int(input))
                myDB.put('Data',"triger", int(1))
        
             
            placeholder_button = st.empty()
            
            with placeholder_button.container():
                placeholder_button.empty() 
                with col5:
                    on = st.button("ON", key = '1')   

                with col6:
                    off = st.button("OFF", key = '2')   
                        
                with col7:
                    placeholder_button_info = st.empty()                        
            
            
            placeholder = st.empty()

            while true:            
                if on:
                    myDB.put('Data', "Data_ON_OFF", 1)            
                    st.experimental_rerun() 
                    
                if off:
                    myDB.put('Data', "Data_ON_OFF", 0)
                    st.experimental_rerun() 
                    
                get_Data_ON_OFF = myDB.get('Data/Data_ON_OFF', None)
                with col7:
                        placeholder_button_info.empty()
                        with placeholder_button_info.container():
                            if get_Data_ON_OFF == 0:
                                st.write('Alat dalam kondisi OFF')
                            else:
                                st.write('Alat dalam kondisi ON')  

                placeholder.empty()
                with placeholder.container():
                    get_Data_Open_Valve = myDB.get('Data/Data_Open_Valve', None)
                    get_Data_Flow = myDB.get('Data/Data_Flow', None)
                    get_Data_Pressure = myDB.get('Data/Data_Pressure', None)

                    fig, (ax1, ax2, ax3) = plt.subplots(nrows=1, ncols=3, figsize=(8, 4))
                    fig.tight_layout()
                    
                    x_valve = (1)
                    y_valve = get_Data_Open_Valve
                    ax1.bar(x_valve, 100.2, alpha = 1, color = 'white', edgecolor = "black")
                    ax1.annotate("Valve", (1, 100 + 5), ha='center') 
                    if y_valve > 100:
                        ax1.annotate(y_valve, (1, 100 - 5), ha='center')      
                        ax1.bar(x_valve, 100, color = 'green', edgecolor = "black")
                    elif y_valve >= 95:
                        ax1.annotate(y_valve, (1, y_valve - 5), ha='center')
                        ax1.bar(x_valve, y_valve, color = 'green', edgecolor = "black")
                    else:
                        ax1.annotate(y_valve, (1, y_valve + 2), ha='center')
                        ax1.bar(x_valve, y_valve, color = 'green', edgecolor = "black")
                    
                    ax1.set_ylim([0, 105.2])
                    ax1.xaxis.set_visible(False)
                    #ax1.yaxis.set_visible(False)
                    ax1.spines['top'].set_visible(False)
                    ax1.spines['right'].set_visible(False)
                    ax1.spines['bottom'].set_visible(False)
                    ax1.spines['left'].set_visible(False)

                    x_flow = (3)
                    y_flow = get_Data_Flow
                    ax2.bar(x_flow, 100.2, alpha = 1, color = 'white', edgecolor = "black")
                    ax2.annotate("Flow", (3, 100 + 5), ha='center')
                    if y_flow > 100:
                        ax2.annotate(y_flow, (3, 100 - 5), ha='center')
                        ax2.bar(x_flow, 100, color = 'green', edgecolor = "black")
                    elif y_flow >= 95:
                        ax2.annotate(y_flow, (3, y_flow - 5), ha='center')
                        ax2.bar(x_flow, y_flow, color = 'green', edgecolor = "black")
                    else:
                        ax2.annotate(y_flow, (3, y_flow + 2), ha='center')
                        ax2.bar(x_flow, y_flow, color = 'green', edgecolor = "black")

                    ax2.set_ylim([0, 105.2])
                    ax2.xaxis.set_visible(False)
                    #ax2.yaxis.set_visible(False)
                    ax2.spines['top'].set_visible(False)
                    ax2.spines['right'].set_visible(False)
                    ax2.spines['bottom'].set_visible(False)
                    ax2.spines['left'].set_visible(False)

                    x_pressure = (5)
                    y_pressure = get_Data_Pressure
                    ax3.bar(x_pressure, 10.02, alpha = 1, color = 'white', edgecolor = "black")
                    ax3.annotate("Pressure", (5, 10 + 0.5), ha='center')
                    if y_pressure >= 10:
                        ax3.annotate(y_pressure, (5, 10 - 0.5), ha='center')
                        ax3.bar(x_pressure, 10, color = 'green', edgecolor = "black")
                    elif y_pressure >= 9.5:
                        ax3.annotate(y_pressure, (5, y_pressure - 0.5), ha='center')
                        ax3.bar(x_pressure, y_pressure, color = 'green', edgecolor = "black")
                    else:
                        ax3.annotate(y_pressure, (5, y_pressure + 0.2), ha='center')
                        ax3.bar(x_pressure, y_pressure, color = 'green', edgecolor = "black")


                    ax3.set_ylim([0, 10.52])
                    ax3.xaxis.set_visible(False)
                    #ax3.yaxis.set_visible(False)
                    ax3.spines['top'].set_visible(False)
                    ax3.spines['right'].set_visible(False)
                    ax3.spines['bottom'].set_visible(False)
                    ax3.spines['left'].set_visible(False)
                    
                    #fig.patch.set_alpha(0)
                    st.pyplot(fig)
                    plt.close(fig)
            

def main():
        st.set_page_config(page_title="Monitoring", layout="wide")
        
        st.markdown("""<style>.css-1vq4p4l {
        padding: 1rem 1rem 1.5rem;
        } </style> """, unsafe_allow_html=True)   

       
        logo = Image.open('foto/logo.jpeg')
        st.sidebar.image(logo, use_column_width = True )
        
        st.sidebar.title("Login Menu")
        username = st.sidebar.text_input("User Name")
        password = st.sidebar.text_input("Password",type='password')
        login = st.sidebar.checkbox("Login")

        if login:
            if username == 'admin' and password == '12345678':
                st.sidebar.warning("Berhasil Masuk")
                run_1(kode = 1)
            
            else:
                st.sidebar.warning("Password atau User Name salah")
                run_1(kode = 0)         
        else:
            st.sidebar.warning(" Masukan User Name dan Password, kemudian Centang pada bagian Login untuk mengatur Set Point")
            run_1(kode = 0)
        

main()

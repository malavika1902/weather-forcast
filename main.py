import streamlit as st
import plotly.express as px
from backend import get_data

#add title,text input, selectbox, and subheader
st.title("Weather Forcast for the Next Days")
place = st.text_input("Place:")
days = st.slider("Forcast days", min_value=1, max_value=5,
                 help="Select the number of forcasted days")
option = st.selectbox("Select data to view",
                      ("Temperature","Sky"))
st.subheader(f"{option} for the next {days} days in {place}")

if place:
    #get the temperature or sky data
    filtered_data = get_data(place, days)

    if option == "Temperature":
        temperatures = [dict["main"]["temp"] for dict in filtered_data]
        dates = [dict["dt_text"] for dict in filtered_data]
        #create a temperature plot
        figure = px.line(x=dates,y=temperatures,labels={"x": "Date", "y": "Temperature (C)"})
        st.plotly_chart(figure)

    if option == "Sky":
        images = {"Clear": "img/clear.png", "Clouds": "img/cloud.png",
                  "Rain": "img/rain.png", "Snow": "img/snow.png"}
        sky_conditions = [dict["weather"][0]["main"] for dict in filtered_data]
        image_paths = [images[condition] for condition in sky_conditions]
        print(sky_conditions)
        st.image(image_paths,width=115)
import streamlit as st
import datetime
import time

st.subheader("Data entry", divider=True)

col1, col2, col3 = st.columns(3)

with col1:
    dateLog = st.date_input("Date:", datetime.date(2025, 4, 1))

with col2:
    stepsLog = st.number_input("Steps nr.:", min_value=1, max_value=1000000, value=1)
    intensityLog = st.selectbox("Select exercise intensity", ["Slow", "Moderate", "Fast"], index=1)

with col3:
    timeLog = st.number_input("Time (hours):", min_value=0.01, max_value = 48.00, value=0.01, step=0.01)
    weightLog = st.number_input("Weight (kgs):", min_value=0.01, max_value=500.00, value=1.00, step=0.01)


if st.button("Save"):
    with st.spinner("Saving data ...", show_time=True):
        time.sleep(4)
    st.write("Data saved")
    # st.info(f"Has pinchado {i}")
    # st.link_button(f"Go to gallery {i}", "https://streamlit.io/gallery")


# user_input = st.text_input("Ingresa tu nombre:")


# st.markdown("# Conversión de temperaturas")
# dato = st.text_input("Introduce número:")

# # Crear botón para calcular
# accion = st.selectbox("Convertir a:", ["Celcius", "Farenheit"])

# if st.button("Calcular"): # button onclick con texto "Calcular" haz ...
#     dato = int(dato)

#     if accion == "Celcius":
#         conversion = (dato - 32) * (5/9)
#     elif accion == "Farenheit":
#         conversion = dato * (9/5) + 32
#     else:
#         conversion = "opción no válida"

#     st.write(f"Resultado final es: {conversion}!")

# on = st.toggle("Activar botones")

# if on:
#     # st.write("Feature activated!")

#     for i in range(3):
#         if st.button(str(i)):
#             st.info(f"Has pinchado {i}")
#             st.link_button(f"Go to gallery {i}", "https://streamlit.io/gallery")
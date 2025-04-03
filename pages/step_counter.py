import streamlit as st
import datetime

st.subheader("Data entry", divider=True)

dateLog = st.date_input("Date:", datetime.date(2025, 4, 1))
stepsLog = st.number_input("Steps nr.:")
intensityLog = st.selectbox("Select exercise intensity", ["Low", "Medium", "high"])
distanceLog = st.number_input("Distance (km):")
weightLog = st.number_input("Weight (kgs):")

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
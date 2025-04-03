import streamlit as st

#convertir el conversorGrados.py a streamlit

st.markdown("# Conversión de temperaturas")
dato = st.text_input("Introduce número:")

# Crear botón para calcular
accion = st.selectbox("Convertir a:", ["Celcius", "Farenheit"])

if st.button("Calcular"): # button onclick con texto "Calcular" haz ...
    dato = int(dato)

    if accion == "Celcius":
        conversion = (dato - 32) * (5/9)
    elif accion == "Farenheit":
        conversion = dato * (9/5) + 32
    else:
        conversion = "opción no válida"

    st.write(f"Resultado final es: {conversion}!")

on = st.toggle("Activar botones")

if on:
    # st.write("Feature activated!")

    for i in range(3):
        if st.button(str(i)):
            st.info(f"Has pinchado {i}")
            st.link_button(f"Go to gallery {i}", "https://streamlit.io/gallery")


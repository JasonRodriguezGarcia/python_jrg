import streamlit as st

# ejemplos de distintos elementos

st.title("Hola Clase")

st.write("Aqui estoy")

st.markdown("# Titulo 1")
st.markdown("## Titulo 2")

st.markdown("```python print('hola')```")
st.code("print('hola mundo ...')", language="python")

# Crear entrada de texto
user_input = st.text_input("Ingresa tu nombre:")

# Crear botón para mostrar saludo
if st.button("¡Salúdame!"):
    st.write(f"¡Hola, {user_input}!")

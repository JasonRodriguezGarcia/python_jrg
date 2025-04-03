import streamlit as st
import time

PATH = "./pages/"
st.title("Aplicación de Streamlit")

# st.write("Instrucciones")

# page = st.sidebar.selectbox("Choose a peich", ["Otro", "Home", "Page 1"])

# fecha
# pasos
# intensidad
# distancia
# peso

pages = {
    "Main menu": [
        st.Page(PATH + "home.py", title="Home"),
    ],
    "Step counter": [
        st.Page(PATH + "step_counter.py", title="Data entry"),
    ],
    # "Your account": [
    #     st.Page(PATH + "create_account.py", title="Create your account"),
    #     st.Page(PATH + "manage_account.py", title="Manage your account"),        
    # ],
    # "Your account": [
    #     st.Page(PATH + "create_account.py", title="Create your account"),
    #     st.Page(PATH + "manage_account.py", title="Manage your account"),        
    # ],
    "Your account": [
        st.Page(PATH + "create_account.py", title="Create your account"),
        st.Page(PATH + "manage_account.py", title="Manage your account"),        
    ],
    "Resources": [
        st.Page(PATH + "about.py", title="About us"),
        st.Page(PATH + "tryit.py", title="Try it out"),        
    ]
}

# if page == "Home":
#     mostrar_home()
# elif page == "Page 1":
#     pass
#     # mostrar_pagina1()
# else:
#     st.write("página no encontrada")

pg = st.navigation(pages)
pg.run()
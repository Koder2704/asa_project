import streamlit as st
import time


st.set_page_config(
    page_title="ASA", 
    page_icon="💻",
    menu_items={
        'Get Help': None,
        'Report a bug': None,
        'About': None
    }
)


if time.localtime().tm_hour >= 12 and time.localtime().tm_hour < 16:
    st.header("Bon après-midi !")
elif time.localtime().tm_hour >= 16:
    st.header("Bonsoir !")
elif time.localtime().tm_hour >= 22:
    st.header("Bon repos !")
elif time.localtime().tm_hour >= 5:
    st.header("Bonjour !")


'---'

with st.container():
    st.header("Introduction")
    st.info(''':orange[Bienvenue dans le projet ASA].(Algorithme et Structures de données avancés)
    Ce projet a pour but de faire asseoir les connaissances des étudiants en cycles Licence
    sur les notions portées par le nom du projet.           
    ''')
    

with st.container():
    st.header("Présentation générale")
    
    
    col1, col2, col3, col4 = st.columns(4)

    with col1:
        with st.container(border=True):
            st.caption(':orange[Conjugaison]')
            
            st.markdown('''
            Conjugaison des verbes du premiers groupe au present et au futur.
        ''')
            
    with col2:
        with st.container(border=True):
            st.caption(':orange[Fiche de TD]')
            
            st.markdown('''
            Une série d'exercices bien définis sur les algorithmes.
        ''')
    with col3:
        with st.container(border=True):
            st.caption(':orange[Algorithmes de Tris]')
            
            st.markdown('''
            Implémentation des 03 algorithmes de tris les plus communs.
        ''')
    with col4:
        with st.container(border=True):
            st.caption(':orange[Support & Documentation]')
            
            st.markdown('''
            Accéssible, simple et facile à parcourir et comprendre.
        ''')


with st.container():
    st.header("Staff Technique")
    
    with st.container(border=True):
        st.write('''
        Projet sous la coordination académique de :orange[M. EYENGA](Professeur du cours ASA).             
    ''')
        
        st.subheader(":orange[Équipe technique]")
        st.markdown('''
        1. KEMBEU Daniel :orange[(Chef du groupe)],
        2. METIO Samantha,
        3. NDI Rex,
        4. Boris,
        5. SIDDIKI Aboubakar
    ''')
            
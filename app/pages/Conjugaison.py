import streamlit as st
import time
from utils.conj import conjugate_in_tense

def set_error(message: str ='Tous les champs sont requis !'):
    st.error(message)


with st.container(border=True):
    st.header(":orange[Conjugaison]")

    st.write('''Vous pouvez conjuguer des verbes du premier groupe sans au présent de l\
        indicatif et au futur.''')



verb = ''
tense = ''
with st.form("form_c1", border=True):
    verb = st.text_input('Verbe à conjuguer', placeholder="Entrez le verbe")
    tense = st.selectbox('Temps de conjugaison', [None,'Présent de l\'indicatif', 'Futur'])
    
    clicked = st.form_submit_button('Conjuguer', use_container_width=True)
    
    if clicked:
        
        with st.spinner():
            if verb == '':
                set_error('Entrez un verbe à conjuguer !')
            elif not tense:
                set_error('Choisissez le temps de conjugaison !') 
            else:   
                time.sleep(3)
                with st.container(border=True):
                    st.subheader("Résultats")
                    st.write(f"Conjugaison du verbe '{verb}' au '{tense}'")
                    
                    # short codes for the tenses:
                    if tense == "Présent de l'indicatif":
                        tense = 'pre'
                    else:
                        tense = 'fut'
                    
                    try:
                        conjugate_in_tense(verb.lower(), tense)
                    except ValueError as e:
                        set_error(e)
import time
import streamlit as st

from pages.Exercices_de_la_fiche import set_error
from utils import exercices

st.header(':orange[Algorithmes de Tris]')

st.header("")  # Setting vertical margin between items

st.warning("Présentement, aucune des fonctionnalités de tris n'a été implémentée à cet interface.\
        Seuls les algorithmes ont été écrits !")





#=====================================================================================================================================================





st.subheader('Tri Insertion')
with st.expander('Tri Insertion', expanded=True) as main_wrapper:

    with st.form(key="tri_insertion", border=False):

        n = st.text_input(':blue[Entre un tableau]')
        submitted = st.form_submit_button('Evaluate', use_container_width=True)

        if submitted:
            if n:
                n = int(n)

                if n < 0:
                    set_error("Entrez un nombre supérieur à 0 !")
                else:
                    with st.container(border=True):
                        with st.spinner("Evaluating results..."):
                            time.sleep(2)
                            result = exercices.calculer_factoriel(n)

                            st.subheader("Results")
                            f"Le factoriel de {n} est:", result
            else:
                set_error()



#=====================================================================================================================================================




st.subheader('Tris Bulle')
with st.expander('Tris Bulle') as main_wrapper:

    with st.form(key="tri_bulle", border=False):

        n = st.text_input(':blue[Entre un tableau]')
        submitted = st.form_submit_button('Evaluate', use_container_width=True)

        if submitted:
            if n:
                try:
                    n = int(n)
                    if n < 0:
                        set_error("Entrez un nombre supérieur à 0 !")
                    else:
                        with st.container(border=True):
                            with st.spinner("Evaluating results..."):
                                time.sleep(2)
                                result = exercices.calculer_factoriel(n)

                                st.subheader("Results")
                                f"Le factoriel de {n} est:", result
                except ValueError:
                    set_error("Seuls les nombres sont permis !")

            else:
                set_error("Ce champ est requit !")



#=====================================================================================================================================================




st.subheader('Tris Sélection')
with st.expander('Tris Sélection') as main_wrapper:

    with st.form(key="tri_selection", border=False):

        n = st.text_input(':blue[Entre un tableau]')
        submitted = st.form_submit_button('Evaluate', use_container_width=True)

        if submitted:
            if n:
                try:
                    n = int(n)
                    if n < 0:
                        set_error("Entrez un nombre supérieur à 0 !")
                    else:
                        with st.container(border=True):
                            with st.spinner("Evaluating results..."):
                                time.sleep(2)
                                result = exercices.calculer_factoriel(n)

                                st.subheader("Results")
                                f"Le factoriel de {n} est:", result
                except ValueError:
                    set_error("Seuls les nombres sont permis !")

            else:
                set_error("Ce champ est requit !")



#=====================================================================================================================================================

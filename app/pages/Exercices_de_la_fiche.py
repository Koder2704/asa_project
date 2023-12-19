import streamlit as st
import numpy as np
import time

from utils import exercices



# The Error message to print
def set_error(message: str ='Tous les champs sont requis !'):
    st.error(message)


st.title(':orange[Exercices de la fiche]')


#=======================================================================================================================================================


#EXO 9:
st.subheader('Exercice 09')
with st.expander('Factoriel d\'un nombre', expanded=True) as main_wrapper:

    with st.form(key="exo9", border=False):
#         st.markdown('''
#     :orange[Principe]: *Le schtroumpf se calcule en faisant la somme des produits de chaque élément du
# premier tableau par chaque élément du second tableau.*
# ''')

        n = st.text_input(':blue[Entre un nombre positif]')
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




#=======================================================================================================================================================



#EXO 10:
st.subheader('Exercice 10')
with st.expander('Nombre premier') as main_wrapper:

    with st.form(key="exo10", border=False):
        st.markdown('''
    :orange[Principe]: *Un nombre premier est un nombre entier positif supérieur à 1 qui n'a pas 
                    de diviseurs autres que 1 et lui-même.*
''')

        n = st.text_input(':blue[Entre un nombre positif]')
        submitted = st.form_submit_button('Evaluate', use_container_width=True)

        if submitted:
            if n:
                n = int(n)

                if n < 0:
                    set_error("Entrez un nombre positif ! (n > 0)")
                else:
                    with st.container(border=True):
                        with st.spinner("Evaluating results..."):
                            time.sleep(2)
                            result = exercices.est_premier(n)

                            if result:
                                f"{n} est un nombre premier !"
                            else:
                                f'{n} n\'est pas un nombre premier !'
            else:
                set_error()




#=======================================================================================================================================================



#EXO 11:
st.subheader('Exercice 11')
with st.expander('Nombres Copains') as main_wrapper:

    with st.form(key="exo11", border=False):
        st.markdown('''
    :orange[Principe]: *Deux entiers positifs p et q sont dits copains si la somme des diviseurs de p autre que 1 et p est
égale à q et dans le même temps, la somme des diviseurs de q autre que 1 et q est égale à p*
''')

        col1, col2 = st.columns(2)

        with col1:
            p = st.text_input(':blue[Entre le premier nombre]')
        with col2:
            q = st.text_input(':blue[Entre le deuxième nombre]')

        submitted = st.form_submit_button('Evaluate', use_container_width=True)

        if submitted:
            if p and q:
                p, q = int(p), int(q)

                if p <= 0 or q <= 0:
                    set_error("Entrez un nombre positif ! (n > 0)")
                else:
                    with st.container(border=True):
                        with st.spinner("Evaluating results..."):
                            time.sleep(2)
                            result = exercices.sont_copains(p, q)

                            st.subheader("Results")
                            f'Somme des diviseurs de {p}:', result['d_p']
                            f'Somme des diviseurs de {q}:', result['d_q']

                            if not result['is']:
                                'Les nombres ne sont pas copains !'
                            else:
                                'Les nombres sont copains !'
            else:
                set_error()




#=======================================================================================================================================================



#EXO 17:
st.subheader('Exercice 17')
with st.expander('Schtroumpf') as main_wrapper:

    with st.form(key="exo17", border=False):
        st.markdown('''
    :orange[Principe]: *Le schtroumpf se calcule en faisant la somme des produits de chaque élément du
premier tableau par chaque élément du second tableau.*
''')

        col1, col2 = st.columns(2)
        with col1:
            first_array = st.text_input(':blue[Premier tableau]', key="exo17_input1")
        with col2:
            second_array = st.text_input(':blue[Deuxième tableau]', key="exo17_input2")
        
        submitted = st.form_submit_button('Evaluate', use_container_width=True)

        if submitted:
            if first_array and second_array:
                first_array = first_array.strip("[]").replace(' ', '').split(',')
                second_array = second_array.strip("[]").replace(' ', '').split(',')
                first_array = [int(i) for i in first_array]
                second_array = [int(i) for i in first_array]

                with st.container(border=True):
                    with st.spinner("Evaluating results..."):
                        time.sleep(2)
                        result = exercices.calculer_schtroumpf(first_array, second_array)

                        st.subheader("Results")
                        "La valeur du schtroumpf est:", result
            else:
                set_error('Please all the fields are required !')




#=======================================================================================================================================================



# EXO 22:
st.subheader("Exercice 22")
with st.expander('Trace d\'une matrice carrée') as main_wrapper:

    with st.form(key="exo22", border=False):
        st.markdown('''
    :orange[Principe]: *Ecrire un algorithme qui fait la lecture d'une matrice carrée A, son degré n et calcule
la trace de A. On rappelle que : si A = (aij), alors trace(A) = ∑ aii*
''')
        
        st.caption('''
    *Chaque élément de la matrice doit être séparée par une virgule. Pour le cas de la séparation d'une ligne dans la
                    matrice, un espace blanc suffira.(exemple: 1,2,3:orange[[espace vide ici]]4,5,6)*
    ''')

        exo22_matrix = st.text_input(':blue[Matrix]', placeholder="Entrez votre matrice")
        size = st.text_input(':blue[Degree]', placeholder='Entrez un nombre valide')
        submitted = st.form_submit_button('Evaluate', use_container_width=True)

        if submitted:
            if exo22_matrix and size:
                size = int(size)

                try:
                    # matrix = [[int(el) for el in row.split(',')] for row in exo22_matrix.split()]
                    matrix = np.matrix([list(map(int, ligne.split(','))) for ligne in exo22_matrix.split()])
                    "Matrice:", matrix
                    
                    with st.container(border=True):
                        with st.spinner("Computing..."):
                            time.sleep(2)
                            result = 0
                            result = exercices.calculer_trace(matrix, size)
                            
                            st.subheader("Results")
                            "La trace de la matrice est:", result
                except ValueError as error:
                    set_error(error)

            else:
                set_error()



#=======================================================================================================================================================


# EXO 23:
st.subheader("Exercice 23")

with st.expander("Transposée d'une matrice carrée"):
    with st.form(key="exo23", border=False):
        st.markdown('''
    :orange[Principe]: *Ecrire un algorithme qui fait la lecture d'une matrice carrée A, son degré n et affiche
la matrice transposée de A. On rappelle que : si A = (aij), alors transposée(A) = (aji)*
    ''')
        
        st.caption('''
    *Chaque élément de la matrice doit être séparée par une virgule. Pour le cas de la séparation d'une ligne dans la
                    matrice, un espace blanc suffira.(exemple: 1,2,3:orange[[espace vide ici]]4,5,6)*
    ''')

        matrix = st.text_input(':blue[Matrice]', placeholder="Entrez votre matrice")
        size = st.text_input(':blue[Degre]', placeholder='Enter a valid number')
        submitted = st.form_submit_button('Evaluate', use_container_width=True)

        if submitted:
            if matrix and size:
                size = int(size)
                matrix = np.matrix([list(map(int, ligne.split(','))) for ligne in matrix.split()])
                
                # Printing the formated matrix:
                'Format de matrice:', matrix

                with st.container(border=True):
                    with st.spinner("Evaluating results..."):
                        time.sleep(2)
                        result = exercices.transposer_matrix(matrix, size)

                        st.subheader("Results")
                        "Resultat:", result
            else:
                set_error()

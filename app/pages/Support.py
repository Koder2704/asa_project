import streamlit as st

st.header(":orange[Page de support]")
with st.container(border=True):
    st.subheader("Notes")
    
    with st.container():
        st.warning('''Cette page vient en complément aux petites descriptions déjà présentes dans
la section :orange["Exercices de la fiche"]. Néanmoins, il y'aura plus de détails, de plus amples explications
non pas sur les exercices mais sur :orange[l'utilisation de l'application en elle-même].
    Donc, voyez la comme un guide d'utilisation plus qu'un résumé de cours.
''')

st.title('')
st.title('Détails sur les pages')

with st.container(border=True):
    st.header(':orange[Conjugaison]', divider='rainbow')
    with st.container(border=True):
        st.subheader("Fonctionnalités")
        st.write('''
1. Temps de conjugaison correctement supportés\n
    a. Présent de l'indificatif\n
    b. Futur
2. Algorithme autodidacte\n
3. Gestion fluide des exceptions\n 
             ''')
    st.success('Remarque: lorem ipsum dolor sit ammet')
    with st.container(border=True):
        st.title('')




with st.container(border=True):
    st.header(':orange[Exercices de la fiche]', divider='rainbow')
    with st.container(border=True):
        st.subheader("Fonctionnalités")
        st.write('''
1. Temps de conjugaison correctement supportés\n
    a. Présent de l'indificatif\n
    b. Futur
2. Algorithme autodidacte\n
3. Gestion fluide des exceptions\n 
             ''')
    st.success('Remarque: lorem ipsum dolor sit ammet')
    with st.container(border=True):
        st.title('')
        
        
        
    
with st.container(border=True):
    st.header(':orange[les Tris]', divider='rainbow')
    with st.container(border=True):
        st.subheader("Fonctionnalités")
        st.write('''
1. Temps de conjugaison correctement supportés\n
    a. Présent de l'indificatif\n
    b. Futur
2. Algorithme autodidacte\n
3. Gestion fluide des exceptions\n 
             ''')
    st.success('Remarque: lorem ipsum dolor sit ammet')
    with st.container(border=True):
        st.title('')
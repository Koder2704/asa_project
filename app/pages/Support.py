import streamlit as st

st.header(":orange[Page de Support]: Guide d'utilisation")
with st.container(border=True):
    st.subheader("Note introductive")
    
    with st.container():
        st.info('''Cette page vient en complément aux petites descriptions déjà présentes dans
la section :orange["Exercices de la fiche"]. Néanmoins, il y'aura plus de détails, de plus amples explications
non pas sur les exercices mais sur :orange[l'utilisation de l'application en elle-même].
    Donc, voyez la comme un guide d'utilisation plus qu'une documentation à part entière.
''')

st.title('')
st.title('Détails sur les pages')

with st.container(border=True):
    st.header(':orange[Conjugaison]', divider='rainbow')
    with st.container(border=True):
        st.subheader("Modules")
        st.write('''
1. Temps de conjugaison correctement supportés\n
    a. Présent de l'indificatif\n
    b. Futur
2. Algorithme autodidacte\n
3. Gestion fluide des exceptions\n 
             ''')




with st.container(border=True):
    st.header(':orange[Exercices de la fiche]', divider='rainbow')
    with st.container():
        st.subheader("Fonctionnement")
    st.success('''
    Certains exercices de la fiche exigent une méthode particulière de remplissage des informations,
    afin de pouvoir proprement exécuter l'algorithme en arrière-plan.               
''')
    with st.container():
        st.write("1. Calcul des schtroumpfs")
        st.info('''
    Le champ requiert une entrée du type: [n1, n2, n3], avec n1, n2 et n3 des nombres.                
''')
        
        st.write("2. Exercices sur les matrices")
        st.info('''
    Pour construire une matrice convenablement, l'utilisateur doit donner en entrée une série de nombres séparés
    par des virgules (sans espaces entre eux), pour différencier les i éléments d'une ligne dans une matrice. \n
    \nPour ce qui
    est de la séparation entre les lignes, elle se fait en insérant un espace, comme suit:
    Dans une matrice carrée de taille 2 (Deux lignes et deux colonnes), voila à quoi devra ressembler l'entrée:
    1,3 5,2    \n
    Notez bien l'espace entre les séries de nombres !           
''')
        
        
        
    
with st.container(border=True):
    st.header(':orange[les Tris]', divider='rainbow')
    with st.container():
        st.subheader("Fonctionnalités")
        
        st.info("Section non implémentée à ce jour.")
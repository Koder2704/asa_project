import streamlit as st

normal_list = ['jouer', 'donner', 'chanter', 'parler', 'discuter', 'disputer',
              'ordonner', 'annuler', 'crier', 'nouer', 'lier', 'envier']

# Verbs with the sound 'g' which forms their present with 'geons' at the 1st person of plural:
g_verbs = ['manger']

irregular_verbs = ['envoyer']

def conjugate_in_tense(verb: str, tense: str):
    
    print({verb, tense})
    
    if not verb.endswith('er') or verb == 'aller' or verb == 'boer':
        raise ValueError(f"''{verb}'' n'est pas du premier groupe !")
    else:
        # Nourrir le store des verbes...
        if verb not in normal_list or verb not in g_verbs:
            # Si c'est un verbe qui aura la terminaison 'eons' a la 1ere personne du pluriel,
            # ajouter dans la liste des 'g_verbs' pour pouvoir avoir le support de la bonne
            # terminaison lors de la conjugaison.
            
            if verb[-3] == 'g':
                g_verbs.append(verb)
                st.toast(f"Nouveau verbe: {verb} ajouté au dictionnaire avec incidence sur la terminaison !", icon='💙')
            else: 
                normal_list.append(verb)
                st.toast(f"Nouveau verbe: {verb} ajouté au dictionnaire sans incidence sur la terminaison !", icon='💚')
            print(normal_list)
            
        if tense == 'pre':
            
            # Si c'est un verbe en 'g' (geons):
            if verb in g_verbs:
                st.text(f"Je {verb[:-1]}")
                st.text(f"Tu {verb[:-1] + 's'}")
                st.text(f"Il/Elle {verb[:-1]}")
                st.text(f"Nous {verb[:-1] + 'ons'}")
                st.text(f"Vous {verb[:-2] + 'ez'}")
                st.text(f"Ils/Elles {verb[:-1] + 'nt'}")
            
            # Si c'est un verbe normal:
            elif verb in normal_list:
                st.text(f"Je {verb[:-1]}")
                st.text(f"Tu {verb[:-1] + 's'}")
                st.text(f"Il/Elle {verb[:-1]}")
                st.text(f"Nous {verb[:-2] + 'ons'}")
                st.text(f"Vous {verb[:-2] + 'ez'}")
                st.text(f"Ils/Elles {verb[:-1] + 'ont'}")
            
                
        elif tense == 'fut':
             # Si le verbe est un irregulier:
            if verb in irregular_verbs:
                if verb == 'envoyer':
                    st.text(f"J\' {verb[:3] + 'errai'}")
                    st.text(f"Tu {verb[:3] + 'erras'}")
                    st.text(f"Il/Elle {verb[:3] + 'erra'}")
                    st.text(f"Nous {verb[:3] + 'errons'}")
                    st.text(f"Vous {verb[:3] + 'errez'}")
                    st.text(f"Ils/Elles {verb[:-1] + 'erront'}")
            else:
                st.text(f"Je {verb + 'ai'}")
                st.text(f"Tu {verb + 'as'}")
                st.text(f"Il/Elle {verb + 'a'}")
                st.text(f"Nous {verb + 'ons'}")
                st.text(f"Vous {verb + 'ez'}")
                st.text(f"Ils/Elles {verb + 'ont'}")


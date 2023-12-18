import numpy


def calculer_schtroumpf(tableau1, tableau2):
    schtroumpf = 0

    for element1 in tableau1:
        for element2 in tableau2:
            schtroumpf += element1 * element2

    return schtroumpf




def est_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre**0.5) + 1):
        if nombre % i == 0:
            return False
    return True





def transposer_matrix(matrix, degre):
    if matrix.shape[0] != degre and matrix.shape[1] != degre:
        raise ValueError("La taille de la matrice ne correspond pas a la taille entrée.")
    return numpy.transpose(matrix)





def calculer_factoriel(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * calculer_factoriel(n - 1)
    




def sont_copains(p, q):
    def somme_diviseurs(nombre):
    # Calcule la somme des diviseurs de 'nombre' autre que 1 et 'nombre' lui-même
        return sum(i for i in range(2, nombre) if nombre % i == 0)
    # Vérifie si p et q sont copains
    return { 
        'is': somme_diviseurs(p) == q and somme_diviseurs(q) == p,
        'd_p': somme_diviseurs(p),
        'd_q': somme_diviseurs(q)
        }



def calculer_trace(matrix, size):
    # Vérification si la matrix est carrée
    if (matrix.shape[0] != size and matrix.shape[1] != size):
        raise ValueError("La taille de la matrice ne correspond pas a la taille entrée.")
    
    # Calcul de la trace (somme des éléments diagonaux)
    trace = numpy.trace(matrix)
    
    return trace




#============================================== Meme exercice =================================================
def occurence(x, L):
    count = 0

    if not isinstance(str, L):
        raise ValueError("L'iterable n'est pas une chaine de caractere !")
    else:
        for el in L:
            if x == el:
                count += 1
    return count

def concat_listes(liste1: list, liste2: list):
    if not liste1:
        return liste2
    elif not liste2:
        return liste1
    
    try: 
        liste1.extend(liste2)
    except:
        raise ValueError('Les elements entres ne sont pas des listes !')

    return liste1

def rechercher_caractere(x, L):
    try:
        if x in L: return L.index(x)
        else: return -1 
    except:
        raise ValueError("L'iterable n'est ni une chaine de caractere, ni une liste !")

print('position: ', rechercher_caractere('a', ''))
#============================================== Meme exercice =================================================


# 1: Structure de donnees a utiliser:
# 1-a
class Competition:
    coureur_arrives = []

    # 1-b
    class Coureur:
        def __init__(self, nom, dossard, performance):
            self.nom = nom
            self.dossard = dossard
            self.performance = performance


    # 2 et 3
    def enregister_coureur(self):
        # Le coureur est a la bonne place directement lors de l'enregistrement:

        n = input('Quel est le nom du coureur ? ')
        d = int(input("Quel est le dossard du coureur ? "))
        p = float(input("Quelle est la performance du coureur ? (ex: 8.6) "))

        # initialiser le coureur:
        coureur = self.Coureur(n, d, p)

        # Insérer le coureur à la bonne place:
        # Logique à implémenter.






#===========================================================================================================
# Tri selection en utilisant un tableau:
def tri_selection_tableau(arr):
    n = len(arr)

    for i in range(n - 1):
        # Trouver l'élément minimum dans la partie non triée
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # Échanger l'élément minimum avec le premier élément non trié
        arr[i], arr[min_index] = arr[min_index], arr[i]

    return arr



# En utilisant les listes chainees:
# Definition de la classe Node, pour representer un element de la liste chainee:
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

    def tri_selection_liste_chainee(self, head):
        current = head

        while current:
            # Trouver le minimum dans la partie non triée de la liste chaînée
            min_node = current
            temp = current.next
            while temp:
                if temp.data < min_node.data:
                    min_node = temp
                temp = temp.next

            # Échanger les données
            current.data, min_node.data = min_node.data, current.data
            current = current.next

        return head


# Exemple d'utilisation
# tableau_non_trie = [64, 25, 12, 22, 11]
# tableau_trie = tri_selection_tableau(tableau_non_trie)
# print("Tableau trié:", tableau_trie)

# # Exemple d'utilisation
# liste_non_triee = Node(64)
# liste_non_triee.next = Node(25)
# liste_non_triee.next.next = Node(12)
# liste_non_triee.next.next.next = Node(22)
# liste_non_triee.next.next.next.next = Node(11)

# liste_triee = tri_selection_liste_chainee(liste_non_triee)

# # Afficher la liste triée
# current = liste_triee
# while current:
#     print(current.data, end=" ")
#     current = current.next

#===========================================================================================================



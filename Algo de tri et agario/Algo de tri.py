def partitionner(l, debut, fin):

    valeur_pivot = l[fin]
    indice_pivot = debut

    for i in range(debut, fin):

        if l[i] <= valeur_pivot:

            l[i], l[indice_pivot] = l[indice_pivot], l[i]
            indice_pivot += 1

    l[indice_pivot], l[fin] = l[fin], l[indice_pivot]
    return indice_pivot

def tri_rapide(l, debut=0, fin=None):

    if fin == None:
        fin = len(l)-1

    if fin > debut:

        pivot = partitionner(l, debut, fin)
        tri_rapide(l, debut, pivot-1)
        tri_rapide(l, pivot+1, fin)

l = [59, 75, 20, 49, 45648, 216, 57, 4567, 0, 347, 53, 9, 75, 25, 98736]
print(l)
tri_rapide(l)
print(l)

def insertion(l):

    for indice in range(len(l)):

        j = indice

        while j > 0 and l[j-1] > l[j]:

            l[j], l[j-1] = l[j-1], l[j]
            j-=1


l = [11054, 56, 2, 4, 456, 65, 42, 65, 83, 92, 51, 67, 74, 98, 31]
print(l)
insertion(l)
print(l)
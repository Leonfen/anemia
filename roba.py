'''
def funzioneA(a: int,b: list[int]): 
    i = len(b) - 1 # i = 6
    # Iterare lista numero 2
    while i >= 0 and a != b[i]: # a = 1; b = 5; a = 1; b = 8; a = 1; b = 1
        i -= 1 # i =  
    return i == -1 # 

def funzioneB(a,b): 
    x = 0 <- inizialmente x = 0
    # Qui si itera la lista 1
    for i in a: # i = 1 # i = 2 
        if funzioneA(i,b): # 1, l2; x = 0 # i = 7, b = l2,  
            x += 1 
    return x 

l1 = [1,7,4,9,22,33] 
l2 = [2,4,1,8,5, 9, 7] 
print(funzioneB(l1, l2))
'''
# La funzione trova gli elementi non uguali presenti nelle due diverse liste; nella funzioneA si andrà a creare un'iterazione che continuerà fino a che non si troverà il valore uguale fra le due liste oppure finchè non finirà l'index della lista b. 
# Nell'ultimo caso il valore sarà uguale a -1, permettendo allora a aumentare di un'unità il valore x della seconda funzione, quale andrà invece a iterare ogni valore della lista A. 

def filter(l1: list[int]) -> list[int]:
    l2: list[int] = [l1[0]]
    for index in range(1, len(l1)):
        if l1[index] < l1[index - 1]:
            l2.append(l1[index])
    return l2

print(filter([8,6,5,7,3,1]))



def count(MAT: list[list[int]], i: int):
    counter: int = 0
    for index in range(len(MAT)):
        if i == MAT[index][index]: counter += 1
    return counter

print(count([[1,0,5,3], [4,1,4,3], [5,7,1,1], [1,1,1,9]], 1))

def check(l1: list[int], l2: list[int]):
    l3: list[bool] = []
    if len(l1) == len(l2):
        for element1, element2 in zip(l1, l2):
            l3.append(element1 == element2)
    else:
        for _ in range(len(l1)):
            l3.append(False)
    return l3
    
print(check([1, 3, 2, 5], [1,1,7,7,6]))

def A(p,q): 
    x = len(q) - 1 
    while x >= 0 and p != q[x]: 
        x -= 1 
    return x == -1 

def B(x,y): 
    m = 0
    i = 0
    while i < len(x):
        if A(x[i], y): 
            m = m + 1
        i += 1
    return m 

a = [2,4,1,6] 
b = [4,4,4,4,4] 
print(B(a,b))

# La funzione conta le occorrenze diverse esistenti fra la prima e la seconda lista; nella prima si itera la seconda lista finchè non si incontrerà il valore uguale, oppure finchè non finisce la lista; nell'ultimo caso vorrà quindi dire che il valore uguale della prima lista non è stato trovato nella seconda, aumentando quindi il valore di return

'''
Si scriva una funzione filtra che riceve una lista l1 di interi e restituisce una lista l2 ottenuta a partire da l1 eliminando tutti gli elementi che ne violano l’ordinamento decrescente. 
Un elemento di l1 dev’essere inserito in l2 se e solo se è maggiore di tutti gli elementi che lo seguono in l1.
Esempio: Se l1 = [8, 6, 6, 5, 3, 6, 2, 8] allora filtra (l1) restituisce la lista l2 = [8, 6, 5, 3, 2].
'''

def filtra(l1: list[int]) -> list[int]:
    l2: list[int] = [l1[0]]
    for index in range(0, len(l1) - 1):
        if l1[index] > l1[index + 1]: l2.append(l1[index + 1])
    return l2

print(filtra([8, 6, 6, 5, 3, 6, 2, 8]))

'''
Si scriva una funzione conta_valori che riceve una matrice di interi ed un intero n e restituisce il numero di occorrenze di n nella diagonale principale della matrice data.

Esempio: M = [[1,2,5,7], [3,3,4,1], [5,7,2,4], [2,7,8,3]] e n=3, la funzione restituirà 2.
'''

def conta_valori(MAT: list[list[int]], n: int) -> int:
    counter: int = 0
    for index in range(len(MAT)):
        if MAT[index][index] == n: counter += 1 
    return counter

print(conta_valori([[1,2,5,7], [3,3,4,1], [5,7,2,4], [2,7,8,3]], 3))

'''
Si implementi una funzione verifica che riceve in input due liste di interi l1 e l2 ed un intero i e ritorna una lista che ha nella posizione i-esima True se l’elemento i-esimo di l1 è multiplo dell’i-esimo elemento di l2 
oppure è strettamente maggiore di i e False altrimenti. Nel caso in cui le liste abbiano lunghezze diverse la funzione restituisce una lista della stessa lunghezza di l2 contenente tutti i valori False.
  
Esempio: l1 = [8, 11, 6, 14, 15, 9],  l2 = [4, 1, 9, 7, 6, 1], i = 9, output = [True, True, False, True,  True, False ]

'''

def verifica(l1: list[int], l2: list[int], i: int):
    l3: list[bool] = []
    if len(l1) == len(l2):
        for index in range(len(l1)):
            l3.append(((l1[index] > i) or (l1[index] % l2[index] == 0) and (l1[index] != i)))
    else:
        for _ in range(len(l2)):
            l3.append(False)
    return l3


l1 = [8, 11, 14, 15, 9]
l2 = [4, 1, 9, 7, 6, 1]
i = 9 
print(verifica(l1, l2, i))

def f_1(x,t): # conta tutti i valori elevati al quadrato minori di w; in quesot caso essi saranno allora 2 (cioè il valore -3 e 4)
    p = f_2(x)
    s=0
    for i in range(len(p)): 
        if p[i] < t:
            s+=1
    return s

def f_2(x): # Ritorna i valori della lista q elevati al quadrato
    r = []
    for i in range(len(x)):
        c = x[i] * x[i]
        r.append(c)
    return r

q = [5,-3,10,-7,9,4]
w = 18
print(f_1(q,w))

def filtra_multipli(L1: list[int], k: int) -> list[int]:
    l2: list[int] = []
    for element in L1:
        if (not element in l2) and (element % k == 0): l2.append(element)
    return l2

L1 = [2, 6, 3, 5, 6, 9, 3, 9]
k=3
print(filtra_multipli(L1, k)) 

def conta_frequenze(M: list[list[int]], i, k):
    counter: int = 0
    for element in M[i]:
        if element == k: counter += 1
    return counter

M = [[2,2,5,5], [3,5,4,5], [3,3,2,1], [4,5,2,3]] 
i=1 
k=5
print(conta_frequenze(M, i, k))

'''
Si implementi una funzione verifica che riceve in input due liste di interi L1 ed L2, e ritorna una lista che ha nella posizione i-esima True se l’elemento i-esimo di L1 è minore o uguale dell’i-esimo elemento di L2, False altrimenti. 
Nel caso in cui le liste abbiano lunghezze diverse la funzione restituisce una lista della stessa lunghezza di L1 contenente tutti i valori False.
  
Esempio: L1 = [2, 10, 6, 7, 15, 9],  L2 = [3, 1, 9, 7, 6, 1], la lista restituita sarà [True, False, True, True, False, False ]

'''

def verifica(L1: list[int], L2: list[int]):
    l3: list[bool] = []
    if len(L1) == len(L2):
        for index in range(len(L1)):
            l3.append((L1[index] <= L2[index]))
    else:
        for _ in range(len(L1)):
            l3.append(False)
    return l3

L1 = [2, 10, 6, 7, 15, 9]
L2 = [3, 1, 9, 7, 6, 1]
print(verifica(L1, L2))

def fun_1(a,b): # Seconda funzione, conta gli elementi true, e quindi quanti sono gli elementi diversi fra la seconda e la prima lista, in questo caso saranno allora 2
    c = 0 
    for i in a: 
        if fun_2(i,b): 
            c += 1 
    return c 

def fun_2(x,y): # Seconda funzione che viene chiamata, itera la seconda lista finchè non troverà l'elemento della prima lista, oppure finchè non è finito la lunghezza della stessa lista (per cui l'elemento non è stato trovaot). Nell'ultimo caso la lista restituirà true
    k = len(y) - 1 
    while k >= 0 and x != y[k]: 
        k -= 1 
    return k == -1 

list_1 = [1,7,4,9] 
list_2 = [2,4,1,8,5] 
print(fun_1(list_1, list_2))

def filtra_crescente(lista_1: list[int]) -> list[int]:
    l2: list[int] = [lista_1[0]]
    for index in range(1, len(lista_1)):
        if lista_1[index - 1] < lista_1[index]: l2.append(lista_1[index])
    return(l2)

print(filtra_crescente([2,3,6,5,8,7,4,10]))

def conta_occorrenze(M: list[list[int]], k: int):
    counter: int = 0
    for i in M:
        for j in i:
            if j == k: counter += 1
    return counter

print(conta_occorrenze([[1,2,5,7], [3,5,4,1], [5,7,2,4], [2,7,8,3]], 3))

'''
Si implementi una funzione verifica_lista che riceve in input due liste di interi lista_1 e lista_2 ed un intero k e, dopo aver verificato che le liste abbiano uguale lunghezza, ritorna una lista che ha nella posizione i-esima True 
se l’elemento i-esimo di lista_1 è maggiore o uguale dell’i-esimo elemento di lista_2 ed è inferiore o uguale a k e False altrimenti. 
Nel caso in cui le liste abbiano lunghezze diverse la funzione restituisce una lista della stessa lunghezza di lista_1 contenente tutti i valori False.

Esempio: lista_1 = [2, 10, 6, 7, 15, 9],  lista_2 = [3, 1, 9, 7, 6, 1], k = 10, output = [False, True, False, True,  False, True ]

'''
def verifica_lista(lista_1: list[int], lista_2: list[int], k: int) -> list[bool]:
    l3: list[bool] = []
    if len(lista_1) == len(lista_2):
        for element1, element2 in zip(lista_1, lista_2):
            l3.append(((element1 >= element2) and (element1 <= k)))
    else:
        for _ in range(len(lista_1)):
            l3.append(False)
    return(l3)

lista_1 = [2, 10, 6, 7, 15, 9]
lista_2 = [3, 1, 9, 7, 6, 1]
k = 10

print(verifica_lista(lista_1, lista_2, k))
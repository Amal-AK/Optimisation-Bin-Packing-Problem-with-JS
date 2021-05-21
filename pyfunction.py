from __future__ import unicode_literals
import io
import eel
import time
eel.init('web')
#****************************************ffd***************************************
@eel.expose      # Expose this function to Javascript
def ffd_py(c,w):
  start_time = time.time()
  n = len(w)
  order = sorted([i for i in range(n)], key = lambda i:w[i],reverse=True)
  bin_for_item = [-1 for i in range(n)]
  bin_space = []
  for i in order:
    for j in range(len(bin_space)):
      if w[i]<bin_space[j]:
        bin_for_item[i]=j
        bin_space[j]-=w[i]
        break
    if bin_for_item[i] < 0:
      j = len(bin_space)
      bin_for_item[i] = j
      bin_space.append(c-w[i])
  n_bin = len(bin_space)
  print(n_bin,bin_for_item) 
  t = time.time() - start_time
  print("Exec time :",t)
  eel.jsaffich(n_bin,t) 
  return n_bin, bin_for_item
#*******************************************************************************
#******************************FFI**********************************************
@eel.expose
def ffi_py(c,w):
  start_time = time.time()
  n = len(w)
  order = sorted([i for i in range(n)],key = lambda i:w[i])
  bin_for_item = [-1 for i in range(n)]
  bin_space = []
  for i in order:
    for j in range(len(bin_space)):
      if w[i]<bin_space[j]:
        bin_for_item[i]=j
        bin_space[j]-=w[i]
        break
    if bin_for_item[i] < 0:
      j = len(bin_space)
      bin_for_item[i] = j
      bin_space.append(c-w[i])
  n_bin = len(bin_space)
  print(n_bin,bin_for_item)
  t = time.time() - start_time
  print("Exec time :",t)
  eel.jsaffich(n_bin,t) 
  return n_bin, bin_for_item
#*******************************************************************************
#************************************BF*****************************************
@eel.expose
def bf_py(c,w):
  start_time = time.time()
  n = len(w)
  bin_for_item = [-1 for i in range(n)]
  bin_space = []
  for i,wi in enumerate(w):
    tmp = sorted(bin_space)
    k=0
    while len(tmp)!=0:
      #k = bin_space.index(min(bin_space))
      if wi < tmp[k]:
        j = bin_space.index(tmp[k])
        bin_for_item[i]=j
        bin_space[j]-=wi
        break
      else:
        k+=1
        if (k == len(bin_space)): break
      
    if bin_for_item[i] < 0:
      j = len(bin_space)
      bin_for_item[i] = j
      bin_space.append(c-wi)
  n_bin = len(bin_space)
  print(n_bin,bin_for_item)
  t = time.time() - start_time
  print("Exec time :",t)
  eel.jsaffich(n_bin,t)
  return n_bin, bin_for_item
#*******************************************************************************
#*************************************WF****************************************
@eel.expose
def wf_py(c,w):
  start_time = time.time()
  n = len(w)
  bin_for_item = [-1 for i in range(n)]
  bin_space = []
  for i,wi in enumerate(w):
    if (bin_space != []):
      k = bin_space.index(max(bin_space))
      if wi < bin_space[k]:
        bin_for_item[i]=k
        bin_space[k]-=wi
      
    if bin_for_item[i] < 0:
      j = len(bin_space)
      bin_for_item[i] = j
      bin_space.append(c-wi)
  n_bin = len(bin_space)
  print(n_bin,bin_for_item)
  t = time.time() - start_time
  print("Exec time :",t)
  eel.jsaffich(n_bin,t)
  return n_bin, bin_for_item
#*******************************************************************************
#*************************************AWF***************************************
@eel.expose
def awf_py(c,w):
  start_time = time.time()
  n = len(w)
  bin_for_item = [-1 for i in range(n)]
  bin_space = []
  for i,wi in enumerate(w):
    tmp = bin_space
    if (len(tmp)!=0):
      k = tmp.index(max(tmp)); tmp[k] = 0; k = tmp.index(max(tmp))
      if w[i]<bin_space[k]:
        bin_for_item[i]=k
        bin_space[k]-=wi
      
    if bin_for_item[i] < 0:
      j = len(bin_space)
      bin_for_item[i] = j
      bin_space.append(c-wi)
  n_bin = len(bin_space)
  print(n_bin,bin_for_item)
  t = time.time() - start_time
  print("Exec time :",t)
  eel.jsaffich(n_bin,t)
  return n_bin, bin_for_item
#*******************************************************************************
#***********************************NF******************************************
@eel.expose
def nf_py(c,w):
  start_time = time.time()
  n = len(w)
  bin_for_item = [-1 for i in range(n)]
  bin_space = []
  for i,wi in enumerate(w):
    for j in range(len(bin_space),0,-1):
      if wi<bin_space[j-1]:
        bin_for_item[i]=j-1
        bin_space[j-1]-=wi
        break
    if bin_for_item[i] < 0:
      j = len(bin_space)
      bin_for_item[i] = j
      bin_space.append(c-wi)
  n_bin = len(bin_space)
  print(n_bin,bin_for_item)
  t = time.time() - start_time
  print("Exec time :",t)
  eel.jsaffich(n_bin,t)
  return n_bin, bin_for_item
#*******************************************************************************
#*************************************BRANCH AND BOUND**************************
class Node:
    def __init__(self, poidrest, niveau, numbin):
        self.poidrest = poidrest    #Tableau des poids restants pour chaque boîte
        self.niveau = niveau              #Le niveau du noeud dans l'arbre
        self.numbin = numbin        #nombre de boîtes utilisées

    def getNiveau(self):
        return self.niveau

    def getNumBin(self):
        return self.numbin

    def getpoidrests(self):
        return self.poidrest

    def getpoidrest(self, i):
        return self.poidrest[i]
    
def branchAndBound( c, w):
        n = len(w)
      
        minBins = n  # initialiser la valeur optimale à n
        Nodes = []  # les noeuds à traiter
        poidrest = [c] * n  # initialiser les poids restants dans chaque boite [c,c,c,.......c]
        numBins = 0  # initialiser le nombre de boites utilisées
        for k in range(len(w)):
            if w[k] > c:
                print("les poids des objets ne doivent pas dépasser la capacité du bin")
                return 0
            else:
                
                curN = Node(poidrest, 0, numBins)  # créer le premier noeud, niveau 0, nombre de boites utilisées 0

                Nodes.append(curN)  # ajouter le noeud à l'arbre

                while len(Nodes) > 0:  # tant qu'on a un noeud à traiter

                    curN = Nodes.pop()  # récupérrer un noeud pour le traiter (curN)
                    curNiveau = curN.getNiveau()  # récupérrer son niveau

                    if (curNiveau == n) and (
                            curN.getNumBin() < minBins):  # si c'est une feuille et nbr boites utilisées < minBoxes
                        minBins = curN.getNumBin()  # umettre à jour minBoxes

                    else:

                        indNewBox = curN.getNumBin()

                        if (indNewBox < minBins):

                            poidCurNiveau = w[curNiveau]
                            for i in range(indNewBox + 1):
                                if (curNiveau < n) and (curN.getpoidrest(
                                        i) >= poidCurNiveau):  # si cet possible d'insérer l'objet dans la boite i
                                    # on crée un nouveau noeud.
                                    newWRemaining = curN.getpoidrests().copy()
                                    newWRemaining[i] -= poidCurNiveau  # la capacité restante i - le poids du nouvel objet

                                    if (i == indNewBox):  # nouvelle boite
                                        newNode = Node(newWRemaining, curNiveau + 1, indNewBox + 1)
                                        for j in range(curNiveau + 1, len(w)):
                                            s = + w[j]
                                        if (((indNewBox + 1) + s / c) < minBins):
                                            Nodes.append(newNode)
                                    else:  # boite deja ouverte
                                        newNode = Node(newWRemaining, curNiveau + 1, indNewBox)
                                        for j in range(curNiveau + 1, len(w)):
                                            s = + w[j]
                                        if ((indNewBox + s / c) < minBins):
                                            Nodes.append(newNode)

                return minBins
#*******************************************************************************
#****************************************AG*************************************

#*******************************************************************************

#*******************************************************************************
#*******************************************************************************








eel.start('heuristics.html', size=(1000, 600))
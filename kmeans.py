import random
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

K = 3

  
PATH = '/home/etienne12341/Documents/Projet/kMEANS/wine.data.txt'
tab=[[20, 20, 11],[21, 11, 23],[20, 16, 1],[57, 5, 74],[12, 4, 26],[32, 6, 54],[9, 35, 12],[16, 27, 15],[2, 40, 13]]
TAB2d=[[random.randint(0,100) for r in range(2)] for k in range(1000)]


def fileToListe():
  return np.loadtxt(PATH,delimiter=',')

def divide(lst, min_size, split_size):
    it = iter(lst)
    from itertools import islice
    size = len(lst)
    for i in range(split_size - 1,0,-1):
        s = random.randint(min_size, size -  min_size * i)
        yield list(islice(it,0,s))
        size -= s
    yield list(it)

def findCentroid(liste):
  soP=len(liste[0])
  centroid=[]
  for i in range (soP):
    centroid.append(0)
  for i in range(len(liste)):
    for j in range(len(liste[i])):
      centroid[j]+=liste[i][j]
  for i in range(len(centroid)):
    centroid[i]/=len(liste)
  return centroid


def distance(point,centroid):
  a=0
  for i in range(len(centroid)):
    a=a +((centroid[i]-point[i])**2)
  return a


def asl(T):
  for i in range(len(T)):
   print("Centroid ",i,T[i])
   print('\n')

def graph(t,c,Xindex,Yindex):
  
  tc=['b', 'g', 'r', 'c', 'm', 'y', 'k', 'pink']
  for i in range(len(t)):
    d = {'x': [], 'y': []}
    ce = {'x': [c[i][Xindex]], 'y': [c[i][Yindex]]}
    for j in range(len(t[i])):
      d['x'].append(t[i][j][Xindex])
      d['y'].append(t[i][j][Yindex])
    df = pd.DataFrame(data=d) 
    dc = pd.DataFrame(data=ce) 
    plt.plot( 'x','y', data=df, color=tc[i], linestyle='none', marker='o',markersize=0.5)
    plt.plot( 'x','y', data=dc, color=tc[i], linestyle='none', marker='d')

  plt.show()


def Kmeans(liste):

  random.shuffle(liste)
  splited = list(divide(liste,2,K))
  out = 0
  itera = 0
  OldCentroids=[]
  while out!=1:
    print('iteration'+str(itera))
    newListe=[]
    centroids=[]
    for i in range(K):
      centroids.append(findCentroid(splited[i]))
      newListe.append([])
    for i in range(K):
      for j in range(len(splited[i])):
        max = distance(splited[i][j],centroids[0])
        kmax=0
        for k in range(len(centroids)): 
          if distance(splited[i][j],centroids[k])<max:
            max = distance(splited[i][j],centroids[k])
            kmax=k
        newListe[kmax].append(splited[i][j])
    if centroids == OldCentroids:
      out += 1
    splited=newListe
    itera+=1
    OldCentroids=centroids[:]
  return newListe,centroids


#________________RUN________________#
l,c=Kmeans(fileToListe())
asl(c)
graph(l,c,1,2)

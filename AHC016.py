import io
import sys

_INPUT = """\
10 0.21
"""

sys.stdin = io.StringIO(_INPUT)

from random import random,randint
from heapq import heappush, heappop
def create_edge():
  global now,next
  if len(now)==0:
    now=next.copy()
    next=[]
  x=heappop(now)
  heappush(next,(random(),x[1]))
  return x[1]

def index(i,j):
  return (2*N-i-1)*i//2+j-i-1

def graph_distance(g,h,N):
  vg,vh=[0]*N,[0]*N
  for i in range(N-1):
    for j in range(N-1-i):
      if g[index(i,j)]==1: vg[i]+=1; vg[j]+=1
      if h[index(i,j)]==1: vh[i]+=1; vh[j]+=1
  vg.sort()
  vh.sort()
  return (sum([abs(vg[i]-vh[i])**.5 for i in range(N)])/N)**2

M, eps = input().split()
M = int(M)
eps = float(eps)

score=0
G=[]

N=100
Ngraphs=[]
for i in range(M):
  edge_num=i*N*(N-1)//2//(M-1)
  g=[0]*(N*(N-1)//2)
  now=[]
  next=[]
  for j in range(N):
    heappush(now,(random(),j))
  e=0
  while e<edge_num:
    u=create_edge()
    v=create_edge()
    if u>v: u,v=v,u
    if g[index(u,v)]==1: continue
    e+=1
    g[index(u,v)]=1
  Ngraphs.append(g)

print(N)
for i in range(M):
  print(*Ngraphs[i],sep='')

for q in range(100):
  H = list(map(int,input()))
  pred,dist=0,10**4
  for i in range(M):
    if graph_distance(Ngraphs[i],H,N)<dist: pred,dist=i,graph_distance(Ngraphs[i],H,N)
  print(pred)
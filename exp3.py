from sys import maxsize
from itertools import permutations
v=4
def travellingsalesperson(graph,s):
    vertex=[]
    for i in range(v):
        if i!=s:
            vertex.append(i)
    min_path=maxsize
    next_permutation=permutations(vertex)
    for i in next_permutation:
        current_path=0
        k=s
        for j in i:
            current_path +=graph[k][j]
            k=j
        current_path +=graph[k][s] 
        min_path=min(min_path,current_path)
    return min_path

if __name__=='__main__':
    graph=[[0,10,15,20],[10,0,35,25],[15,35,0,30],[20,25,30,0]]
    s=0
    print(travellingsalesperson(graph,s))

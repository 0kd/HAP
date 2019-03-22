import counthaps as ch

graph = ch.aaa
grapha=[]

for i in range(len(graph)):
    list = sorted(graph[i][0])
    eval = graph[i][1]
    list=sorted(list, key = lambda kv: kv.split('.')[1])
    grapha.append([list,eval])

print(grapha)

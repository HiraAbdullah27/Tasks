tree = {
    'A' : ['B','C'] ,
    'B' : ['D','E'] ,
    'C' : ['F','G'] ,
    'D' : [] ,
    'E' : [] ,
    'F' : [] ,
    'G' : [] ,
}
#print(tree)

queue = []
visit = []


def queue_bfs(start,goal):
    queue.append(start)    
    while queue:
        print(f'queue: {queue}')
        last = queue.pop(0)
        visit.append(last)
        print(f'visited list: {visit}, visiting: {last}')
        for i in tree[last]:
            if i not in queue:
                queue.append(i)
        if  not queue:
            print('Lisit is completely visited.')
        if str(last) == goal:
            print(f'{last}, Goal is found.')
            return

      

queue_bfs('A','F')


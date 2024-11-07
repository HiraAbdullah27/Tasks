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

stack = []
visit = []


def queue_bfs(start,goal):
    stack.append(start)    
    while stack:
        print(f'stack: {stack}')
        last = stack.pop(0)
        visit.append(last)
        print(f'visited list: {visit}, visiting: {last}')
        for i in tree[last]:
            if i not in stack:
                stack.append(i)
        if  not stack:
            print('Lisit is completely visited.')
        if str(last) == goal:
            print(f'{last}, Goal is found.')
            return

      

queue_bfs('A','F')


n = int(input('Enter the size of the board: '))
size = n*n
matrix = ['-'] * size
def mat():
    for i in range(1,size+1):
        print(matrix[i-1],end='')    
        if i % n !=0:
            void= n-i
            print('|',end='')
        if i % n == 0:
            print()
            for j in range(1,n+n):
                if i % n ==0 and i < size:
                    print('-',end='')
            print()       
mat()     
def play():
    loop = len(matrix) / 2
    loop = int(loop) + 1
    for i in range(loop):
        count = True
        o = int(input('Enter your value of \'o\': '))
        while count == True:
            if o > 0 and o < size + 1 and matrix[o-1] == '-':
                matrix[o-1] = 'o'
                mat()
                count = False
            else:
                print('invalid value')
                o = int(input('Enter your value of \'o\': '))
                continue

        if i == loop - 1:
            break

        count = True
        x = int(input('Enter your value of \'x\': '))
        while count == True:
            if x > 0 and x < size + 1 and matrix[x-1] == '-':
                matrix[x-1] = 'x'
                mat()
                count = False
            else:
                print('invalid value')
                x = int(input('Enter your value of \'x\': '))
                continue

play()
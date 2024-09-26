def sort(value):
    value  = value
    list = []
    list = value.split(' ')
    print('your text: ')
    print(value)
    for i in range(len(list)):
        for j in range(i,len(list)):
            if ord(list[i][0:1]) > ord(list[j][0:1]):
                list[i],list[j] =  list[j],list[i] 
    print('sorted text: ')      
    for i in list:

        print(i,end=' ')

value = input("Enter data: ")
sort(value)

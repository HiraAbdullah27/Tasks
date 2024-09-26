def debit_card():
    listy = []
    for i in range(16):
        num = int(input(f'enter num {i+1}: '))
        listy.append(num)
    print('your debit card num is: ',listy)
    x = listy.pop()
    listy.reverse()
    sum = 0
    for i in range(len(listy)):
        if i % 2 == 0:
            listy[i] = listy[i] * 2 
        if listy[i] > 9:
            listy[i] =  listy[i] - 9
        sum += listy[i]
    sum += x
    print(sum)
    if sum % 10 == 0:
        print('Yes, debit card is valid,')
    else:
        print('NO, debit card is invalid.')
debit_card()

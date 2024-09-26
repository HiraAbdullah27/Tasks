import random
print('''***Rules***
    Add last two number.
    If the number is divided by 3 type fizz
    If the number is divided by 5 type buzz
    If the number is divided by both type fizz buzz
    If the number is not divided by 3 nor 5 press any key.

              ***Good Luck***
      ''')
a = random.randint(1,100)
f_num = a
s_num = 0
flag = True
while True:
    print(f'The number is {a}')
    num = f_num + s_num
    user = input('Is it fizz or buzz or fizz-buzz: ')
    if num % 3 == 0 and user.lower() != 'fizz':
        flag = False
    elif num % 5 == 0 and user.lower() != 'buzz':
        flag = False
    elif num % 3 == 0 and num % 5 == 0 and user.lower() != 'fizz buzz':
        flag = False
    elif num % 3 != 0 and user.lower() == 'fizz':
        flag = False
    elif num % 5 != 0 and user.lower() == 'buzz':
        flag = False
    elif num % 3 != 0 and num % 5 != 0 and user.lower() == 'fizz buzz':
        flag = False
    else:
        print('correct')


    if flag == False:
        print('''you lose.
if you want to play again press 1: 
if you want to exit press 2:''')
        op = int(input('Enter 1 or 2: '))
        if op == 2:
            break
        else:
            a = random.randint(1,100)
            f_num = a
            s_num = 0
            continue

    else:

        s_num  = f_num
        a = random.randint(1,100)
        f_num = a
        num = f_num + s_num
        print(f'The number is {a}')
        print('computer turn: ')
        if num % 3 == 0:
            print('fizz')
        elif num % 5 == 0:
            print('buzz')
        elif num % 3 == 0 and f_num + s_num % 5 == 0:
            print('fizz buzz')
        else:
            print(f'no fizz buzz')
            print('your turn')
    
        s_num  = f_num
        a = random.randint(1,100)
        f_num = a

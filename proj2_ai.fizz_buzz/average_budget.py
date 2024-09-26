movies = [
    ("Eternal Sunshine of the Spotless Mind", 20000000),
    ("Memento", 9000000),
    ("Requiem for a Dream", 4500000),
    ("Pirates of the Caribbean: On Stranger Tides", 379000000),
    ("Avengers: Age of Ultron", 365000000),
    ("Avengers: Endgame", 356000000),
    ("Incredibles 2", 200000000)
]
num = []
add = 0
print(f'Current movies are: {movies}')
user = input('Do you want to add more movies yes or no: ')
if user.lower() == 'yes':
    leng = int(input('How many movies you want to add: '))
    for i in range(leng):
        name = input('Enter the name of movie: ')
        budget = int(input('Enter budget of movie: '))
        tup = (name,budget)
        movies.append(tup)

for i in movies:
    for j in range(len(i)):
        if j == 1:
            num.append(i[j])
for i in num:
    add = add + int(i) 
t_num = len(num)
avg = add / t_num
avg = int(avg)
print(f'The average budget of the movies is: {avg}.')

for i in movies:
    for j in range(1):
        if i[1] > avg:
            subs = i[1] - avg
            print(f'The film {i[0]} budget is {subs} greater.')
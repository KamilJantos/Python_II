# comprehensions dla list
x = [i for i in range(5)]
print(x)

for i in range(5):
    print(i)

y = [i for i in range(10) if i % 2 == 0]
print(y)

literoliczby = ["1", "2", "3", "4", "5"]
liczby = [int(i) for i in literoliczby]
print(liczby)

vec_of_vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
single = [num for elem in vec_of_vec for num in elem]
print(single)

# comprehensions i słowniki
slownik = {1: "Burek", 2: "Azor", 3: "Fafik"}
print({value: key for key, value in slownik.items()})

# comprehensions i zbiory
lista = [1, 2, 2, 3, 4, 4, 4, 5]
zbior = {i for i in lista}
print(zbior)

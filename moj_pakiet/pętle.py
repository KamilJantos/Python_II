#Pętla For
for i in range(3):
    print(i)

print("\n")

lista = [4, 5, 6]
for i in lista:
    print(i)

for index, wartosc in enumerate(lista):
    print(str(index) + " -> " + str(wartosc))

print("\n")

for krotka in enumerate(lista):
    print("idx: {0}, value: {1}".format(krotka[0], krotka[1]))

print("\n")

print(type(krotka[0]))
print(type(krotka[1]))
print(type(krotka))

print("\n")

#Pętla for i słowniki

slownik = {"imie": "Marek", "nazwisko": "Kowalski", "plec": "mezczyzna"}

for key in slownik:
    print(key)

for val in slownik.values():
    print(val)

for key, value in slownik.items():
    print(key + " -> " + value)

for key in slownik:
    print(key + " -> " + slownik[key])

print("\n")

#Pętla While
counter = 0
while True:
    counter += 1
    if counter > 10:
        break
    print(counter)
print("\n")
counter = 0
while counter < 5:
    print(str(counter) + " mniejsze od 5")
    counter += 1


lista = []
print("Podaj liczby całkowite, które chcesz umieścić w pętli.")
print("Wpisz 'stop' aby zakończyć")
while True:
    wej = input()
    if wej == 'stop':
        break
    lista.append(int(wej))

print("Twoja lista -> " + repr(lista))

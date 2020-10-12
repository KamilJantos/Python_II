liczba1 = 1
liczba2 = 2

if liczba1 > liczba2:
    print("Pierwsza liczba jest większa")
liczba = input("Podaj liczbę całkowitą ")
liczba = int(liczba)

if liczba < 10:
    print("To dość mała liczba")
elif 9 < liczba < 100:
    print("To już całkiem duża liczba")
else:
    print("To musi być wielka liczba")

if liczba < 10 or liczba > 15:
    print("Liczba nie jest z odpowiedniego przedziału")

zbior_dopuszczalny = [1, 3, 5, 7, 9]
if liczba not in zbior_dopuszczalny:
    print("Podana liczba nie znajduje się w zbiorze")
nic = None
pusty_ciag = ""

if not nic:
    print("None to False")
if not pusty_ciag:
    print("Pusty ciąg to False")
if nic == pusty_ciag:
    print("None i pusty ciąg to boolowskie False, ale nie są sobie równe")
if pusty_ciag == "":
    print("To jest pusty ciąg")

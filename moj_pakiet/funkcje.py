def zainicjalizuj():
    print("inicjalizacja...")


zainicjalizuj()


###
def powiel(tekst, ile_razy):
    return (tekst + " ") * ile_razy


print(powiel("jesień", 5))


###
def powiel(tekst="Hello ", ile_razy=3):
    return (tekst + " ") * ile_razy


print(powiel())

###
print(powiel(ile_razy=5, tekst="Jingle bells"))


###
def robie_duzo_rzeczy(*args, **kwargs):
    print(args)
    print(kwargs)


robie_duzo_rzeczy(3, 4, 5.6, imie="Krzysztof", hobby=["sport", "fantasy"])


###
def mam_globala():
    global a
    a = 1
    b = 2
    return a + b


def nie_mam_globala():
    c = 3
    return a + c


print(mam_globala())
print(nie_mam_globala())

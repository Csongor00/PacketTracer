def lista_elemek_szama(lista):
  szamlalo = 0
  for i in lista:
    szamlalo += 1
  return szamlalo
print(lista_elemek_szama([1,4,8,11]))

def legkisebb(lista):
  legkisebb = lista[0]
  for i in lista:
    if i < legkisebb:
      legkisebb = i
  return legkisebb

def osszeg(lista):
    osszeg = 0 
    for i in lista:
        osszeg += i
    return osszeg

def szorzat(lista):
    szorzat = 1
    for i in lista:
        szorzat *= i
    return szorzat

def legnagyobb(lista):
    legnagyobb = lista[0]
    for i in lista:
        if i > legnagyobb:
            legnagyobb = i
    return legnagyobb

def parosok_szama(lista):
    szamlalo = 0
    for i in lista:
        if i % 2 == 0:
            szamlalo += 1
    return szamlalo

def legelso(lista):
    return lista[0]

def utolso(lista):
    return lista[-1]

def elso_ketto(lista):
    listaa = [lista[0],lista[1]]
    return listaa

def elso_utolso(lista):
    listaaa = [lista[0],lista[-1]]
    return listaaa
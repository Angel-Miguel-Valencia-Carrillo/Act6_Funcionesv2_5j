print("Funciones version 2")
print("Angel Valencia")
# zona de listas tuplas: sets: diccionario
celulares=["Samsung a52", "Iphone 11", "chafa"]
nombredefutbolistas=("Neymar","Mbappe","Cr7")
juegosfamosos={"fifa", "dragon ball", "clash royale"}
datos = {
  "Nombre": "Angel",
  "Apellido": "Valencia",
  "Edad": 17
}
# zona de funciones
def verlista(telefonos):
    for uncelular in telefonos:
        print(uncelular)
def vertuplas(futbolistas):
    for unfutbolista in futbolistas:
        print(unfutbolista)
def versets(juegos):
    for unjuego in juegos:
        print(unjuego)
def verdiccionario(informacion):
    for undato in informacion:
        print(undato)
# Llamar a funciones
print("imprime celulares de una lista")
verlista(celulares)
print("imprime nombres de futbolistas tupla")
vertuplas(nombredefutbolistas)
print("Imprime juegos sets")
versets(juegosfamosos)
print("Imprime datos diccionario")
verdiccionario(datos)

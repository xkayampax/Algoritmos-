cadenan = input("Ingrese una cadena de texto: ")
ecadena = cadenan.strip()
ncadena = ecadena.split()
totalc = len(ncadena)
cadenam = []
for ncadenas in ncadena:
    cadenam.append(ncadenas.upper())
print("Total de palabras:", totalc)
opcion = int(input(f"Elija un número del 1 al {totalc}: "))
if opcion >= 1 and opcion <= totalc:
    seleccionada = cadenam[opcion - 1]
    print("Cadena seleccionada:", seleccionada)
else:
    print("Numero fuera de rango.")







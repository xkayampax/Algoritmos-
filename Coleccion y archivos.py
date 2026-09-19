import csv
 
datos = [
    {"nombre": "Ana Pérez", "nota": 95, "carnet": "26-16-27159", "curso": "algoritmos"},
    {"nombre": "Luis García", "nota": 88, "carnet": "21-15-28150", "curso": "algoritmos"},
    {"nombre": "Juan Lopez", "nota": 77, "carnet": "20-15-29151", "curso": "algoritmos"},
    {"nombre": "Cristhian Torres", "nota": 90, "carnet": "23-14-21257", "curso": "algoritmos"},
]
 
with open("notas.csv", "w", newline="", encoding="utf-8") as archivo:
    escritor = csv.DictWriter(archivo, fieldnames=["nombre", "carnet", "curso", "nota"])
    escritor.writeheader()
    escritor.writerows(datos)


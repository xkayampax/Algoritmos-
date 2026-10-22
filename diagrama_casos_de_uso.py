class Anfitrion:

    def __init__(self, nombre_anfitrion):
        self.nombre = nombre_anfitrion

    def realizar_invitaciones(self):
        print(f"{self.nombre} está realizando invitaciones")

    def preparar_claves(self):
        print(f"{self.nombre} está preparando claves")

    def comprar_alimento(self):
        print(f"{self.nombre} está comprando alimentos")

    def hacer_presupuesto(self):
        print(f"{self.nombre} está realizando el presupuesto")

andres = Anfitrion("Andres")

andres.hacer_presupuesto()
andres.realizar_invitaciones()
andres.preparar_claves()
andres.comprar_alimento()



class Invitado:

    def __init__(self, nombre_invitado):
        self.nombre = nombre_invitado

    def consumir_alimentos(self):
        print(f"{self.nombre} está comiendo")

    def ir_a_la_fiesta(self):
        print(f"{self.nombre} está yendo a la fiesta")

    def llevar_carnet(self):
        print(f"{self.nombre} está mostrando su carnet")

juanito = Invitado("Juanito")
pablo = Invitado("Pablo")

juanito.ir_a_la_fiesta()
juanito.llevar_carnet()
juanito.consumir_alimentos()
pablo.ir_a_la_fiesta()
pablo.llevar_carnet()
pablo.consumir_alimentos()



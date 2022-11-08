class Persona:
    def __init__(self):
        self.nombre=input("Ingrese el nombre: ")
        
 
    def mostrar(self):
        print("Nombre: ",self.nombre)
 
class Empleado(Persona):
    def __init__(self):
        super().__init__()
        self.nota=int(input("Ingrese la nota: "))
 
    def mostrar(self):
        print("Nota: ",self.nota)
        
    def pagar_impuestos(self):
        if self.nota >= 3:
            print("Su no ta es ",self.nota," Ha aprobado")
        else:
            print("Su no ta es ",self.nota," no aprobo")
 
empleado1=Empleado()
empleado1.mostrar()
empleado1.pagar_impuestos()

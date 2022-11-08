class Calculadora:
    def __init__(self):
        self.n1=int(input("Ingrese el primer numero: "))
        self.n2=int(input("Ingrese el segundo numero: "))
        self.multiplicacion=self.n1*self.n2
        self.suma=self.n1+self.n2
        self.resta=self.n1-self.n2
        self.division=self.n1/self.n2

 
 
    def mostrar(self):
        print("Suma: ",self.suma)
        print("Resta: ",self.resta)
        print("Multiplicacion: ",self.multiplicacion)
        print("Division: ",self.division)
        


calculdora1=Calculadora()
calculdora1.mostrar()

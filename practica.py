#crea una clase llamada Producto
#nombre, unidades y precio
#creas un producto camisa, 10, 9.95 de precio
#muestra el nombre de producto por consola

#crea un método de infoProducto. Muestra el nombre, unidades, precio y inventario valorado (uxp)

#práctica de sobreescritura.
#crea una clase llamada Servicio
#tiene un método llamado consultarDetalle que muestra. el servicio es básico.
#la empresa tiene dos servicios. estándar y premium. Son dos clases que derivan de Servicio
#la clase Estandar y Premium tienen un método llamado consultarDetalle y explican que son servicio estándar y premium respectivamente.
#pide por consola un servicio. Elegimos premium y te muestra el resultado de consultarDetalle

class Producto:
    def __init__(self,nombre,unidades,precio):
        self.nombre=nombre
        self.unidades=unidades
        self.precio=precio
    def infoProducto(self):
        print(f'Ha comprado usted {self.unidades} {self.nombre}, a {self.precio}€ ; el total de su compra es {self.unidades * self.precio}')

prd1=Producto('camisas', 10, 9.95)
prd1.infoProducto()


class Servicio:
    def consultarDetalle(self):
        print('El servicio es básico')

class Estandar(Servicio):
    def consultarDetalle(self):
        print('Ha seleccionado servicio estandar')

class Premium(Servicio):
    def consultarDetalle(self):
        print('Ha seleccionado servicio premium')

hh=Premium()
hh.consultarDetalle()
jj=Estandar()
jj.consultarDetalle()
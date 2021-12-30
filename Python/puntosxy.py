import math

class Punto:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __str__(self):
        return "({}, {})".format(self.x, self.y)

    def cuadrante(self):
        if self.x > 0 and self.y > 0:
            print("{} esta en el primer cuadrante".format(self))
        elif self.x < 0 and self.y > 0:
            print("{} esta en el segundo cuadrante".format(self))
        elif self.x < 0 and self.y < 0:
            print("{} esta en el tercer cuadrante".format(self))
        elif self.x > 0 and self.y < 0:
            print("{} esta en el cuarto cuadrante".format(self))
        elif self.x != 0 and self.y == 0:
            print("{} esta sobre el eje X".format(self))
        elif self.x == 0 and self.y != 0:
            print("{} esta sobre el eje Y".format(self))
        else:
            print("{} esta sobre el origen".format(self))

    def vector(self, p):
        print("El vector entre {} y {} es ({}, {})".format(
            self, p, p.x - self.x, p.y - self.y) )

    def distancia(self, p):
        d = math.sqrt( (p.x - self.x)**2 + (p.y - self.y)**2 )
        print("La distancia entre  {} y {} es {}".format( self, p, d))


class Rectangulo:

    def __init__(self, pInicial=Punto(), pFinal=Punto()):
        self.pInicial = pInicial
        self.pFinal = pFinal

        self.vBase = abs(self.pFinal.x - self.pInicial.x)
        self.vAltura = abs(self.pFinal.y - self.pInicial.y)
        self.vArea = self.vBase * self.vAltura

    def base(self):
        print("La base  es {}".format( self.vBase ) )

    def altura(self):
        print("La altura es {}".format( self.vAltura ) )

    def area(self):
        print("El Area es {}".format( self.vArea ) )


A = Punto(2,3)
B = Punto(5,5)
C = Punto(-3, -1)
D = Punto(0,0)

A.cuadrante()
C.cuadrante()
D.cuadrante()

A.vector(B)
B.vector(A)

A.distancia(B)
B.distancia(A)

A.distancia(D)
B.distancia(D)
C.distancia(D)

R = Rectangulo(A, B)
R.base()
R.altura()
R.area()
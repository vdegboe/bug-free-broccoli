from cmath import sqrt
import matplotlib.pyplot as plt  # type:ignore


class Poly2:
    """ Classe permettant de representer un polynôme de degré 2."""

    def __init__(self, *coeffs):
        """ Méthode constructeur qui prend en paramètre, les coefficients du polynôme"""
        self.coeffs=list(coeffs) #pass


    def __add__(self, other):
        """Addition 2 polynômes et qui renvoi du nouveau polynôme"""
        for i in range(0,len(self.coeffs)):
            self.coeffs[i]+=other.coeffs[i]
        return self
        #pass

    def __sub__(self, other):
        """Soustraction de 2 polynômes et renvoi du nouveau polynôme"""
        for i in range(0,len(self.coeffs)):
            self.coeffs[i]-=other.coeffs[i]
        return self
        #pass

    def __repr__(self):
        """Méthode qui affiche les coefficient du polynôme dans l'odre croissant
        """
        msg = 'Poly2(' + ', '.join([str(c) for c in sorted(self.coeffs)]) + ')'
        return msg
        

    def __str__(self):
        """Méthode qui personalise la chaîne de caractère affichée par la fonction print
        Si: p1 = Poly(3, -4, 2)
        Alors print(p1) affiche: '2X^2 - 4X + 3'
        """
        return f"{self.coeffs[0]}X^2 + {self.coeffs[1]}X + {self.coeffs[2]}"#pass

    def solve(self):
        """ Méthode qui renvoie les solutions si elles existent."""
        delta= (self.coeffs[1]**2-(4*self.coeffs[0]*self.coeffs[2]))
        if delta < 0:
            return f"delta inférieur à zéro. \n Pas de solution"
        elif delta == 0:
            sol=-self.coeffs[1]/(2*self.coeffs[0])
            return f"Solution double: {sol}"
        else:
            sol1=(-self.coeffs[1]-sqrt(delta))/(2*self.coeffs[0])
            sol2=(-self.coeffs[1]+sqrt(delta))/(2*self.coeffs[0])
            return f"Deux solutions:\n - X1={sol1}\n - X2={sol2}"
        #pass

    def val(self, x):
        """ Méthode qui calcule et renvoie la valeur de y en fonction de x.
        Si: y = x^2 + 1
        Si: x prend pour valeur 5
        Alors: y = 5^2 + 1 = 26
        """
        y = self.coeffs[0]*x**2+self.coeffs[1]*x+self.coeffs[2]
        return f"y = {y} pour x = {x}" #pass

    def draw(self, x_points=None):
        """ Méthode qui trace la courbe, voir fichier png."""
        #pass


if __name__ == "__main__":
    bar = [1, 1, 1]
    p1 = Poly2(*bar)
    
        
    baz = [1, 1, 1]
    p2 = Poly2(*baz)
    

    p3 = p1 + p2
    print(p3)  # affiche 2x^2 + 2x + 2
    

    print(p3.solve())  # affiche ((-0.5+0.8660254037844386j), (-0.5-0.8660254037844386j))
    p1.draw()  # trace la courbe de p1, voir fichier png

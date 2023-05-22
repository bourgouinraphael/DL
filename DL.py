from fractions import Fraction as F


class DL(list):
    """Représentation d'un DL en 0 sous forme de liste où les x sont rangés par degrés croissants

    Attributs:
        DL (list): coefficients du DL
        ordre (int): ordre du DL
    """

    def __init__(self, DL):
        """Le constructeur de la classe DL

        Args:
            DL (list(str)): coefficients du DL
        """
        super().__init__()
        self.DL = []
        for element in DL:
            if isinstance(element, str):
                i = element.split("/")
                if len(i) == 1:
                    self.DL.append(
                        F(int(i[0]))
                    )
                else:
                    self.DL.append(
                        F(int(i[0]), int(i[1]))
                    )
            else:
                self.DL.append(element)
        self.ordre = len(DL)

    def __add__(self, Q):
        """Permet de faire la somme de 2 DL en 0 donnés en entrée sous forme de liste.
        L'ordre du DL renvoyé sera le plus petit entre self et Q.

        Args:
            Q (DL): DL à ajouter à self

        Returns:
            DL: somme de self et Q.
        """
        n = min(self.ordre, Q.ordre)
        return DL([self.DL[i] + Q.DL[i] for i in range(n)])

    def __sub__(self, Q):
        return self + -1*Q

    def __mul__(self, Q):
        if type(Q) in (float, int):
            return self.scalaire(Q)
        else:
            return self.fois(Q)

    def __rmul__(self, Q):
        if type(Q) in (float, int):
            return self.scalaire(Q)
        else:
            return self.fois(Q)

    def fois(self, Q : list):
        """Permet de faire le produit de 2 DL en 0 donnés en entrée sous forme de liste.
        L'ordre du DL renvoyé sera le plus petit entre self et Q.

        Args:
            Q (DL): DL à multiplier à self

        Returns:
            DL: produit de self et Q.
        """
        n = min(self.ordre, Q.ordre)
        result = []
        for k in range(n):
            s = 0
            for l in range(k + 1):
                s += self.DL[l] * Q.DL[k - l]  # x^l * x^(k-l) = x^k
            result.append(s)
        return DL(result)

    def scalaire(self, a: float):
        """Multiplie un DL par un scalaire

        Args:
            a (float): le scalaire
        """
        return DL([a * element for element in self.DL])

    def __pow__(self, n):
        return self.puissance(n)

    def puissance(self, n):
        """Renvoie le DL a une certaine puissance

        Args:
            n (int): puissance

        Returns:
            DL
        """
        if n == 0:
            return DL(["1"])
        elif n == 1:
            return self
        else:
            return self * self.puissance(n - 1)

    def inversed(self):
        """Renvoie l'inverse du DL en passant par 1/(1+u) avec self ne s'annulant pas en 0"""
        coef = self.DL[0]
        P = DL(self.DL)
        P.DL[0] = F(0)
        P.scalaire(1 / coef)
        result = DL([1] + [0] * (self.ordre - 1))
        for i in range(1, P.ordre):
            result = result + (P * (-1)**i) ** i
        return result.scalaire(coef)

    def __truediv__(self, Q):
        """Renvoie le DL de self sur Q

        Args:
            Q (DL)
        """
        if type(Q) in (int, float):
            return self * 1/Q
        return self * Q.inversed()

    def __rtruediv__(self, Q):
        """Renvoie le DL de Q sur self

            Args:
                Q (DL)
            """
        return self.inversed() * Q

    def __str__(self) -> str:
        result = ""
        for i, element in enumerate(self.DL):
            if element != 0:
                if i == 0:
                    result += element.__str__() + " "
                elif element > 0:
                    result += "+" + element.__str__() + f'*x^{i} '
                else:
                    result += element.__str__() + f'*x^{i} '
        return str(result)


if __name__ == "__main__":
    DL4_exp = DL(["1", "1", "1/2", "1/6", "1/24"])
    DL4_cos = DL(["1", "0", "-1/2", "0", "1/24"])
    exp_cos = DL4_exp - DL4_cos
    print(f"e^x - cos(x)= {exp_cos}")
    DL4_ln = DL(["0", "1", "-1/2", "1/3", "-1/4"])
    DL4_sh = DL(["0", "1", "0", "1/6", "0"])
    P = DL4_ln * DL4_sh
    print(f"ln(1+x)*sh(x) = {P}")
    print(f"2*ln(1+x)*sh(x) = {2*P}")
    print(f"(e^x + cos(x))^3 = {exp_cos**3}")
    print(f"1/cos(x) = {2/DL4_cos}")
    print(f"e^x / cos(x) = {DL4_exp/DL4_cos}")
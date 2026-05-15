from enum import Enum


class TipoTriangulo(Enum):
    EQUILATERO = "Equilátero"
    ISOSCELES = "Isósceles"
    ESCALENO = "Escaleno"


class Triangulo:
    def classificar(self, a: int, b: int, c: int) -> TipoTriangulo:
        
        if a <= 0 or b <= 0 or c <= 0:
            raise ValueError("Os lados devem ser maiores que zero.")

        if (a + b) <= c or (a + c) <= b or (b + c) <= a:
            raise ValueError("Os lados não formam um triângulo válido (condição triangular não satisfeita).")

        if a == b == c:
            return TipoTriangulo.EQUILATERO
        elif a == b or b == c or a == c:
            return TipoTriangulo.ISOSCELES
        else:
            return TipoTriangulo.ESCALENO
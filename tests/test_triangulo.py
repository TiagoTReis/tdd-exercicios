import pytest
from exercicio1.triangulo import Triangulo, TipoTriangulo


class TestTriangulo:
    def setup_method(self):
        self.triangulo = Triangulo()

    # CT01 - Triângulo escaleno válido
    def test_triangulo_escaleno_valido(self):
        resultado = self.triangulo.classificar(3, 4, 5)
        assert resultado == TipoTriangulo.ESCALENO

    # CT02 - Triângulo isósceles válido
    def test_triangulo_isosceles_valido(self):
        resultado = self.triangulo.classificar(5, 5, 3)
        assert resultado == TipoTriangulo.ISOSCELES

    # CT03 - Triângulo equilátero válido
    def test_triangulo_equilatero_valido(self):
        resultado = self.triangulo.classificar(6, 6, 6)
        assert resultado == TipoTriangulo.EQUILATERO

    # CT04 - Isósceles: permutação 1 (a == b)
    def test_isosceles_permutacao_ab(self):
        resultado = self.triangulo.classificar(8, 8, 5)
        assert resultado == TipoTriangulo.ISOSCELES

    # CT05 - Isósceles: permutação 2 (a == c)
    def test_isosceles_permutacao_ac(self):
        resultado = self.triangulo.classificar(5, 3, 5)
        assert resultado == TipoTriangulo.ISOSCELES

    # CT06 - Isósceles: permutação 3 (b == c)
    def test_isosceles_permutacao_bc(self):
        resultado = self.triangulo.classificar(3, 5, 5)
        assert resultado == TipoTriangulo.ISOSCELES

    # CT07 - Um valor zero
    def test_lado_zero(self):
        with pytest.raises(ValueError):
            self.triangulo.classificar(0, 4, 5)

    # CT08 - Um valor negativo
    def test_lado_negativo(self):
        with pytest.raises(ValueError):
            self.triangulo.classificar(-1, 4, 5)

    # CT09 - Soma de 2 lados igual ao terceiro (a + b == c)
    def test_soma_dois_lados_igual_terceiro_ab_c(self):
        with pytest.raises(ValueError):
            self.triangulo.classificar(3, 4, 7)

    # CT10 - Permutação: a + c == b
    def test_soma_dois_lados_igual_terceiro_ac_b(self):
        with pytest.raises(ValueError):
            self.triangulo.classificar(3, 7, 4)

    # CT11 - Permutação: b + c == a
    def test_soma_dois_lados_igual_terceiro_bc_a(self):
        with pytest.raises(ValueError):
            self.triangulo.classificar(7, 3, 4)

    # CT12 - Soma de 2 lados menor que o terceiro (a + b < c)
    def test_soma_dois_lados_menor_terceiro_ab_c(self):
        with pytest.raises(ValueError):
            self.triangulo.classificar(1, 2, 10)

    # CT13 - Permutação: a + c < b
    def test_soma_dois_lados_menor_terceiro_ac_b(self):
        with pytest.raises(ValueError):
            self.triangulo.classificar(1, 10, 2)

    # CT14 - Permutação: b + c < a
    def test_soma_dois_lados_menor_terceiro_bc_a(self):
        with pytest.raises(ValueError):
            self.triangulo.classificar(10, 1, 2)

    # CT15 - Três valores iguais a zero
    def test_todos_lados_zero(self):
        with pytest.raises(ValueError):
            self.triangulo.classificar(0, 0, 0)
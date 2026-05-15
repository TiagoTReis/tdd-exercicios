import pytest
from exercicio3.calculadora_salario import CalculadoraSalario, Funcionario, Cargo


class TestCalculadoraSalario:
    def setup_method(self):
        self.calc = CalculadoraSalario()

    # CT01 - Desenvolvedor com salário >= 3000 (desconto 20%)
    def test_desenvolvedor_salario_alto(self):
        f = Funcionario("Ana Lima", "ana@dev.com", 3000.00, Cargo.DESENVOLVEDOR)
        assert self.calc.calcular_salario_liquido(f) == pytest.approx(2400.00)

    # CT02 - Desenvolvedor com salário > 3000 (desconto 20%)
    def test_desenvolvedor_salario_acima_limite(self):
        f = Funcionario("Ana Lima", "ana@dev.com", 5000.00, Cargo.DESENVOLVEDOR)
        assert self.calc.calcular_salario_liquido(f) == pytest.approx(4000.00)

    # CT03 - Desenvolvedor com salário < 3000 (desconto 10%)
    def test_desenvolvedor_salario_baixo(self):
        f = Funcionario("Pedro Costa", "pedro@dev.com", 2000.00, Cargo.DESENVOLVEDOR)
        assert self.calc.calcular_salario_liquido(f) == pytest.approx(1800.00)

    # CT04 - DBA com salário >= 2000 (desconto 25%)
    def test_dba_salario_alto(self):
        f = Funcionario("Maria DBA", "maria@db.com", 2000.00, Cargo.DBA)
        assert self.calc.calcular_salario_liquido(f) == pytest.approx(1500.00)

    # CT05 - DBA com salário > 2000 (desconto 25%)
    def test_dba_salario_acima_limite(self):
        f = Funcionario("Maria DBA", "maria@db.com", 4000.00, Cargo.DBA)
        assert self.calc.calcular_salario_liquido(f) == pytest.approx(3000.00)

    # CT06 - DBA com salário < 2000 (desconto 15%)
    def test_dba_salario_baixo(self):
        f = Funcionario("Carlos DBA", "carlos@db.com", 1500.00, Cargo.DBA)
        assert self.calc.calcular_salario_liquido(f) == pytest.approx(1275.00)

    # CT07 - Testador com salário >= 2000 (desconto 25%)
    def test_testador_salario_alto(self):
        f = Funcionario("Julia QA", "julia@qa.com", 2000.00, Cargo.TESTADOR)
        assert self.calc.calcular_salario_liquido(f) == pytest.approx(1500.00)

    # CT08 - Testador com salário > 2000 (desconto 25%)
    def test_testador_salario_acima_limite(self):
        f = Funcionario("Julia QA", "julia@qa.com", 3000.00, Cargo.TESTADOR)
        assert self.calc.calcular_salario_liquido(f) == pytest.approx(2250.00)

    # CT09 - Testador com salário < 2000 (desconto 15%)
    def test_testador_salario_baixo(self):
        f = Funcionario("Bruno QA", "bruno@qa.com", 1000.00, Cargo.TESTADOR)
        assert self.calc.calcular_salario_liquido(f) == pytest.approx(850.00)

    # CT10 - Gerente com salário >= 5000 (desconto 30%)
    def test_gerente_salario_alto(self):
        f = Funcionario("Sônia Gerente", "sonia@mgmt.com", 5000.00, Cargo.GERENTE)
        assert self.calc.calcular_salario_liquido(f) == pytest.approx(3500.00)

    # CT11 - Gerente com salário > 5000 (desconto 30%)
    def test_gerente_salario_acima_limite(self):
        f = Funcionario("Sônia Gerente", "sonia@mgmt.com", 8000.00, Cargo.GERENTE)
        assert self.calc.calcular_salario_liquido(f) == pytest.approx(5600.00)

    # CT12 - Gerente com salário < 5000 (desconto 20%)
    def test_gerente_salario_baixo(self):
        f = Funcionario("Roberto Gerente", "roberto@mgmt.com", 4000.00, Cargo.GERENTE)
        assert self.calc.calcular_salario_liquido(f) == pytest.approx(3200.00)

    # CT13 - Funcionário nulo
    def test_funcionario_nulo(self):
        with pytest.raises(ValueError):
            self.calc.calcular_salario_liquido(None)

    # CT14 - Cargo nulo
    def test_cargo_nulo(self):
        f = Funcionario("Alguém", "a@b.com", 3000.00, None)
        with pytest.raises(ValueError):
            self.calc.calcular_salario_liquido(f)

    # CT15 - Salário negativo
    def test_salario_negativo(self):
        f = Funcionario("Alguém", "a@b.com", -100.00, Cargo.DESENVOLVEDOR)
        with pytest.raises(ValueError):
            self.calc.calcular_salario_liquido(f)

    # CT16 - Salário nulo
    def test_salario_nulo(self):
        f = Funcionario("Alguém", "a@b.com", None, Cargo.DESENVOLVEDOR)
        with pytest.raises(ValueError):
            self.calc.calcular_salario_liquido(f)

    # CT17 - Arredondamento de casas decimais
    def test_arredondamento(self):
        f = Funcionario("Dev Decimal", "dev@dev.com", 1999.99, Cargo.DESENVOLVEDOR)
        resultado = self.calc.calcular_salario_liquido(f)
        assert resultado == round(1999.99 * 0.90, 2)

    def test_cargo_desconhecido(self):
        f = Funcionario("Teste", "teste@email.com", 1000.00, "INVALIDO")

        with pytest.raises(ValueError):
            self.calc.calcular_salario_liquido(f)    
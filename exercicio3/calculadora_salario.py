from enum import Enum
from decimal import Decimal, ROUND_HALF_UP


class Cargo(Enum):
    DESENVOLVEDOR = "DESENVOLVEDOR"
    DBA = "DBA"
    TESTADOR = "TESTADOR"
    GERENTE = "GERENTE"


class Funcionario:
    def __init__(self, nome: str, email: str, salario_base: float, cargo: Cargo):
        self.nome = nome
        self.email = email
        self.salario_base = salario_base
        self.cargo = cargo


class CalculadoraSalario:

    def calcular_salario_liquido(self, funcionario: Funcionario) -> float:
        """
        Calcula o salário líquido de um funcionário com base no cargo e salário base.

        Raises:
            ValueError: se o funcionário, cargo ou salário base forem inválidos.
        """
        self._validar_funcionario(funcionario)

        desconto = self._obter_desconto(
            funcionario.cargo,
            funcionario.salario_base
        )

        salario_liquido = funcionario.salario_base * (1 - desconto)

        return float(
            Decimal(str(salario_liquido)).quantize(
                Decimal("0.01"),
                rounding=ROUND_HALF_UP
            )
        )

    def _validar_funcionario(self, funcionario: Funcionario) -> None:
        if funcionario is None:
            raise ValueError("O funcionário não pode ser nulo.")

        if funcionario.cargo is None:
            raise ValueError("O cargo não pode ser nulo.")

        if (
            funcionario.salario_base is None
            or funcionario.salario_base < 0
        ):
            raise ValueError(
                "O salário base não pode ser nulo ou negativo."
            )

    def _obter_desconto(self, cargo: Cargo, salario: float) -> float:

        if cargo == Cargo.DESENVOLVEDOR:
            return 0.20 if salario >= 3000.00 else 0.10

        if cargo in (Cargo.DBA, Cargo.TESTADOR):
            return 0.25 if salario >= 2000.00 else 0.15

        if cargo == Cargo.GERENTE:
            return 0.30 if salario >= 5000.00 else 0.20

        raise ValueError(f"Cargo desconhecido: {cargo}")
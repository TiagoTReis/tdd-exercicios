import re
from typing import List


class Email:
    def __init__(self, endereco: str):
        self.endereco = endereco


class Person:
    def __init__(self, nome: str, idade: int, emails: List[Email] = None):
        self.nome = nome
        self.idade = idade
        self.emails = emails or []

    def is_valid_to_include(self) -> List[str]:
        """
        Valida o objeto Person e retorna uma lista de erros encontrados.
        Lista vazia significa que o objeto é válido.
        """
        erros = []

        erros.extend(self._validar_nome())
        erros.extend(self._validar_idade())
        erros.extend(self._validar_emails())

        return erros

    def _validar_nome(self) -> List[str]:
        erros = []

        if not self.nome or not self.nome.strip():
            erros.append("O nome não pode ser vazio.")
            return erros

        partes = self.nome.strip().split()

        if len(partes) < 2:
            erros.append("O nome deve ser composto por ao menos 2 partes.")

        for parte in partes:
            if not re.match(r"^[a-zA-ZÀ-ÿ]+$", parte):
                erros.append("O nome deve ser composto apenas de letras.")
                break

        return erros

    def _validar_idade(self) -> List[str]:
        erros = []

        if self.idade is None or not (1 <= self.idade <= 200):
            erros.append("A idade deve estar no intervalo [1, 200].")

        return erros

    def _validar_emails(self) -> List[str]:
        erros = []

        if not self.emails:
            erros.append("O objeto Person deve ter pelo menos um Email associado.")
            return erros

        padrao = re.compile(r"^.+@.+\..+$")

        if any(not padrao.match(email.endereco) for email in self.emails):
            erros.append(
                "O email deve estar no formato usuario@dominio.extensao, "
                "com ao menos um caractere em cada parte."
            )

        return erros
    
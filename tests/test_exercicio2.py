import pytest
from exercicio2.person import Person, Email


class TestPerson:

    # CT01 - Person válido
    def test_person_valido(self):
        person = Person("João Silva", 25, [Email("joao@email.com")])
        erros = person.is_valid_to_include()
        assert erros == []

    # CT02 - Nome com apenas uma parte
    def test_nome_uma_parte(self):
        person = Person("João", 25, [Email("joao@email.com")])
        erros = person.is_valid_to_include()
        assert any("ao menos 2 partes" in e for e in erros)

    # CT03 - Nome com número
    def test_nome_com_numero(self):
        person = Person("João2 Silva", 25, [Email("joao@email.com")])
        erros = person.is_valid_to_include()
        assert any("letras" in e for e in erros)

    # CT04 - Nome com caractere especial
    def test_nome_com_caractere_especial(self):
        person = Person("João@ Silva", 25, [Email("joao@email.com")])
        erros = person.is_valid_to_include()
        assert any("letras" in e for e in erros)

    # CT05 - Nome vazio
    def test_nome_vazio(self):
        person = Person("", 25, [Email("joao@email.com")])
        erros = person.is_valid_to_include()
        assert len(erros) > 0

    # CT06 - Idade abaixo do intervalo (0)
    def test_idade_zero(self):
        person = Person("João Silva", 0, [Email("joao@email.com")])
        erros = person.is_valid_to_include()
        assert any("idade" in e for e in erros)

    # CT07 - Idade negativa
    def test_idade_negativa(self):
        person = Person("João Silva", -1, [Email("joao@email.com")])
        erros = person.is_valid_to_include()
        assert any("idade" in e for e in erros)

    # CT08 - Idade acima do intervalo (201)
    def test_idade_acima_limite(self):
        person = Person("João Silva", 201, [Email("joao@email.com")])
        erros = person.is_valid_to_include()
        assert any("idade" in e for e in erros)

    # CT09 - Idade no limite inferior válido (1)
    def test_idade_limite_inferior_valido(self):
        person = Person("João Silva", 1, [Email("joao@email.com")])
        erros = person.is_valid_to_include()
        assert erros == []

    # CT10 - Idade no limite superior válido (200)
    def test_idade_limite_superior_valido(self):
        person = Person("João Silva", 200, [Email("joao@email.com")])
        erros = person.is_valid_to_include()
        assert erros == []

    # CT11 - Sem emails
    def test_sem_emails(self):
        person = Person("João Silva", 25, [])
        erros = person.is_valid_to_include()
        assert any("Email" in e for e in erros)

    # CT12 - Emails nulos
    def test_emails_nulos(self):
        person = Person("João Silva", 25, None)
        erros = person.is_valid_to_include()
        assert any("Email" in e for e in erros)

    # CT13 - Email sem @
    def test_email_sem_arroba(self):
        person = Person("João Silva", 25, [Email("joaoemail.com")])
        erros = person.is_valid_to_include()
        assert any("email" in e.lower() for e in erros)

    # CT14 - Email sem ponto após @
    def test_email_sem_ponto(self):
        person = Person("João Silva", 25, [Email("joao@emailcom")])
        erros = person.is_valid_to_include()
        assert any("email" in e.lower() for e in erros)

    # CT15 - Email sem parte antes do @
    def test_email_sem_usuario(self):
        person = Person("João Silva", 25, [Email("@email.com")])
        erros = person.is_valid_to_include()
        assert any("email" in e.lower() for e in erros)

    # CT16 - Email sem parte após o ponto
    def test_email_sem_extensao(self):
        person = Person("João Silva", 25, [Email("joao@email.")])
        erros = person.is_valid_to_include()
        assert any("email" in e.lower() for e in erros)

    # CT17 - Múltiplos erros ao mesmo tempo
    def test_multiplos_erros(self):
        person = Person("João", -5, [])
        erros = person.is_valid_to_include()
        assert len(erros) >= 3

    # CT18 - Nome com acentuação válida (deve ser aceito)
    def test_nome_com_acentuacao(self):
        person = Person("Ângela Müller", 30, [Email("angela@email.com")])
        erros = person.is_valid_to_include()
        assert erros == []
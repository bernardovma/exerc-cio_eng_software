import re

class TratamentoDeCPF:
    """
    Classe para tratar o CPF.

    Atributos:
    cpf (str): CPF fornecido pelo usuário.
    cpf_tratado (str): CPF tratado, sem caracteres especiais.
    """
    def __init__(self, cpf) -> None:
        """
        Construtor da classe TratamentoDeCPF.
        
        Parâmetros:
        cpf (str): CPF fornecido pelo usuário.
        """
        self.cpf = cpf
        self.cpf_tratado = self.tratar_cpf(cpf)

    def tratar_cpf(self, cpf) -> str:
        """
        Método para tratar o CPF fornecido pelo usuário.

        Parâmetros:
        cpf (str): CPF fornecido pelo usuário.

        Retorno:
        str: CPF tratado, sem caracteres especiais.
        """
        return re.sub(r"\D", "", cpf)

class CPFValidator(TratamentoDeCPF):
    """
    Classe para validar o CPF.
   
    Atributos:
    cpf (str): CPF fornecido pelo usuário.
    cpf_tratado (str): CPF tratado, sem caracteres especiais.
    """ 
    def __init__(self, cpf) -> None:
        """
        Construtor da classe CPFValidator.

        Parâmetros:
        cpf (str): CPF fornecido pelo usuário.
        """

        # Chamando o construtor da classe de TratamentoDeCPF para tratar o CPF fornecido pelo usuário.
        super().__init__(cpf)
        self.cpf = self.cpf_tratado

    def digitos_verificadores(self) -> tuple:
        """
        Método para calcular os dígitos verificadores do CPF. Utiliza o cpf tratado fornecido pelo usuário no construtor da classe.

        Retorno:
        tuple: Dígitos verificadores do CPF.
        """
        cpf_sem_digitos_verificadores = self.cpf[:9]
        nr_digitos = 10
        digito_calculado = 0

        for cada_digito in cpf_sem_digitos_verificadores:
            digito_calculado += int(cada_digito) * nr_digitos
            nr_digitos -= 1

            digito_verificador_1 = (digito_calculado * 10) % 11

        if digito_verificador_1 <= 9:
            digito_verificador_1 = digito_verificador_1
        else:
            digito_verificador_1 = 0

        cpf_com_um_digito_verificador = cpf_sem_digitos_verificadores + str(digito_verificador_1)
        nr_digitos = 11

        digito_calculado = 0

        for cada_digito in cpf_com_um_digito_verificador:
            digito_calculado += int(cada_digito) * nr_digitos
            nr_digitos -= 1

        digito_verificador_2 = (digito_calculado * 10) % 11

        if digito_verificador_2 <= 9:
            digito_verificador_2 = digito_verificador_2
        else:
            digito_verificador_2 = 0

        return digito_verificador_1, digito_verificador_2
    
    def cpf_valido(self) -> bool:
        """
        Método para validar o CPF fornecido pelo usuário.

        Retorno:
        bool: True se o CPF for válido, False se o CPF for inválido.
        """
        if self.cpf == self.cpf[0] * len(self.cpf):
            return False
        
        else:
            digito_verificador_1, digito_verificador_2 = self.digitos_verificadores()

        return int(self.cpf[9]) == digito_verificador_1 and int(self.cpf[10]) == digito_verificador_2

def main() -> None:
    cpf_fornecido = input("Formato para inserir CPF - XXX.XXX.XXX-XX: ")

    cpf_validator = CPFValidator(cpf_fornecido)
    
    if cpf_validator.cpf_valido():
        print("CPF é válido")
    else:
        print("CPF inválido")

if __name__ == "__main__":
    main()

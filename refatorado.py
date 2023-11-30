import re

class CPFValidator:
   
    def __init__(self, cpf):
        self.cpf = self.cpf_limpo(cpf)

    def cpf_limpo(self, cpf):
        return re.sub(r"[^0-9]", "", cpf)

    def digitos_verificadores(self):
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
    
    def cpf_valido(self):
        if self.cpf == self.cpf[0] * len(self.cpf):
            return False
        
        else:
            digito_verificador_1, digito_verificador_2 = self.digitos_verificadores()

        return int(self.cpf[9]) == digito_verificador_1 and int(self.cpf[10]) == digito_verificador_2

def main():

    cpf_fornecido = input("Formato para inserir CPF - XXX.XXX.XXX-XX: ")
    
    cpf_validator = CPFValidator(cpf_fornecido)
    
    if cpf_validator.cpf_valido():
        print("CPF é válido")
    else:
        print("CPF inválido")

if __name__ == "__main__":
    main()

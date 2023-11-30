import unittest
from refatorado import CPFValidator

class TestCPFValidator(unittest.TestCase):

    def teste_cpf_limpo(self):
        validator = CPFValidator("123.456.789-09")
        self.assertEqual(validator.cpf, "12345678909")

    def teste_digitos_verificadores(self):
        validator = CPFValidator("123.456.789-09")
        digito_verificador_1, digito_verificador_2 = validator.digitos_verificadores()
        self.assertEqual(digito_verificador_1, 0)
        self.assertEqual(digito_verificador_2, 9)

    def teste_cpf_e_valido_valido(self):
        validator = CPFValidator("123.456.789-09")
        self.assertTrue(validator.cpf_valido())

    def teste_cpf_e_valido_invalido(self):
        validator = CPFValidator("111.111.111-11")
        self.assertFalse(validator.cpf_valido())

if __name__ == '__main__':
    unittest.main()

import unittest
from refatorado import CPFValidator

class TestCPFValidator(unittest.TestCase):

    def teste_cpf_limpo(self):
        validator1 = CPFValidator("123.456.789-09")
        self.assertEqual(validator1.cpf, "12345678909")
        validator2 = CPFValidator("12345678909")
        self.assertEqual(validator2.cpf, "12345678909")
        validator3 = CPFValidator("123.456.789-09")
        self.assertNotEqual(validator3.cpf, "123.456.789-09")

    def teste_digitos_verificadores(self):
        validator = CPFValidator("123.456.789-09")
        digito_verificador_1, digito_verificador_2 = validator.digitos_verificadores()
        self.assertEqual(digito_verificador_1, 0)
        self.assertEqual(digito_verificador_2, 9)
        self.assertNotEqual(digito_verificador_1, 9)
        self.assertNotEqual(digito_verificador_2, 0)

    def teste_cpf_e_valido_valido(self):
        validator1 = CPFValidator("123.456.789-09")
        self.assertTrue(validator1.cpf_valido())
        validator2 = CPFValidator("161.852.727-41")
        self.assertTrue(validator2.cpf_valido())

    def teste_cpf_e_valido_invalido(self):
        validator1 = CPFValidator("111.111.111-11")
        self.assertFalse(validator1.cpf_valido())
        validator2 = CPFValidator("123.456.789-00")
        self.assertFalse(validator2.cpf_valido())

if __name__ == '__main__':
    unittest.main()

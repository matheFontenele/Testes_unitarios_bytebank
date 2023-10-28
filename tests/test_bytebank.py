import pytest

from pytest import mark
from codigo.bytebank import Funcionarios

class TestClass:
    def test_quando_idade_recebe_03_02_1997_deve_retornar_26(self):
        entrada = '03/02/1997' # Given-Contexto
        esperado = 26
        
        funcionario_teste = Funcionarios('Matheus Fontenele', entrada, 1111)
        # When-Ação
        resultado = funcionario_teste.idade()
        
        # Metodo do pytest assert que verifica se a condição é verdadeira ou não
        assert resultado == esperado # Then-Desfecho
        
    def test_quando_sobrenome_recebe_Matheus_Fontenele_deve_retornar_Fontenele(self):
        entrada = ' Matheus Fontenele ' #Given-Contexto
        esperado = 'Fontenele'
        
        matheus = Funcionarios(entrada, '03/02/1997', 1111)
        resultado = matheus.sobrenome() # When-Ação
        
        assert resultado == esperado
        
        
    def test_quando_decrescimo_salario_recebe_100000_deve_retornar_90000(self):
        entrada_salario = 100000 # Given
        entrada_nome = 'Paulo Bragança'
        esperado = 90000
        
        funcionario_teste = Funcionarios(entrada_nome, '03/02/1997', entrada_salario)
        funcionario_teste.decrescimo_salario() #When
        resultado = funcionario_teste.salario
        
        assert resultado == esperado # Then

    
    @mark.calcular_bonus
    def test_quando_calcular_bonus_recebe_1000_deve_retornar_100(self):
        entrada = 1000 # Given
        esperado = 100
        
        funcionario_teste = Funcionarios('Teste', '03/02/1997', entrada)
        resultado = funcionario_teste.calcular_bonus()# When
        
        assert resultado == esperado # Then
        
    
    @mark.calcular_bonus    
    def test_quando_calcular_bonus_recebe_1000000_deve_retornar_exception(self):
        with pytest.raises(Exception): # Um codigo que no final, vai retornar um exeception
            entrada = 1000000 # Given
        
            funcionario_teste = Funcionarios('Teste', '03/02/1997', entrada)
            resultado = funcionario_teste.calcular_bonus()# When
        
            assert resultado # Then
            

        
        
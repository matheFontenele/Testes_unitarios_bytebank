from datetime import date

# Inicialização e retorno de funções sobre os metodos principais
class Funcionarios:
    def __init__(self, nome, data_nascimento, salario):
        self._nome = nome
        self._data_nascimento = data_nascimento
        self._salario = salario
        
    @property
    def nome(self):
        return self._nome
    
    @property
    def salario(self):
        return self._salario

# Função para gerar a idade do cliente
    def idade(self):
        data_nascimento_quebrada = self._data_nascimento.split('/') # Utilizando o metodo split, estamos quebrando a string e usando, no caso, a / como parametro para quebra la
        ano_nascimento = data_nascimento_quebrada[-1] # -1 ira pegar o ultimo item da variavel data_de_nascimento_quebrada
        ano_atual = date.today().year
        return ano_atual - int(ano_nascimento) # Com o int, estou transformando a data de nascimento que vinha em string para int e assim poder fazer a operação de subtração
    
# Função para retornar o sobrenome do cliente
    def sobrenome(self):
        nome_completo = self._nome.strip()
        nome_quebrado = nome_completo.split(' ')
        return nome_quebrado[-1]
    
# Função para saber se o funcionario é ou não um socio
    def _eh_socio(self):
        sobrenomes_diretores = ['Bragança', 'Windsor', 'Bourbon', 'Yamato', 'Al Saud', 'Khan', 'Tudor', 'Ptolomeu']
        return self._salario >= 100000 and (self.sobrenome() in sobrenomes_diretores)
    
# Função para saber se salario é maior que 100000
    def decrescimo_salario(self):
        if self._eh_socio():
            decrescimo = self._salario * 0.1
            self._salario = self._salario - decrescimo
    
# Função para calcular bonus de salario
    def calcular_bonus(self):
        valor = self._salario * 0.1
        if valor > 1000:
            raise Exception('O salario é muito alto para receber um bônus')
        return valor
    
# Função para retornar string e exibir dados
    def __str__(self):
        return f'Funcionario({self._nome}, {self._data_nascimento}, {self._salario})'
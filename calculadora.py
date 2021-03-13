
class Operacao():
    def __init__(self):
        pass

    def soma(self, num1, num2):
        result = num1 + num2
        return result

    def subs(self, num1, num2):
        result = num1 - num2
        return result

    def mult(self, num1, num2):
        result = num1 * num2
        return result

    def div(self, num1, num2):
        result = num1 / num2
        return result
        
class Calculadora():
    def __init__(self):
        pass
    def calc(self):
        self.calcular = Operacao()
        operacao = int(input('Digite o número da operação: 1 Soma, 2 Subs, 3 Mult, 4 Div '))
        print(operacao)
        num1 = int(input('Digite o primeiro número: '))
        num2 = int(input('Digite o segundo número: '))

        if operacao == 1:
            result = self.calcular.soma(num1, num2)
            print('O resultado da operação é: ',result)
        elif operacao == 2:
            result = self.calcular.subs(num1, num2)
            print('O resultado da operação é: ',result)
        elif operacao == 3:
            result = self.calcular.mult(num1, num2)
            print('O resultado da operação é: ',result)
        elif operacao == 4:
            result = self.calcular.div(num1, num2)
            print('O resultado da operação é: ',result)

start = Calculadora()
start.calc()

        
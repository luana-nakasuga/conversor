from math import pow

operation = input('''
Insira a conversão que deseja fazer:
$ = DECIMAL PARA BINÁRIO
@ = BINÁRIO PARA DECIMAL
''')

soma = 0
potencia = 0
lista_bin = []

while True:
      # Se a pessoa digitar '$' o programa irá fazer a conversão de decimal para binário
      if operation == '$':
        print("-"*60)
        print(" DECIMAL PARA BINÁRIO ".center(60))
        print("-"*60)
        decimal = int(input('Digite o número decimal: '))
        print("-"*60)
        print(f'O número {decimal} convertido para binário: {bin(decimal)[2:]}') 
        # Vai ser imprimido o número que é para ser convertido e o número convertido.
        # Converte um número inteiro para uma string de binários prefixada com “0b”.
        # O [2:] serve para imprimir os caracteres a partir da 2 posição.
        break

      # Se a pessoa digitar '@' o programa irá fazer a conversão de binário para decimal.
      if operation == '@': 
        print("-"*60)
        print(" BINÁRIO PARA DECIMAL ".center(60))
        print("-"*60)
        qtde = int(input('Quantos números vão ter o seu binário? '))
        
        # Os valores vão ser inseridos de um em um de acordo com o valor inserido em qtde.
        for c in range(qtde):
            binario = int(input('Digite um número de cada vez: '))

            # Se for inserido mais de um número ou inserir um número diferente de 1 e 0, vai ser imprimido esta mensagem.
            while binario not in (1, 0): 
                binario = int(input('Digite apenas um número de cada vez: (somente 0 ou 1) '))
            lista_bin.append(binario) # Guarda cada valor na lista.

        # Cálculo para converter binário para decimal.
        for i in range(len(lista_bin), 0, -1): 
            num = (lista_bin[-i])
            potencia = i-1
            soma += num * pow(2, potencia)

            potencia += 1
        print("-"*60)
        print(f'O número binário {lista_bin} em decimal: {soma}')
        break

      # Caso insira uma opção inválida na inserção do tipo de conversão que deseja, vai ser pedido para tentar novamente.
      else:
        print('\nOpção inválida, tente novamente')
        operation = input('''
Insira a conversão que deseja fazer:
$ = DECIMAL PARA BINÁRIO
@ = BINÁRIO PARA DECIMAL
''')
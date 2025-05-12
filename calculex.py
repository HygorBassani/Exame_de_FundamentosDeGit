
#utilizei a funcao de repeticao para que possa ser possivel efetuar o loop
while True:
#efetuado a coleta de dados e ja convertido para inteiros

  num1 = int(input("Digite o primeiro numero: "))
  num2 = int(input("Digite o segundo numero: "))

#implementando as 4 operacoes matematicas

  operador = str(input("Por favor escolha uma das operacoes\n 1-Adicao\n 2-Subtracao\n 3-Multiplicacao\n 4-Divisao\n"))

#Utilizando a funcao de repeticao para efetuar as operacoes desejada

  if operador == "1":
    soma = num1 + num2
    print(f"Resultado da operacao: {soma}")
  elif operador == "2":
    soma = num1 - num2
    print(f"Resultado da operacao: {soma}")
  elif operador == "3":
    soma = num1 * num2
    print(f"Rseltado da operacao: {soma}")
  elif operador == "4":
    if (num1 != 0) and (num2 != 0):
      soma = int(num1 / num2)
      print(f"Resultado da operacao: {soma}")
    else:
      print("Erro: divisao por zero.")
  else:
      print("Operacao invalida")

#Pergunta para o usuario se deseja continuar

  continuar = input("\nDeseja realizar outra operacao?(s/n):\n ").lower()

  if continuar != "s":
    print("Encerramos a operacao")
    break

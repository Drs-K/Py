saldo_conta = 0
extrato= ""
limite_saque = 2000
n_saque = 0
max_saque= 3

MENU = """
 ====================
 // [1]Extrato     //
 // [2]Depositar   //
 // [3]Sacar       //
 // [0]Sair        //
 ====================
  Digite a opção deseja:"""
while True:

  opcao= input(MENU)

  if opcao == "1":
    print("\n \\\\\\\\\\\\\\\\EXTRATO\\\\\\\\\\\\\\")
    print("Nenhuma movimentação foi realizada!" if not extrato else extrato)
    print(f"Saldo:R${saldo_conta:.2f}\n") 
   
  elif opcao == "2":
    valor_deposito = float(input("Infoeme o valor que voce deseja depositar\n"))
    if valor_deposito >0 :
      saldo_conta +=  valor_deposito
      extrato += f"Depósito: R${valor_deposito:.2f}\n"
    else:
     print("Deposito nao efetuado, Digite um valor valido!")
    
  elif opcao == "3":
     valor_saque = float(input("Informe o valor que voce deseja sacar\n"))

     saque_ivalido = valor_saque <= 0
  
     excedeu_limite = valor_saque > limite_saque
     
     excedeu_saldo = valor_saque > saldo_conta
    
     quant_saque = n_saque >= max_saque
   
     if excedeu_limite:
       print( "Voce excedeu o valor limite para um saque, tente oputro valor! ")
     elif saque_ivalido:
       print("Digite um valor maior que 0 para efetuar o saque")
     elif excedeu_saldo:
       print("Você excedeu o valor disponivel para saque, tente um valor menor!")
     elif quant_saque:
       print("Voce excedeu a quantidade de saques diarios, tente novamente no proximo dia! ")
     else:
      saldo_conta -= valor_saque
      n_saque += 1
      extrato += f"Saque: R${valor_saque:.2f}\n"
  elif opcao == "0":
    break
  else:
    print("Opcao Invalida!")
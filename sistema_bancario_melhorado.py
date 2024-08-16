def menu():
     menu = """
        [1] Depositar
        [2] Sacar
        [3] Extrato
        [4] Criar Usuário
        [5] Criar Conta
        [6] Listar Contas
        [7] Sair
        => """
     return input(menu)

def depositar(valor, saldo, extrato,/):
        if valor > 0:
            saldo += valor
            extrato += f"Depósito: R$ {valor:.2f}\n"
            print(f"\nDepósito de R${valor:.2f} realizado com sucesso!\n")
            return saldo, extrato
        else:
            print("\nValor inválido. Digite um valor positivo para depósito.\n")
            return

def sacar(*, valor, limite, saldo, numero_saques, LIMITE_SAQUES, extrato):
        if numero_saques >= LIMITE_SAQUES:
            print("\nOperação falou! Quantidade de saques excedeu o limite.\n")
            return
        elif valor > limite:
            print("\nOperação falhou! Valor excede o limite para saque.\n")
            return
        elif valor > saldo:
            print("\nOperação falhou! Saldo insuficiente para saque.\n")
            return
        else:
            saldo -= valor
            extrato += f"Saque: R$ {valor:.2f}\n"
            numero_saques += 1
            print(f"\nSaque de R${valor:.2f} realizado com sucesso!\n")
            return saldo, extrato, numero_saques

def emitir_extrato(saldo, /, *, extrato):
        print("\n========== EXTRATO ==========")
        print(f"{extrato}\nSaldo: R$ {saldo:.2f}\n")
        print("=============================")
        return

def criar_usuario(usuarios):
    cpf = input("\nDigite o seu CPF, apenas os números:")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("\nJá existe um usuário com esse CPF!\n")
        return
    else:
        nome = input("\nInforme seu nome completo:")
        nascimento = input("\nInforme a data de nascimento (dd-mm-aaaa):")
        endereco = input("\nInforme o seu endereço (rua, nº - bairro - cidade/estado(sigla)):")
        usuarios.append({"nome":nome, "cpf":cpf, "nascimento":nascimento ,"endereco":endereco})
        print("\nUsuário cadastrado com sucesso!\n")
        return
               
def criar_conta(AGENCIA, numero_conta, usuarios):
    cpf = input ("\nDigite o número do CPF do usuario: ")
    usuario = filtrar_usuarios(cpf, usuarios)
    if usuario:
        print("\nConta criada com sucesso!\n")
        return{"AGENCIA": AGENCIA, "numero_conta": numero_conta, "usuario": usuario}
    else:
         print("\nNão foi possível criar a conta, usuário não encontrado!\n")

def listar_contas(contas):
    for conta in contas:
         linha = f"""\
         Agência: {conta['AGENCIA']}
         Conta: {conta['numero_conta']}
         Titular: {conta['usuario']['nome']}
         """
         print(linha)
     

def filtrar_usuarios(cpf, usuarios):
    usuarios_filtrados=[usuario for usuario in usuarios if usuario["cpf"]==cpf]
    return usuarios_filtrados[0] if usuarios_filtrados else None

def main():
    saldo = 0
    limite = 500
    extrato = ""
    numero_saques = 0
    LIMITE_SAQUES = 3
    AGENCIA = "0001"
    usuarios = []
    contas = []

    while True:

        opcao = menu()

        if opcao == "1":
            valor = float(input("\nDigite o valor que deseja depositar: "))
            saldo, extrato = depositar(valor, saldo, extrato)
          
        elif opcao == "2":
            valor = float(input("\nDigite o valor que deseja sacar: "))
            saldo, extrato, numero_saques = sacar(
                 valor=valor, 
                 limite=limite, 
                 saldo=saldo, 
                 numero_saques=numero_saques, 
                 LIMITE_SAQUES=LIMITE_SAQUES, 
                 extrato=extrato)
        
        elif opcao == "3":
            emitir_extrato(saldo, extrato=extrato)

        elif opcao == "4":
             criar_usuario(usuarios)

        elif opcao == "5":
            numero_conta = len(contas)+1
            conta = criar_conta(AGENCIA, numero_conta, usuarios)

            if conta:
                 contas.append(conta)

        elif opcao == "6":
             listar_contas(contas)

        elif opcao == "7":
            break

        else:
            print("\nOperação invalida! Favor selecionar uma operação válida do menu.\n")

main()
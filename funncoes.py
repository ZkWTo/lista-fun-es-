def verificacao(email, senha, cpf, dados):   
    for usuario in dados:
        if (
            usuario['email'] == email and
            usuario['senha'] == senha and
            usuario['cpf'] == cpf
        ):
            return True
    return False


def calculo_produto(calcular):
    desconto = calcular * 0.10
    valor_final = calcular - desconto
    return valor_final

def vef_idade(idade):
        if idade < 18:
            print(" \n vc é menor de idade")
            return ''
        else:
            print("\n vc é maior de idade ")
            return ''
        
def verificador_acao(valor_acao):
    if valor_acao >= 150.99:
         print("essa açao está muito cara, por favor compre com cuidado")
    else:
         print("essa açao está muito barata, está permitido a compra da mesma \n")
    
    print(f"aqui está o valor da açao que vc está querendo comprar {valor_acao} \n")
    
    diferenca = valor_acao - 150.99
    print(f"o valor  do esperado dos custos totais é = {diferenca:.2f}")
    return diferenca
def cal_imc(peso, altura):
    imc = (peso / (altura ** 2))

    if imc < 18.5:
        print(f"Com base no seu IMC = {imc:.2f} vc está abaixo do peso\n")
    elif 18.5 <= imc < 24.9:
        print(f"Com base no seu IMC = {imc:.2f} vc está no peso normal \n")
    elif imc >= 25:
        print(f"Com base no seu IMC = {imc:.2f} vc está acima do peso \n")

    print(f" aqui está o valor exato do seu IMC = {imc:.2f}")

    # retorna o IMC arredondado para 2 casas decimais
    return round(imc, 2)


def imposto(valor_produto):
    imposto = valor_produto * 0.15
    print(f"aqui está o valor que vc ira pagas de imposto {valor_produto + imposto}")
    return imposto
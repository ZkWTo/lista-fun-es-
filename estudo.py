from funncoes import verificacao
from funncoes import calculo_produto
from funncoes import vef_idade
from funncoes import verificador_acao
from funncoes import cal_imc
from funncoes import imposto


dados =[]
print("vc gostaria de fazer o cadastro dentro do nosso site")
resposta = str(input("sim ou nao \n")).strip().lower()

email = ''
senha = ''
cpf = ''

if resposta == 'sim':
    email = str(input("Digite o seu email que dai ser usado durante o cadastro aqui \n"))
    senha = str(input("Digite a sua senha que vai ser armazenada \n"))
    cpf = int(input("Digite o seu cpf aqui  \n"))

    novo_usu = {
        'email': email,
        'senha': senha,
        'cpf': cpf,
    }

    if verificacao(email, senha, cpf, dados) == True:
        print("parabens vc entrou dentro do nosso site, agora desfrute do nosso conteúdo ")
    else:
        dados.append(novo_usu)
        print("parabens, vc acaba de se cadastrar dentro do nosso sistema, agora aproveite o nosso site !!")

else:
    print("Cadastro cancelado, obrigado volte sempre ")


pergunta_produto = str(input("Vc gostaria de adicionar um produto a nossa loga, se sim por favor digite sim ou nao \n")).strip().lower()


# segunda questao 

while pergunta_produto == "sim":


    produto  = str(input("Digite o nome do prouto que vc quer adicionar \n"))
    
    valor_pro = float(input("Digite o valor que vc quer anexar ao produto que vc acabou de digitar  \n"))
    calcular = valor_pro
    break

    if pergunta_produto == "nao":
        print("nada foi cadastrado, obrigado e volte sempre ")
        break


        

print("Bem agora iremos amostrar aqui o valor separado de cada produto com o desconto feito")

print(f"aqui está o valor do produto com o preço original =  R${calcular}")
print(f"aqui está o valor que fai aplicado no desconto  =  R${calcular * 0.10}")

valor_final = calculo_produto(calcular)
print(f"e aqui está o valor após o desconto  = R${-valor_final}")

# terceira questao

print("Bem agora iremos comprar uma açao e precisamos verficiar o valor que vc está disposto a pagar")

valor_acao = float(input("Digite o valor da açao que vc quer comprar aqui = \n"))

print("bem agora iremos calcular o valor da açao em que vc deseja comprar, com base no valor que vc mesmo digitou aqui")

print(f"\n{verificador_acao(valor_acao)}")




# quarta questao 

idade = int(input("Digite a sua idade aqui "))

print(f"agora que verificamos a sua idade iremos verificar se vc é ou nao maior de idade ")

print(f'{vef_idade(idade)}')

# quinta questao

print("bem agora iremos calcular o seu IMC com base na usa altura e peso \n")

peso = float(input("por favor nos informe o valor do seu peso aqui = \n"))

altura = float(input("Por favor, digite a sua altura aqui \n"))

print("Bem agora que os valores foram colocados, faremos o IMC e falaremos o seu estado atual")

print(f"{cal_imc(peso,altura)}")

# sexta questao

print("agora iremos calcular o valor do imposto sobre os produtos que vc quer comprar \n")

valor_produto = float(input("Por favor, Digite o valor do produto aqui  = \n"))
    

print(f"{imposto(valor_produto)}")

# bem, como o senhor pediu pra gente fazer essa de try, eu deixei elas separadas por um comentário 
# que no casso é esse :)


#  primeira questao de try except 
try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))
    resultado = num1 / num2
    print("Resultado da divisão:", resultado)
except ZeroDivisionError:
    print("Erro: Não é possível dividir por zero!")

# segunda questao de try
try:
    numero = float(input("Digite um número: "))
    print("Você digitou:", numero)
except ValueError:
    print("Erro: O valor digitado não é um número!")

# terceira questao de try 
try:
    a = float(input("Digite o numerador: "))
    b = float(input("Digite o denominador: "))
    resultado = a / b
    print("Resultado:", resultado)
except ValueError:
    print("Erro: Você digitou algo que não é número!")
except ZeroDivisionError:
    print("Erro: Divisão por zero não é permitida!")

# quarta questao de try 
def dividir(a, b):
    try:
        return a / b
    except ZeroDivisionError:
        return "Erro: Divisão por zero não permitida."

x = float(input("Digite o primeiro número: "))
y = float(input("Digite o segundo número: "))
print("Resultado:", dividir(x, y))










import datetime 

dados = {}

aposentadoria_ano = []

ano_atual = datetime.date.today().year

salario_minimo_atual = 1630 #cria uma variavael pro salario minimo afim de tornar mais facil de alterar esse valor em caso de correções.

while True: #pega o nome e realiza o tratamente de erro.
    nome = input("Nome: ").strip()
    if nome:
        dados["nome"] = nome.title()
        break
    else:
        print("Nome não pode estar vazio.")

while True: #pega o ano de nascimento e faz o tratamento de erro. tambem confere se o ano digitado não é antigo demais pra ser real.
    try:
        ano_nascimento = int(input("Ano de nascimento: "))
        if 1900 <= ano_nascimento <= ano_atual:
            dados["ano de nascimento"] = ano_nascimento
            break
        else:
            print("Ano negado por razões de segurança. Tente novamente inserindo seu ano de nascimento real.")
    except ValueError:
        print("Digite um número inteiro válido.")

while True: #pega o sexo e faz o tratamento de erro.
    sexo = input("Sexo: [M/F] ").strip().upper()
    if sexo in ["M", "F"]:
        dados["sexo"] = sexo
        break
    else:
        print("Digite apenas 'M' ou 'F'.")

while True: #pega o numero da CTPS e faz o tratamento de erro.
    try:
        ctps = int(input("CTPS: (0 se nã0 tiver) "))
        if ctps >= 0:
            dados["ctps"] = ctps
            break
        else:
            print ("CTPS não pode receber um valor negativo.")
    except ValueError:
        print ("Digite um valor válido.")
    

idade = ano_atual - dados['ano de nascimento']

dados["idade"] = idade

if dados['ctps'] != 0: #pega os dados caso a pessoa possua uma CTPS, ou seja, esteja empregada
    while True:
        try: #pega o ano de contratação e faz o tratamente de erro.
            ano_contratacao = int(input("Ano de contratação: "))
            if 2000 <= ano_contratacao <= ano_atual: #considera-se que 2000 seja o ano de fundação da empresa, portanto, naturalment, ninguem pode ter sido contratado antes dessa data
                dados["ano de contratacao"] = ano_contratacao
                break
            else:
                print ("Você digitou um ano inválido. Tente novamente.")
        except ValueError:
                print ("Você digitou um valor inválido. Tente novamente")
    while True:
        try: #pega o salário e faz o tratamento de erro
            salario = float(input("Salário: "))
            if salario >= salario_minimo_atual:
                dados["salario"] = salario
                break
            else:
                print ("Você digitou um salário inválido. Tente novamente.")
        except ValueError:
            print ("Você digitou um valor inválido. Tente novamente.")

    if dados["sexo"] == "M":
        ano_aposentadoria_idade_homem = dados["ano de nascimento"] + 65#calcula em que ano a pessoa tera a idade minima para a aposentadoria
        ano_aposentadoria_contribuicao_homem = dados["ano de contratacao"] + 35 #calcula em que ano a pessoa tera cumprido a contribuição minima para a aposentadoria

        aposentadoria_ano.append(ano_aposentadoria_idade_homem)
        aposentadoria_ano.append(ano_aposentadoria_contribuicao_homem)

    elif dados["sexo"] == "F":
        ano_aposentadoria_idade_mulher = dados["ano de nascimento"] + 60#calcula em que ano a pessoa tera a idade minima para a aposentadoria
        ano_aposentadoria_contribuicao_mulher = dados["ano de contratacao"] + 30 #calcula em que ano a pessoa tera cumprido a contribuição minima para a aposentadoria

        aposentadoria_ano.append(ano_aposentadoria_idade_mulher)
        aposentadoria_ano.append(ano_aposentadoria_contribuicao_mulher)

print ("=-="*13)
print ("Dados do funcionário: ")
print (f"Nome: {dados['nome']}")
print (f"Idade: {dados['idade']}")
print (f"Sexo: {dados['sexo']}")
print (f"CTPS: {dados['ctps']}")

if dados['ctps'] != 0:
    print (f"Ano de contratação: {dados['ano de contratacao']}")
    print (f"Salário: R${dados['salario']:.2f}")
    print (f"O funcionário poderá se aposentar no ano {max(aposentadoria_ano)}")

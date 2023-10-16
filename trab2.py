import requests
from colorama import init, Fore
init()

url_vinicola_freitas = "http://localhost:3000"
url_vinicola_soares = "http://localhost:3001"

response_freitas = requests.get(url_vinicola_freitas + "/vinhos")
response_soares = requests.get(url_vinicola_soares + "/vinhos")

#enfeites
def titulo(msg, simbolo="-", cor=Fore.LIGHTMAGENTA_EX):
    print()
    print(cor + msg + Fore.RESET)
    print(simbolo * 70)

def sinais(msg2, cor=Fore.YELLOW):
    print(cor + msg2 + Fore.RESET)


#1- opção 1 | função de listar os vinhos por preço (- Listagem dos dados classificados (em ordem) de algum atributo)
def vinhos_por_preco():
    if response_freitas.status_code == 200:

        vinhos = response_freitas.json()

        #ordena a lista (vinhos) pelo preço de menor a maior
        vinhos_ordenados = sorted(vinhos, key=lambda vinho: float(vinho['preco']))
        
        titulo("Listagem de Vinhos por Preço:", cor=Fore.LIGHTGREEN_EX)
        print("{:<15} {:<15} {:<15}".format("Tipo", "Preço (R$)", "Teor Alcoólico"))
        
        for vinho in vinhos_ordenados:
            preco = float(vinho.get('preco', 0))  #converte pra float
            teor = float(vinho.get('teor', 0))  #converte pra float
            print("{:<15} R$ {:<11.2f} {:<15.2f}".format(vinho['tipo'], preco, teor))
    else:
        print("Erro ao listar os vinhos do mais barato ao mais caro.")


#2- opção 2 | função pra AGRUPAR OS DADOS por atributo e CONTAR O TOTAL, nesse caso por tipo
def vinhos_tipo():
    if response_freitas.status_code == 200:
        vinhos = response_freitas.json()

        #dicio pra contar a quantia de vinhos por tipo
        tipos_contador = {}

        for vinho in vinhos:
            tipo = vinho['tipo']
            tipos_contador[tipo] = tipos_contador.get(tipo, 0) + 1

        titulo("Quantidade de Vinhos por Tipo:", cor=Fore.LIGHTBLUE_EX)
        print("{:<15} {:<15}".format("Tipo", "Quantidade"))

        for tipo, quantidade in tipos_contador.items():
            print("{:<15} {:<15}".format(tipo, quantidade))
    else:
        print("Erro ao listar a quantidade dos vinhos por tipo.")


#3- opção 3 | função de conjuntos que vai fazer uma INTERSECÇÃO, mostrando o que as duas vinicolas tem de marcas em comum e quais marcas não são em comum, e sim unicas de cada
def compara_vinicolas():
    #puxa as marcas de cada vinícola
    dados_freitas = response_freitas.json()
    marcas_freitas = set(vinho['Marca']['nome'] for vinho in dados_freitas)

    dados_soares = response_soares.json()
    marcas_soares = set(vinho['Marca']['nome'] for vinho in dados_soares)

    # intersecção - ve as marcas em comum
    intersec = marcas_freitas.intersection(marcas_soares)

    titulo("\nMarcas em Comum entre as Vinícolas:", cor=Fore.YELLOW)
    print("\n".join(intersec))


#3- opção 4 | função de conjuntos que vai fazer a DIFERENÇA, mostrando as marcas de vinho exclusivas de cada vinícola
def marca_exclusiva():
    dados_freitas = response_freitas.json()
    marcas_freitas = set(vinho['Marca']['nome'] for vinho in dados_freitas)

    dados_soares = response_soares.json()
    marcas_soares = set(vinho['Marca']['nome'] for vinho in dados_soares)

    exclusivas_freitas = marcas_freitas.difference(marcas_soares)
    exclusivas_soares = marcas_soares.difference(marcas_freitas)

    if exclusivas_freitas:
        titulo("Marcas Exclusivas da Vinícola Freitas:", cor=Fore.LIGHTRED_EX)
        for marca in exclusivas_freitas:
            print(marca)
    else:
        titulo("A Vinícola Freitas não possui marcas exclusivas.\n", cor=Fore.RED)
        
    if exclusivas_soares:
        titulo("Marcas Exclusivas da Vinícola Soares:", cor=Fore.LIGHTBLUE_EX)
        for marca in exclusivas_soares:
            print(marca)
    else:
        titulo("A Vinícola Soares não possui marcas exclusivas.\n", cor=Fore.BLUE)

#4 - opção 5 | pesquisa. pesquisa feita na vinícola escolhida, busca por marca de vinho ou tipo de vinho
def pesquisar():
    while True:
        titulo("Pesquisa por Marca de Vinho e Tipo", cor=Fore.LIGHTYELLOW_EX)
        vinicola_escolhida = int(input("Escolha uma Vinícola Primeiro:\n1. Vinícola Freitas\n2. Vinícola Soares\nOpção: "))

        if vinicola_escolhida == 1:
            response = response_freitas
            break 
        elif vinicola_escolhida == 2:
            response = response_soares
            break 
        else:
            titulo("Opção inválida. Escolha 1 para Vinícola Freitas ou 2 para Vinícola Soares.", cor=Fore.RED)

    palavra_chave = input("Digite a palavra-chave (Marca, Tipo ou ambas): ")

    if response.status_code == 200:
        vinhos = response.json()
        resultados = []

        for vinho in vinhos:
            marca = vinho['Marca']['nome']
            tipo = vinho['tipo']
            if (palavra_chave.lower() in marca.lower() or palavra_chave.lower() in tipo.lower()):
                resultados.append(vinho)

        if resultados:
            titulo(f"Resultados da pesquisa '{palavra_chave}' na Vinícola {('Freitas' if vinicola_escolhida == 1 else 'Soares')}:\n", cor=Fore.GREEN)
            for vinho in resultados:
                sinais("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
                print(f"Marca de Vinho: {vinho['Marca']['nome']}")
                print(f"Tipo de Vinho: {vinho['tipo']}")
                print(f"Preço: R$ {vinho['preco']}")
                print(f"Teor Alcoólico: {vinho['teor']}%")
                sinais("-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*-*")
        else:
            titulo(f"Nenhum resultado encontrado com a palavra-chave '{palavra_chave}' na Vinícola {('Freitas' if vinicola_escolhida == 1 else 'Soares')}.", cor=Fore.RED)
    else:
        titulo(f"Erro... Não foi possível encontrar os vinhos na Vinícola {('Freitas' if vinicola_escolhida == 1 else 'Soares')}.", cor=Fore.RED)

        
#--------------------------------------------------------------------programa principal
while True:
    print()
    titulo("Faça uma Análise de Vinícola! Escolha uma opção:")
    print()
    print("1. Listar Vinhos por Preço (listagem de dados ordenados por preço)")
    print("2. Ver Total de Vinhos por Tipo (agrupamento de dados e total)")
    print("3. Ver Marcas em Comum entre as Vinícolas (intersecção de dados)")
    print("4. Ver Marcas Exclusivas de cada Vinícola (diferença de dados)")
    print("5. Pesquisar por marca de vinho e tipo")
    print("6. Sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        vinhos_por_preco()
    elif opcao == 2:
        vinhos_tipo()
    elif opcao == 3:
        compara_vinicolas()
    elif opcao == 4:
        marca_exclusiva()
    elif opcao == 5:
        pesquisar()
    else:
       print("Obrigada por usar nosso programa de Análise de Vinícola! :) ")
       break

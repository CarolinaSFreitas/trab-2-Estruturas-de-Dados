import requests

url_vinicola_freitas = "http://localhost:3000"
url_vinicola_soares = "http://localhost:3001"

response_freitas = requests.get(url_vinicola_freitas + "/vinhos")
response_soares = requests.get(url_vinicola_soares + "/vinhos")

def titulo(msg, simbolo="-"):
    print()
    print(msg)
    print(simbolo * 70)


#1- função de listar os vinhos por preço (- Listagem dos dados classificados (em ordem) de algum atributo)
def vinhos_por_preco():
    if response_freitas.status_code == 200:

        vinhos = response_freitas.json()

        #ordena a lista (vinhos) pelo preço de menor a maior
        vinhos_ordenados = sorted(vinhos, key=lambda vinho: float(vinho['preco']))
        
        titulo("Listagem de Vinhos por Preço:")
        print("{:<15} {:<15} {:<15}".format("Tipo", "Preço (R$)", "Teor Alcoólico"))
        
        for vinho in vinhos_ordenados:
            preco = float(vinho.get('preco', 0))  #converte pra float
            teor = float(vinho.get('teor', 0))  #converte pra float
            print("{:<15} R$ {:<11.2f} {:<15.2f}".format(vinho['tipo'], preco, teor))
    else:
        print("Erro ao listar os vinhos do mais barato ao mais caro.")


#2- função pra agrupar os dados por atributo e contar o total, nesse caso por tipo
def vinhos_tipo():
    if response_freitas.status_code == 200:
        vinhos = response_freitas.json()

        #dicio pra contar a quantia de vinhos por tipo
        tipos_contador = {}

        for vinho in vinhos:
            tipo = vinho['tipo']
            tipos_contador[tipo] = tipos_contador.get(tipo, 0) + 1

        titulo("Quantidade de Vinhos por Tipo:")
        print("{:<15} {:<15}".format("Tipo", "Quantidade"))

        for tipo, quantidade in tipos_contador.items():
            print("{:<15} {:<15}".format(tipo, quantidade))
    else:
        print("Erro ao listar a quantidade dos vinhos por tipo.")


#3- função de conjuntos que vai fazer uma intersecção, mostrando o que as duas vinicolas tem de marcas em comum e quais marcas não são em comum, e sim unicas de cada
def compara_vinicolas():
    #puxa as marcas de cada vinícola
    dados_freitas = response_freitas.json()
    marcas_freitas = set(vinho['Marca']['nome'] for vinho in dados_freitas)

    dados_soares = response_soares.json()
    marcas_soares = set(vinho['Marca']['nome'] for vinho in dados_soares)

    # intersecção - ve as marcas em comum
    intersec = marcas_freitas.intersection(marcas_soares)

    titulo("Marcas em Comum entre as Vinícolas:")
    print(", ".join(intersec))


#3- função de conjuntos que vai fazer a diferença, mostrando as marcas de vinho exclusivas de cada vinícola
def marca_exclusiva():
    dados_freitas = response_freitas.json()
    marcas_freitas = set(vinho['Marca']['nome'] for vinho in dados_freitas)

    dados_soares = response_soares.json()
    marcas_soares = set(vinho['Marca']['nome'] for vinho in dados_soares)

    exclusivas_freitas = marcas_freitas.difference(marcas_soares)
    exclusivas_soares = marcas_soares.difference(marcas_freitas)

    if exclusivas_freitas:
        print("Marcas Exclusivas da Vinícola Freitas:")
        print("-" * 70)
        for marca in exclusivas_freitas:
            print(marca)
    else:
        print()
        print("A Vinícola Freitas não possui marcas exclusivas.")
        print()
    if exclusivas_soares:
        print("Marcas Exclusivas da Vinícola Soares:")
        print("-" * 70)
        for marca in exclusivas_soares:
            print(marca)
    else:
        print()
        print("A Vinícola Soares não possui marcas exclusivas.")
        print()


#--------------------------------------------------------------------programa principal
while True:
    print()
    titulo("Faça uma Análise de Vinícola! Escolha uma opção:")
    print()
    print("1. Listar Vinhos por Preço (listagem de dados ordenados por preço)")
    print("2. Ver Total de Vinhos por Tipo (agrupamento de dados e total)")
    print("3. Ver Marcas em Comum entre as Vinícolas (intersecção de dados)")
    print("4. Ver Marcas Exclusivas de cada Vinícola (diferença de dados)")
    opcao = int(input("Opção: "))

    if opcao == 1:
        vinhos_por_preco()
    elif opcao == 2:
        vinhos_tipo()
    elif opcao == 3:
        compara_vinicolas()
    elif opcao == 4:
        marca_exclusiva()
    else:
       break


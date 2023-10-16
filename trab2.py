import requests

url_vinicola_freitas = "http://localhost:3000"

def titulo(msg, simbolo="-"):
    print()
    print(msg)
    print(simbolo * 70)

def listar_vinhos_por_preco_ordenado(url_vinicola_freitas):
    response = requests.get(url_vinicola_freitas + "/vinhos")

    if response.status_code == 200:
        vinhos = response.json()

        #ordena a lista (vinhos) pelo preço de menor a maior
        vinhos_ordenados = sorted(vinhos, key=lambda vinho: float(vinho['preco']))
        
        titulo("Listagem de Vinhos por Preço:")
        print("{:<15} {:<15} {:<15}".format("Tipo", "Preço (R$)", "Teor Alcoólico"))
        
        for vinho in vinhos_ordenados:
            preco = float(vinho.get('preco', 0))  #converte pra float
            teor = float(vinho.get('teor', 0))  #converte pra float
            print("{:<15} R$ {:<11.2f} {:<15.2f}".format(vinho['tipo'], preco, teor))
    else:
        print("Erro ao listar os vinhos.")

#programa principal
while True:
    print()
    titulo("Faça uma Análise de Vinícola! Escolha uma opção:")
    print()
    print("1. Listar Vinhos por Preço")
    print("2. Sair")
    opcao = int(input("Opção: "))

    if opcao == 1:
        listar_vinhos_por_preco_ordenado(url_vinicola_freitas)
    elif opcao == 2:
        pass
    else:
       break


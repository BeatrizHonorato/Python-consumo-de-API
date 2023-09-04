import requests

historico = []

while True:
    print("==============Consulta CEP=================")

    cep = input("Insira o CEP desejado: ")
    if len(cep) != 8:
        print("Quantidade de dígitos inválida")
        exit()

    url = f'http://viacep.com.br/ws/{cep}/json/'

    req = requests.get(url)

    if req.status_code == 200:
        data = req.json()
        if 'erro' not in data:
            print("CEP:", data['cep'])
            print("Logradouro:", data['logradouro'])
            print("Bairro:", data['bairro'])
            print("Cidade:", data['localidade'])
            print("Estado:", data['uf'])
            historico.append(data)  # Adiciona os dados ao histórico
        else:
            print("CEP não encontrado")
    elif req.status_code == 404:
        print("Erro na consulta.", req.status_code)
    else:
        print("Erro na consulta.", req.status_code)

    continuar = input("Deseja realizar outra consulta? S/s para sim ")
    if continuar.lower() != "s":
        break

# Historico
print("\n=============Histórico de consultas: ======================")
for consulta in historico:
    print("\nCEP:", consulta['cep'])
    print("Logradouro:", consulta['logradouro'])
    print("Bairro:", consulta['bairro'])
    print("Cidade:", consulta['localidade'])
    print("Estado:", consulta['uf'])

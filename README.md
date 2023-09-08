# Python-consumo-de-API

***Identificador_de_CEP***  

Python script que identifica o CEP de um endereço através do consumo da API de CEP.

O script se resume a uma função python que recebe um CEP brasileiro e retorna o endereço que corresponde ao CEP inserido pelo usuario. Ele faz isso por meio do consumo da API:https://viacep.com.br/. A própria API retorna o endereço que corresponde ao CEP.

Exemplo de uso:

Insira o CEP desejado: 01001000  
A API irá retornar o endereço.  
  CEP: 01001-000  
  Logradouro: Praça da Sé  
  Bairro: Sé  
  Cidade: São Paulo  
  Estado: SP  

Dependências  
Requests  
pip install requests  
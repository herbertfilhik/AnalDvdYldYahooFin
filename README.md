# Readme

Este é um script que busca as ações com os maiores dividend yields na bolsa de valores.

## Instalação

Este script requer as seguintes bibliotecas:

- requests
- bs4
- yfinance
- concurrent.futures
- time

Você pode instalar todas as bibliotecas necessárias com o seguinte comando:

```sh
pip install requests bs4 yfinance concurrent.futures time

Uso
Abra o terminal ou o prompt de comando e execute o script Python.

O script irá buscar as ações disponíveis na bolsa de valores através da URL "https://finance.yahoo.com/lookup/".
O script irá então calcular o dividend yield para cada ação.
O script irá imprimir as 10 ações com os maiores dividend yields.
Ao final, será exibido o tempo de execução do script.
Nota
Ao utilizar este script, tenha em mente que ele pode ser afetado por mudanças na página web ou na API yfinance. Além disso, o tempo de execução do script pode ser afetado por questões de velocidade da internet ou do computador que está executando o script.

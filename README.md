# Resolução de um desafio de programação como parte de um processo seletivo da Arkmeds utilizando Python 3.

## O desafio consiste em ler uma arquivo CSV e mostrar ao usuário as informações que estão em formato incorreto, de modo que o usuário possa corrigí-las

### Bibliotecas padrão utilizadas

- sys
- re
- csv
- datetime
- unicodedata

<hr>

### Validação dos dados
<br>

|  Nome do Campo  |  Tipo   |  Descrição                                            |
|  :------------  |  :----- |  :--------------------------------------------------  |
| nome            | string  | tamanho máximo de 25 caracteres                       |
| email           | string  | formato “primeiroNome.últimoNome@gmail.com”           |
| cpf             | string  | formato "xxx.xxx.xxx-xx" representando um cpf válido  |
| celular         | string  | formato "(xx) xxxxx-xxxx"                             |
| idade           | inteiro | -                                                     |
| data_nascimento | data    | formato "dd/mm/YYYY"                                  |
| data_cadastro   | data    | formato "dd/mm/YYYY"                                  |

<hr>

### Utilização
<br>

- Acesse a pasta com o programa em em um terminal com Python 3 instalado
- Digite o nome do programa e o nome do arquivo CSV: `python3 validador.py cadastros.csv`
- Para Linux com makefile, o comando a seguir imprime o resultado em um arquivo saida.txt: `make`
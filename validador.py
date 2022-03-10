# Nome do script        : validador.py
# Autor                 : Vinicius Cardoso Antunes
# Criado/Modificado     : 10 de Marco de 2022

from sys import argv
from re import search
from csv import reader
from datetime import datetime
from unicodedata import normalize

# Abre o arquivo com o nome digitado no terminal
with open(argv[1], 'r') as f:
    # Variavel que le o arquivo csv
    leitor_csv = reader(f)

    # Pula o cabecalho
    cabecalho = next(leitor_csv)

    # Variavel que conta qual linha esta sendo processada
    nr_linha = 1

    # Verifica se a linha nao e o cabecalho
    if cabecalho != None:
        for linha in leitor_csv:
            nr_linha += 1

            # 1. Nome
            # Verifica se o nome eh maior que 25
            if len(linha[0]) > 25:
                print("Linha " + str(nr_linha) +
                      ": Tamanho maximo ultrapassado (25)")

            # 2. E-mail
            primeiro_nome = linha[0].split()[0]
            ultimo_nome = linha[0].split()[-1]

            email_formato = primeiro_nome + "." + ultimo_nome + "@gmail.com"

            # Retira as pontuacoes da string
            email_formato = normalize('NFKD', email_formato).encode(
                'ASCII', 'ignore').decode('ASCII')

            # Converte para minusculas
            if linha[1] != email_formato.lower():
                print("Linha " + str(nr_linha) +
                      ": Formato de e-mail incorreto (primeiroNome.últimoNome@gmail.com)")

            # 3. CPF
            # Expressao regular para o cpf
            cpf_formato = "[0-9]{3}[\.][0-9]{3}[\.][0-9]{3}[\-][0-9]{2}"

            # Verifica se o formato de cpf nao eh compativel com a expressao regular definida acima
            if search(cpf_formato, linha[2]) == None:
                print("Linha " + str(nr_linha) +
                      ": Formato de CPF nao suportado (xxx.xxx.xxx-xx)")

            # 4. Celular
            celular_formato = "[\(][0-9]{2}[\)][\ ][0-9]{5}[\-][0-9]{4}"

            if search(celular_formato, linha[3]) == None:
                print("Linha " + str(nr_linha) +
                      ": Formato de celular nao suportado ((xx) xxxxx-xxxx)" + " ")

            # 5. Idade

            # Tenta converter a string idade em inteiro, caso nao consiga, retorna que nao foi digitado um numero
            try:
                int(linha[4])
            except:
                print("Linha " + str(nr_linha) +
                      ": Idade em tipo nao suportado (int)")

            # 6. Data de nascimento
            data_nascimento = linha[5]

            # Tenta converter a string data_nascimento em um formato data, caso nao consiga, a data eh inexistente
            try:
                # %d -> dd; %m -> mm; %Y -> YYYY
                datetime.strptime(data_nascimento, "%d/%m/%Y")
            except:
                print("Linha " + str(nr_linha) +
                      ": Data de nascimento em formato não suportado (dd/mm/YYYY)")

            # 7. Data de cadastro
            data_cadastro = linha[6]

            try:
                datetime.strptime(data_cadastro, "%d/%m/%Y")
            except:
                print("Linha " + str(nr_linha) +
                      ": Data de cadastro em formato não suportado (dd/mm/YYYY)")

# Fecha o arquivo csv
f.close()

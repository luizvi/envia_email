import json
import smtplib, ssl, email

arquivo = open('Prova_Infra.json')
check_execucao = 'false'

def envia_email():
    global check_execucao, PART1
    check_execucao = 'true'
    print('Prezados,\nOs servicos abaixo encontram-se fora com o seguinte status:\n\n')

for _linha in arquivo:
    if '{' not in _linha and '}' not in _linha:
        if 'down' in _linha:
            if check_execucao != 'true':
                envia_email()
            print(_linha.lstrip(' '))
arquivo.close()

print('\nAtenciosamente,\n\nGrupo Nexxees')
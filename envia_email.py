from http import server
import json
import smtplib, ssl, email

arquivo = open('Prova_Infra.json')
email_login = 'luizvi99@gmail.com'
email_password = 'senha123'
check_execucao = 'false'
SERVICOS = []

remetente = email_login
destinatario = ['luizvi99@gmail.com']
assunto = 'AUTOMATICO - Services Down'

def envia_email():
    global check_execucao, PART1
    check_execucao = 'true'
    PART1 = 'Prezados,\nOs servicos abaixo encontram-se fora com o seguinte status:\n\n'

for _linha in arquivo:
    if '{' not in _linha and '}' not in _linha:
        if 'down' in _linha:
            if check_execucao != 'true':
                envia_email()
            SERVICOS.append(_linha.lstrip(' '))
arquivo.close()

PART2 = '\nAtenciosamente,\n\nGrupo Nexxees'
#print(remetente,'\n', destinatario,'\n', assunto,'\n', PART1, SERVICOS, PART2)

try:
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.ehlo
    server.login(email_login, email_password)
    server.sendmail(remetente, destinatario, assunto, PART1, SERVICOS, PART2)
    #print(remetente, destinatario, assunto, PART1, SERVICOS, PART2)
    server.quit()
except:
    print('Ocorreu um erro durante a execucao')


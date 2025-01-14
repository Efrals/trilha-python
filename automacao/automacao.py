import pyautogui
import time
# pip install pyautogui

# pyautogui.write -> escrever um texto
# pyautogui.press -> simula o pressionamento de 1 tecla
# pyautogui.click -> clicar em algum lugar da tela
# pyautogui.hotkey -> atalho de teclado ("ctrl", "c")

#pausa global a cada passo
pyautogui.PAUSE = 0.5

# Passo 1 entrar no sistema
# abrir o navegador (chrome)
pyautogui.press("win")
pyautogui.write("chrome")
#aperta enter
pyautogui.press("enter")
time.sleep(1.5)
pyautogui.click(x=691, y=617)


# entrar no link 
pyautogui.write("https://pypi.org/")
pyautogui.press("enter")

#pausa em específico
time.sleep(3)


# Passo 2: Fazer login
# selecionar o campo de email
pyautogui.click(x=1369, y=163)
time.sleep(2)
pyautogui.click(x=481, y=385)
# escrever o seu email
pyautogui.write("e-mail@gmail.com")
pyautogui.press("tab") # passando pro próximo campo
pyautogui.write("sua senha")
pyautogui.press("tab") # clique no botao de login
pyautogui.press("enter")
time.sleep(3)

# Passo 3: Importar a base de produtos pra cadastrar
# pip install pandas openpyxl
import pandas as pd

tabela = pd.read_csv("produtos.csv")

print(tabela)

# Passo 4: Cadastrar um produto
for linha in tabela.index:
    # clicar no campo de código
    pyautogui.click(x=653, y=294)
    # pegar da tabela o valor do campo que a gente quer preencher
    codigo = tabela.loc[linha, "codigo"]
    # preencher o campo
    pyautogui.write(str(codigo))
    # passar para o proximo campo
    pyautogui.press("tab")
    # preencher o campo
    pyautogui.write(str(tabela.loc[linha, "marca"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "tipo"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "categoria"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "preco_unitario"]))
    pyautogui.press("tab")
    pyautogui.write(str(tabela.loc[linha, "custo"]))
    pyautogui.press("tab")
    obs = tabela.loc[linha, "obs"]
    if not pd.isna(obs):
        pyautogui.write(str(tabela.loc[linha, "obs"]))
    pyautogui.press("tab")
    pyautogui.press("enter") # cadastra o produto (botao enviar)
    # dar scroll de tudo pra cima, negativo d[a scroll para baixo]
    pyautogui.scroll(5000)
    # Passo 5: Repetir o processo de cadastro até o fim
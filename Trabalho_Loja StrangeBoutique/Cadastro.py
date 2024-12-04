import tkinter as tk
from PIL import ImageTk,Image
from datetime import datetime
import pytz
from pytz import timezone

#Cadastra os dados do cliente no sistema
def Cadastrar():
    global conta_criada
    Email_cliente = textbox_cad.get()
    Senha_cliente = textbox1_cad.get()
    Nome_cliente = textbox2_cad.get()
    

    Verificado = False

    #Verifica se os campos são válidos
    if Email_cliente == "" or Senha_cliente == "" or Nome_cliente == "":
        cad_erro = tk.Label(janela_cadastro,text = "Preencha os campos",background="white",fg="red",width=40)
        cad_erro.grid(row=11,columnspan=2)
    else:
        for cont in Email_cliente:
            if cont == "@":
                corte = Email_cliente[-4:]
                if corte==".com":
                    Verificado = True
            else:
                cad_erro = tk.Label(janela_cadastro,text = "Formato de email Inválido",background="white",fg="red",width=40)
                cad_erro.grid(row=11,columnspan=2)


    #Armazena os dados no sistema
    if Verificado:
        global se
        se = 1
        if Email_cliente == conta_usuario.email:
            cad_erro = tk.Label(janela_cadastro,text='Este email já está vinculado a uma conta',background="white",fg="red",width=40)
            cad_erro.grid(row=11,columnspan=2) 
        else:  
            conta_cliente.email = Email_cliente
            conta_cliente.nome = Nome_cliente
            conta_cliente.senha = Senha_cliente
            conta_login.email = conta_cliente.email
            conta_login.senha = conta_cliente.senha
            conta_login.nome = conta_cliente.nome
            conta_criada = True
            Aba_CatalogoCliente()

#Função que abre a aba de cadastro
def Aba_Cadastro():

    global janela_cadastro
    janela_cadastro = tk.Toplevel()
    janela_cadastro.title('Cadastro')
    janela_cadastro.columnconfigure(1,weight=1)
    janela_cadastro.config(background="white")
    janela_cadastro.iconbitmap("Trabalho Loja de Roupa/IMG/Logo.ico")
    janela_cadastro.geometry('500x300')
    janela_cadastro.state('zoomed')

    
    
    global textbox_cad
    global textbox1_cad
    global textbox2_cad

    titulo = tk.Label(janela_cadastro,text = 'Cadastro', font=('Arial Bold',40),background = '#fecad9',fg='#af4759',height=2)
    titulo.grid(row=0,columnspan=2,sticky='NSEW')
    
    logo = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Logo-Photoroom.jpg'))
    tk.Label(janela_cadastro,image = logo,background='#fecad9').grid(row=0,column=0)

    espaco = tk.Label(janela_cadastro,text='',background='white')
    espaco.grid(row=1,pady=50)

    mensagem2 = tk.Label(janela_cadastro,text = "Email:",font=('Arial Bold',15),background="White",fg='#af4759')
    mensagem2.grid(row=2,column=0)

    textbox_cad = tk.Entry(janela_cadastro,width = 20,font=('Arial Bold',15),background='#fecad9',fg='#af4759',borderwidth=0)
    textbox_cad.grid(row=3,columnspan=2,sticky='NSEW',padx=50,pady=20)

    mensagem3 = tk.Label(janela_cadastro,text = "Criar senha:",fg='#af4759',font=('Arial Bold',15),background="White")
    mensagem3.grid(row=4,column=0)

    textbox1_cad = tk.Entry(janela_cadastro,width = 20,font=('Arial Bold',15),background='#fecad9',fg='#af4759',borderwidth=0)
    textbox1_cad.grid(row=5,columnspan=2,sticky='NSEW',padx=50,pady=20)

    mensagem4 = tk.Label(janela_cadastro,text = "Nome:",fg='#af4759',font=('Arial Bold',15),background="White")
    mensagem4.grid(row=6,column=0)

    textbox2_cad = tk.Entry(janela_cadastro,width = 20,font=('Arial Bold',15),background='#fecad9',fg='#af4759',borderwidth=0)
    textbox2_cad.grid(row=7,columnspan=2,sticky='NSEW',padx=50,pady=20)

    botao_Cadastro = tk.Button(janela_cadastro,text = "Cadastrar",font=('Arial Bold',15),width=13,background='#fecad9',fg='#af4759',activebackground='#fdb4c9',activeforeground='#af4759',borderwidth=0,command = Cadastrar)
    botao_Cadastro.grid(row=8,columnspan=2)

    espaco1 = tk.Label(janela_cadastro,text='',background='white')
    espaco1.grid(row=9)

    botao_Voltar = tk.Button(janela_cadastro,text = "Voltar",font=('Arial Bold',15),width=13,background='#fecad9',fg='#af4759',activebackground='#fdb4c9',activeforeground='#af4759',borderwidth=0, command=janela_cadastro.destroy)
    botao_Voltar.grid(row=10,columnspan=2)
    
#Função que abra a aba do catalogo mas para o cliente(sem ter o botão para verificar o histórico de vendas)
def Aba_CatalogoCliente():

    janela.destroy()
    global janela_CatalogoCliente
    global escolha
    janela_CatalogoCliente = tk.Tk()

    janela_CatalogoCliente.title('Catalogo')
    janela_CatalogoCliente.columnconfigure(1,weight=1)
    janela_CatalogoCliente.config(background='white')
    janela_CatalogoCliente.iconbitmap("Trabalho Loja de Roupa/IMG/Logo.ico")
    janela_CatalogoCliente.geometry("500x500")
    janela_CatalogoCliente.state('zoomed')

    titulo = tk.Label(janela_CatalogoCliente,text = 'Catalogo', font=('Arial Bold',40),background = '#fecad9',fg='#af4759',height=2)
    titulo.grid(row=0,columnspan=6,sticky='NSEW')

    logo = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Logo-Photoroom.jpg'))
    tk.Label(janela_CatalogoCliente,image = logo,background='#fecad9').grid(row=0,column=0,padx=50)

    espaco = tk.Label(janela_CatalogoCliente,text='Histórico de Vendas',background='#fecad9',fg='#fecad9')
    espaco.grid(row=0,column=5,padx=50)

    produto_cat = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Bolsa.jpg'))
    produto_cat1 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Salto.jpg'))
    produto_cat2 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Calça.jpg'))
    produto_cat3 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Vestido.jpg'))
    
    tk.Button(janela_CatalogoCliente, image=produto_cat,borderwidth=0,command=Info_Bolsa).place(x = 315, y = 300)

    tk.Button(janela_CatalogoCliente, image=produto_cat1,borderwidth=0,command=Info_Salto).place(x = 565, y = 300)

    tk.Button(janela_CatalogoCliente, image=produto_cat2,borderwidth=0,command=Info_Calca).place(x = 815, y = 300)

    tk.Button(janela_CatalogoCliente, image=produto_cat3,borderwidth=0,command=Info_Vestido).place(x = 1065, y = 300)

    sairimg = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Sair_botão.png'))
    escolha = 0
    botao_sair = tk.Button(janela_CatalogoCliente,image= sairimg,borderwidth=0,bg='white',command=voltar_login)
    botao_sair.place(x = 100, y = 600)

    janela_CatalogoCliente.mainloop()
    
#Função que abre a janela do catalogo para o Usuário
def Aba_Catalogo():
    if se > 0:
        janela.destroy()

    global janela_Catalogo
    global vestido_prod
    global escolha
    janela_Catalogo = tk.Tk()

    janela_Catalogo.title('Catalogo')
    janela_Catalogo.columnconfigure(1,weight=1)
    janela_Catalogo.config(background='white')
    janela_Catalogo.iconbitmap("Trabalho Loja de Roupa/IMG/Logo.ico")
    janela_Catalogo.geometry("500x500")
    janela_Catalogo.state('zoomed')

    titulo = tk.Label(janela_Catalogo,text = 'Catalogo', font=('Arial Bold',40),background = '#fecad9',fg='#af4759',height=2)
    titulo.grid(row=0,columnspan=6,sticky='NSEW')

    logo = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Logo-Photoroom.jpg'))
    tk.Label(janela_Catalogo,image = logo,background='#fecad9').grid(row=0,column=0,padx=50)

    Vendas = tk.Button(janela_Catalogo,text= "Histórico de Vendas",font=('Arial Bold',10),width=15,background='#fecad9',fg='#af4759',activebackground='#fdb4c9',activeforeground='#af4759',borderwidth=0,command = Aba_Vendas ) 
    Vendas.grid(row=0,column=5,padx=50)
   
    

    produto_cat = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Bolsa.jpg'))
    produto_cat1 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Salto.jpg'))
    produto_cat2 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Calça.jpg'))
    produto_cat3 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Vestido.jpg'))

    tk.Button(janela_Catalogo, image=produto_cat,borderwidth=0,command=Info_Bolsa).place(x = 315, y = 300)

    tk.Button(janela_Catalogo, image=produto_cat1,borderwidth=0,command=Info_Salto).place(x = 565, y = 300)

    tk.Button(janela_Catalogo, image=produto_cat2,borderwidth=0,command=Info_Calca).place(x = 815, y = 300)

    tk.Button(janela_Catalogo, image=produto_cat3,borderwidth=0,command=Info_Vestido).place(x = 1065, y = 300)

    sairimg = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Sair_botão.png'))
    escolha = 1 
    botao_sair = tk.Button(janela_Catalogo,image= sairimg,borderwidth=0,bg='white',command=voltar_login)
    botao_sair.place(x = 100, y = 600)

    janela_Catalogo.mainloop()
    

    pass

#Função para voltar para a aba de login
def voltar_login():
    if escolha == 1:
        janela_Catalogo.destroy()
    else:
        janela_CatalogoCliente.destroy()

    Login(1)
    
#Funções para passar parâmetros para a "Aba_Produto"
def Info_Bolsa():

    Aba_Produto(bolsa_prod.prodNome,bolsa_prod.prodDesc,bolsa_prod.preco,ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Bolsa1.png')),bolsa_prod.quant)

    pass

def Info_Calca():

    Aba_Produto(calca_prod.prodNome,calca_prod.prodDesc,calca_prod.preco,ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Calça1.png')),calca_prod.quant)

    pass

def Info_Salto():

    Aba_Produto(salto_prod.prodNome,salto_prod.prodDesc,salto_prod.preco,ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Salto1.png')),salto_prod.quant)

    pass

def Info_Vestido():
    
    Aba_Produto(vestido_prod.prodNome,vestido_prod.prodDesc,vestido_prod.preco,ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Vestido1.png')),vestido_prod.quant)

    pass

#Função que abre a janela dos produtos
def Aba_Produto(nomeprod,descprod,precoprod,prodimg,prodquant):
    global janela_produto
    janela_produto = tk.Toplevel()
    janela_produto.title("Comprar")
    janela_produto.columnconfigure(1,weight=1)
    janela_produto.iconbitmap("Trabalho Loja de Roupa/IMG/Logo.ico")
    janela_produto.state("zoomed")
    janela_produto.geometry("500x500")
    janela_produto.config(background="White")

    titulo = tk.Label(janela_produto,text = '', font=('Arial Bold',40),background = '#fecad9',fg='#af4759',height=2)
    titulo.grid(row=0,columnspan=2,sticky='NSEW')

    logo = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Logo-Photoroom.jpg'))
    tk.Label(janela_produto,image = logo,background='#fecad9').grid(row=0,column=0)

    global produto
    global textbox_prod

    produto = Produto(nomeprod,precoprod,descprod,prodimg,prodquant)

    Imgprod = tk.Label(janela_produto,image=produto.img)
    Imgprod.place(x = 200, y = 200)

    nome_prod = tk.Label(janela_produto,text=produto.prodNome,font=('Arial Bold',10),background="White")
    nome_prod.place(x = 200, y = 505)

    desc_prod = tk.Label(janela_produto,text=produto.prodDesc,font=('Arial Bold',13),background="White",fg = 'black')
    desc_prod.place(x = 700, y = 200)

    preco_prod = tk.Label(janela_produto,text='Preço: R$'+produto.preco,font=('Arial Bold',15),background="White",fg = 'black')
    preco_prod.place(x = 200, y = 540)

    quant_prod = tk.Label(janela_produto,text=f'Em estoque:{produto.quant}',font=('Arial Bold',15),background="White",fg = 'black')
    quant_prod.place(x = 200, y = 565)

    if conta_login.email == conta_cliente.email:
    
        if produto.prodNome == vestido_prod.prodNome:
            botao_compra = tk.Button(janela_produto,text="Comprar",font=('Arial Bold',15),width=13,command=vestido_prod.Venda)
            botao_compra.place(x = 200, y = 595)

        elif produto.prodNome == bolsa_prod.prodNome:
            botao_compra = tk.Button(janela_produto,text="Comprar",font=('Arial Bold',15),width=13,command=bolsa_prod.Venda)
            botao_compra.place(x = 200, y = 595)

        elif produto.prodNome == calca_prod.prodNome:
            botao_compra = tk.Button(janela_produto,text="Comprar",font=('Arial Bold',15),width=13,command=calca_prod.Venda)
            botao_compra.place(x = 200, y = 595)
    
        elif produto.prodNome == salto_prod.prodNome:
            botao_compra = tk.Button(janela_produto,text="Comprar",font=('Arial Bold',15),width=13,command=salto_prod.Venda)
            botao_compra.place(x = 200, y = 595)
    
    else:
        if produto.prodNome == bolsa_prod.prodNome:

            mensagem_prod = tk.Label(janela_produto,text='Digite a quantidade desejada',bg = 'White', fg = 'Black')
            mensagem_prod.place(x = 198, y = 600)

            textbox_prod = tk.Entry(janela_produto,width=25)
            textbox_prod.place(x = 200, y = 620 )

            botao_reabastecer = tk.Button(janela_produto,text="Reabastecer",font=('Arial Bold',15),width=13,command=bolsa_prod.reabastecer)
            botao_reabastecer.place(x = 200, y = 640)
        
        elif produto.prodNome == vestido_prod.prodNome:

            mensagem_prod = tk.Label(janela_produto,text='Digite a quantidade desejada',bg = 'White', fg = 'Black')
            mensagem_prod.place(x = 198, y = 600)

            textbox_prod = tk.Entry(janela_produto,width=25)
            textbox_prod.place(x = 200, y = 620 )

            botao_reabastecer = tk.Button(janela_produto,text="Reabastecer",font=('Arial Bold',15),width=13,command=vestido_prod.reabastecer)
            botao_reabastecer.place(x = 200, y = 640)

        elif produto.prodNome == calca_prod.prodNome:

            mensagem_prod = tk.Label(janela_produto,text='Digite a quantidade desejada',bg = 'White', fg = 'Black')
            mensagem_prod.place(x = 198, y = 600)

            textbox_prod = tk.Entry(janela_produto,width=25)
            textbox_prod.place(x = 200, y = 620 )

            botao_reabastecer = tk.Button(janela_produto,text="Reabastecer",font=('Arial Bold',15),width=13,command=calca_prod.reabastecer)
            botao_reabastecer.place(x = 200, y = 640)
        
        elif produto.prodNome == salto_prod.prodNome:

            mensagem_prod = tk.Label(janela_produto,text='Digite a quantidade desejada',bg = 'White', fg = 'Black')
            mensagem_prod.place(x = 198, y = 600)

            textbox_prod = tk.Entry(janela_produto,width=25)
            textbox_prod.place(x = 200, y = 620 )

            botao_reabastecer = tk.Button(janela_produto,text="Reabastecer",font=('Arial Bold',15),width=13,command=salto_prod.reabastecer)
            botao_reabastecer.place(x = 200, y = 640)

    janela_produto.mainloop()
    pass

#Funçao para voltar na aba catalogo pela aba histórico de vendas
def Voltar():
    global se
    se = 0
    janela_Vendas.destroy()
    Aba_Catalogo()
    
#Função que abre a janela de histórico de vendas
def Aba_Vendas():

    janela_Catalogo.destroy()
    global janela_Vendas 
    janela_Vendas = tk.Tk()
    janela_Vendas.title('Histórico de vendas')
    janela_Vendas.columnconfigure(1,weight=5)
    janela_Vendas.config(background='white')
    janela_Vendas.title('Histórico de Vendas')
    janela_Vendas.iconbitmap("Trabalho Loja de Roupa/IMG/Logo.ico")
    janela_Vendas.geometry("500x500")
    janela_Vendas.state('zoomed')
    global num_venda

    titulo = tk.Label(janela_Vendas,text = 'Vendas', font=('Arial Bold',40),background = '#fecad9',fg='#af4759',height=2)
    titulo.grid(row=0,columnspan=5,sticky='NSEW')

    logo = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Logo-Photoroom.jpg'))
    tk.Label(janela_Vendas,image = logo,background='#fecad9').grid(row=0,column=0)

    Voltar_catalogo = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Seta_Voltar.png'))
    tk.Button(janela_Vendas,image=Voltar_catalogo,background='#fecad9',borderwidth=0,activebackground='#af4759',command=Voltar).grid(row=0,column=3)


    Total = tk.Label(janela_Vendas,text='Nenhuma venda feita', bg='white')
    if venda_total > 0:
        Total = tk.Label(janela_Vendas,text=f'Vendas Totais: {venda_total}',bg='white')
    Total.grid(row=1,column=0)

    print(num_venda)


    if num_venda == 1:

        if venda_feita:

            mensagem = tk.Label(janela_Vendas,text='Cliente:'+Mensagem_comprador[0],background='white',fg='black')
            mensagem.place(x = 200, y = 400)

            Mensagem = tk.Label(janela_Vendas,text=f'Preço: R$ {Mensagem_preco[0]}',background='White',fg='black')
            Mensagem.place(x = 200, y = 420)

            data = tk.Label(janela_Vendas,text=f'Data: {data_venda[0]}',background='White',fg='black')
            data.place(x = 200, y = 440)

            if prod_comprado[0] == 'bolsa':
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Bolsa.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)
            elif prod_comprado[0] == 'vestido':
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Vestido.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)
            elif prod_comprado[0] == 'calça':
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Calça.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)
            else:
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Salto.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)
                
    elif num_venda == 2:

        if venda_feita:

            mensagem = tk.Label(janela_Vendas,text=f'Cliente: {Mensagem_comprador[1]}',background='white',fg='black')
            mensagem.place(x = 200, y = 400)

            Mensagem = tk.Label(janela_Vendas,text=f'Preço: R$ {Mensagem_preco[1]}',background='White',fg='black')
            Mensagem.place(x = 200, y = 420)

            data = tk.Label(janela_Vendas,text=f'Data: {data_venda[1]}',background='White',fg='black')
            data.place(x = 200, y = 440)

            if prod_comprado[1] == 'bolsa':
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Bolsa.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)
            elif prod_comprado[1] == 'vestido':
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Vestido.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)
            elif prod_comprado[1] == 'calça':
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Calça.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)
            else:
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Salto.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)

        print('chegou')

        if venda_feita:

            mensagem1 = tk.Label(janela_Vendas,text=f'Cliente: {Mensagem_comprador[0]}',background='white',fg='black')
            mensagem1.place(x = 500, y = 400)

            Mensagem1 = tk.Label(janela_Vendas,text=f'Preço: R$ {Mensagem_preco[0]}',background='White',fg='black')
            Mensagem1.place(x = 500, y = 420)

            data1 = tk.Label(janela_Vendas,text=f'Data: {data_venda[0]}',background='White',fg='black')
            data1.place(x = 500, y = 440)

            if prod_comprado[0] == 'bolsa':
                prod_img1 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Bolsa.jpg'))
                tk.Label(janela_Vendas,image=prod_img1,bg='White').place(x = 500, y = 200)
            elif prod_comprado[0] == 'vestido':
                prod_img1 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Vestido.jpg'))
                tk.Label(janela_Vendas,image=prod_img1,bg='White').place(x = 500, y = 200)
            elif prod_comprado[0] == 'calça':
                prod_img1 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Calça.jpg'))
                tk.Label(janela_Vendas,image=prod_img1,bg='White').place(x = 500, y = 200)
            else:
                prod_img1 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Salto.jpg'))
                tk.Label(janela_Vendas,image=prod_img1,bg='White').place(x = 500, y = 200)
        
    elif num_venda == 3:

        if venda_feita:

            mensagem = tk.Label(janela_Vendas,text=f'Cliente: {Mensagem_comprador[2]}',background='white',fg='black')
            mensagem.place(x = 200, y = 400)

            Mensagem = tk.Label(janela_Vendas,text=f'Preço: {Mensagem_preco[2]}',background='White',fg='black')
            Mensagem.place(x = 200, y = 420)

            data = tk.Label(janela_Vendas,text=f'Data: {data_venda[2]}',background='White',fg='black')
            data.place(x = 200, y = 440)

            if prod_comprado[2] == 'bolsa':
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Bolsa.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)
            elif prod_comprado[2] == 'vestido':
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Vestido.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)
            elif prod_comprado[2] == 'calça':
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Calça.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)
            else:
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Salto.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)

        print('chegou')

        if venda_feita:

            mensagem1 = tk.Label(janela_Vendas,text=f'Cliente: {Mensagem_comprador[1]}',background='white',fg='black')
            mensagem1.place(x = 500, y = 400)

            Mensagem1 = tk.Label(janela_Vendas,text=f'Preço: R$ {Mensagem_preco[1]}',background='White',fg='black')
            Mensagem1.place(x = 500, y = 420)

            data1 = tk.Label(janela_Vendas,text=f'Data: {data_venda[1]}',background='White',fg='black')
            data1.place(x = 500, y = 440)

            if prod_comprado[1] == 'bolsa':
                prod_img1 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Bolsa.jpg'))
                tk.Label(janela_Vendas,image=prod_img1,bg='White').place(x = 500, y = 200)
            elif prod_comprado[1] == 'vestido':
                prod_img1 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Vestido.jpg'))
                tk.Label(janela_Vendas,image=prod_img1,bg='White').place(x = 500, y = 200)
            elif prod_comprado[1] == 'calça':
                prod_img1 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Calça.jpg'))
                tk.Label(janela_Vendas,image=prod_img1,bg='White').place(x = 500, y = 200)
            else:
                prod_img1 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Salto.jpg'))
                tk.Label(janela_Vendas,image=prod_img1,bg='White').place(x = 500, y = 200)

        if venda_feita:

            mensagem2 = tk.Label(janela_Vendas,text=f'Cliente: {Mensagem_comprador[0]}',background='white',fg='black')
            mensagem2.place(x = 800, y = 400)

            Mensagem2 = tk.Label(janela_Vendas,text=f'Preço: R${Mensagem_preco[0]}',background='White',fg='black')
            Mensagem2.place(x = 800, y = 420)

            data2 = tk.Label(janela_Vendas,text=f'Data: {data_venda[0]}',background='White',fg='black')
            data2.place(x = 800, y = 440)

            if prod_comprado[0] == 'bolsa':
                prod_img2 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Bolsa.jpg'))
                tk.Label(janela_Vendas,image=prod_img2,bg='White').place(x = 800, y = 200)
            elif prod_comprado[0] == 'vestido':
                prod_img2 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Vestido.jpg'))
                tk.Label(janela_Vendas,image=prod_img2,bg='White').place(x = 800, y = 200)
            elif prod_comprado[0] == 'calça':
                prod_img2 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Calça.jpg'))
                tk.Label(janela_Vendas,image=prod_img2,bg='White').place(x = 800, y = 200)
            else:
                prod_img2 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Salto.jpg'))
                tk.Label(janela_Vendas,image=prod_img2,bg='White').place(x = 800, y = 200)
        
    elif num_venda == 4:

        if venda_feita:

            mensagem = tk.Label(janela_Vendas,text=f'Cliente: {Mensagem_comprador[3]}',background='white',fg='black')
            mensagem.place(x = 200, y = 400)

            Mensagem = tk.Label(janela_Vendas,text=f'Preço: R${Mensagem_preco[3]}',background='White',fg='black')
            Mensagem.place(x = 200, y = 420)

            data = tk.Label(janela_Vendas,text=f'Data: {data_venda[3]}',background='White',fg='black')
            data.place(x = 200, y = 440)

            if prod_comprado[3] == 'bolsa':
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Bolsa.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)
            elif prod_comprado[3] == 'vestido':
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Vestido.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)
            elif prod_comprado[3] == 'calça':
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Calça.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)
            else:
                prod_img = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Salto.jpg'))
                tk.Label(janela_Vendas,image=prod_img,bg='White').place(x = 200, y = 200)

        print('chegou')

        if venda_feita:

            mensagem1 = tk.Label(janela_Vendas,text=f'Cliente: {Mensagem_comprador[2]}',background='white',fg='black')
            mensagem1.place(x = 500, y = 400)

            Mensagem1 = tk.Label(janela_Vendas,text=f'Preço: R${Mensagem_preco[2]}',background='White',fg='black')
            Mensagem1.place(x = 500, y = 420)

            data1 = tk.Label(janela_Vendas,text=f'Data: {data_venda[2]}',background='White',fg='black')
            data1.place(x = 500, y = 440)

            if prod_comprado[2] == 'bolsa':
                prod_img1 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Bolsa.jpg'))
                tk.Label(janela_Vendas,image=prod_img1,bg='White').place(x = 500, y = 200)
            elif prod_comprado[2] == 'vestido':
                prod_img1 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Vestido.jpg'))
                tk.Label(janela_Vendas,image=prod_img1,bg='White').place(x = 500, y = 200)
            elif prod_comprado[2] == 'calça':
                prod_img1 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Calça.jpg'))
                tk.Label(janela_Vendas,image=prod_img1,bg='White').place(x = 500, y = 200)
            else:
                prod_img1 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Salto.jpg'))
                tk.Label(janela_Vendas,image=prod_img1,bg='White').place(x = 500, y = 200)

        if venda_feita:

            mensagem2 = tk.Label(janela_Vendas,text=f'Cliente: {Mensagem_comprador[1]}',background='white',fg='black')
            mensagem2.place(x = 800, y = 400)

            Mensagem2 = tk.Label(janela_Vendas,text=f'Preço: R$ {Mensagem_preco[1]}',background='White',fg='black')
            Mensagem2.place(x = 800, y = 420)

            data2 = tk.Label(janela_Vendas,text=f'Data: {data_venda[1]}',background='White',fg='black')
            data2.place(x = 800, y = 440)

            if prod_comprado[1] == 'bolsa':
                prod_img2 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Bolsa.jpg'))
                tk.Label(janela_Vendas,image=prod_img2,bg='White').place(x = 800, y = 200)
            elif prod_comprado[1] == 'vestido':
                prod_img2 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Vestido.jpg'))
                tk.Label(janela_Vendas,image=prod_img2,bg='White').place(x = 800, y = 200)
            elif prod_comprado[1] == 'calça':
                prod_img2 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Calça.jpg'))
                tk.Label(janela_Vendas,image=prod_img2,bg='White').place(x = 800, y = 200)
            else:
                prod_img2 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Salto.jpg'))
                tk.Label(janela_Vendas,image=prod_img2,bg='White').place(x = 800, y = 200)

        if venda_feita:

            mensagem3 = tk.Label(janela_Vendas,text=f'Cliente: {Mensagem_comprador[0]}',background='white',fg='black')
            mensagem3.place(x = 1100, y = 400)

            Mensagem3 = tk.Label(janela_Vendas,text=f'Preço: R$ {Mensagem_preco[0]}',background='White',fg='black')
            Mensagem3.place(x = 1100, y = 420)

            data3 = tk.Label(janela_Vendas,text=f'Data: {data_venda[0]}',background='White',fg='black')
            data3.place(x = 1100, y = 440)

            if prod_comprado[0] == 'bolsa':
                prod_img3 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Bolsa.jpg'))
                tk.Label(janela_Vendas,image=prod_img3,bg='White').place(x = 1100, y = 200)
            elif prod_comprado[0] == 'vestido':
                prod_img3 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Vestido.jpg'))
                tk.Label(janela_Vendas,image=prod_img3,bg='White').place(x = 1100, y = 200)
            elif prod_comprado[0] == 'calça':
                prod_img3 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Calça.jpg'))
                tk.Label(janela_Vendas,image=prod_img3,bg='White').place(x = 1100, y = 200)
            else:
                prod_img3 = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Salto.jpg'))
                tk.Label(janela_Vendas,image=prod_img3,bg='White').place(x = 1100, y = 200)
    else:
        num_venda = 0



            

   
    janela_Vendas.mainloop()

#Função que armazena as vendas
def Vender(repete):
    global Mensagem_quant
    global Mensagem_comprador
    global Mensagem_preco
    global venda_feita
    global img_compra
    global num_venda
    global repetir
    global venda_total

    if repetir == 0:
        Mensagem_comprador = [None]*4
        Mensagem_preco = [None]*4
    
    venda_total = venda_total+1

    repetir = repetir + 1


    img_compra = None
    venda_feita = True


    Mensagem_quant[repete]  = quantidade
    Mensagem_comprador[repete] = comprador
    Mensagem_preco[repete] = venda_preco
    num_venda = num_venda + 1
    print(num_venda)

#Objeto que guarda as informações do produto
class Produto():

    @staticmethod
    def data_hora():
        fuso_BR = pytz.timezone('Brazil/East')
        horario_BR = datetime.now(fuso_BR)
        return horario_BR.strftime('%d/%m/%Y')

    def __init__(self,_prodNome,_Preco,_prodDesc,_IMG,_quant):
        self.prodNome = _prodNome
        self.prodDesc = _prodDesc
        self.preco = _Preco
        self.quant = _quant
        self.img = _IMG

    def Venda(self):
        
        global quantidade
        global comprador
        global conta_usuario
        global conta_login
        global venda_preco
        global prod_comprado
        global repetir
        global data_venda
        

        if repetir == 0:
            prod_comprado = [None]*4
            data_venda = [None]*4

            if self.prodNome == 'Bolsa Preta de Couro "Sofisticação Noir"':
                prod_comprado[0] = 'bolsa'
            elif self.prodNome == 'Vestido Vichy Azul "Verão Campestre"':
                prod_comprado[0] = 'vestido'
            elif self.prodNome == 'Calça Jeans Reta "Casual Indigo"':
                prod_comprado[0] = 'calça'
            else:
                prod_comprado[0] = 'salto'
        elif repetir == 1:
            if self.prodNome == 'Bolsa Preta de Couro "Sofisticação Noir"':
                prod_comprado[1] = 'bolsa'
            elif self.prodNome == 'Vestido Vichy Azul "Verão Campestre"':
                prod_comprado[1] = 'vestido'
            elif self.prodNome == 'Calça Jeans Reta "Casual Indigo"':
                prod_comprado[1] = 'calça'
            else:
                prod_comprado[1] = 'salto'
        elif repetir == 2:
            if self.prodNome == 'Bolsa Preta de Couro "Sofisticação Noir"':
                prod_comprado[2] = 'bolsa'
            elif self.prodNome == 'Vestido Vichy Azul "Verão Campestre"':
                prod_comprado[2] = 'vestido'
            elif self.prodNome == 'Calça Jeans Reta "Casual Indigo"':
                prod_comprado[2] = 'calça'
            else:
                prod_comprado[2] = 'salto'
        elif repetir == 3:
            if self.prodNome == 'Bolsa Preta de Couro "Sofisticação Noir"':
                prod_comprado[3] = 'bolsa'
            elif self.prodNome == 'Vestido Vichy Azul "Verão Campestre"':
                prod_comprado[3] = 'vestido'
            elif self.prodNome == 'Calça Jeans Reta "Casual Indigo"':
                prod_comprado[3] = 'calça'
            else:
                prod_comprado[3] = 'salto'


        comprador = ''

        self.quant = self.quant - 1
        quantidade = self.quant
        venda_preco = self.preco

        quant_prod1 = tk.Label(janela_produto,text=f'Em estoque:{self.quant}',font=('Arial Bold',15),background="White",fg = 'black',width=13)
        quant_prod1.place(x = 190, y = 565)

        if conta_login.email == conta_usuario.email:
            comprador = conta_usuario.nome
        else:
            comprador = conta_cliente.nome
        
        data_venda[repetir] = self.data_hora()
        
            
        
        Vender(repetir)
        

        pass

    def reabastecer(self):
        reabastecimento = int(textbox_prod.get())
        self.quant = self.quant + reabastecimento

        quant_prod1 = tk.Label(janela_produto,text=f'Em estoque:{self.quant}',font=('Arial Bold',15),background="White",fg = 'black',width=13)
        quant_prod1.place(x = 190, y = 565)

    
#Objeto que guarda as informações do Cliente
class Conta():
    def __init__(self,_email,_senha,_nome):
        self.email = _email
        self.senha = _senha
        self.nome = _nome

#Função para verificar se a conta existe
def Verificar_Login():
    global se
    global conta_login



    #Verificar se os campos estão devidamente preenchidos
    Email_login = textbox.get()
    Senha_login = textbox1.get()
    conta_login = Conta(Email_login,Senha_login,"")
    VerificarLogin = False
    if Email_login == "" or Senha_login == "":
        erro_login = tk.Label(janela,text = "Preencha todos os campos",bg="white",fg="red")
        erro_login.grid(row=10,columnspan=2)
    else: 
        for x in Email_login:
            if x == "@":
                corte = Email_login[-4:]
                if corte == ".com":
                    VerificarLogin = True
            else:
                erro_login = tk.Label(janela,text="Formato de email inválido",bg="white",fg="red",width=40)
                erro_login.grid(row=10,columnspan=2)

    #Verifica se a conta existe
    if VerificarLogin:

        if conta_login.email == conta_usuario.email and conta_login.senha == conta_usuario.senha:
            se = 1
            conta_login.nome = conta_usuario.nome
            Aba_Catalogo()
        elif conta_criada:
            if conta_login.email == conta_cliente.email:
                if conta_login.senha == conta_cliente.senha:
                    conta_login.nome == conta_cliente.nome
                    Aba_CatalogoCliente()   
                else:
                    erro_login2 = tk.Label(janela,text='Senha incorreta',bg = 'white',fg='red',width=40)
                    erro_login2.grid(row=10,columnspan=2)

            else:
                erro_login3 = tk.Label(janela,text = "Essa conta não existe",bg="white",fg="red",width=40)
                erro_login3.grid(row=10,columnspan=2)
        
        else:
            erro_login3 = tk.Label(janela,text = "Essa conta não existe",bg="white",fg="red",width=40)
            erro_login3.grid(row=10,columnspan=2)


#Função que abre aba de Login(com parâmetro que salva ela em seu estado atual, se não ela ficaria resetando)
def Login(salvar):

    global conta_cliente
    global textbox
    global textbox1
    global janela
    global conta_usuario
    global conta_criada
    global conta_login

    global vestido_prod
    global bolsa_prod
    global calca_prod
    global salto_prod

    global Mensagem_quant 
    global venda_feita
    global num_venda
    global repetir
    global venda_total

    janela = tk.Tk()
    janela.title('Login')
    janela.columnconfigure(1,weight=1)
    janela.config(background='white')
    janela.iconbitmap("Trabalho Loja de Roupa/IMG/Logo.ico")
    janela.geometry("500x300")
    janela.state("zoomed")
    
    if salvar == 0 :
        
        repetir = 0
        venda_feita = False
        Mensagem_quant = [None] * 4
        num_venda = 0
        venda_total = 0

        bolsaimg = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Bolsa.jpg'))
        bolsa_prod = Produto('Bolsa Preta de Couro "Sofisticação Noir"','%.2f'%329.90,' A bolsa "Sofisticação Noir" é uma peça elegante\nconfeccionada em couro preto de alta qualidade, que combina\ndurabilidade e sofisticação. Seu design apresenta linhas suaves e \nmodernas, com detalhes em acabamento impecável que destacam o estilo minimalista.\nPossui alças duplas fixas, reforçadas por rebites\nmetálicos, além de uma alça longa removível e ajustável, permitindo\nversatilidade no uso.',bolsaimg,10)

        vestidoimg = ImageTk.PhotoImage(Image.open("Trabalho Loja de Roupa/IMG/Vestido.jpg"))
        vestido_prod = Produto('Vestido Vichy Azul "Verão Campestre"','%.2f'%100.50,'Este vestido traz um design delicado e feminino, perfeito para \nocasiões descontraídas. Ele possui estampa xadrez em tons de azul,\ncom um busto franzido que proporciona ajuste confortável e valoriza \na silhueta. As alças duplas e finas cruzadas nas costas adicionam um \ntoque charmoso e diferenciado ao visual. A saia rodada garante\nmovimento e leveza, ideal para dias quentes e momentos casuais. \nCombine com sandálias ou tênis para criar looks versáteis e frescos!',vestidoimg,10)

        calcaimg = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Calça.jpg'))
        calca_prod = Produto('Calça Jeans Reta "Casual Indigo"','%.2f'%179.90,'Essa é uma calça jeans reta no tom de "indigo casual", ideal para \nquem busca um visual despojado e versátil. Ela apresenta um design \nclássico com cintura média-alta, bolsos frontais e traseiros\nfuncionais e fecho de zíper com botão metálico. O jeans tem uma \nlavagem azul clara com leves desbotados que dão um toque vintage \ne moderno ao mesmo tempo. Esse modelo é perfeito tanto para \ncomposições casuais com tênis e camiseta quanto para looks mais \narrumados com uma camisa e sapatos.',calcaimg,10)

        saltoimg = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Salto.jpg'))
        salto_prod = Produto('Sandália de Salto Fino "Elegância Nude"','%.2f'%249.90,'Esta sandália de salto fino "Elegância Nude" combina sofisticação e\nminimalismo em um design impecável. Feita em material de alta \nqualidade com acabamento nude, ela apresenta tiras delicadas que \nabraçam o pé de forma elegante. O detalhe trançado na parte \nfrontal adiciona um toque moderno e refinado, enquanto a tira \najustável no tornozelo garante conforto e estabilidade. O salto alto e \nfino alonga a silhueta, tornando-a perfeita para ocasiões especiais \nou eventos formais. Uma escolha versátil e atemporal para \ncomplementar diversos looks, do casual chic ao sofisticado. ',saltoimg,10)

        conta_cliente = Conta(None,None,None)
        conta_login = Conta(None,None,None)

        conta_criada = False

    conta_usuario = Conta('Usuário@gmail.com','Usuário123','NomeQualquer')

    titulo = tk.Label(janela,text = 'Login', font=('Arial Bold',40),background = '#fecad9',fg='#af4759',height=2)
    titulo.grid(row=0,columnspan=2,sticky='NSEW')

    logo = ImageTk.PhotoImage(Image.open('Trabalho Loja de Roupa/IMG/Logo-Photoroom.jpg'))
    tk.Label(janela,image = logo,background='#fecad9').grid(row=0,column=0)

    espaco = tk.Label(janela,text='',background='white')
    espaco.grid(row=1,pady=50)


    mensagem = tk.Label(janela,text = "Email:",font=('Arial Bold',15),background="White",fg='#af4759')
    mensagem.grid(row=2,column=0)

    textbox = tk.Entry(width = 20,font=('Arial Bold',15),background='#fecad9',fg='#af4759',borderwidth=0)
    textbox.grid(row=3,columnspan=2,sticky='NSEW',padx= 50,pady=20)

    mensagem1 = tk.Label(janela,text = "Senha:",fg='#af4759',font=('Arial Bold',15),background="White")
    mensagem1.grid(row=4,column=0)

    textbox1 = tk.Entry(width = 20,font=('Arial Bold',15),background='#fecad9',fg='#af4759',borderwidth=0)
    textbox1.grid(row=5,columnspan=2,sticky='NSEW',padx=50,pady=20,)

    botao_Logar = tk.Button(janela,text = "Entrar",font=('Arial Bold',15),width=13,background='#fecad9',fg='#af4759',activebackground='#fdb4c9',activeforeground='#af4759',borderwidth=0,command = Verificar_Login)
    botao_Logar.grid(row=6,columnspan=2)

    espaco1 = tk.Label(janela,text='',background='white')
    espaco1.grid(row=7)

    mensagem2 = tk.Label(janela,text = "Não tem um conta?",fg='#af4759',font=('Arial Bold',15),background="White")
    mensagem2.grid(row=8,columnspan=2)

    botao_novaConta = tk.Button(janela,text= "Cadastrar-se",font=('Arial Bold',15),width=13,background='#fecad9',fg='#af4759',activebackground='#fdb4c9',activeforeground='#af4759',borderwidth=0,command=Aba_Cadastro)
    botao_novaConta.grid(row=9,columnspan=2)

    janela.mainloop()

Login(0)

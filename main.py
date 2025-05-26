import customtkinter as ctk
import webbrowser
def validar_login():
    usuario = entry_usuario.get()
    senha = entry_senha.get()

    #verificar se o usuario eh pedro e a senha 123456
    if usuario == 'pedro' and senha == '123456':
        resultado_login.configure(text='Login feito com sucesso',text_color='green')
        webbrowser.open('file:///C:/Users/User/OneDrive/Área%20de%20Trabalho/Projeto%20Interface/site.html')
    else:
        resultado_login.configure(text='Login icorreto',text_color='red')    
# iniciar

ctk.set_appearance_mode('dark')

app = ctk.CTk()

app.title('Entre em sua conta')
app.geometry('300x300')

#label
label_usuario = ctk.CTkLabel(app,text='Usuário')
label_usuario.pack(pady=10)

#entry
entry_usuario = ctk.CTkEntry(app,placeholder_text='Digite seu Usuário')
entry_usuario.pack(pady=10)
#label
label_senha = ctk.CTkLabel(app,text='Senha')
label_senha.pack(pady=10)
#entry
entry_senha = ctk.CTkEntry(app, placeholder_text='Digite sua Senha', show='*')
entry_senha.pack(pady=10)

#button
botao_login = ctk.CTkButton(app,text='Login',command=validar_login)
botao_login.pack(pady=10)

resultado_login = ctk.CTkLabel(app,text='')
resultado_login.pack(pady=10)

app.mainloop()


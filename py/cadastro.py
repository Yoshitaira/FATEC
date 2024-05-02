import sqlite3
# Conexão com SGDB
conn = sqlite3.connect("banco.db")
# Obter dados  
print("Cadastramento")
vcpf = int(input("n° do CPF: "))
vnome = input("NOME COMPLETO: ")
vemail = input("E-mail: ")
vsenha = input("Senha: ")
# enviar instrução sql para ser executada pelo banco
conn.execute("insert into user values (?, ?, ?, ?)", (vcpf, vnome, vemail, vsenha))
conn.commit()   
## fechar conexão


quit()

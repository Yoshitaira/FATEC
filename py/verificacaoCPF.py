import sqlite3
#conexão com banco de dados

conn = sqlite3.connect("banco.db")
cursor = conn.cursor()
vcpf = input("CPF: ")

#verifica se o código informado 
cursor.execute( """
                SELECT NOME, EMAIL, SENHA FROM user
                WHERE CPF = ?
                """,(vcpf,)
                )

#recebe retorno do sql
rs = cursor.fetchall()
if rs == []:
    print("CPF não localizado")

else:
    for dados in rs:
        print("NOME", dados[0])
        print("EMAIL", dados[1])
        print("SENHA", dados[2])

#fechar conexão
conn.close
quit()

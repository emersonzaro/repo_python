import sqlite3

conexao = sqlite3.connect("alunos.db")

conexao.execute('''CREATE TABLE IF NOT EXISTS planilha
                (id INTEGER PRIMARY KEY AUTOINCREMENT,
                nome TEXT NOT NULL,
                idade INT NOT NULL); ''')

def criar_aluno(nome,idade):
    conexao.execute("INSERT INTO planilha (nome,idade) VALUES (?,?);", (nome,idade))
    conexao.commit()
    print("Aluno registrado com sucesso.")

def listar_alunos():
    alunos = conexao.execute("SELECT * FROM planilha;")
    for aluno in alunos:
        print(aluno)

def atualizar_aluno(id,novo_nome,nova_idade):
    conexao.execute("UPDATE planilha SET nome = ?, idade = ? WHERE id = ?;", (novo_nome,nova_idade,id))
    conexao.commit()
    print("Aluno atualizado com sucesso.")

def remover_aluno(id):
    conexao.execute("DELETE FROM planilha WHERE id = ?;", (id,))
    conexao.commit()
    print("Aluno removido com sucesso.")

#criar_aluno("Emerson", 49)

listar_alunos()

#remover_aluno(1)
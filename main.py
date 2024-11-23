import os
import mariadb
import  datetime as dt
import time

db = mariadb.connect(
        host="localhost",   # SUBSTITUIR OS # PELO SEU USUARIO E SENHA
        user="##########",
        passwd="#########",
        database="BIBLIOTECA"
        )

cursor = db.cursor()

def cls():
    os.system('cls')
    os.system('clear')

def print_menu_con_aluno(o):
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CONSULTAR ALUNO")
    print("---------------------------------------------------------------------------------------------")
    print("(1) Consultar por nome")
    print("(2) Consultar por turma")
    print("(3) Consultar por matrícula")
    print("\n(4) voltar\n")

    if o == 404:
        print("\n\nOpção inválida! Digite novamente.")

def res_con(cmd, pes):
    cursor.execute(cmd, (pes,))
    res = cursor.fetchall()

    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   Resultado")
    print("---------------------------------------------------------------------------------------------")
    for x in res:
        print(x)

    input("\n\nDigite qualquer tecla para continuar... ")



def con_aluno_nome():
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CONSULTAR ALUNO")
    print("---------------------------------------------------------------------------------------------")
    pes = input("Digite o nome: ")
    cmd = "SELECT * FROM alunos WHERE nome LIKE CONCAT((?), '%')"

    res_con(cmd, pes)


def con_aluno_turma():
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CONSULTAR ALUNO")
    print("---------------------------------------------------------------------------------------------")
    pes = input("Digite a turma: ")
    cmd = "SELECT * FROM alunos WHERE serie LIKE CONCAT((?), '%')"

    res_con(cmd, pes)

def con_aluno_mat():
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CONSULTAR ALUNO")
    print("---------------------------------------------------------------------------------------------")
    pes = int(input("Digite a matrícula: "))
    cmd = "SELECT * FROM alunos WHERE id = (?)"

    res_con(cmd, pes)

def menu_con_aluno():
    o = 0
    while o != 4:
        try:
            print_menu_con_aluno(o)
            o = int(input())
            if o == 1:
                con_aluno_nome()
            elif o == 2:
                con_aluno_turma()
            elif o == 3:
                con_aluno_mat()
            elif o == 4:
                return
            else:
                o = 404
        except:
            o = 404

def print_menu_con_livro(o):
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CONSULTAR LIVRO")
    print("---------------------------------------------------------------------------------------------")
    print("(1) Consultar por titulo")
    print("(2) Consultar por autor")
    print("(3) Consultar por gênero")
    print("(4) Consultar por acervo")
    print("(5) Consultar por id")
    print("\n(6) voltar\n")

    if o == 404:
        print("\n\nOpção inválida! Digite novamente.")

def con_livro_id():
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CONSULTAR LIVRO")
    print("---------------------------------------------------------------------------------------------")
    pes = int(input("Digite o id: "))
    cmd = "SELECT * FROM livros WHERE id = (?)"

    res_con(cmd, pes)

def con_livro_titulo():
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CONSULTAR LIVRO")
    print("---------------------------------------------------------------------------------------------")
    pes = input("Digite o titulo: ")
    cmd = "SELECT * FROM livros WHERE titulo LIKE CONCAT((?), '%')"

    res_con(cmd, pes)

def con_livro_autor():
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CONSULTAR LIVRO")
    print("---------------------------------------------------------------------------------------------")
    pes = input("Digite o autor: ")
    cmd = "SELECT * FROM livros WHERE autor LIKE CONCAT((?), '%')"

    res_con(cmd, pes)

def con_livro_genero():
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CONSULTAR LIVRO")
    print("---------------------------------------------------------------------------------------------")
    pes = input("Digite o gênero: ")
    cmd = "SELECT * FROM livros WHERE genero LIKE CONCAT((?), '%')"

    res_con(cmd, pes)

def con_livro_acervo():
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CONSULTAR LIVRO")
    print("---------------------------------------------------------------------------------------------")
    pes = input("Digite o acervo: ")
    cmd = "SELECT * FROM livros WHERE acervo LIKE CONCAT((?), '%')"

    res_con(cmd, pes)

def print_menu_con_emprestimo(o):
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CONSULTAR EMPRESTIMO")
    print("---------------------------------------------------------------------------------------------")
    print("(1) Consultar por ID do emprestimo")

    print("\n(2) Listar emprestimos ativos")
    print("(3) Listar atrasos")
    print("(4) Listar devoluções")

    print("\n(5) Listar por ID do aluno")
    print("(6) Listar por ID do livro")

    print("\n(7) voltar\n")

    if o == 404:
        print("\n\nOpção inválida! Digite novamente.")

def list_emprestimo_a():
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CONSULTAR EMPRESTIMO")
    print("---------------------------------------------------------------------------------------------")
    pes = int(input("Digite a matrícula: "))
    cmd = "SELECT * FROM emprestimo WHERE idAluno = (?)"

    res_con(cmd, pes)

def list_emprestimo_l():
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CONSULTAR EMPRESTIMO")
    print("---------------------------------------------------------------------------------------------")
    pes = int(input("Digite o ID do livro: "))
    cmd = "SELECT * FROM emprestimo WHERE idLivro = (?)"

    res_con(cmd, pes)

def con_emprestimo_id():
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CONSULTAR EMPRESTIMO")
    print("---------------------------------------------------------------------------------------------")
    pes = int(input("Digite o ID do emprestimo: "))
    cmd = "SELECT * FROM emprestimo WHERE id = (?)"

    res_con(cmd, pes)

def list_emprestimo_ac():
    cmd = "SELECT * FROM emprestimo WHERE estado = 'ATIVO'"
    pes = 0

    res_con(cmd, pes)

def list_atraso():
    cmd = "SELECT * FROM emprestimo WHERE estado = 'ATRASADO'"
    pes = 0

    res_con(cmd, pes)

def list_devolucao():
    cmd = "SELECT * FROM emprestimo WHERE estado = 'ENTREGUE'"
    pes = 0

    res_con(cmd, pes)

def menu_con_emprestimo():
    o = 0
    while o != 9:
        try:
            print_menu_con_emprestimo(o)
            o = int(input())
            if o == 1:
                con_emprestimo_id()
            elif o == 2:
                list_emprestimo_ac()
            elif o == 3:
                list_atrasos()
            elif o == 4:
                list_devolucao()
            elif o == 5:
                list_emprestimo_a()
            elif o == 6:
                list_emprestimo_l()
            elif o == 7:
                return
            else:
                o = 404
        except:
            o = 404

def menu_con_livro():
    o = 0
    while o != 6:
        try:
            print_menu_con_livro(o)
            o = int(input())
            if o == 1:
                con_livro_titulo()
            elif o == 2:
                con_livro_autor()
            elif o == 3:
                con_livro_genero()
            elif o == 4:
                con_livro_acervo()
            elif o == 5:
                con_livro_id()
            elif o == 6:
                return
            else:
                o = 404
        except:
            o = 404

def print_menu_consulta(o):
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CONSULTAS")
    print("---------------------------------------------------------------------------------------------")
    print("(1) Consultar aluno")
    print("(2) Consultar livro")
    print("(3) Consultar emprestimo")
    print("\n(4) voltar\n")

    if o == 404:
        print("\n\nOpção inválida! Digite novamente.")

def menu_consulta():
    o = 0
    while o != 4:
        try:
            print_menu_consulta(o)
            o = int(input())
            if o == 1:
                menu_con_aluno()
            elif o == 2:
                menu_con_livro()
            elif o == 3:
                menu_con_emprestimo()
            elif o == 4:
                return
            else:
                o = 404
        except:
            o = 404

def print_menu_cadastro(o):
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CADASTROS")
    print("---------------------------------------------------------------------------------------------")
    print("(1) Cadastrar aluno")
    print("(2) Cadastrar livro")
    print("\n(3) Remover aluno")
    print("(4) Remover livro")
    print("\n(5) voltar\n")

    if o == 404:
        print("\n\nOpção inválida! Digite novamente.")

def cad_aluno():
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CADASTRAR ALUNO")
    print("---------------------------------------------------------------------------------------------")
    nome = input("Digite o nome: ")
    turma = input("Digite a turma: ")
    mat = int(input("Digite a matrícula: "))

    cmd = "INSERT INTO alunos (id, nome, serie) VALUES (%d, %s, %s)"

    cursor.execute(cmd, (mat, nome, turma))
    db.commit()

def cad_livro():
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   CADASTRAR LIVRO")
    print("---------------------------------------------------------------------------------------------")
    titulo = input("Digite o titulo: ")
    autor = input("Digite o autor: ")
    genero = input("Digite o genero: ")
    acervo = input("Digite o acervo: ")
    n = int(input("Digite o id: "))

    cmd = "INSERT INTO livros (id, titulo, autor, acervo, genero, disponivel) VALUES (%d, %s, %s, %s, %s, 'DISPONIVEL')"

    cursor.execute(cmd, (n, titulo, autor, acervo, genero))
    db.commit()

def rem_aluno():
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   REMOVER ALUNO")
    print("---------------------------------------------------------------------------------------------")
    n = int(input("Digite a matrícula: "))

    cmd = "DELETE FROM alunos WHERE id = (?)"

    cursor.execute(cmd, (n,))
    db.commit()

def rem_livro():
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   REMOVER LIVRO")
    print("---------------------------------------------------------------------------------------------")
    n = int(input("Digite o id: "))

    cmd = "DELETE FROM livros WHERE id = (?)"

    cursor.execute(cmd, (n,))
    db.commit()

def menu_cadastro():
    o = 0
    while o != 5:
        try:
            print_menu_cadastro(o)
            o = int(input())
            if o == 1:
                cad_aluno()
            elif o == 2:
                cad_livro()
            elif o == 3:
                rem_aluno()
            elif o == 4:
                rem_livro()
            elif o == 5:
                return
            else:
                o = 404
        except:
            o = 404


def print_menu_emprestimo(o):
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   EMPRESTIMOS")
    print("---------------------------------------------------------------------------------------------")
    print("(1) Registrar emprestimo")
    print("(2) Registrar devolução")
    print("\n(3) Voltar\n")

    if o == 404:
        print("\n\nOpção inválida! Digite novamente.")

def reg_devolucao():
    valid = 0
    while valid != 1:
        cls()
        print("---------------------------------------------------------------------------------------------")
        print("   REGISTRAR DEVOLUCAO")
        print("---------------------------------------------------------------------------------------------")
        if valid == -1:
            print("\nID não encontrado! Digite 0 para sair ou tente novamente\n")

        n = int(input("Digite o id do emprestimo: "))
        if n == 0:
            return
        cursor.execute("SELECT * FROM emprestimo WHERE id = (?) ", (n,))
        chk = cursor.fetchall()
        if not chk:
            valid = -1
            continue
        else:
            valid = 1

    cursor.execute("SELECT idLivro FROM emprestimo WHERE id = (?) ", (n,))
    x = cursor.fetchall()
    idlivro = 0 + x[0][0]
    cursor.execute("UPDATE emprestimo SET estado = 'ENTREGUE' WHERE id = (?)", (n,))
    cursor.execute("UPDATE livros SET disponivel = 'DISPONIVEL' WHERE id = (?)", (idlivro,))

    db.commit()

def reg_emprestimo():
    valid = 0
    while valid != 1:
        cls()
        print("---------------------------------------------------------------------------------------------")
        print("   REGISTRAR EMPRESTIMO")
        print("---------------------------------------------------------------------------------------------")
        if valid == -1:
            print("\nID não encontrado! Digite 0 para sair ou tente novamente\n")

        idaluno = int(input("Digite a matrícula: "))
        if idaluno == 0:
            return
        cursor.execute("SELECT * FROM alunos WHERE id = (?)", (idaluno,))
        chk = cursor.fetchall()
        if not chk:
            valid = -1
        else:

            idlivro = int(input("Digite o id do livro: "))
            if idlivro == 0:
                return
            cursor.execute("SELECT * FROM livros WHERE id = (?)", (idlivro,))
            chk = cursor.fetchall()
            if not chk:
                valid = -1
                continue
            else:
                valid = 1

    print("---------------------------------------------------------------------------------------------")
    print("   PRAZO")
    print("---------------------------------------------------------------------------------------------")

    inicio = time.strftime('%Y-%m-%d')

    ano = int(input("Digite o ano: "))
    mes = int(input("Digite o mês: "))
    dia = int(input("Digite o dia: "))

    prazo = dt.date(ano,mes,dia)

    prazo = prazo.strftime('%Y-%m-%d')

    cursor.execute("SELECT id FROM emprestimo WHERE id=(SELECT max(id) FROM emprestimo)")
    x = cursor.fetchall()
    if not x:
        idEm = 100000
    else:
        idEm = 1 + x [0][0]

    cmd = "INSERT INTO emprestimo (id, idAluno, idLivro, inicio, prazo, estado) VALUES (%d, %d, %d, %s, %s, %s)"

    cursor.execute(cmd, (idEm, idaluno, idlivro, inicio, prazo, 'ATIVO'))
    cursor.execute("UPDATE livros SET disponivel = 'EMPRESTADO' WHERE id = (?)", (idlivro,))
    db.commit()

def menu_emprestimo():
    o = 0
    while o != 3:
        try:
            print_menu_emprestimo(o)
            o = int(input())
            if o == 1:
                reg_emprestimo()
            elif o == 2:
                reg_devolucao()
            elif o == 3:
                return
            else:
                o = 404
        except:
            o = 404

def print_main_menu(o):
    cls()
    print("---------------------------------------------------------------------------------------------")
    print("   BIBLIOSYS v1.0")
    print("---------------------------------------------------------------------------------------------")
    print("(1) Emprestimos")
    print("(2) Consultas")
    print("(3) Cadastros")
    print("\n(4) Sair\n")

    if o == 404:
        print("\nOpção inválida! Digite novamente.\n")

def main_menu():
    o = 0
    while o != 4:
        try:
            print_main_menu(o)
            o = int(input())
            if o == 1:
                menu_emprestimo()
            elif o == 2:
                menu_consulta()
            elif o == 3:
                menu_cadastro()
            elif o == 4:
                return
            else:
                o = 404
        except:
            o = 404
#MAIN
hoje = time.strftime('%Y-%m-%d')
cursor.execute("UPDATE emprestimo SET estado = 'ATRASADO' WHERE DATE(prazo) < (?) AND estado = 'ATIVO'", (hoje,))
db.commit()

main_menu()

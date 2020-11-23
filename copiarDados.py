from classes import Inscricao, Aluno, Disciplina, Curso
import csv
#Funcao Responsavel por copiar os dados do arquivo para os respectivos objetos.
def copiarDados(arquivo):
    inscricoes = []
    alunos = []
    disciplinas = []
    cursos = []

    codigos_disciplinas = []
    codigos_cursos = []

    with open(arquivo) as csv_file:
        
        csv_reader = csv.reader(csv_file, delimiter=',')

        csv_reader.__next__()

        #copia os dados do arquivo criando objetos do tipo Inscricao.
        for row in csv_reader:
            inscricao = Inscricao(row[0], row[1], row[2], row[3], row[4], row[5])
            inscricoes.append(inscricao)


    #itera entre os objetos criados.
    for i in range(0, len(inscricoes)):
        #cria o objeto Aluno a partir da analise do atributo matricula do objeto Inscricao.
        if(inscricoes[i].matricula != inscricoes[i - 1].matricula):
            inscricoes_aluno = []
            for j in range(i, len(inscricoes)):
                if(inscricoes[j].matricula == inscricoes[i].matricula):
                    inscricoes_aluno.append(inscricoes[j])
                else:
                    break
            aluno = Aluno(inscricoes[i].matricula, inscricoes_aluno)
            alunos.append(aluno)

        #cria o objeto Disciplina a partir da analise do atributo codigo_disciplina do objeto Inscricao.              
        if(inscricoes[i].codigo_disciplina not in codigos_disciplinas):
            codigos_disciplinas.append(inscricoes[i].codigo_disciplina)
            alunos_disciplina = []
            for j in range(0, len(alunos)):
                for k in range(0, len(alunos[j].inscricoes)):
                    if(inscricoes[i].codigo_disciplina == alunos[j].inscricoes[k].codigo_disciplina):
                        alunos_disciplina.append(alunos[j])
                        break
            disciplina = Disciplina(inscricoes[i].codigo_disciplina, inscricoes[i].codigo_curso, inscricoes[i].carga_horaria, alunos_disciplina)
            disciplinas.append(disciplina)

        #cria o objeto Curso a partir da analise do atributo codigo_curso do objeto Inscricao.
        if(inscricoes[i].codigo_curso not in codigos_cursos):
            codigos_cursos.append(inscricoes[i].codigo_curso)
            disciplinas_curso = []
            for j in range(0, len(disciplinas)):
                if(inscricoes[i].codigo_curso == disciplinas[j].codigo_curso):
                    disciplinas_curso.append(disciplinas[j])
            curso = Curso(inscricoes[i].codigo_curso, disciplinas_curso)
            cursos.append(curso)
            
    return inscricoes, alunos, disciplinas, cursos

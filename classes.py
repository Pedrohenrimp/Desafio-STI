#Objeto Inscricao para armazenar os dados de cada linha do arquivo.
class Inscricao:
    def __init__(self, matricula, codigo_disciplina, codigo_curso, nota, carga_horaria, ano_semestre):
        self.matricula = matricula
        self.codigo_disciplina = codigo_disciplina
        self.codigo_curso = codigo_curso
        self.nota = nota
        self.carga_horaria = carga_horaria
        self.ano_semestre = ano_semestre

#Objeto Aluno para armazenar os dados agrupados por numero de matricula.
class Aluno:
    def __init__(self, matricula, inscricoes):
        self.matricula = matricula
        self.inscricoes = inscricoes
    #Funcao para calcular o CR do aluno a partir das materias que esta inscrito.
    def calcularCR(self):
        soma_notas = 0
        soma_ch = 0
        cr_aluno = 0
        for i in range(0, len(self.inscricoes)):
            soma_notas += int(self.inscricoes[i].nota) * int(self.inscricoes[i].carga_horaria)
            soma_ch += int(self.inscricoes[i].carga_horaria)
        cr_aluno = soma_notas / soma_ch
        return cr_aluno

#Objeto Disciplina para armazenar os dados agrupados por codigo da disciplina.
class Disciplina:
    def __init__(self, codigo_disciplina, codigo_curso, carga_horaria, alunos):
        self.codigo_disciplina = codigo_disciplina
        self.codigo_curso = codigo_curso
        self.carga_horaria = carga_horaria
        self.alunos = alunos
    #Funcao para calcular a media entre os CRs dos alunos na disciplina.
    def calcularMediaCR(self):
        soma_notas = 0
        soma_ch = 0
        cr_disciplina = 0
        for i in range(0, len(self.alunos)):
            for j in range(0, len(self.alunos[i].inscricoes)):
                if(self.codigo_disciplina == self.alunos[i].inscricoes[j].codigo_disciplina):
                    soma_notas += int(self.alunos[i].inscricoes[j].nota) * int(self.alunos[i].inscricoes[j].carga_horaria)
                    soma_ch += int(self.alunos[i].inscricoes[j].carga_horaria)
        cr_disciplina = soma_notas / soma_ch
        return cr_disciplina
        
#Objeto Curso para armazenar os dados agrupados por codigo do curso.
class Curso:
    def __init__(self, codigo_curso, disciplinas):
        self.codigo_curso = codigo_curso
        self.disciplinas = disciplinas
    #Funcao para calcular a media entre as medias de CR das disciplinas pertencentes ao curso.
    def calcularMediaCR(self):
        soma_notas = 0
        soma_ch = 0
        cr_curso = 0
        for i in range(0, len(self.disciplinas)):
            soma_notas += int(self.disciplinas[i].calcularMediaCR()) * int(self.disciplinas[i].carga_horaria)
            soma_ch += int(self.disciplinas[i].carga_horaria)
        cr_curso = soma_notas / soma_ch
        return cr_curso
        


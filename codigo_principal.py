from classes import Inscricao, Aluno, Disciplina, Curso
from copiarDados import copiarDados
import csv

arquivo = 'notas.csv'

#Armazena os dados do arquivo "notas.csv" nos respectivos objetos.
inscricoes, alunos, disciplinas, cursos = copiarDados(arquivo)

#Mostra uma lista de matriculas e seus respectivos CRs.
print("------- O CR dos alunos é: --------")
for i in range(0, len(alunos)):
    alunos[i].mostrarCR()
print("-----------------------------------")

#Mostra uma lista de codigos de curso e suas respectivas medias de CR.
print("----- Média de CR dos cursos ------")
for i in range(0, len(cursos)):
    cursos[i].mostrarMediaCR()        
print("-----------------------------------")


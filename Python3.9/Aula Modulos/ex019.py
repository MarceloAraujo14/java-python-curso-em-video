"""Sortear um entre 4 alunos. Descobrir como fazer um loop"""
import random
nome1 = input('Primeiro nome: ')
nome2 = input('Segundo nome: ')
nome3 = input('Terceiro nome: ')
nome4 = input('Quarto nome: ')
lista = [nome1, nome2, nome3, nome4]
alunos = random.choice(lista)
print(f'O escolhido foi: {alunos}')

#Controle de Alunos Academia

#Etapa 1 - Cadastrar alunos
#Etapa 2 - Calcular a média das avaliações de cada aluno
#Etapa 3 - Identificar alunos ativos e inativos
#Etapa 4 - Mostrar os dados de todos os alunos

# Etapa 1 - separar todos os alunos com seus atributos em uma lista.

#"Colchetes" eu abro uma lista de alunos, "Chaves" eu adiciono os alunos;
alunos = [
    {"nome": "Adrian", "idade": 24, "altura": 1.70, "ativo": True, "avaliacoes": [9, 7.5, 8]
    },

#"", uso para guardar na memória e : para linkar um ao outro ex "1": "2", likei 1 ao 2;
    {"nome": "Bruna", "idade": 23, "altura": 1.59, "ativo": False, "avaliacoes": [10, 8, 9.5]
    },

#Se eu linkar algo que precise de mais valores posso usar "[]" para abrir colocar as infos e fechar, criando uma lista dentro da lista;
    {"nome": "Snoop D", "idade": 42, "altura": 1.85, "ativo": True, "avaliacoes": [10, 9, 9.5]
    }
]

#Etapa 2 - Colocar uma função que calcule a média da lista de avaliações dos alunos;
def calcular_media(avaliacoes):
    return sum(avaliacoes) / len(avaliacoes)#sum: soma os valores da lista, len: conta quantos valores tem na lista, assim descobrindo a média;

#Etapa 4 - Criar uma função que mostre apenas os alunos ativos;
def mostrar_alunos_ativos(alunos):
    print("Alunos Ativos: ")
    for aluno in alunos:
        if aluno["ativo"]:
            media = calcular_media(aluno["avaliacoes"])
        print(f"Nome: {aluno["nome"]}")
        print(f"Idade: {aluno["idade"]}")
        print(f"Altura: {aluno["altura"]}")
        print(f"Média Avaliações: {media:.1f}")
        print("-"*20)

def mostrar_alunos_inativos(alunos):
    print("Alunos Inativos: ")
    for aluno in alunos:
        if not aluno["ativo"]:
            media = calcular_media(aluno["avaliacoes"])
        print(f"Nome: {aluno["nome"]}")
        print(f"Idade: {aluno["idade"]}")
        print(f"Altura: {aluno["altura"]}")
        print(f"Média Avaliações: {media:.1f}")
        print("-"*20)
    
mostrar_alunos_ativos(alunos)
mostrar_alunos_inativos(alunos)

from class_alunos import alunos

alunos = alunos()

carga = [
    {"nome": "Ana", "materia": "matematica", "nota": 8.5},
    {"nome": "Bruno", "materia": "historia", "nota": 7.0},
    {"nome": "Carlos", "materia": "matematica", "nota": 9.0},
    {"nome": "Ana", "materia": "historia", "nota": 6.5},
]

for i in carga:
    alunos.adicionar_aluno(i['nome'], i['materia'], i['nota'])

while True:
    print("\nMenu:")
    print("1. Adicionar aluno")
    print("2. Listar alunos")
    print("3. Buscar aluno por nome")
    print("4. Buscar alunos por matéria")
    print("5. Calcular média de um aluno")
    print("6. Calcular média de uma matéria")
    print("7. Sair")

    escolha = input("\nEscolha uma opção: ")

    match escolha:
        #Adicionar aluno
        case "1":
            print("Indique o nome do aluno: ")
            nome = input()
            print("Indique a matéria: ")
            materia = input()
            print("Indique a nota: ")
            nota = float(input())
            alunos.adicionar_aluno(nome, materia, nota)
            print("Aluno adicionado com sucesso!")

        #Listar alunos
        case "2":
            lista_alunos = alunos.listar_alunos()
            print("Lista de alunos:\n")
            for aluno in lista_alunos:
                print(f"Nome: {aluno['nome']}, Matéria: {aluno['materia']}, Nota: {aluno['nota']}")

        #Buscar aluno por nome
        case "3":
            print("Indique o nome do aluno a buscar: ")
            nome = input()
            lista_alunos = alunos.buscar_aluno(nome)
            for aluno in lista_alunos:
                print(f"Nome: {aluno['nome']}, Matéria: {aluno['materia']}, Nota: {aluno['nota']}")

        #Buscar alunos por matéria 
        case "4":
            print("Indique a matéria a buscar: ")
            materia = input()
            lista_alunos = alunos.buscar_materia(materia)
            for aluno in lista_alunos:
                print(f"Nome: {aluno['nome']}, Matéria: {aluno['materia']}, Nota: {aluno['nota']}")
        
        #Calcular média de um aluno
        case "5":
            print("Indique o nome do aluno para calcular a média: ")
            nome = input()
            media = alunos.calcular_media(nome)
            print(f"Média do aluno {nome}: {media}")

        #Calcular média de uma matéria    
        case "6":
            print("Indique a matéria para calcular a média: ")
            materia = input()
            media = alunos.calcular_media_materia(materia)
            print(f"Média da matéria {materia}: {media}")

        #Sair
        case "7":
            print("Saindo...")
            break
        case _:
            print("Opção inválida. Tente novamente.")
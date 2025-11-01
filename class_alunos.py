class alunos:
    def __init__(self):
        self.lista_alunos = []
    
    def adicionar_aluno(self, nome, materia, nota):
        self.lista_alunos.append({"nome": nome.lower().strip(), "materia": materia.lower().strip(), "nota": float(nota)})
    
    def listar_alunos(self):
        return self.lista_alunos

    def buscar_aluno(self, nome):
        nome = nome.lower().strip()
        aluno = []
        for i in self.lista_alunos:
            if i['nome'] == nome:
                aluno.append(i)
        return aluno

    def buscar_materia(self, materia):
        materia = materia.lower().strip()
        materia_lista = []
        for i in self.lista_alunos:
            if i['materia'] == materia:
                materia_lista.append(i)
        return materia_lista

    #calcular média das notas por aluno
    def calcular_media(self, nome):
        nome = nome.lower().strip()
        aluno = self.buscar_aluno(nome)
        check_aluno = len(aluno)
        if check_aluno == 0:
            return "Aluno não encontrado"
        soma_notas = 0
        for i in aluno:
            soma_notas += i['nota']
        media =  soma_notas / check_aluno
        return media
    
    #calcular média das notas por matéria
    def calcular_media_materia(self, materia):
        materia = materia.lower().strip()
        materia_lista = self.buscar_materia(materia)
        check_materia = len(materia_lista)
        if check_materia == 0:
            return "Matéria não encontrada"
        soma_notas = 0
        for i in materia_lista:
            soma_notas += i['nota']
        media = soma_notas / check_materia
        return media
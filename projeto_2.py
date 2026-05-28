import json
import os

class Tarefa:
    def __init__(self, titulo, concluida=False):
        self.titulo = titulo
        self.concluida = concluida
    
    def to_dict(self):
        return{
            "titulo": self.titulo,
            "concluida": self.concluida,
        }

class GerenciadorTarefas:
    def __init__(self):
        self.tarefas = []
        self.arquivo = "tarefas.json"
        self.carregar()
    
    def adicionar(self, titulo):
        if not titulo.strip():
            print("[!] Título não pode ser vazio.")
            return
        tarefa = Tarefa(titulo)
        self.tarefas.append(tarefa)
        self.salvar()

    def listar(self):
        if not self.tarefas:
            print("Nenhuma tarefa.")
            return

        for i, tarefa in enumerate(self.tarefas, start=1):
            status = "X" if tarefa.concluida else " "
            print(f"[{status}] {i}. {tarefa.titulo}")

    def concluir(self, indice):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice].concluida = True
            self.salvar()
            print("✔ Tarefa concluída!")
        else:
            print("[!] Número inválido.")

    def remover(self, indice):
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
            self.salvar()
            print("✔ Tarefa removida!")
        else:
            print("[!] Número inválido.")

    def salvar(self):
        dados = [t.to_dict() for t in self.tarefas]
        with open(self.arquivo, "w") as f:
            json.dump(dados, f, indent=4, ensure_ascii=False)
    
    def carregar(self):
        if os.path.exists(self.arquivo):
            with open(self.arquivo, "r") as f:
                dados = json.load(f)
                for item in dados:
                    tarefa = Tarefa(
                        item["titulo"],
                        item["concluida"]
                    )
                    self.tarefas.append(tarefa)

gerenciador = GerenciadorTarefas()

while True:
    print("\n1-Adicionar")
    print("2-Listar")
    print("3-Concluir")
    print("4-Remover")
    print("5-Sair")
    
    opcao = input("Escolha: ")

    if opcao == "1":
        titulo = input("Digite a tarefa: ")
        gerenciador.adicionar(titulo)
    
    elif opcao == "2":
        gerenciador.listar()
    
    elif opcao == "3":
        gerenciador.listar()
        try:
            indice = int(input("Número da tarefa: "))-1
            gerenciador.concluir(indice)
        except ValueError:
            print("[!] Digite apenas números.")
    
    elif opcao == "4":
        gerenciador.listar()
        try:
            indice = int(input("Número da tarefa: "))-1
            gerenciador.remover(indice)
        except ValueError:
            print("[!] Digite apenas números.")

    elif opcao == "5":
        print("Saindo...")
        break
    
    else:
        print("[!] Opcao invalida.")

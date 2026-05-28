# ✅ Gerenciador de Tarefas CLI

Projeto 2 do Módulo 1.2 — Roadmap Arquiteto de Convergência Tecnológica  
**Fase 1 › Fundamentos › Python**

---

## 📌 Problema resolvido

Aplicação de linha de comando em Python para gerenciar tarefas do dia a dia, com persistência automática em JSON e estrutura orientada a objetos.

---

## ⚙️ Funcionalidades

- Adicionar tarefas com validação de entrada
- Listar tarefas com status visual `[X]` concluída / `[ ]` pendente
- Marcar tarefa como concluída
- Remover tarefa da lista
- Persistência automática em JSON — dados mantidos entre sessões
- Tratamento de erros de entrada (letras no lugar de números, título vazio)

---

## 🗂️ Estrutura do projeto

```
F1M12-Projeto2/
├── projeto_2.py   # Script principal
├── tarefas.json   # Gerado automaticamente na execução
└── README.md
```

---

## 🚀 Como executar

**Pré-requisitos:** Python 3.8+

```bash
# Clone o repositório
git clone https://github.com/arqconvtec2026/-F1M12-Projeto2.git
cd -F1M12-Projeto2

# Execute
python projeto_2.py
```

---

## 🖥️ Exemplo de uso

```
1-Adicionar
2-Listar
3-Concluir
4-Remover
5-Sair
Escolha: 1
Digite a tarefa: Estudar Python

Escolha: 2
[ ] 1. Estudar Python

Escolha: 3
[ ] 1. Estudar Python
Número da tarefa: 1
✔ Tarefa concluída!

Escolha: 2
[X] 1. Estudar Python
```

---

## 🏗️ Arquitetura

O projeto é dividido em duas classes:

| Classe | Responsabilidade |
|---|---|
| `Tarefa` | Representa uma tarefa com título e status |
| `GerenciadorTarefas` | Controla a lista, persistência e operações |

---

## 🛠️ Tecnologias utilizadas

| Tecnologia | Uso |
|---|---|
| Python 3 | Linguagem principal |
| `json` | Persistência de dados |
| `os` | Verificação de arquivo existente |

---

## 📚 Conceitos praticados

- Programação Orientada a Objetos (classes, métodos, atributos)
- Serialização e desserialização de objetos com JSON
- Leitura e escrita de arquivos
- Tratamento de exceções (`ValueError`)
- Validação de entrada do usuário
- Controle de fluxo com `while` e `break`

# 🧋 Sistema de Pedidos com Cadastro e Cashback

## 📌 Descrição
Este projeto consiste em um sistema de atendimento para pedidos de bebidas, desenvolvido em Python. 
O sistema permite cadastrar clientes, registrar pedidos personalizados, aplicar descontos de acordo com a categoria do cliente e gerenciar um sistema de cashback com persistência de dados em arquivo.
As informações dos clientes são armazenadas localmente utilizando serialização com `pickle`.


## 🎯 Objetivo
Aplicar conceitos fundamentais e intermediários de programação, como:

- Programação orientada a objetos (POO)
- Criação de classes
- Manipulação de dicionários
- Estruturas condicionais e de repetição
- Validação de entrada de dados
- Persistência de dados com arquivos binários (`pickle`)
- Modularização com múltiplos arquivos


## 🧠 Funcionalidades

- 👤 Cadastro automático de clientes
- 🔎 Verificação de cliente já existente
- 🧋 Montagem personalizada de bebida (base + complementos)
- 🎓 Desconto por categoria:
  - Estudante → 25% de desconto
  - Funcionário → desconto fixo de R$ 1,00
- 💰 Sistema de cashback (10% do valor final)
- 💾 Armazenamento permanente dos dados dos clientes
- 📂 Atualização automática do arquivo `registro.dat`


## 🗂 Estrutura do projeto

- `principal1.py` → Arquivo principal com a lógica de atendimento
- `secundário.py` → Definição das classes e funções auxiliares
- `registro.dat` → Arquivo binário onde os dados dos clientes são armazenados


## 🛠 Tecnologias utilizadas

- Python
- Biblioteca `pickle` (persistência de dados)


## ▶️ Como executar

1. Certifique-se de ter o Python instalado
2. Baixe ou clone este repositório
3. Execute o arquivo principal
4. Siga as instruções exibidas no terminal

## 💾 Persistência de Dados

O sistema utiliza a biblioteca pickle para salvar e recuperar informações dos clientes em um arquivo binário (registro.dat).
Isso permite que:
1. O cashback seja mantido entre execuções
2. Clientes já cadastrados sejam reconhecidos automaticamente

## 📚 Contexto

Projeto desenvolvido para a disciplina MI - Algoritmos, com foco na prática de:
1. Programação orientada a objetos
2. Manipulação de arquivos
3. Modelagem de sistemas reais

## 📄 Relatório completo
Para mais detalhes sobre o desenvolvimento do projeto, acesse o relatório completo.

## ✍️ Autora
Vivian Martins Moura

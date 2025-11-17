# 🐲 Implementação Estrutura de Ficha Old Dragon 🐲

## 📚 Disciplina: Tópicos Especiais em Software  
## 👨‍🏫 Professor: Aryel Marlus Repula de Oliveira  
## 👩‍💻 Aluno: Gabriela Pedroso dos Santos Pontes

### ✨ Descrição

Este projeto visa a criação de um sistema de geração de personagens para o RPG *Old Dragon*. Através dessa implementação, é possível criar personagens com diferentes opções de **atributos**, **raça** e **classe**, além de salvar as informações do personagem em um arquivo JSON para persistência de dados.

A implementação é feita em Python, utilizando **orientação a objetos** para a lógica de criação de personagens e **Flask** para a interface web. A arquitetura segue o padrão **MVC**, separando claramente a lógica de negócios, a visualização e o controle da aplicação.

### 🗂️ Estrutura do Repositório

O repositório está organizado em três diretórios principais, que representam as diferentes partes do projeto:

#### 📂 Diretório: `Model`

Aqui está a parte central da aplicação, onde a lógica de criação do personagem é implementada. A estrutura segue os princípios de **orientação a objetos** e inclui:

- **Distribuição de Atributos**: Implementação das três formas de distribuição de atributos (clássica, heróica e aventureira) conforme as regras do *Old Dragon*.
- **Raças**: A definição das características comuns das raças e suas habilidades específicas. São levadas em conta as três características comuns (movimento, infravisão e alinhamento).
- **Classes**: Implementação de pelo menos três classes de personagem, com as habilidades específicas para cada uma delas.

#### 📂 Diretório: `FLASK`

Este diretório contém o front-end desenvolvido em **Flask**. Ele permite que o usuário interaja com a aplicação e crie seu personagem. A estrutura inclui:

- **Distribuição de Atributos**: O usuário pode escolher entre os três modos de distribuição de atributos.
- **Escolha de Raça e Classe**: O sistema permite escolher entre três raças e três classes disponíveis.
- **Interface Simples**: O front-end lista as habilidades de cada classe e raça, sem necessidade de implementação completa das habilidades neste momento.

A arquitetura segue o padrão **MVC**, com separação clara entre o modelo de dados e a interface do usuário.

#### 📂 Diretório: `JSON`

Após a criação do personagem, os dados são salvos em um arquivo **JSON**. O sistema usa o método `.__dict__` para serializar a instância do personagem em formato JSON e armazenar os atributos do personagem de maneira persistente.

### 🛠️ Requisitos

- **Distribuição de Atributos**: O sistema deve oferecer as três opções de distribuição de atributos: **clássica**, **heróica** e **aventureira**.
- **Raças e Classes**: O sistema deve permitir a escolha de pelo menos 3 raças e 3 classes, cada uma com habilidades específicas.
- **Arquitetura MVC**: O projeto segue a arquitetura **MVC** para organizar o código em Model (lógica de dados), View (interface) e Controller (controle da aplicação).
- **Flask**: O front-end é feito com **Flask**, enquanto o modelo é separado em um diretório/package `model`.
- **Salvar em JSON**: Após a criação do personagem, os dados são salvos em um arquivo **JSON**.

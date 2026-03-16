# Projeto Pilha & Hash - Tratamento de Colisão

Este projeto apresenta a implementação de uma **Tabela Hash** utilizando a técnica de **Encadeamento Exterior (Separate Chaining)** para a resolução de colisões. O sistema permite o armazenamento e busca de objetos da classe `Empregado` de forma eficiente.

## 🛠️ Tecnologias
* **Linguagem:** Python 3.x (Migrado de uma base Java)
* **Estrutura de Dados:** Tabela Hash e Listas Encadeadas

## 📌 Funcionalidades
- **Função Hash:** Calcula o índice com base no ID do empregado utilizando a operação de módulo.
- **Tratamento de Colisão:** Utiliza uma lista encadeada (baseada em Nós) para armazenar múltiplos elementos que geram o mesmo índice.
- **Busca Eficiente:** Localiza empregados percorrendo apenas a lista específica do índice calculado.
- **Visualização:** Exibe o estado interno da tabela, evidenciando as conexões entre os nós nos índices.

## 📂 Estrutura do Código
* `Empregado`: Entidade principal com ID e Nome.
* `No`: Estrutura de suporte para a lista encadeada.
* `TabelaHashEncadeada`: Lógica central da tabela, incluindo inserção, busca e visualização.

## 🚀 Como Executar
Basta rodar o script principal:
```bash
python main.py

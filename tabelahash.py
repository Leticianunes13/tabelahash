class Empregado:
    def __init__(self, id_emp, primeiro_nome, ultimo_nome):
        self.id = id_emp [cite: 267]
        self.primeiro_nome = primeiro_nome [cite: 268]
        self.ultimo_nome = ultimo_nome [cite: 268]

    def __str__(self):
        return f"Empregado{{id={self.id}, nome='{self.primeiro_nome} {self.ultimo_nome}'}}"


class No:
    def __init__(self, empregado):
        self.empregado = empregado [cite: 315]
        self.proximo = None  # Equivalente ao 'private No no' em Java [cite: 314]


class TabelaHashEncadeada:
    def __init__(self, capacidade):
        self.capacidade = capacidade
        # Inicializa a tabela com slots vazios (None)
        self.tabela = [None] * capacidade

    def _funcao_hash(self, id_emp):
        return abs(id_emp) % self.capacidade

    def inserir(self, empregado):
        indice = self._funcao_hash(empregado.id)
        novo_no = No(empregado)
        
        novo_no.proximo = self.tabela[indice]
        self.tabela[indice] = novo_no

    def buscar(self, id_emp):
        indice = self._funcao_hash(id_emp)
        atual = self.tabela[indice]
        
        while atual:
            if atual.empregado.id == id_emp:
                return atual.empregado
            atual = atual.proximo
        return None

    def imprimir_tabela(self):
        print("\n=== ESTADO DA TABELA HASH ===")
        for i in range(self.capacidade):
            print(f"Índice {i}:", end=" ")
            atual = self.tabela[i]
            if not atual:
                print("[Vazio]")
            else:
                caminho = []
                while atual:
                    caminho.append(str(atual.empregado))
                    atual = atual.proximo
                print(" -> ".join(caminho))
        print("=============================\n")


if __name__ == "__main__":
    e1 = Empregado(1123, "Gabriel", "Brasil")
    e2 = Empregado(5432, "Lucas", "Souza")
    e3 = Empregado(2221, "Dina", "Borges")
    e4 = Empregado(4314, "Moises", "Cerqueira")

    hash_table = TabelaHashEncadeada(3)

    # Inserção
    hash_table.inserir(e1)
    hash_table.inserir(e2)
    hash_table.inserir(e3)
    hash_table.inserir(e4)

    # Visualização
    hash_table.imprimir_tabela()

    # Teste de Busca
    id_para_busca = 2221
    resultado = hash_table.buscar(id_para_busca)
    if resultado:
        print(f"Busca pelo ID {id_para_busca}: {resultado}")
    else:
        print(f"ID {id_para_busca} não encontrado.")
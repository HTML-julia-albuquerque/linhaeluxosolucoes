#4 concluído
class PaymentMethods:
    """
    Classe para gerenciar formas de pagamento usando fila (deque).
    Formas disponíveis: Débito, Crédito, Pix.
    """
    def __init__(self):

        self._fila: deque[str] = deque(["Cartão Débito", "Cartão Crédito", "Pix"])  # Fila (deque) com as formas de pagamento na ordem desejada

    def mostrar_formas(self) -> None:
        """
        Exibe as formas de pagamento disponíveis, em ordem da fila.
        """
        print("\n--- Formas de Pagamento Disponíveis ---")
        temp_queue = deque()
        idx = 1
        while self._fila: # Percorremos a fila sem esvaziar, usando deque temporária
            metodo = self._fila.popleft()
            print(f"{idx} - {metodo}")
            temp_queue.append(metodo)
            idx += 1
        self._fila = temp_queue # Restauramos a fila original
        print("---------------------------------------\n")

    def calcular_pagamento(self, valor: float, opcao: int) -> float | None:
        """
        Retorna o valor final a pagar. Aqui, não há juros/descontos: retorna valor original
        se a opção for válida (1, 2 ou 3). Caso contrário, retorna None.
        """
        if opcao in [1, 2, 3]:
            return valor
        print("Opção de pagamento inválida.")
        return None

    def metodo_por_indice(self, opcao: int) -> str | None:
        """
        Retorna a forma de pagamento correspondente ao índice (1-based), ou None se inválido.
        """
        if opcao < 1 or opcao > len(self._fila):
            return None
        return list(self._fila)[opcao - 1] # Como precisamos iterar sem alterar a fila, convertemos para lista temporária

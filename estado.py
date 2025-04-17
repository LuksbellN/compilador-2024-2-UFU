class EstadoProcessamento:
    def __init__(self):
        self.linha = 1
        self.coluna = 1

    def atualizar_posicao(self, linha, coluna):
        self.linha = linha
        self.coluna = coluna

    def obter_posicao(self):
        return self.linha, self.coluna

# Instância global do estado
estado = EstadoProcessamento() 
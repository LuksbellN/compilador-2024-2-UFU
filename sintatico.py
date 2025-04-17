from lexico import retornatoken, Token
from estado import estado

class Pilha:
    def __init__(self):
        self.items = []
    
    def esta_vazia(self):
        return len(self.items) == 0
    
    def empilha(self, item):
        self.items.append(item)
    
    def desempilha(self):
        if not self.esta_vazia():
            return self.items.pop()
        return None
    
    def topo(self):
        if not self.esta_vazia():
            return self.items[-1]
        return None

class AnalisadorSintatico:
    def __init__(self, arquivo):
        self.arquivo = arquivo
        self.pilha = None
        self.prox_token = None
        self.token_atual = None
        
        self.producoes = {
            1: ['programa', 'ID', '(', ')', 'BLOCO'],
            2: ['{%', 'DEC_VARIAVEIS', 'SEQ_CMD', '%}'],
            3: ['DEC_VARIAVEL', 'DEC_VARIAVEIS'],
            4: ['ε'],
            5: ['TIPO', ':', 'LISTA_IDS', ';'],
            6: ['int'],
            7: ['float'],
            8: ['char'],
            9: ['ID', 'LISTA_IDS\''],
            10: [',', 'ID', 'LISTA_IDS\''],
            11: ['ε'],
            12: ['COMAND', 'SEQ_CMD'],
            13: ['ε'],
            14: ['CMD_IF'],
            15: ['CMD_WHILE'],
            16: ['CMD_DO_WHILE'],
            17: ['CMD_ATRIBUICAO'],
            18: ['ID', ':=', 'EXPRE', ';'],
            19: ['if', '[', 'CONDICAO', ']', 'then', 'CMD_OR_BLOCO', 'CMD_IF_TAIL'],
            20: ['CMD_ELSEIF_LIST', 'CMD_ELSE_OPT'],
            21: ['elseif', '[', 'CONDICAO', ']', 'then', 'CMD_OR_BLOCO', 'CMD_ELSEIF_LIST'],
            22: ['ε'],
            23: ['else', 'CMD_OR_BLOCO'],
            24: ['ε'],
            25: ['while', '[', 'CONDICAO', ']', 'CMD_OR_BLOCO'],
            26: ['do', 'CMD_OR_BLOCO', 'while', '[', 'CONDICAO', ']', ';'],
            27: ['COMAND'],
            28: ['BLOCO'],
            29: ['EXPRE', 'relop', 'EXPRE'],
            30: ['TERMO', 'EXPRE\''],
            31: ['+', 'TERMO', 'EXPRE\''],
            32: ['-', 'TERMO', 'EXPRE\''],
            33: ['ε'],
            34: ['EXP', 'TERMO\''],
            35: ['*', 'EXP', 'TERMO\''],
            36: ['/', 'EXP', 'TERMO\''],
            37: ['ε'],
            38: ['FATOR', 'EXP\''],
            39: ['**', 'FATOR', 'EXP\''],
            40: ['ε'],
            41: ['-', 'FATOR'],
            42: ['caractere'],
            43: ['num'],
            44: ['ID'],
            45: ['(', 'EXPRE', ')']
        }

        self.tabela = {
            'APLICATIVO': {'programa': 1},
            'BLOCO': {'{%': 2},
            'DEC_VARIAVEIS': {
                'int': 3, 'float': 3, 'char': 3,
                'ID': 4, 'if': 4, 'while': 4, 'do': 4, '%}': 4
            },
            'DEC_VARIAVEL': {'int': 5, 'float': 5, 'char': 5},
            'TIPO': {'int': 6, 'float': 7, 'char': 8},
            'LISTA_IDS': {'ID': 9},
            'LISTA_IDS\'': {';': 11, ',': 10},
            'SEQ_CMD': {'ID': 12, '%}': 13, 'if': 12, 'while': 12, 'do': 12},
            'COMAND': {'ID': 17, 'if': 14, 'while': 15, 'do': 16},
            'CMD_ATRIBUICAO': {'ID': 18},
            'CMD_IF': {'if': 19},
            'CMD_IF_TAIL': {'ID': 20, '%}': 20, 'if': 20, 'while': 20, 'do': 20, 'elseif': 20, 'else': 20},
            'CMD_ELSEIF_LIST': {'ID': 22, '%}': 22, 'if': 22, 'while': 22, 'do': 22, 'else': 22, 'elseif': 21},
            'CMD_ELSE_OPT': {'ID': 24, '%}': 24, 'if': 24, 'while': 24, 'do': 24, 'else': 23},
            'CMD_WHILE': {'while': 25},
            'CMD_DO_WHILE': {'do': 26},
            'CMD_OR_BLOCO': {'ID': 27, '{%': 28, 'if': 27, 'while': 27, 'do': 27},
            'CONDICAO': {'ID': 29, '(': 29, 'num': 29, 'caractere': 29, '-': 29},
            'EXPRE': {'ID': 30, '(': 30, 'num': 30, 'caractere': 30, '-': 30},
            'EXPRE\'': {')': 33, ']': 33, ';': 33, 'relop': 33, '+': 31, '-': 32, '%}': 33},
            'TERMO': {'ID': 34, '(': 34, 'num': 34, 'caractere': 34, '-': 34},
            'TERMO\'': {')': 37, ']': 37, ';': 37, 'relop': 37, '+': 37, '-': 37, '*': 35, '/': 36, '%}': 37},
            'EXP': {'ID': 38, '(': 38, 'num': 38, 'caractere': 38, '-': 38},
            'EXP\'': {')': 40, ']': 40, ';': 40, 'relop': 40, '+': 40, '-': 40, '*': 40, '/': 40, '**': 39, '%}': 40},
            'FATOR': {'ID': 44, '(': 45, 'num': 43, 'caractere': 42, '-': 41}
        }

        self.terminais = {
            'programa', 'ID', '(', ')', '{%', '%}', ':', ';', 'int', 'float', 'char',
            ',', ':=', 'if', '[', ']', 'then', 'elseif', 'else', 'while', 'do',
            'relop', '+', '-', '*', '/', '**', 'caractere', 'num', '$'
        }

    def inicializa_pilha(self):
        self.pilha = Pilha()
        self.pilha.empilha('$')
        self.pilha.empilha('APLICATIVO')

    def lex(self):
        while True:
            try:
                token = retornatoken(self.arquivo)
                
                
                print(f"Token lido: {token}")
                
                if isinstance(token, str):
                    if token == '$':
                        return '$'
                    else:
                        return token
                elif token is None:
                    return '$'
                
                if token.token == 'ws':
                    continue
                
                self.token_atual = token
                
                return token.token
                
            except Exception as e:
                
                print(f"Erro ao ler token: {str(e)}")
                return '$'

    def erro(self, mensagem=""):
        if self.token_atual:
            linha = self.token_atual.linha
            coluna = self.token_atual.coluna
            print(f"Erro de sintaxe na linha {linha}, coluna {coluna}: {mensagem}")
            print(f"Token encontrado: {self.token_atual.token} (lexema: {self.token_atual.lexema})")
        else:
            linha, coluna = estado.obter_posicao()
            print(f"Erro de sintaxe na linha {linha}, coluna {coluna}: {mensagem}")
        return False

    def eh_terminal(self, simbolo):
        return simbolo in self.terminais

    def trata_producao(self, num_producao):
        if num_producao not in self.producoes:
            self.erro(f"Produção {num_producao} não encontrada")
            return
        
        X = self.pilha.topo()
        self.pilha.desempilha()
        producao = self.producoes[num_producao]
        
        
        print(f"Aplicando produção {num_producao}: {X} -> {' '.join(producao)}")
        
        for simbolo in reversed(producao):
            if simbolo != 'ε':
                self.pilha.empilha(simbolo)
                
                print(f"Empilhando: {simbolo}")

    def analisar(self):
        self.inicializa_pilha()
        self.prox_token = self.lex()
        
        
        print("Iniciando análise sintática")
        print(f"Token inicial: {self.prox_token}")

        while not self.pilha.esta_vazia():
            X = self.pilha.topo()
            
            
            print(f"\nTopo da pilha: {X}")
            print(f"Token atual: {self.prox_token}")

            if self.eh_terminal(X) or X == '$':
                if X == self.prox_token:
                    print(f"Match: {X}")
                    self.pilha.desempilha()
                    self.prox_token = self.lex()
                else:
                    self.erro(f"Token inesperado. Esperado '{X}', mas encontrado '{self.prox_token}'")
                    return False
            else:
                if X not in self.tabela:
                    return self.erro(f"Erro interno: símbolo não-terminal '{X}' não encontrado na tabela de análise")
                elif self.prox_token not in self.tabela[X]:
                    esperados = ", ".join(f"'{t}'" for t in self.tabela[X].keys())
                    return self.erro(f"Token '{self.prox_token}' inesperado. Tokens esperados: {esperados}")
                else:
                    num_producao = self.tabela[X][self.prox_token]
                    self.trata_producao(num_producao)

        print("Análise sintática concluída com sucesso!")
        return True

def main():
    nome_arquivo = input("Digite o nome do arquivo a ser analisado: ")
    try:
        with open(nome_arquivo, "r", encoding="utf-8") as arquivo:
            analisador = AnalisadorSintatico(arquivo)
            try:
                if analisador.analisar():
                    print("Programa aceito pela gramática!")
            except SyntaxError as e:
                print(e)
    except FileNotFoundError:
        print(f"Arquivo '{nome_arquivo}' não encontrado.")

if __name__ == "__main__":
    main()
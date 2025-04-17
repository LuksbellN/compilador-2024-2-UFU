tabela_simbolos = {}

class Token:
    def __init__(self, token, lexema, valor, linha, coluna):
        self.token = token
        self.lexema = lexema
        self.valor = valor
        self.linha = linha
        self.coluna = coluna

    def __repr__(self):
        return f"Token(token='{self.token}', lexema='{self.lexema}' valor='{self.valor}', linha={self.linha}, coluna={self.coluna})"


def tok_id(lexema, linha, coluna):
    token2 = Token('ID', lexema, '__', linha, coluna)
    if token2.lexema not in tabela_simbolos:
        tabela_simbolos[token2.lexema] = token2
    print(token2)
    return token2
def tok_while(linha, coluna):
    token2 = Token('while','while', '__', linha, coluna)
    print(token2)
    return token2
def tok_ws(linha, coluna):
    token2 = Token('ws','__', '__', linha, coluna)
    print(token2)
    return token2
def tok_prog(linha, coluna):
    token2 = Token('programa','programa', '__', linha, coluna)
    print(token2)
    return token2
def tok_if(linha, coluna):
    token2 = Token('if','if', '__', linha, coluna)
    print(token2)
    return token2
def tok_int(linha, coluna):
    token2 = Token('int','int', '__', linha, coluna)
    print(token2)
    return token2
def tok_then(linha, coluna):
    token2 = Token('then','then', '__', linha, coluna)
    print(token2)
    return token2
def tok_else(linha, coluna):
    token2 = Token('else','else', '__', linha, coluna)
    print(token2)
    return token2
def tok_elseif(linha, coluna):
    token2 = Token('elseif','elseif', '__', linha, coluna)
    print(token2)
    return token2
def tok_do(linha, coluna):
    token2 = Token('do','do', '__', linha, coluna)
    print(token2)
    return token2
def tok_float(linha, coluna):
    token2 = Token('float','float', '__', linha, coluna)
    print(token2)
    return token2
def tok_char(linha, coluna):
    token2 = Token('char','char', '__', linha, coluna)
    print(token2)
    return token2
def tok_char(linha, coluna):
    token2 = Token('char','char', '__', linha, coluna)
    print(token2)
    return token2
def tok_relop(lexema, tipo, linha, coluna):
    token2 = Token('relop', lexema, tipo, linha, coluna)
    print(token2)
    return token2
def tok_op(lexema, tipo, linha, coluna):
    token2 = Token(lexema, lexema, tipo, linha, coluna)
    print(token2)
    return token2
def tok_comment(linha, coluna):
    token2 = Token('comment', '__', '__', linha, coluna)
    print(token2)
    return token2
def tok_ok(linha, coluna):
    token2 = Token('{%', '{%', '__', linha, coluna)
    print(token2)
    return token2
def tok_ko(linha, coluna):
    token2 = Token('%}', '%}','__', linha, coluna)
    print(token2)
    return token2
def tok_carac(lexema, linha, coluna):
    token2 = Token('carac', lexema, '__', linha, coluna)
    if token2.lexema not in tabela_simbolos:
        tabela_simbolos[token2.lexema] = token2
    print(token2)
    return token2
def tok_pontvirg(linha, coluna):
    token2 = Token(';', ';', '__', linha, coluna)
    print(token2)
    return token2
def tok_parentesq(linha, coluna):
    token2 = Token('(', '(', '__', linha, coluna)
    print(token2)
    return token2
def tok_parentdir(linha, coluna):
    token2 = Token(')', ')', '__', linha, coluna)
    print(token2)
    return token2
def tok_doispont(linha, coluna):
    token2 = Token(':', ':', '__', linha, coluna)
    print(token2)
    return token2
def tok_doisponteq(linha, coluna):
    token2 = Token(':=', ':=', '__', linha, coluna)
    print(token2)
    return token2
def tok_num(lexema, linha, coluna):
    valor = lexema
    token2 = Token('num', lexema, valor, linha, coluna)
    if token2.lexema not in tabela_simbolos:
        tabela_simbolos[token2.lexema] = token2
    print(token2)
    return token2

def tok_colchesq(linha, coluna):
    token2 = Token('[', '[', '__', linha, coluna)
    print(token2)
    return token2

def tok_colchdir(linha, coluna):
    token2 = Token(']', ']', '__', linha, coluna)
    print(token2)
    return token2

def tok_virg(linha, coluna):
    token2 = Token(',', ',', '__', linha, coluna)
    print(token2)
    return token2


def retornatoken(arquiv):
    c = " "
    estado = 0
    linha = 0
    coluna = 0
    value = ''
    while c: 
        c = arquiv.read(1)
        if c == '\n':
            linha += 1
            coluna = 0
        if c != '\n':
            coluna += 1
        if estado == 0:
            if c == '':
                return '$'
            elif c.isspace():
                estado = 91
                continue
            elif c.isalpha() or c == '_':
                value = c
                if c == 'd':
                    estado = 35
                elif c == 'p':
                    estado = 1
                elif c == 'i':
                    estado = 10
                elif c == 't':
                    estado = 16
                elif c == 'e':
                    estado = 21
                elif c == 'w':
                    estado = 29
                elif c == 'f':
                    estado = 38
                elif c == 'c':
                    estado = 44
                else:
                    estado = 63
                continue
            elif c == '>':
                estado = 49
                value += c
                continue
            elif c == '=':
                token = tok_relop(c, 'EQ', linha, coluna)
                estado = 0
                value = ''
                return token
            elif c == '<':
                estado = 53
                value += c
                continue
            elif c == '+':
                token = tok_op(c, '+', linha, coluna)
                estado = 0
                value = ''
                return token
            elif c == '-':
                token = tok_op(c, '-', linha, coluna)
                estado = 0
                value = ''
                return token
            elif c == '/':
                token = tok_op(c, '/', linha, coluna)
                estado = 0
                value = ''
                return token
            elif c == '*':
                estado = 60
                continue
            elif c == '{':
                estado = 65
                continue
            elif c == '%':
                estado = 70
                continue
            elif c == "'":
                estado = 72
                continue
            elif c == ';':
                token = tok_pontvirg(linha, coluna)
                estado = 0
                value = ''
                return token
            elif c == '(':
                token = tok_parentesq(linha, coluna)
                estado = 0
                value = ''
                return token
            elif c == ')':
                token = tok_parentdir(linha, coluna)
                estado = 0
                value = ''
                return token
            elif c == ':':
                estado = 78
                continue
            elif c == '[':
                token = tok_colchesq(linha, coluna)
                estado = 0
                value = ''
                return token
            elif c == ']':
                token = tok_colchdir(linha, coluna)
                estado = 0
                value = ''
                return token
            elif c == ',':
                token = tok_virg(linha, coluna)
                estado = 0
                value = ''
                return token            
            elif c.isdigit():
                estado = 81
                value += c
                continue
            elif c in ['\n', '\t']:
                linha += 1
                estado = 91
                continue
            elif c == ' ':
                estado = 91
                continue
            elif c.isalnum():
                value = value + c
                estado = 63
                continue
        
        elif estado == 1:
            if c == 'r':
                value = value + c
                estado = 2
                continue
            elif c.isalnum() or c == '_':
                estado = 63
                value += c
                continue
            elif c in ['\n', '\t', ' ']:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                linha += 1 
                return token
            elif c in [' ']:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
                
        elif estado == 2:
            if(c == 'o'):
                value = value + c
                estado = 3
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 3:
            if(c == 'g'):
                value = value + c
                estado = 4
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 4:
            if(c == 'r'):
                value = value + c
                estado = 5
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 5:
            if(c == 'a'):
                value = value + c
                estado = 6
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 6:
            if(c == 'm'):
                value = value + c
                estado = 7
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 7:
            if(c == 'a'):
                value = value + c
                estado = 8
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 8:
            if(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            elif(c == '\n' or c == '\t' or c == ''):
                token = tok_prog(linha, coluna)
                if(c == '\n'):
                    linha += 1
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            elif(c == ' '):
                token = tok_prog(linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            else:
                estado = 94
                continue

        elif estado == 10:
            if(c == 'f'):
                value = value + c
                estado = 11
                continue
            elif(c == 'n'):
                value = value + c
                estado = 13
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 11:
            if(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            elif(c == '\n' or c == '\t' or c == ''):
                token = tok_if(linha, coluna)
                if(c == '\n'):
                    linha += 1
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            elif(c == ' '):
                token = tok_if(linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            else:
                estado = 94
                continue

        elif estado == 13:
            if(c == 't'):
                value = value + c
                estado = 14
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 14:
            if(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            elif(c == '\n' or c == '\t' or c == ''):
                token = tok_int(linha, coluna)
                if(c == '\n'):
                    linha += 1
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            elif(c == ' '):
                token = tok_int(linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            else:
                estado = 94
                continue

        elif estado == 16:
            if(c == 'h'):
                value = value + c
                estado = 17
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else: 
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 17:
            if(c == 'e'):
                value = value + c
                estado = 18
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 18:
            if(c == 'n'):
                value = value + c
                estado = 19
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 19:
            if(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            elif(c == '\n' or c == '\t' or c == ''):
                token = tok_then(linha, coluna)
                if(c == '\n'):
                    linha += 1
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            elif(c == ' '):
                token = tok_then(linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            else:
                estado = 94
                continue

        elif estado == 21:
            if(c == 'l'):
                value = value + c
                estado = 22
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 22:
            if(c == 's'):
                value = value + c
                estado = 23
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 23:
            if(c == 'e'):
                value = value + c
                estado = 24
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 24:
            if(c == 'i'):
                value = value + c
                estado = 26
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            elif(c == '\n' or c == '\t' or c == ''):
                token = tok_else(linha, coluna)
                if(c == '\n'):
                    linha += 1
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            elif(c == ' '):
                token = tok_else(linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 26:
            if(c == 'f'):
                value = value + c
                estado = 27
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 27:
            if(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            elif(c == '\n' or c == '\t' or c == ''):
                token = tok_elseif(linha, coluna)
                if(c == '\n'):
                    linha += 1
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            elif(c == ' '):
                token = tok_elseif(linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            else:
                estado = 94
                continue

        elif estado == 29:
            if(c == 'h'):
                value = value + c
                estado = 30
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 30:
            if(c == 'i'):
                value = value + c
                estado = 31
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 31:
            if(c == 'l'):
                value = value + c
                estado = 32
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 32:
            if(c == 'e'):
                value = value + c
                estado = 33
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 33:
            if(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            elif(c == '\n' or c == '\t' or c == ''):
                token = tok_while(linha, coluna)
                if(c == '\n'):
                    linha += 1
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            elif(c == ' '):
                token = tok_while(linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            else:
                estado = 94
                continue

        elif estado == 35:
            if(c == 'o'):
                value = value + c
                estado = 36
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 36:
            if(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            elif(c == '\n' or c == '\t' or c == ''):
                token = tok_do(linha, coluna)
                if(c == '\n'):
                    linha += 1
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            elif(c == ' '):
                token = tok_do(linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            else:
                estado = 94
                continue

        elif estado == 38:
            if(c == 'l'):
                value = value + c
                estado = 39
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 39:
            if(c == 'o'):
                value = value + c
                estado = 40
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 40:
            if(c == 'a'):
                value = value + c
                estado = 41
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 41:
            if(c == 't'):
                value = value + c
                estado = 42
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 42:
            if(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            elif(c == '\n' or c == '\t' or c == ''):
                token = tok_float(linha, coluna)
                if(c == '\n'):
                    linha += 1
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            elif(c == ' '):
                token = tok_float(linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            else:
                estado = 94
                continue

        elif estado == 44:
            if(c == 'h'):
                value = value + c
                estado = 45
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 45:
            if(c == 'a'):
                value = value + c
                estado = 46
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 46:
            if(c == 'r'):
                value = value + c
                estado = 47
                continue
            elif(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            else:
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 47:
            if(c.isalnum() or c == '_'):
                value = value + c
                estado = 63
                continue
            elif(c == '\n' or c == '\t' or c == ''):
                token = tok_char(linha, coluna)
                if(c == '\n'):
                    linha += 1
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            elif(c == ' '):
                token = tok_char(linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            else:
                estado = 94
                continue

        elif estado == 49:
            if(c != '='):
                value += c
                token = tok_relop(value, 'GT', linha, coluna)
                estado = 0
                value = ''
                return token
            else:
                value += c
                token = tok_relop(value, 'GE', linha, coluna)
                estado = 0
                value = ''
                return token
        
        elif estado == 53:
            if(c == '>'):
                value += c
                token = tok_relop(value, 'NE', linha, coluna)
                estado = 0
                value = ''
                return token
            elif(c == '='):
                value += c
                token = tok_relop(value, 'LE', linha, coluna)
                estado = 0
                value = ''
                return token
            else: 
                value += c
                token = tok_relop(value, 'LT', linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif(estado == 60):
            if(c == '*'):
                estado = 62
                value = ''
                continue
            else:
                token = tok_op(c, '*', linha, coluna)
                estado = 0
                value = ''
                return token

        elif estado == 62:
            if(c == '\n' or c == '\t' or c == ''):
                value += c
                token = tok_op('**', '**', linha, coluna)
                estado = 0
                value = ''
                return token
            if(c == ' '):
                value += c
                token = tok_op('**', '**', linha, coluna)
                estado = 0
                value = ''
                return token
            else: 
                estado = 94
                continue
        
        elif estado == 63:
            if c.isalnum() or c == '_':
                estado = 63
                value += c
                continue
            if(c == '\n' or c == '\t' or c == ''):
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            if(c == ' '):
                token = tok_id(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            else:
                estado = 94
                continue

        elif estado == 65:
            if(c == '#'):
                estado = 66
                continue
            elif(c == '%'):
                token = tok_ok(linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            else:
                estado = 94
                continue

        elif estado == 66:
            if c == '#':
                estado = 67
                continue
            else:
                estado = 66
                continue

        elif estado == 67:
            if c == '}':
                token = tok_comment(linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            else:
                estado = 66
                continue

        elif estado == 70:
            if c == '}':
                token = tok_ko(linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token
            else:
                estado = 94
                continue

        elif estado == 72:
            if c != "'":
                estado = 73
                continue
            else:
                estado = 94
                continue

        elif estado == 73:
            if c == "'":
                token = tok_carac(value, linha, coluna)
                estado = 0
                value = ''
                return token
            else: 
                estado = 94
                continue

        elif estado == 78:
            if c != '=':
                token = tok_doispont(linha, coluna)
                estado = 0
                value = ''
                return token
            else:
                token = tok_doisponteq(linha, coluna)
                estado = 0
                value = ''
                return token

        elif estado == 81:
            if c.isdigit():
                estado = 81
                value += c
                continue
            elif c == '.':
                estado = 83
                value += c
                continue
            elif c == 'E':
                estado = 86
                value += c
                continue
            else:
                token = tok_num(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 83:
            if(c.isdigit()):
                estado = 84
                value += c
                continue
            else:
                estado = 94
                continue

        elif estado == 84:
            if (c.isdigit()):
                estado = 84
                value += c
                continue
            elif c == 'E':
                estado = 86
                value += c
                continue
            else:
                token = tok_num(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 86:
            if c == '+' or c == '-':
                estado = 87
                value += c
                continue
            elif (c.isdigit()):
                estado = 88
                value += c
                continue
            else:
                estado = 94
                continue

        elif estado == 87:
            if (c.isdigit()):
                estado = 88
                value += c
                continue
            else:
                estado = 94
                continue

        elif estado == 88:
            if (c.isdigit()):
                estado = 88
                value += c
                continue
            else:
                token = tok_num(value, linha, coluna)
                estado = 0
                value = ''
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                return token

        elif estado == 91:
            if c in ['\n', '\t']:
                linha += 1
                estado = 91
                continue
            elif c == ' ':
                estado = 91
                continue
            else:
                coluna -= 1
                arquiv.seek(arquiv.tell() - 1)
                estado = 0
                value = ''
                continue
        
        elif estado == 94:
            if(c == '\n' or c == '\t' or c == ' ' or c == ''):
                value = ''
                estado = 0
                print('erro')
                continue
            else:
                estado = 94
                continue
            
            
def main():
    with open("teste.txt", "r", encoding="utf-8") as arquivo:
        retornatoken(arquivo)

if __name__== "__main__":
    main()
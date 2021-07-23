TOK_FN = 101
TOK_LET = 102
TOK_IF = 103
TOK_FOR = 104
TOK_WHILE = 105
TOK_ID = 1
TOK_CHAR = 2
TOK_EQ = 3
TOK_BIGGER = 4
TOK_SMALLER = 5
TOK_NOT = 6
TOK_NUM = 7


class Token:

    def __init__(self, token_id, data):
        self.token_id = token_id
        self.data = data

    def __repr__(self):
        rep = 'Token(' + str(self.token_id) + ',' + self.data + ')'
        return rep

    def __eq__(self, other):
        if isinstance(other, Token):
            return self.token_id == other.token_id and \
                   self.data == other.data
        else:
            return False


def tokenize(data):
    data_list = data.split()
    res = []

    lex_keywords(data_list)
    lex_identifier(data_list)
    lex_chars(data_list)


def lex_keywords(data_list):
    res = []

    for key in data_list:
        if key == 'fn':
            res.append(Token(TOK_FN, key))
        elif key == 'let':
            res.append(Token(TOK_LET, key))
        elif key == 'if':
            res.append(Token(TOK_IF, key))
        elif key == 'for':
            res.append(Token(TOK_FOR, key))
        elif key == 'while':
            res.append(Token(TOK_WHILE, key))
        elif key == '==':
            res.append(Token(TOK_EQ, key))
        elif key == '>=':
            res.append(Token(TOK_BIGGER, key))
        elif key == '<=':
            res.append(Token(TOK_SMALLER, key))
        elif key == '!=':
            res.append(Token(TOK_NOT, key))
    print(res)
    return res


def lex_identifier(data_list):
    keywords = ['fn', 'let', 'if', 'for', 'while']
    id_alphabet = '0123456789abcdefjhijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ_'
    res = []

    for key in data_list:
        if key not in keywords:
            state = 1
            id_name = ''

            for char in key:
                if state == 1:
                    if char in '0123456789':
                        return None
                    elif char in id_alphabet:
                        id_name += char
                        state = 2
                elif state == 2:
                    if char in id_alphabet:
                        id_name += char
                        state = 2
                    else:
                        return id_name
            res.append(Token(TOK_ID, id_name))
    print(res)
    return res


def lex_chars(data_list):
    keywords = ['fn', 'let', 'if', 'for', 'while']
    id_alphabet = '0123456789abcdefjhijklmnopqrstuvwxyzABCDEFJHIJKLMNOPQRSTUVWXYZ_'
    id_name = ''
    res = []

    for key in data_list:
        if key not in keywords and key not in id_alphabet:

            for char in key:
                id_name += char

            res.append(Token(TOK_CHAR, id_name))
            id_name = ''
    print(res)
    return res


if __name__ == '__main__':
    print(tokenize('if a = b @! let data jhc1_1'))

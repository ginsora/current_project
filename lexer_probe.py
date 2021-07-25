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

    for key in data_list:
        if lex_keywords(key) is not None:
            res.append(lex_keywords(key))
        else:
            if lex_identifier(key) is not None:
                res.append(lex_identifier(key))
            else:
                if lex_numbers(key) is not None:
                    res.append(lex_numbers(key))
                else:
                    res.append(lex_chars(key))
    return res


def lex_keywords(key):
    if key == 'fn':
        token = (Token(TOK_FN, key))
    elif key == 'let':
        token = (Token(TOK_LET, key))
    elif key == 'if':
        token = (Token(TOK_IF, key))
    elif key == 'for':
        token = (Token(TOK_FOR, key))
    elif key == 'while':
        token = (Token(TOK_WHILE, key))
    elif key == '==':
        token = (Token(TOK_EQ, key))
    elif key == '>=':
        token = (Token(TOK_BIGGER, key))
    elif key == '<=':
        token = (Token(TOK_SMALLER, key))
    elif key == '!=':
        token = (Token(TOK_NOT, key))
    else:
        return None
    return token


def lex_identifier(key):
    id_alphabet = '0123456789abcdefgjhijklmnopqrstuvwxyzABCDEFGJHIJKLMNOPQRSTUVWXYZ_'
    state = 1
    id_name = ''

    for char in key:
        if state == 1:
            if char in '0123456789':
                return None
            elif char in id_alphabet:
                id_name += char
                state = 2
            else:
                return None
        elif state == 2:
            if char in id_alphabet:
                id_name += char
                state = 2
            else:
                return id_name
        else:
            return None
    token = (Token(TOK_ID, id_name))
    return token


def lex_numbers(key):
    id_alphabet = '0123456789'
    state = 1
    id_number = ''

    for char in key:
        if state == 1:
            if char in id_alphabet:
                id_number += char
                state = 2
            else:
                return None
        elif state == 2:
            if char in id_alphabet:
                id_number += char
                state = 2
            elif char == '.':
                id_number += char
                state = 3
            else:
                return None
        elif state == 3:
            if char in id_alphabet:
                id_number += char
                state = 3
            else:
                return id_number
        else:
            return None
    token = Token(TOK_NUM, id_number)
    return token


def lex_chars(key):
    token = Token(TOK_CHAR, key)
    return token


if __name__ == '__main__':
    print(tokenize('if a = b @! 12.3 123 let data jhc1_1'))

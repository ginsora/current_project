import unittest

from lexer_probe import *


class TestLexer(unittest.TestCase):

    def test_lex_keywords(self):
        data = 'if let for while'
        result = tokenize(data)
        self.assertEqual([Token(TOK_IF, 'if'),
            Token(TOK_LET, 'let'),
            Token(TOK_FOR, 'for'),
            Token(TOK_WHILE, 'while')],
            result)

    def test_identifier(self):
        data = 'dat qjg122_'
        result = tokenize(data)
        self.assertEqual([Token(TOK_ID, 'dat'), Token(TOK_ID, 'qjg122_')], result)

    def test_numbers(self):
        data = '123 12.4'
        result = tokenize(data)
        self.assertEqual([Token(TOK_NUM, '123'), Token(TOK_NUM, '12.4')], result)

    def test_chars(self):
        data = '@@!'
        result = tokenize(data)
        self.assertEqual([Token(TOK_CHAR, '@@!')], result)


if __name__ == '__main__':

    unittest.main()

import unittest

from lexer import *


class TestLexer(unittest.TestCase):

    # def test_work(self):
    #     data = 'if let for while'
    #     result = tokenize(data)
    #     self.assertEqual([
    #         Token(TOK_IF, 'if'),
    #         Token(TOK_LET, 'let'),
    #         Token(TOK_FOR, 'for'),
    #         Token(TOK_WHILE, 'while')],
    #         result)

    def test_lex_keywords(self):
        data = 'if let for while'
        result = tokenize(data)
        self.assertEqual([Token(TOK_IF, 'if'),
            Token(TOK_LET, 'let'),
            Token(TOK_FOR, 'for'),
            Token(TOK_WHILE, 'while')],
            result)

    def test_numbers(self):
        data = '123 12.4'
        result = tokenize(data)
        self.assertEqual([Token(TOK_NUM, '123'), (TOK_NUM, '12.4')], result)

if __name__ == '__main__':

    unittest.main()

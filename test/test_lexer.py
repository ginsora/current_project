import unittest

from lexer import tokenize


class TestLexer(unittest.TestCase):

    def test_work(self):
        data = 'if let for while'
        result = tokenize(data)
        self.assertEqual([103, 102, 104, 105], result)

    def test_upper(self):
        data = 'IF LET FOR WHILE'
        result = tokenize(data)
        self.assertEqual([], result)

    def test_gib(self):
        data = 'jcnlidshoaisc'
        result = tokenize(data)
        self.assertEqual([], result)

    def test_slip(self):
        data = 'if let bread while'
        result = tokenize(data)
        self.assertEqual([103, 102, 105], result)


if __name__ == '__main__':

    unittest.main()

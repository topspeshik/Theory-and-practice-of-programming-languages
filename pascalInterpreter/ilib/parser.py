# interpreter.py
from tokens import Token, TokenType
from lexer import Lexer
from tree import Node, BinOp, Number, UnaryOp, Variable, AssignOp

class ParserException(Exception):
    ...

class Parser:

    def __init__(self):
        self.current_token: Token = None
        self.lexer = Lexer()

    def init_parser(self, s: str):
        self.lexer.init_lexer(s)
        self.current_token = self.lexer.next()


    def check_type(self, type_:TokenType):
        if self.current_token.type == type_:
            self.current_token = self.lexer.next()
            return
        raise ParserException(f"Invalid token order. Expected {type_}, Received {self.current_token}")


    def complex_statement(self) -> Node:
        self.check_type(TokenType.BEGIN)
        statement_list = []
        statement_list.append(self.statement())

        while self.current_token.type == TokenType.SEMI:
            self.check_type(TokenType.SEMI)
            statement_list.append(self.statement())

        self.check_type(TokenType.END)

        return statement_list


    def statement(self) -> Node:
        if self.current_token.type == TokenType.VARIABLE:
            return self.assignment()
        elif self.current_token.type == TokenType.BEGIN:
            return self.complex_statement()

    def assignment(self) -> Node:
        var = Variable(self.current_token)
        self.check_type(TokenType.VARIABLE)
        token = self.current_token
        self.check_type(TokenType.ASSIGN)
        return AssignOp(var, token, self.expr())


    def factor(self) -> Node:
        token = self.current_token
        if token.type == TokenType.MINUS:
            self.check_type(TokenType.MINUS)
            return UnaryOp(self.expr(), token)
        if token.type == TokenType.PLUS:
            self.check_type(TokenType.LPAREN)
            result = self.expr()
            self.check_type(TokenType.RPAREN)
            return result
        if token.type == TokenType.NUMBER:
            self.check_type(TokenType.NUMBER)
            return Number(token)
        if token.type == TokenType.LPAREN:
            self.check_type(TokenType.LPAREN)
            result = self.expr()
            self.check_type(TokenType.RPAREN)
            return result
        if token.type == TokenType.VARIABLE:
            self.check_type(TokenType.VARIABLE)
            return Variable(token)
        raise ParserException("invalid factor")

    def term(self) -> Node:
        ops = [TokenType.DIV, TokenType.MUL]
        result = self.factor()
        while self.current_token.type in ops:
            token = self.current_token
            match token.type:
                case TokenType.DIV:
                    self.check_type(TokenType.DIV)
                case TokenType.MUL:
                    self.check_type(TokenType.MUL)
            result = BinOp(result, token, self.factor())
        return result

    def expr(self) -> float:
        ops = [TokenType.PLUS, TokenType.MINUS]
        result = self.term()
        while self.current_token.type in ops:
            token = self.current_token
            match token.type:
                case TokenType.PLUS:
                    self.check_type(TokenType.PLUS)
                    # result += self.term()
                case TokenType.MINUS:
                    self.check_type(TokenType.MINUS)
                   # result -= self.term()
            result = BinOp(result, token, self.term())
        return result

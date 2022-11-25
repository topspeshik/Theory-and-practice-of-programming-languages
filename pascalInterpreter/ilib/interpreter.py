# interpreter.py
from re import match

from tokens import Token, TokenType
from lexer import Lexer
from tree import NodeVisitor, Node, Number, BinOp, UnaryOp, AssignOp, Variable
from parser import Parser

class InterpreterException(Exception):
    ...


class Interpreter(NodeVisitor):

    def __init__(self):
        self.parser = Parser()
        self.values = dict()


    def visit(self, node: Node) -> float:
        if isinstance(node, Number):
            return self.visit_number(node)
        if isinstance(node, BinOp):
            return self.visit_binop(node)
        if isinstance(node, UnaryOp):
            return self.visit_unaryop(node)
        elif isinstance(node, list):
            return self.visit_statements(node)
        elif isinstance(node, AssignOp):
            return self.visit_initop(node)
        elif isinstance(node, Variable):
            return self.visit_var(node)
        elif node is None:
            return

        raise InterpreterException("Invalid node")

    def visit_number(self, node: Number)-> float:
        return float(node.value.value)

    def visit_binop(self, node: BinOp)-> float:
        match node.op.type:
            case TokenType.PLUS:
                return self.visit(node.left) + self.visit(node.right)
            case TokenType.MINUS:
                return self.visit(node.left) - self.visit(node.right)
            case TokenType.DIV:
                return self.visit(node.left) / self.visit(node.right)
            case TokenType.MUL:
                return self.visit(node.left) * self.visit(node.right)
        raise InterpreterException("Invalid operator")


    def visit_unaryop(self, node: UnaryOp) -> float:
        match node.op.type:
            case TokenType.PLUS:
                return self.visit(node.left)
            case TokenType.MINUS:
                return 0 - self.visit(node.left)
        raise InterpreterException("Invalid operator")


    def visit_statements(self, node: list):
        for statement in node:
            self.visit(statement)


    def visit_var(self, node: Variable):
        value = node.value
        return self.values[value]


    def visit_initop(self, node: AssignOp):
        self.values[node.left.value] = self.visit(node.right)

    def eval(self, s: str) -> float:
            self.parser.init_parser(s)
            tree = self.parser.complex_statement()
            self.visit(tree)
            return self.values

    def returnTree(self, s:str):
            self.parser.init_parser(s)
            tree = self.parser.complex_statement()

            return tree





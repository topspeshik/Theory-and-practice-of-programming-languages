from abc import ABC
from tokens import Token


class Node(ABC):
    ...


class Number(Node):
    def __init__(self, value: Token):
        self.value = value

    def __str__(self):
        return f"( {self.value})"


class BinOp(Node):

    def __init__(self, left: Node, op: Token, right: Node):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self):
        return f"BinOp {self.op.type}  (left - {self.left}, right - {self.right})"


class UnaryOp(Node):
    def __init__(self, left: Node, op: Token):
        self.left = left
        self.op = op

    def __str__(self):
        return f"UnaryOp {self.op.type} ({self.left}, {self.op})"


class AssignOp(Node):
    def __init__(self, left: Node, op: Token, right: Node):
        self.left = left
        self.op = op
        self.right = right

    def __str__(self) -> str:
        return f"AssignOp {self.op.type} (left: {self.left}, right: {self.right})"


class Variable(Node):
    def __init__(self, var: Token):
        self.var = var
        self.value = var.value

    def __repr__(self):
        return f"{self.value}"


class NodeVisitor:
    def visit(self, node: Node) -> float:
        raise NotImplementedError

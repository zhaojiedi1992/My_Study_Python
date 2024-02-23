class Node:
    pass

class UnaryOperator(Node):
    def __init__(self, operand):
        self.operand = operand

class BinaryOperator(Node):
    def __init__(self, left, right):
        self.left = left
        self.right = right

class Add(BinaryOperator):
    pass

class Sub(BinaryOperator):
    pass

class Mul(BinaryOperator):
    pass

class Div(BinaryOperator):
    pass

class Negate(UnaryOperator):
    pass

class Number(Node):
    def __init__(self, value):
        self.value = value


class Evaluator:
    def visit(self, node):
        method_name = 'visit_' + type(node).__name__
        visitor = getattr(self, method_name, self.generic_visit)
        return visitor(node)

    def generic_visit(self, node):
        raise RuntimeError('No {} method'.format('visit_' + type(node).__name__))
    
class Interpreter(Evaluator):
    def visit_Number(self, node):
        return node.value
    def visit_Add(self, node):
        return self.visit(node.left) + self.visit(node.right)

    def visit_Sub(self, node):
        return self.visit(node.left) - self.visit(node.right)
    def visit_Mul(self, node):
        return self.visit(node.left) * self.visit(node.right)

    def visit_Div(self, node):
        return self.visit(node.left) / self.visit(node.right)

    def visit_Neg(self, node):
        return -self.visit(node.operand)
    
class InterpreterV2(Evaluator):
    def visit_Number(self, node):
        return str(node.value)
    
    def visit_Add(self, node):
        return '({left} + {right})'.format(left=self.visit(node.left) ,right=self.visit(node.right))

    def visit_Sub(self, node):
         return '({left} - {right})'.format(left=self.visit(node.left) ,right=self.visit(node.right))
    def visit_Mul(self, node):
          return '({left} * {right})'.format(left=self.visit(node.left) ,right=self.visit(node.right))

    def visit_Div(self, node):
          return '({left} / {right})'.format(left=self.visit(node.left) ,right=self.visit(node.right))

    def visit_Neg(self, node):
          return '(-{value})'.format(value=self.visit(node.value))
    
t1 = Add(Number(1), Number(2))
t2 = Mul(t1, Number(4))
i = Interpreter()
print(i.visit(t2))

i2 = InterpreterV2()
print(i2.visit(t2))

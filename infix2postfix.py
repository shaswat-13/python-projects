from stack_and_queue import Stack




def main():

    # declarations
    prec_order = {'^': 3, '/': 2, '*': 2, '+': 1, '-':1}
    operators = list(prec_order.keys())
    operators.append(['(', ')'])
    stack = Stack()
    postfix = list()
    
    print("Enter an expression in infix: ", end="")
    infix = input()
    
    for character in infix:
        if character == ' ':
            continue
        elif character.isalnum():
            postfix.append(character)
        elif character in operators:
            if stack.isEmpty() or stack.peek() == '(':
                stack.push(character)
                



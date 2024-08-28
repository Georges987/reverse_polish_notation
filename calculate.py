def calculate_rpn(rpn_list):
    """
    This function calculates the result of an RPN list
    :param rpn_list: list
    :return: float
    """
    stack = []
    for i in rpn_list:
        if i.isdigit():
            stack.append(i)
        elif i in ["+", "-", "*", "/"]:
            if len(stack) < 2:
                print("Invalid RPN list")
                return None
            else:
                second = stack.pop()
                first = stack.pop()
                if i == "+":
                    stack.append(first + second)
                elif i == "-":
                    stack.append(first - second)
                elif i == "*":
                    stack.append(first * second)
                elif i == "/":
                    stack.append(first / second)
        else:
            print(f"Invalid character {i}")
    return stack[0]


def eval_rpn_el(tokens) -> int:
    stack = []
    for char in tokens:
        if char == '+':
            stack.append(stack.pop() + stack.pop())
        elif char == '-':
            a, b = stack.pop(), stack.pop()
            stack.append(b - a)
        elif char == '/':
            a, b = stack.pop(), stack.pop()
            stack.append(int(b / a))
        elif char == '*':
            stack.append(stack.pop() * stack.pop())
        else:
            stack.append(int(char))

    return stack[0]


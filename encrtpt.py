def rpn_converter(value):
    """
    This function converts a string to an RPN list
    :param value: string
    :return: list
    """
    if type(value).__name__ == list:
        value = "".join(value)
    value = value.replace(")(", ")*(")
    value = [i for i in value]
    stack = []
    rpn_list = []
    for i in value:
        if i.isdigit():
            rpn_list.append(i)
        elif i in ["+", "-", "*", "/"]:
            while stack and stack[-1] in ["+", "-", "*", "/"]:
                rpn_list.append(stack.pop())
            stack.append(i)
        elif i in ["(", ")"]:
            if i == "(":
                stack.append(i)
            else:
                while stack and stack[-1] != "(":
                    rpn_list.append(stack.pop())
                stack.pop()
        else:
            print(f"Invalid character {i}")
    print(stack)
    while stack:
        rpn_list.append(stack.pop())
    return rpn_list

from collections import deque
#utilitez functions
def do_operation(opr: chr, num1: float, num2: float)->float:
    if opr == '+':
        return num1 + num2
    elif opr == '-':
        return num1 - num2
    elif opr == '*':
        return num1 * num2
    elif opr == '/':
        return num1 /num2
    elif opr == '^':
        return num1 ** num2
    return 0


def evaluate_postfix(exprission: str)->int:
    """very simple
       if you find number push it at number stack
       if you find operation apply it num1 (operation) num2 
       and add to number stack
       finally return stack.pop()
    
    """
  
    stkNumbers = deque()
    
    for element in exprission:
        if element ==' ':
            continue
        
        elif element.isdigit():
            stkNumbers.append(element)

        else:
            right = int(stkNumbers.pop())
            left = int(stkNumbers.pop())

            stkNumbers.append(do_operation(element, left, right))

    return stkNumbers.pop()

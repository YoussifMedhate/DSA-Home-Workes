#  I tried covering all wrong cases :)
def check_infix(expression: str) -> bool:
    operatores = ('+', '-', '*', '/')
    l = len(expression)

    if not expression:
        return False

    if expression[0] in operatores or expression[-1] in operatores:
        return False

    for i in range(l - 1):
        if expression[i] in operatores and expression[i + 1] in operatores:
            return False

        if (not expression[i].isdigit() and
            expression[i] not in operatores and
            expression[i] not in ('(', ')')):
            return False

    last = expression[-1]
    if (not last.isdigit() and
        last not in operatores and
        last not in ('(', ')')):
        return False

    return True

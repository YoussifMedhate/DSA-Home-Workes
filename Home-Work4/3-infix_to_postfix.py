#utilitize functions
def precedence(oper: str) -> int:
    if oper in ('+', '-'):
        return 1
    elif oper in ('*', '/'):
        return 2
    elif oper == '^':
        return 3
    return -1


def infix_to_postfix(infix: str)->str:
    """dijkstra to convert infix -> postfix
    add check practes
    using 4 roles + 2 to implement () + one condition to implement ^
    i will name every element in the string ->(var)
    ...
    i) handel ^
    +, -, *, / are left -> right operator 
    but ^ is not :(
    ^ is left <- right so it neeed special case to handel it
    it very easy 
      -first ^ has pirority stronger than any operator
      -second if there are two ^ ^ dont pop() to implement left <- right
    
    ii) handel ()
    1- if you found ( : push it to stack
    2- if you found ) : add all operatores to  postfix until find ( stop and pop it
    
    iii) handel normal case
    1- if var.isdigit(): add it to postfix dirictily
    2- if  not var.isdigit() and stack is empty: add it to stak dirictily
    3- if  not var.isdigit() and stack isn't empty:
        if priority(var) > priority(stack.top()):
            stack.puch(var)
        if priority(var) <= priority(stack.top()):
            postfix += stack.top() ... stack.pop().... untill condition stop
            when condition stop:
                stack.puch(var) 
    4- check if stack is not empty: add all operators to postfix

    finaly :) -> return postfixt """

    ####### I remove check from this file becouse i want abstract algorithm and this details  isn't big deal now :) #######
    # if not check_infix(infix):
    #     raise ValueError("expression is not correct")

    # if not check_parentheses(infix):
    #     raise ValueError("the parentheses is not correct")

    postfix = ""
    stkOperators = deque()
    
    infix += '-' # to don't repeate loop 
    stkOperators.append('#') # to remove stk.empty() check :)

    for char in infix:
        if char =='(':
            stkOperators.append('(')

        elif char ==")":
            while stkOperators[-1] != '(':
               postfix += stkOperators.pop()
            stkOperators.pop()
        
        elif char.isdigit():
            postfix += char

        else:
            while(precedence(char) <= precedence(stkOperators[-1]) and
                  not(char == '^' and stkOperators[-1] == '^')):
                postfix += stkOperators.pop()
            stkOperators.append(char)
    
    return postfix

def is_operator(char):
    if char=="+" or char =="-" or char=="*" or char=="/" or char=="^":
        return True
    else:
        return False
    
def precedence(char):
    if char=="^":
        return 3
    elif char=="*" or char=="/":
        return 2
    elif char=="+" or char=="-":
        return 1
    else:
        return 0
    

def infix_to_postfix(expression):
    stck=[]
    postfix=""
    for char in expression:
        if char=="":
            continue
        elif char.isdigit() or char.isalpha():
            postfix=postfix+char

        elif char=="(":
            stck.append(char)
        elif char ==")":
            while stck and stck[-1] !="(":
                postfix=postfix+stck.pop()

            if stck and stck[-1]=="(":
                stck.pop()


        elif is_operator(char):
            while stck and stck[-1] !="(" and precedence(char)<=precedence(stck[-1]):
                postfix +=stck.pop()

            stck.append(char)

    while stck:
        postfix +=stck.pop()

    return postfix
            


expre="((A + B) - C * (D / E)) + F"

t=infix_to_postfix(expre)

print("Before Conversion =",expre)
print("After Conversion =",t)
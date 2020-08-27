def chek_brac(s):
    c=0
    for i in s:
        if i==")":
            c-=1
        elif i=="(":
            c+=1
        if c<0:
            return 0
    return 0 if c else 1
s=input("Enter an infix expression: ")
stack=[]
op=[]
while(not chek_brac(s)):
    print("Invalid...Try again")
    input()
    s=input("Enter an infix expression: ")
oprtor="+-*/^()%"
x={"+":1,"-":1,"*":2,"/":2,"%":3,"^":4,"(":0}
tab=" "*12
print("InputElement"+" "*10+"Stack"+tab+"Output")
for i in range(len(s)):
    if s[i] in oprtor:
        if len(stack)>0:
            if s[i]=="(":
                pass
            elif s[i]==")":
                while stack[-1]!="(":
                    op.append(stack[-1])
                    stack.pop(-1)
                stack.pop(-1)
            elif s[i]=="+" or s[i]=="-" or s[i]=="*" or s[i]=="/" or s[i]=="%":
                if stack[-1]=="(":
                    pass
                else:
                    while(len(stack)>0 and x[stack[-1]]>=x[s[i]]):
                        op.append(stack[-1])
                        stack.pop(-1)
            elif s[i]=="^":
                pass
        if s[i]!=")":
            stack.append(s[i])
    else:
        op.append(s[i])
    a,b="".join(stack),"".join(op)
    print("  "+s[i]+" "*19+a+" "*(18-len(a))+b)
while(len(stack)>0):
    op.append(stack[-1])
    stack.pop(-1)
a,b="".join(stack),"".join(op)
print("   "+" "*19+a+" "*(18-len(a))+b)
print("Infix expression :",s)
print("Postfix expression :",b)
    

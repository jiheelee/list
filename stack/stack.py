stack = []

string = "((( )((((( )( )((( )( ))((( ))))))))))"
print(string.count("("))
print(string.count(")"))

result = "success"

for i in string:
    if i == "(":
        stack.append(i)
    elif i == ")":
        if len(stack) == 0:
            result = "wrong"

        elif result != "wrong":
            stack.pop(-1)


for i in stack:
    if "(" in stack:
        result = "wrong"

print(result)


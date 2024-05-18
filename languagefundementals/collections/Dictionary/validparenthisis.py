bracket_pairs = { "(":")", "{":"}", "[":"]"}
stack_list = []
top = -1
user_input = "(){}" 
top = -1
for symbol in user_input:
    if symbol in bracket_pairs:
        top +=1
        stack_list.append(symbol)
    else:
        if top == -1:
            print("invalid")
            break
        else:
            current_symbol = stack_list[top]
            clossing_current_symbol = bracket_pairs.get(current_symbol)
            if symbol ==clossing_current_symbol:
                stack_list.pop()
                top -=1 
            else:
                break
if len(stack_list)  == 0:
    print("valid")
else:
    print("invalid")

           


dials = {
    "1": ["a", "b", "c"],
    "2": ["d", "e", "f"],
    "3": ["g", "h", "i"]
}
main_list = []
all_list = []
user_input = input("Please enter the number: ")
for ch in user_input:
    first_list = dials.get(ch)
    main_list.append(first_list)

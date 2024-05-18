items = ["bat", "ball", "pencil", "candy", "adapter"]
curr_word = ""
min_words = items[0]
for i in range(1,len(items)):
    curr_word= items[i]
    if len(curr_word) < len(min_words):
        min_words = curr_word
print(min_words)
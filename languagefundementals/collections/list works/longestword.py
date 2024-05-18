items = ["bat", "ball", "pencil", "candy", "adapter"]
longest_word = max(items, key=lambda w: len(w))
print(longest_word)
smalllest_word = min(items, key=lambda w: len(w))
print(smalllest_word)

length = 0

for i in range(0, len(items)):
    length +=len(items[i])
print(length)

largest_word = items[0]

for i in range(0, len(items)):
   curr_word = items[i]
   if len(curr_word)>len(largest_word):
       largest_word = curr_word
print(largest_word)



#min word and sum
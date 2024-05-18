items = ["bat", "ball", "pencil", "candy", "adapter"]


items.append("tea")
print(items) 


order = ["cb", "cb","gheeroast", "juice", "pineapple", "gheeroast"]

print(order.count("cb"))


print(order.index("pineapple"))
print(order.pop(-2))
print(order)


order.pop(-3)
print(order)

order.insert(1,"gobi")
print(order)


order.remove("cb")
print(order)


manoj_fav_colors = ["black", "green", "white", "yellow", "pink"]
mobin_fav_colors = manoj_fav_colors.copy()
mobin_fav_colors.remove("yellow")
print(mobin_fav_colors)
print(manoj_fav_colors)

manoj_fav_colors.reverse()
print(manoj_fav_colors)
source_wrd = "myself"
target_word = "self"

src_wrd_list = [ch for ch in source_wrd]

tar_wrd_list = [ch for ch in target_word]

for ch in tar_wrd_list:
    if ch in src_wrd_list:
        src_wrd_list.remove(ch)
    else:
        print("not a kangaroo word")
        break

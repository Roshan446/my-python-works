from re import *
# text = "asdedecrscedvsdJUdhwiim[pc[k324wepomwenciewnmciewmcionwriovnpoewn6789mINWEMQ34354WODMPOWMPVIOFEPOFCEMI076775 CLAS;D.QW;VLDCLEAz]]"
# # pattern = "[acAC]"
# # pattern = "[a-z]"
# # pattern = "[A-B]"
# # pattern = "[0-9]"
# #pattern = "[0-9a-zA-Z]"
# pattern = "[^0-9a-zA-Z]" #speacil characters
# # pattern = "[^a-z]" #exclude the pattern given
# match_word = finditer(pattern, text)
# for m in match_word:
#     print(m.start(), m.group())

password='Pass@34567cvghj'
pattern=r'^(?=.*[a-z])(?=.*[A-Z])(?=.*[0-9])(?=.*[\W_]).{8,}$'
if match(pattern,password):
    print(True)
else:
    print(False)
source_wor = "chicken"
form_word = "hen"
value = 0
srt_source = sorted(source_wor)
srt_form = sorted(form_word)
for i in srt_source:
    for k in srt_form:
        if i == k:
            value +=1
print("True" if value  ==len(form_word) else "fLSE" ) 
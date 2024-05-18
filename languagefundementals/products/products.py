from json import load
f = open("C:\\Users\\rosha\\OneDrive\Desktop\\mypython works luminar\\languagefundementals\\products\\items.json", "r", encoding="utf-8")
result = load(f)
print(len(result))
all_category = {c.get("category") for c in result}
print(all_category)
electronics = [p for p in result if p.get("category") == "electronics"]
print(len(electronics))
jewellery = [j for j in result if j.get("category")=="jewelery"]
print(len(jewellery))
from json import load
f = open("C:\\Users\\rosha\\OneDrive\\Desktop\\mypython works luminar\\languagefundementals\\rest countries\\data.json", "r", encoding="utf-8" )
data = load(f)
print(len(data))
all_names = [n.get("name") for n in data]
print(all_names)

#independentcountry names

all_independent_country = [i.get("name") for i in data if i.get("independent") == True]
print(all_independent_country)


all_region = [r.get("region") for r in data]

all_asian_countries = [r.get("name") for r in data if r.get("region") == "asia"]

print(all_asian_countries)


#capital of ukraine

capital_of_ukr = [u.get("capital") for u in data if u.get("name") == "Ukraine"]
print(capital_of_ukr)

#capital and name together

capital_name = [(cn.get("name"), cn.get("capital")) for cn in data]
print(capital_name)

#country name and currency

# name_currency = [(nc.get("name"), c.get("name")for c in nc.get("currencies")) for nc in data]
# print(name_currency)

for cn in data:
    if "currencies" in cn:
        currencies_data = cn.get("currencies")[0]
        print(currencies_data)
        print(cn.get("name"), ", " , currencies_data.get("name"))

# border countries of india
# for br in data:
#     if "borders" in br:
#         if "IND" in br.get("borders"):
#             print(br.get("name"))

india_borders = [n.get("borders") for n in data if n.get("name")=="India"]

print(india_borders[0])

alpha_code_con = [n.get("name") for n in data if n.get("alpha3Code") in india_borders]
print(alpha_code_con)


for n in data:
    if "borders" in n and len(n.get("borders")) > 4:
        print(n.get("name"))
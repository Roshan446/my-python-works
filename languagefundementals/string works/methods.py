company = "luminar"
print(company.capitalize())
name = "ROSHAN"
print(name.casefold())
print(name.lower())
print(company.upper())
car = "nissan24"
print(car.isalpha())
print(car.isdigit())
print(car.isalnum())
sal = "nhellon"
print(sal.strip("n"))
print(sal.rstrip("n"))
print(sal.lstrip("n"))
r =  "hi im Roshan"
word = r.split()
print(word)

text  = "pakistan, lost, to, india, by, 40, runs"
words = text.split(",")

for i in words:
    print(i)

print(company.startswith("lu"))

print(company.endswith("ny"))
print(company.count("a"))
print(company.index("ar"))
out = ",".join(company)
print(out)
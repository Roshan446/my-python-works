from json import load
f = open("C:\\Users\\rosha\\OneDrive\\Desktop\\mypython works luminar\\languagefundementals\\exchangerate\\rate.json", "r", encoding="UTF - 8")
data = load(f)


source_currency = input("please enter the source currency? ")
target_currency = input("please enter the target currency? ")
amount = int(input("please enter the amount? "))


conversion_rates = data.get("conversion_rates")
source_currency_code_rate = conversion_rates.get(source_currency)
target_currency_code_rate = conversion_rates.get(target_currency)
exchange_rates = target_currency_code_rate/source_currency_code_rate
desired_amount = exchange_rates*amount
print(f'the amount is {desired_amount} {target_currency}' if source_currency in conversion_rates and target_currency in conversion_rates else "please enter a valid code")


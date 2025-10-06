price = float(input("Введите стоимость: ").replace(',', '.'))
discount = float(input("Введите скидку: ").replace(',', '.'))
vat = float(input("Введите НДС: ").replace(',', '.'))
base = price * (1 - discount/100)
vat_amount = base * (vat/100)
total = base + vat_amount

print("%-20s %.2f ₽\n%-20s %.2f ₽\n%-20s %.2f ₽" % ("База после скидки:", base, "НДС:", vat_amount, "Итого к оплате:", total))

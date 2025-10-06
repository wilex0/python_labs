iniList = input("ФИО: ").split()
print(f"Инициалы: {''.join(map(lambda x: x[0].upper(), iniList))}")
print(f"Длина (символов): {len(''.join(iniList)) + 2}")

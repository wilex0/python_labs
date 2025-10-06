mins = int(input("Минуты: "))
hours = mins // 60
mins %= 60
print("%d:%02d" % (hours, mins))

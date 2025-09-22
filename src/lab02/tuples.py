def format_record(rec: tuple[str, str, float]) -> str:
    if len(rec) != 3 or not (isinstance(rec[0], str) and isinstance(rec[1], str)):
        raise ValueError
    if not isinstance(rec[2], (int, float)) or not ( 1 < rec[2] < 5 ):
        raise TypeError
    if not (2 <= len(rec[0].strip().split()) <= 3) or not (rec[1].find('-') != -1 and all(len(x) > 0 for x in rec[1].strip().split('-'))):
        raise ValueError

    inits = [i[0].upper() + i[1:] for i in rec[0].strip().split()]
    initsFormatStr = inits[0] + f" {inits[1][0]}." + (f"{inits[2][0]}." if len(inits) == 3 else '')
    return "%s, гр. %s, GPA %.2f" % (initsFormatStr, rec[1].strip(), round(rec[2], 2))

#format_record
print("(\"Иванов Иван Иванович\", \"BIVT-25\", 4.6) -> %s\n(\"Петров Пётр\", \"IKBO-12\", 5.0) -> %s\n(\"Петров Пётр Петрович\", \"IKBO-12\", 5.0) -> %s\n(\"  сидорова  анна   сергеевна \", \"ABB-01\", 3.999) -> %s" % (format_record(("Иванов Иван Иванович", "BIVT-25", 4.6)), format_record(("Петров Пётр", "IKBO-12", 5.0)), format_record(("Петров Пётр Петрович", "IKBO-12", 5.0)), format_record(("  сидорова  анна   сергеевна ", "ABB-01", 3.999))))

#format_record - error cases
print('\n\n')

try:
    # 1 empty 1 or 2 arg
    format_record(('', 'BIVT-25', 3.45))
    format_record(('Иван', '', 3.45))
except ValueError:
    print('(\'\', \'BIVT-25\', 3.45) / (\'Иван\', \'\', 3.45) -> ValueError')
try:
    # 2 name/surname/second name in 1 instance
    format_record(("Иван", "BIVT-25", 4.2))
    format_record(("Иванович", "BIVT-25", 4.2))
    format_record(("Иванов", "BIVT-25", 4.2))
except ValueError:
    print("(\"Иванов/Иван/Иванович\", \"BIVT-25\", 4.2) -> ValueError")
try:
    # 3 incorrect 3 arg
    format_record(("Иванов Иван Иванович", "BIVT-25", 3))
except TypeError:
    print("(\"Иванов Иван Иванович\", \"BIVT-25\", 3) -> TypeError")


def format_record(rec: tuple[str, str, float]) -> str:
    if len(rec) != 3 or not (isinstance(rec[0], str) and isinstance(rec[1], str)):
        raise ValueError
    if not isinstance(rec[2], (int, float)) or not (1 <= rec[2] <= 5):
        raise TypeError
    if not (2 <= len(rec[0].strip().split()) <= 3) or not (
        rec[1].find("-") != -1 and all(len(x) > 0 for x in rec[1].strip().split("-"))
    ):
        raise ValueError

    inits = [i[0].upper() + i[1:] for i in rec[0].strip().split()]
    initsFormatStr = (
        inits[0] + f" {inits[1][0]}." + (f"{inits[2][0]}." if len(inits) == 3 else "")
    )
    return "%s, гр. %s, GPA %.2f" % (initsFormatStr, rec[1].strip(), round(rec[2], 2))

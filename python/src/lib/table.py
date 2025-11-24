def table(tn: list[tuple[str, int]], *, onTable: bool = True, K: int = 2):
    if not tn:
        return "пусто"
    if onTable:
        mLen = max([len(x[0]) for x in tn]) * K
        pattern = f"%-{mLen}s | %-{mLen}s"
        title = pattern % ("слово", "частота")

        print(title)
        print("-" * len(title))

        for i in tn:
            print(pattern % (i[0], i[1]))
    else:
        for x in tn:
            print(f"{x[0]}:{x[1]}")

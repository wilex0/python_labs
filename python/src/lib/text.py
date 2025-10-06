import re

def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
    if casefold:
        text = text.casefold()
    if yo2e:
        text = text.replace('Ё', 'Е').replace('ё', 'е')
    return re.sub(r'( )+', ' ', string=text.strip())

def tokenize(text: str) -> list[str]:
    return re.findall(r'\w+(?:-\w+)*', string=text)

def count_freq(tokens: list[str]) -> dict[str, int]:
    tokens_set = set(tokens)
    return { x: tokens.count(x) for x in tokens_set }

def top_n(freq: dict[str, int], n: int) -> list[tuple[str, int]]:
    return sorted([(k,v) for k,v in freq.items()], key= lambda x: (-x[1], x[0]))[:n]



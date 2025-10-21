import sys
from src.lib.text import normalize, tokenize, count_freq, top_n

print("normalise:")
print(normalize("\r\n        word пурумпурум"))
print(normalize("Hello\r\nWorld"))
print(normalize("привет   мир"))
print(normalize("ёжик, Ёлка", yo2e = True))
print("tokenize:")
print(tokenize("привет мир"))
print(tokenize("hello,world!!!"))
print(tokenize("по-настоящему не круто"))
print(tokenize("1992 год"))
print(tokenize("emoji 😀 не слово"))
print("count_freq:")
print(count_freq(["a","b","a","c","b","a"]))
print(count_freq(["bb","aa","bb","aa","cc"]))

freq = count_freq(["a","b","a","c","b","a"])
print(top_n(freq,2))
freq_1 = count_freq(["bb","aa","bb","aa","cc"])
print(top_n(freq_1, 2))

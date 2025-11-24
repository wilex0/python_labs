import sys

sys.path.append("/home/wilex/Документы/GitHub/python_labs/python/src/lib")
from text import normalize, tokenize, count_freq, top_n
from table import table

s = sys.stdin.buffer.read().decode("utf-8")
combed = tokenize(normalize(s))
unique_combed = count_freq(combed)

print(f"Всего слов {len(combed)}")
print(f"Уникальных слов {len(unique_combed)}")
print(f"Top-5:")

t5 = top_n(unique_combed, 5)

ON_TABLE = True

table(t5, onTable=ON_TABLE, K=2)

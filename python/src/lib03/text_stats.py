import sys
sys.path.append('/home/wilex/Документы/GitHub/python_labs/python/src/lib')

from text import *

s = sys.stdin.buffer.read().decode('utf-8')
combed = tokenize(normalize(s))

print(f"Всего слов {len(combed)}")
print(f"Уникальных слов {len(set(combed))}")
print(f"Top-5:")

t5 = top_n(count_freq(combed), 5)

ON_TABLE = True

if ON_TABLE:
    K = 2

    mLen = max([len(x[0]) for x in t5]) * K
    pattern = f"%-{mLen}s | %-{mLen}s"
    title = pattern % ("слово", "частота")

    print(title)
    print('-' * len(title))

    for i in t5:
        print( pattern % (i[0], i[1]) )
else:
    v = [print(f'{x[0]}:{x[1]}') for x in t5]
    print(v)

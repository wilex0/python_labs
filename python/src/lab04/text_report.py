import sys, os.path, csv
sys.path.append('/home/wilex/Документы/GitHub/python_labs/python/src/lib')
from table import table
from text import normalize, tokenize, count_freq, top_n
from io_txt_csv import read_text, write_csv, ensure_parent_dir

input_f, output_f, per_f = [], None, None
stdpath = { "--in": ["/home/wilex/Документы/GitHub/python_labs/python/data/lab04/input.txt"], "--out":"/home/wilex/Документы/GitHub/python_labs/python/data/lab04/report.csv", "--per-file": "/home/wilex/Документы/GitHub/python_labs/python/data/lab04/report_per_file.csv"}
mainpath = "/home/wilex/Документы/GitHub/python_labs/python/"

if sys.argv[-1] in ("--in", "--out"):
    raise Exception()

for i, arg in enumerate(sys.argv):
    if arg == "--in":
        for v in sys.argv[i+1:]:
            if v == "--out" or v == '--per-file':
                break
            input_f.append(v)
    elif arg == "--per-file":
        per_f = sys.argv[i+1]
    elif arg == "--out":
        output_f = sys.argv[i+1]


input_f, output_f, per_f = (stdpath["--in"] if not input_f else input_f if all(os.path.isdir(os.path.dirname(x)) for x in input_f) else [mainpath + x for x in input_f],
                            stdpath["--out"] if not output_f else output_f if os.path.isdir(os.path.dirname(output_f)) else mainpath + output_f,
                            stdpath["--per-file"] if not per_f else per_f if os.path.isdir(os.path.dirname(per_f)) else mainpath + per_f)

if any(not os.path.exists(x) for x in input_f):
    raise Exception()

flen = len(input_f)

if flen > 1:
    from collections import Counter
    per_list = []
    total_freq = Counter()

    for path in input_f:
        text = read_text(path)
        freq = count_freq(tokenize(normalize(text)))
        total_freq.update(freq)
        for k,v in freq.items():
            per_list.append((os.path.basename(path), k, v))
    ensure_parent_dir(os.path.dirname(per_f))
    per_list.sort(key= lambda x: (x[0], -x[2], x[1]))
    write_csv(per_list, per_f, header=("file", "word", "count"))

    ensure_parent_dir(os.path.dirname(output_f))
    total_freq = sorted(total_freq.items(), key=lambda x: (-x[1], x[0]))
    write_csv(total_freq, output_f, header=["word", "count"])
else:
    text = read_text(input_f[0])
    freq = count_freq(tokenize(normalize(text)))
    ensure_parent_dir(os.path.dirname(output_f))
    result = sorted(freq.items(), key=lambda x: (-x[1], x[0]))
    write_csv(result, output_f, header=["word", "count"])

    print(f"Всего слов: {sum(freq.values())}")
    print(f"Уникальных слов: {len(freq.keys())}")
    print(f"Top-5:")
    table(top_n(freq, 5), onTable=True)
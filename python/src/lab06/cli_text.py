import argparse
from src.lib.io_helper import read_text, check_path_in
from src.lib.text import normalize, tokenize, top_n, count_freq
from src.lib.table import table

parser = argparse.ArgumentParser(description="Работа с файлом (прочитать, статистика слов)")

subparsers = parser.add_subparsers(dest="command")
cat_comm = subparsers.add_parser("cat", help="Прочитать файл и вывести содержимое")
cat_comm.add_argument("--input", required=True)
cat_comm.add_argument("--top", action="store_true", help="Флаг для нумерования строк")

stats_comm = subparsers.add_parser("stats", help="Частота слов")
stats_comm.add_argument("--input", required=True)
stats_comm.add_argument("--top", type=int, default=5)
stats_comm.add_argument("--table", action="store_true", help="Флаг для вывода в табличном формате")

args = parser.parse_args()
args.input = check_path_in(args.input)
text = read_text(args.input)
if args.command == "cat":
    arr = text.strip().split('\n')
    for i in range(len(arr)):
        print(f"{i+1}. {arr[i]}" if args.top else f"{arr[i]}")
elif args.command == "stats":
    arr = top_n(count_freq(tokenize(normalize(text))), args.top)
    table(arr, onTable=args.table)
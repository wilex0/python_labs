# Лабораторная работа №4
## `IOTxtCsv.ReadText`
### Ввод путь к файлу + проверка -> вывод прочитанная строка

## `IOTxtCsv.WriteCsv`
### Ввод список строк, путь и заголовк при необходимости -> запись в *.csv файл данных + проверки
## `IOTxtCsv.EnsureParentDir`
### Ввод путь к директории -> создание директорий
![io_txt_csv](../../images1/lab04/IoTxtCsv.png)

## `text_report.py`
## Разбивка путей + проверки если программа запускается без аргументов в поток ввода то запускается со стандартным набором параметров, если же 1 аргумент в поток ввода то работа с одним файлом + вывод в report.csv, с 2 и более создается report_per_file.csv и report_total.csv
![Progra.cs-file](../../images1/lab04/Program_1.png)
![Progra.cs-file2](../../images1/lab04/Program_2.png)
## `Вывод report.csv при работе с одним файлом`
![report](../../images1/lab04/WithOutArgs.png)
## `Вывод report_total.csv и report_per.csv при работе с 2 и более файлмаи`
![reportArgs](../../images1/lab04/WithArgs.png)
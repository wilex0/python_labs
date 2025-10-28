using System.Text;
using System.CommandLine;
using Lib;
namespace Lab06;
class CLI
{
    public static int Main(string[] args)
    {
        Option<string> inputFileOp = new("--in") { Description = "Путь к читаемому файлу (--in <string>)" };
        Option<string> outputFileOp = new("--out") { Description = "Путь к файлу для записи результата (--out <string>)"};
        Option<int> topOp = new("--top") { Description = "Вывод необходимого количества элементов (--top <int>)"};
        Option<bool> countOp = new("-n") { Description = "Флаг для нумерации строк (-n/without -n)"};
        Option<bool> tableOp = new("-table") { Description = "Флаг для удобного табличного вывода (-table/without -table)" };

        Command csv2jsonCommand = new Command("csv2json", "csv в json") { inputFileOp, outputFileOp };
        Command json2csvCommand = new Command("json2csv", "json в csv") { inputFileOp, outputFileOp };
        Command csv2xlsxCommand = new Command("csv2xlsx", "csv в xlsx") { inputFileOp, outputFileOp };
        
        csv2jsonCommand.SetAction(parseRes =>
        {
            var (input, output) = (parseRes.GetValue(inputFileOp), parseRes.GetValue(outputFileOp));
            (input, output) = CsvXlsx.CheckPath(input, output);
            CsvXlsx.CsvToJson(input, output);
        }); 
        json2csvCommand.SetAction(parseRes =>
        {
            var (input, output) = (parseRes.GetValue(inputFileOp), parseRes.GetValue(outputFileOp));
            (input, output) = CsvXlsx.CheckPath(input, output);
            CsvXlsx.JsonToCsv(input, output);
        });
        csv2xlsxCommand.SetAction(parseRes =>
        {
            var (input, output) = (parseRes.GetValue(inputFileOp), parseRes.GetValue(outputFileOp));
            (input, output) = CsvXlsx.CheckPath(input, output);
            CsvXlsx.CsvToXlsx(input, output);
        });
        
        Command readCommand = new Command("cat", "Чтение и вывод построчно строк из файла с возможностью нумерации каждой строки") { inputFileOp, countOp };
        readCommand.SetAction(parseRes =>
        {
            var input = parseRes.GetValue(inputFileOp);
            CsvXlsx.CheckPath(ref input);
            var isCount = parseRes.GetValue(countOp);
            using StreamReader reader = new(input);
            for (int i = 1; !reader.EndOfStream; ++i)
                Console.WriteLine($"{(isCount ? $"{i}. " : "")}{reader.ReadLine()}");
        });

        Command statsCommand = new Command("stats", "Вывод частот строк в файле с возможностью необходимого количества элементов + сортировка") { inputFileOp, topOp, tableOp };
        statsCommand.SetAction(parseRes =>
        {
            var input = parseRes.GetValue(inputFileOp);
            CsvXlsx.CheckPath(ref input);
            var top = parseRes.GetValue(topOp);
            var table = parseRes.GetValue(tableOp);
            var text = IOTxtCsv.ReadText(input, Encoding.UTF8);
            
            var dic = Text.CountFreq(Text.Tokenize(Text.Normalize(text)));
            if (top != 0)
                dic = Text.TopN(dic, top);
            if (table)
                Output.Table(dic);
            else
                foreach (var keyValuePair in dic)
                    Console.WriteLine($"{keyValuePair.Key} {keyValuePair.Value}");
        });
        
        RootCommand rootCommand = new();
        rootCommand.Subcommands.Add(csv2jsonCommand);
        rootCommand.Subcommands.Add(json2csvCommand);
        rootCommand.Subcommands.Add(csv2xlsxCommand);
        rootCommand.Subcommands.Add(readCommand);
        rootCommand.Subcommands.Add(statsCommand);

        return rootCommand.Parse(args).Invoke();
    }
}
using System.Text;
using Lib;

class Program {
  public static void Main(string[] args) {
    string pathToInput;
    using (StreamReader sr =
               new StreamReader(Console.OpenStandardInput(), Encoding.UTF8))
        pathToInput = sr.ReadToEnd().Trim();
    Console.WriteLine(pathToInput);
    var fileData =
        Text.Normalize(IOTxtCsv.ReadText(pathToInput, Encoding.UTF8));
    var tokenize = Text.Tokenize(fileData);
    var freqDic = Text.CountFreq(tokenize)
                      .OrderByDescending(x => x.Value)
                      .ThenBy(x => x.Key)
                      .ToDictionary();
    var freqList =
        freqDic.Select(x => new List<object>() { x.Key, x.Value }).ToList();

    string pathToData =
        pathToInput[..pathToInput.LastIndexOf('/')] + "/report.csv";
    IOTxtCsv.WriteCsv(freqList, pathToData, new() { "word", "count" });
    Console.WriteLine($"Всего слов: {freqDic.Values.Sum()}");
    Console.WriteLine($"Уникальных слов: {freqDic.Keys.Count}");
    var top5 = Text.TopN(freqDic, 5);
    Output.Table(top5);
  }
}

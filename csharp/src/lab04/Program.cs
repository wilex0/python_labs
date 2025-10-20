using System.Diagnostics;
using System.Text;
using Lib;
using System.Threading.Tasks;

struct Element
{
    public string Name { get; set; }
    public string Key { get; set; }
    public int Count { get; set; }
    public Element()
    {
    }
}

class Program
{
    public static Dictionary<string, object> StandardPaths = new()
    {
        { "--in", new List<string>() { "/home/wilex/Документы/GitHub/python_labs/csharp/data/input"} },
        { "--out", "/home/wilex/Документы/GitHub/python_labs/csharp/data/report.csv" },
        { "--per-file", "/home/wilex/Документы/GitHub/python_labs/csharp/data/report_per_file.csv" }
    };

    private static readonly string _projectPath = "/home/wilex/Документы/GitHub/python_labs/csharp";
    public static string NormalizePath(string path)
    {
        if (File.Exists(path) || File.Exists(_projectPath + path))
            return (File.Exists(path) ? path : _projectPath + path);
        else
            throw new FileNotFoundException(path);
    }
    
    public static void Main(string[] args)
    {
        List<string> inputPath = StandardPaths["--in"] as List<string>;
        string outPath = StandardPaths["--out"] as string;
        string perFilePath = StandardPaths["--per-file"] as string;
        
        if (Console.IsInputRedirected)
        {
            string[] text;
            using (StreamReader sr = new StreamReader(Console.OpenStandardInput(), Encoding.UTF8))
                text = sr.ReadToEnd().Trim().Split();
            if (text.Where((x, i) =>
                {
                    if (x is "--in" or "--out" or "--per-file")
                        return (text.Length - 1) == i || text[i + 1] is "--in" or "--out" or "--per-file";
                    return false;
                }).Any())
            {
                throw new ArgumentException();
            }
            if (text.Contains("--in"))
                inputPath = new();

            for (int i = 0; i < text.Length; ++i)
            {
                switch (text[i])
                {
                    case "--in":
                        for (int j = i + 1; j < text.Length; ++j)
                            if (text[i] is not ("--out" or  "--per-file"))
                                inputPath.Add(NormalizePath(text[j]));
                        break;
                    case "--out":
                        outPath = NormalizePath(text[i]);
                        break;
                    case "--per-file":
                        perFilePath = NormalizePath(text[i]);
                        break;
                }
            }
        }
                
        if (inputPath.Count > 1)
        {
            DateTime start = DateTime.Now;
            Dictionary<string, int> totalFreq = new();
            List<List<object>> perList = new();
            
            foreach (var path in inputPath)
            {
                var text = File.ReadAllText(path);
                Text.CountFreq(Text.Tokenize(Text.Normalize(text)), out var freq);
                foreach (var k in freq.Keys)
                {
                    if (totalFreq.ContainsKey(k))
                        totalFreq[k] += freq[k];
                    else
                        totalFreq.Add(k, freq[k]);
                    perList.Add(new() { Path.GetFileName(path), k, freq[k] });
                }
                IOTxtCsv.WriteCsv(perList, perFilePath, header:new() {"file", "word", "count"});
            }
            Console.WriteLine((DateTime.Now - start).Milliseconds);
        }
        
       // var fileData = Text.Normalize(IOTxtCsv.ReadText(pathToInput, Encoding.UTF8));
       // var tokenize = Text.Tokenize(fileData);
       // var freqDic = Text.CountFreq(tokenize)
       //     .OrderByDescending(x => x.Value)
       //     .ThenBy(x => x.Key)
       //     .ToDictionary();
       // var freqList = freqDic.Select(x => new List<object>() { x.Key, x.Value }).ToList();
       // string pathToData = pathToInput[..pathToInput.LastIndexOf('/')] + "/report.csv";
       // IOTxtCsv.WriteCsv(freqList, pathToData, new() { "word", "count" });
       // Console.WriteLine($"Всего слов: {freqDic.Values.Sum()}");
       // Console.WriteLine($"Уникальных слов: {freqDic.Keys.Count}");
       // var top5 = Text.TopN(freqDic, 5);
       // Output.Table(top5);
    }
}

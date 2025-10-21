using System.Diagnostics;
using System.Text;
using Lib;
using System.Threading.Tasks;

class Program
{
    public static Dictionary<string, object> StandardPaths = new()
    {
        { "--in", new List<string>() { "/home/wilex/Документы/GitHub/python_labs/csharp/data/lab04/input"} },
        { "--out", "/home/wilex/Документы/GitHub/python_labs/csharp/data/lab04/report.csv" },
        { "--per-file", "/home/wilex/Документы/GitHub/python_labs/csharp/data/lab04/report_per_file.csv" }
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
            //DateTime start = DateTime.Now;
            Dictionary<string, int> totalFreq = new();
            List<string[]> perList = new();
            foreach (var path in inputPath)
            {
                var text = File.ReadAllText(path);
                Text.CountFreq(Text.Tokenize(Text.Normalize(text)), out var freq);
                foreach (var (k, v) in freq)
                {
                    if (totalFreq.ContainsKey(k))
                        totalFreq[k] += v;
                    else
                        totalFreq.Add(k, v);
                    perList.Add(new string[3] { Path.GetFileName(path), k, Convert.ToString(v) });
                }

                var perListSorted = perList.OrderByDescending(x => x[2]).ThenBy(x => x[0]).ThenBy(x => x[1]).ToList();
                IOTxtCsv.WriteCsv(perListSorted, perFilePath, header: new string[] { "file", "word", "count"});
                var totalFreqSorted = totalFreq.OrderByDescending(x => x.Key).ThenBy(x => x.Key).ToDictionary();
                IOTxtCsv.WriteCsv(totalFreqSorted, outPath, header: new string[] {"word", "count"});
            }
            //Console.WriteLine((DateTime.Now - start).Milliseconds);
        }
        else
        {
            var text = File.ReadAllText(inputPath.First());
            Text.CountFreq(Text.Tokenize(Text.Normalize(text)), out var freq);
            var freqSorted = freq.OrderByDescending(x => x.Value).ThenBy(x => x.Key).ToDictionary();
            IOTxtCsv.WriteCsv(freqSorted, inputPath.First(), header: new string[] { "word", "count" });
            
            Console.WriteLine($"Всего слов {freq.Values.Sum()}");
            Console.WriteLine($"Уникальных слов {freq.Keys.Count}");
            Console.WriteLine("Top-5:");
            Output.Table(Text.TopN(freqSorted, 5));
        }
    }
}

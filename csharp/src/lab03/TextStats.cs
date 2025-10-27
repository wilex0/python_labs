using System.Text;
using System.Xml;
using Lib;

public static partial class MyTests 
{
    public static bool OnTable = true;
    public static void Stats(Encoding encoding) 
    {
        string result;
        using (StreamReader path = new StreamReader(Console.OpenStandardInput(), encoding)) 
            result = Text.Normalize(File.ReadAllText(path.ReadToEnd().TrimEnd('\r', '\n')));
        
        Dictionary<string, int> freq = Text.CountFreq(Text.Tokenize(result));
        var top5 = Text.TopN(freq, 5);
        
        if (OnTable)
            Output.Table(top5.ToDictionary(x => x.Key, x => x.Value));
        else 
        {
            Console.WriteLine($"Всего слов {freq.Values.Sum()}");
            Console.WriteLine($"Уникальных слов {freq.Keys.Count}");
            Console.WriteLine("Top-5");
            foreach (var pair in top5)
                Console.WriteLine($"{pair.Key}: {pair.Value}");
        }
    }
}
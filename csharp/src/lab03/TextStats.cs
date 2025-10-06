using System.Text;
using System.Xml;
using Lib;

public static partial class MyTests {
  public static bool OnTable = true;
  public static void Stats(Encoding encoding) {
    string result;
    using (StreamReader sr = new StreamReader(Console.OpenStandardInput(), encoding)) 
    {
      result = Text.Normalize(sr.ReadToEnd());
    }

    Dictionary<string, int> freq = Text.CountFreq(Text.Tokenize(result));

    if (OnTable) 
    {
      Output.Table(freq);
    } else 
    {
      Console.WriteLine($"Всего слов {freq.Values.Sum()}");
      Console.WriteLine($"Уникальных слов {freq.Keys.Count}");
      Console.WriteLine("Top-5");
      Dictionary<string, int> top5 = Text.TopN(freq, 5);
      foreach (var pair in top5)
        Console.WriteLine($"{pair.Key}: {pair.Value}");
    }
  }
}

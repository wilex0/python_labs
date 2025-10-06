using Lib;

public static partial class MyTests 
{
    public static void Cases()
    {
        Console.WriteLine("Normalise:");
        Console.WriteLine(Text.Normalize("ёжик, Ёлка"));
        Console.WriteLine(Text.Normalize("Hello\r\nWorld"));
        Console.WriteLine(Text.Normalize("  двойные   пробелы  "));

        Console.WriteLine("Tokenize");
        Text.Tokenize("привет мир").ToList().ForEach(x => Console.Write($"[{x}] "));
        Text.Tokenize("hello,world!!!").ToList().ForEach(x => Console.Write($"[{x}] "));
        Text.Tokenize("2025 год").ToList().ForEach(x => Console.Write($"[{x}] "));
        Text.Tokenize("emoji 😀 не слово").ToList().ForEach(x => Console.Write($"[{x}] "));
        Console.WriteLine("\nCountFreq");
        string[] t1 = { "a", "b", "a", "c", "b", "a" };
        Dictionary<string, int> res1 = Text.CountFreq(t1);
        foreach (var v in res1)
            Console.Write($"{v.Key}:{v.Value} ");
        string[] t2 = { "bb","aa","bb","aa","cc" };
        Dictionary<string, int> res2 = Text.CountFreq(t2);
        foreach (var v in res2)
            Console.Write($"{v.Key}:{v.Value} ");
            
        Console.WriteLine("\nTopN");
        var freq1 = Text.TopN(Text.CountFreq(t1), 2);
        foreach (var v in freq1)
            Console.Write($"{v.Key}:{v.Value} ");
        var freq2 = Text.TopN(Text.CountFreq(t2), 2);
        foreach (var v in freq2)
            Console.Write($"{v.Key}:{v.Value} ");
        Console.WriteLine();
    }
}
using System.Text.RegularExpressions;
using System.Collections;
using System.Collections.Generic;
using System.Text;

namespace Lib
{
    public static class Text
    {
        public static string Normalize(string text, bool caseFold = true, bool yo2e = true)
        {
            if (caseFold)
                text = text.ToLowerInvariant();
            if (yo2e)
            {
                text = text.Replace("ё", "е");
                if (!caseFold)
                    text = text.Replace("Ё", "Е");            
            }
                    
            text = Regex.Replace(text, @"[\t\n\r\f]+ | ( )+", " ");
            text = Regex.Replace(text, @"-{2,}", "-");
            text = Regex.Replace(text, @"_{2,}", "_");
            return text.Trim();
        }
        public static List<string> Tokenize(string text)
        {
            return Regex.Matches(text, @"\w+(?:-\w+)*")
                .Select(x => x.Value)
                .ToList();
        }

        public static Dictionary<string, int> CountFreq(IEnumerable<string> tokens)
        {
            return tokens.GroupBy(x => x)
                .ToDictionary(x => x.Key, x => x.Count());
        }
        
        public static Dictionary<string, int> TopN(Dictionary<string, int> freq, int n = -1)
        {
            if (freq.Keys.Count < n)
                n = freq.Count;
            return freq.OrderByDescending(x => x.Value)
                .ThenBy(x => x.Key)
                .Take(n)
                .ToDictionary();
        }
    }    
}

public static class Output
{
    public static void Table<T>(Dictionary<string,T> dic, int k = 2)
    {
        int mLen = dic.Keys.Max(x => x.Length) * k;

        string patt = $"{{0, -{mLen}}} | {{1}}";
        string title = string.Format(patt, "слово", "частота");

        Console.WriteLine(title);
        Console.WriteLine(new string('-', title.Length));

        foreach (var pair in dic)
            Console.WriteLine(String.Format(patt, pair.Key, pair.Value));
    }
}


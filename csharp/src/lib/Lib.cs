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
            text = Regex.Replace(Regex.Replace(text, @"( )+", " "), @"[\t\n\r\f]+" ," ");
            return text.Trim();
        }
        public static void Normalize(string text, out string normText, bool caseFold = true, bool yo2e = true) => normText = Normalize(text, caseFold, yo2e);
        public static List<string> Tokenize(string text)
        {
            return Regex.Matches(text, @"\w+(?:-\w+)*")
                .Select(x => x.Value)
                .ToList();
        }
        public static void Tokenize(string text, out List<string> tokens) => tokens = Tokenize(text);
        
        public static Dictionary<string, int> CountFreq(IEnumerable<string> tokens)
        {
            return tokens.GroupBy(x => x)
                .ToDictionary(x => x.Key, x => x.Count());
        }
        public static void CountFreq(IEnumerable<string> tokens, out Dictionary<string, int> freq) => freq = CountFreq(tokens);
        
        public static List<KeyValuePair<string, int>> TopN(Dictionary<string, int> freq, int n = -1)
        {
            if (freq.Keys.Count < n)
                n = freq.Count;
            return freq.OrderByDescending(x => x.Value)
                .ThenBy(x => x.Key)
                .Take(n)
                .ToList();
        }
        public static void TopN(Dictionary<string, int> freq, out List<KeyValuePair<string, int>> topN, int n = -1) => topN = TopN(freq, n);
    }    
}

public static class Output
{
     public static void Table<T>(List<KeyValuePair<string,T>> dic, int k = 2)
     {
         int mLen = dic.Max(x => x.Key.Length) * k;
         //int mLen = dic.Max(x => x.Length) * k;
        
         string patt = $"{{0, -{mLen}}} | {{1}}";
         string title = string.Format(patt, "слово", "частота");

         Console.WriteLine(title);
         Console.WriteLine(new string('-', title.Length));
        
         foreach (var pair in dic)
             Console.WriteLine(String.Format(patt, pair.Key, pair.Value));
     }
}


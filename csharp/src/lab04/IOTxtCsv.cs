using System.Runtime.InteropServices.JavaScript;
using System.Text;

public static class IOTxtCsv
{
    public static string ReadText(string path, Encoding encoding)
    {
        if (!File.Exists(path))
            throw new FileNotFoundException(path);
        using StreamReader sr = new StreamReader(path, encoding);
        return sr.ReadToEnd();
    }

    public static void WriteCsv(List<string[]> rows, string path, string[]? header = null)
    {
        if (rows.Any(row => row.Count() != rows.First().Count()))
            throw new ArgumentException("Rows must have the same number of rows");
        using StreamWriter sw = new StreamWriter(path, false, Encoding.UTF8);
        if (header is not null)
            sw.WriteLine(string.Join(',', header));
        rows.ForEach(row => sw.WriteLine(string.Join(',', row)));
    }

    public static void WriteCsv(IDictionary<string, int> rows, string path, string[]? header = null)
    {
        using StreamWriter sw = new StreamWriter(path, false, Encoding.UTF8);
        if (rows.Count == 0)
            return;
        if (header is not null) 
            sw.WriteLine(string.Join(',', header));
        foreach (var (k, v) in rows)
        {
            sw.WriteLine(string.Join(',', k, v));
        }
    }

public static void EnsureParentDir(string path)
    {
        if (!Path.Exists(path[..path.LastIndexOf('/')]) || path == string.Empty)
            throw new ArgumentException(path);
        if (!Directory.Exists(path))
            Directory.CreateDirectory(path);
    }
}
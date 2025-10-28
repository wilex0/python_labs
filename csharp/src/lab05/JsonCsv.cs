using System.Text.Json;
using Lib;
namespace System.Text;
public static partial class CsvXlsx
{
    public static ValueTuple<string?, string?> CheckPath(string? readPath, string? writePath)
    {
        if (!File.Exists(readPath))
            if (!File.Exists(Lib.Text.ProjectDirectory + readPath))
                throw new ArgumentException($"File {readPath} does not exist");                
            else 
                readPath = Lib.Text.ProjectDirectory + readPath;
        if (!Directory.Exists(Path.GetDirectoryName(writePath)))
            if (!Directory.Exists(Path.GetDirectoryName(Lib.Text.ProjectDirectory + writePath)))
                throw new ArgumentException($"Directory {Path.GetDirectoryName(writePath)} does not exist");
            else 
                writePath = Lib.Text.ProjectDirectory + writePath;
        return (readPath, writePath);
    }
    public static string? CheckPath(string? inputPath)
    {
        if (!File.Exists(inputPath))
            if (!File.Exists(Lib.Text.ProjectDirectory + inputPath))
                throw new FileNotFoundException($"Файл {inputPath} не найден");
            else
                inputPath = Lib.Text.ProjectDirectory + inputPath;
        return inputPath;
    }
    public static void CheckPath(ref string? inputPath)
    {
        Console.WriteLine(inputPath);
        if (!File.Exists(inputPath))
            if (!File.Exists(Lib.Text.ProjectDirectory + inputPath))
                throw new FileNotFoundException($"Файл {inputPath} не найден");
            else
                inputPath = Lib.Text.ProjectDirectory + inputPath;
    }
    public static void JsonToCsv(string? jsonPath, string? csvPath)
    {
        (jsonPath, csvPath) = CheckPath(jsonPath, csvPath);
        using StreamReader fs = new StreamReader(jsonPath, Encoding.UTF8);
        if (fs.EndOfStream)
            throw new ArgumentException($"File {jsonPath} is empty");
        string jsonContent = fs.ReadToEnd();
        using (JsonDocument doc = JsonDocument.Parse(jsonContent))
        {
            JsonElement root = doc.RootElement;
            if (root.GetArrayLength() == 0)
                throw new JsonException("Root element length is zero.");
            var items = root.EnumerateArray();
            
            var header = root[0].EnumerateObject().Select(x => x.Name);
            
            if (items.Any(x => x.EnumerateObject().Count() != header.Count()) ||
                items.Any(x => !x.EnumerateObject().Select(x => x.Name).SequenceEqual(header)))
            {
                throw new ArgumentException("Uncorrected keys");
            }
            
            using StreamWriter writer = new StreamWriter(csvPath, false, Encoding.UTF8);
            writer.WriteLine(string.Join(',', header));
            foreach (var el in items)
                writer.WriteLine(string.Join(',' , el.EnumerateObject().Select(x => x.Value)));
        }
    }

    public static void CsvToJson(string? csvPath, string? jsonPath)
    {
        (csvPath, jsonPath) = CheckPath(csvPath, jsonPath);
        using StreamReader fs = new StreamReader(csvPath, Encoding.UTF8);
        if (fs.EndOfStream)
            throw new ArgumentException($"File {csvPath} is empty");
        var header = fs.ReadLine().Split(',');
        
        List<Dictionary<string, string>> items = new();
        while (!fs.EndOfStream)
        {
            var line = fs.ReadLine().Split(',');
            if (line.Length != header.Length)
                throw new ArgumentException($"Invalid number of lines in file {csvPath}");
            items.Add(header.Zip(line, (x, y) => new { x, y }).ToDictionary(x => x.x, x => x.y ));
        }
        
        var result = JsonSerializer.Serialize(items);
        using StreamWriter writer = new StreamWriter(jsonPath, false, Encoding.UTF8);
        writer.Write(result);
    }
}
using System.Text;

public class Program
{
    public static void Main(string[] args)
    {
        CsvXlsx.JsonToCsv("/home/wilex/Документы/GitHub/python_labs/csharp/data/samples/people.json", "/home/wilex/Документы/GitHub/python_labs/csharp/data/out/people_from_json.csv"); 
        CsvXlsx.CsvToJson("/home/wilex/Документы/GitHub/python_labs/csharp/data/samples/people.csv", "/home/wilex/Документы/GitHub/python_labs/csharp/data/out/people_from_csv.json");
        CsvXlsx.CsvToXlsx("/home/wilex/Документы/GitHub/python_labs/csharp/data/samples/cities.csv",
            "/home/wilex/Документы/GitHub/python_labs/csharp/data/out/cities.xlsx");
    }    
}
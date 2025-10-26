using System.Reflection;
using OfficeOpenXml;

namespace System.Text;
public static partial class CsvXlsx
{
    private static bool _isInitialized = false;
    public static void CsvToXlsx(string csvPath, string xlsxPath)
    {
        CheckPath(csvPath, xlsxPath);

        if (!_isInitialized)
        {
            _isInitialized = true;
            Version? vers = Assembly.GetAssembly(typeof(ExcelPackage)).GetName().Version;
            if (vers != null)
                if (vers.Major > 5)
                    ExcelPackage.License.SetNonCommercialOrganization("Labs");
                else
                    ExcelPackage.LicenseContext = LicenseContext.NonCommercial;
        }
        
        FileInfo xlsxFile = new FileInfo(xlsxPath);
        if (xlsxFile.Exists)
            xlsxFile.Delete();
        
        StreamReader csvReader = new StreamReader(csvPath, Encoding.UTF8);
        if (csvReader.EndOfStream)
            throw new ArgumentException($"File {csvPath} is empty");
        
        List<string[]> items = new();
        while (!csvReader.EndOfStream)
            items.Add(csvReader.ReadLine().Split(','));
        if (items.Any(x => x.Length != items[0].Length))
            throw new ArgumentException("Different line length");
        csvReader.Close();
        
        using (ExcelPackage package = new ExcelPackage(xlsxFile))
        {
            var workSheet = package.Workbook.Worksheets.Add("Sheet1");
            for (int row = 0; row < items.Count; ++row)
            {
                for (int col = 0; col < items[0].Length; ++col)
                {
                    workSheet.Cells[row + 1, col + 1].Value = items[row][col];
                }
            }
            for (int col = 0; col < items[0].Length; ++col)
            {
                var mCol = items.Max(x => x[col].Length) + 5;
                workSheet.Columns[col+1].Width = mCol > 8 ? mCol : 8;

                workSheet.Cells[1, col+1].Style.Font.Bold = true;
            }
            package.Save();
        }
    }
}
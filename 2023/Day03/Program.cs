using System.Text.RegularExpressions;

const string filePath = "data.txt";
// Add Padding
var lines = File.ReadAllLines(filePath).ToArray();

var gears = new Dictionary<(int x, int y), List<int>>();

var part1 = 0;
var part2 = 0;

for (var y = 0; y < lines.Length; y++)
{
    var numberMatches = Regex.Matches(lines[y], @"\d+");
    foreach (Match match in numberMatches)
    {
        LookAroundNumber(match, lines, y);
    }
}

foreach (var gear in gears)
{
    if (gear.Value.Count != 2)
        continue;
    part2 += gear.Value.Aggregate((x, y) => x * y);
}

void LookAroundNumber(Match match, string[] lines, int row)
{
    //Row above to row below
    for (int i = row - 1; i <= row + 1; i++)
    {
        if (i < 0 || i >= lines.Length)
            continue;
        
        var first = match.Index;
        var last = match.Index + match.Length;
        
        //Columns left and right of match
        for (int j = first - 1; j <= last; j++)
        {
            if (j < 0 || j >= lines[i].Length)
                continue;

            if (Char.IsDigit(lines[i][j]) || lines[i][j] == '.')
                continue;
            
            var number = int.Parse(match.Value);

            if (lines[i][j] == '*')
            {
                if (gears.TryGetValue((i, j), out var list))
                    list.Add(number);
                else
                    gears[(i, j)] = new List<int>() { number };
            }

            part1 += number;
            return;
        }
    }
}

Console.WriteLine("Part1: " + part1);
Console.WriteLine("Part2: " + part2);

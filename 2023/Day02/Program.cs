using System.Text.RegularExpressions;

const string filePath = "input.txt";
var lines = File.ReadAllLines(filePath);

var validGames = new List<int>();
var gamesPower = new List<int>();

foreach (var ln in lines)
{
    var gameId = int.Parse(Regex.Match(ln, @"Game \d+").Value.Replace("Game ",""));

    var redCounts = Regex.Matches(ln, @"\d+ red").Select(x => int.Parse(x.Value.Replace(" red", ""))).ToList();
    var blueCounts = Regex.Matches(ln, @"\d+ blue").Select(x => int.Parse(x.Value.Replace(" blue", ""))).ToList();
    var greenCounts = Regex.Matches(ln, @"\d+ green").Select(x => int.Parse(x.Value.Replace(" green", ""))).ToList();
    
    if (redCounts.Max() <= 12 && blueCounts.Max() <= 14 && greenCounts.Max() <= 13)
    {
        validGames.Add(gameId);
    }
    
    gamesPower.Add(redCounts.Max() * blueCounts.Max() * greenCounts.Max());
}

Console.WriteLine("Part One: " + validGames.Sum());
Console.WriteLine("Part Two: " + gamesPower.Sum());
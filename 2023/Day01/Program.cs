using System.Text.RegularExpressions;

const string filePath = "./data.txt";
var lines = File.ReadAllLines(filePath);

// Part One
var total = 0;

foreach (string ln in lines) {
    string firstDigit = Regex.Match(ln, @"\d").Value;
    string lastDigit = Regex.Match(ln, @"\d", RegexOptions.RightToLeft).Value;
    string value = firstDigit + lastDigit;
    
    total += int.Parse(value);
}
Console.WriteLine(total);

// Part Two
var part2Total = 0;
var pattern = @"\d|one|two|three|four|five|six|seven|eight|nine";
foreach (string ln in lines) {
    string firstDigit = Regex.Match(ln,pattern).Value;
    string lastDigit = Regex.Match(ln, pattern, RegexOptions.RightToLeft).Value;
    string value = WordConvert(firstDigit) + WordConvert(lastDigit);
    
    part2Total += int.Parse(value);
}

Console.WriteLine(part2Total);

string WordConvert(string word) => word switch {
    "one" => "1",
    "two" => "2",
    "three" => "3",
    "four" => "4",
    "five" => "5",
    "six" => "6",
    "seven" => "7",
    "eight" => "8",
    "nine" => "9",
    var value => value
};
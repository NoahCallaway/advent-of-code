using System;
using System.Text.RegularExpressions;

namespace MyApp // Note: actual namespace depends on the project name.
{
    internal class Program
    {
        static void Main(string[] args)
        {
            string filePath = "data.txt";
            string[] lines = File.ReadAllLines(filePath);

            // Part One
            int total = 0;

            foreach (string ln in lines) {
                string firstDigit = Regex.Match(ln, @"\d").Value;
                string lastDigit = Regex.Match(ln, @"\d", RegexOptions.RightToLeft).Value;
                string value = firstDigit + lastDigit;
                
                total += int.Parse(value);
            }
            Console.WriteLine(total);

            // Part Two
            var part2_total = 0;
            var pattern = @"\d|one|two|three|four|five|six|seven|eight|nine";
            foreach (string ln in lines) {
                string firstDigit = Regex.Match(ln,pattern).Value;
                string lastDigit = Regex.Match(ln, pattern, RegexOptions.RightToLeft).Value;
                string value = wordConvert(firstDigit) + wordConvert(lastDigit);
                
                part2_total += int.Parse(value);
            }

            Console.WriteLine(part2_total);

            string wordConvert(string word) => word switch {
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
        }

    }
}

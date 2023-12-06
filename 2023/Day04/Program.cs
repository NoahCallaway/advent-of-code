
var filePath = "data.txt";
var lines = File.ReadLines(filePath);

var cards = new Dictionary<int, List<HashSet<int>>>();
var copies = Enumerable.Repeat(1, lines.Count()).ToArray();

var part1 = 0;

foreach (var ln in lines)
{
    var cardId = int.Parse(ln.Split(' ', StringSplitOptions.RemoveEmptyEntries)[1].Split(':')[0]);
    
    var numbers= ln.Split(':')[1].Split('|');
    var winning = numbers[0].Split(' ', StringSplitOptions.RemoveEmptyEntries).Select(x => int.Parse(x)).ToHashSet();
    var scratched = numbers[1].Split(' ', StringSplitOptions.RemoveEmptyEntries).Select(x => int.Parse(x)).ToHashSet();
    
    //Thought this might be useful but wasn't... leaving for future reference
    cards.Add(cardId, new List<HashSet<int>>() {winning, scratched});

    var matches = winning.Intersect(scratched).Count();
    if (matches > 0)
        part1 += Convert.ToInt32(1 * Math.Pow(2, winning.Intersect(scratched).Count() - 1));

    for (var i = cardId; i < cardId + matches; i++)
        copies[i] += copies[cardId - 1];
}

Console.WriteLine("Part 1: " + part1);
Console.WriteLine("Part 2: " + copies.Sum());
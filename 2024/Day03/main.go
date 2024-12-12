package main

import (
	"bufio"
	"fmt"
	"os"
	"regexp"
	"strconv"
	"strings"
)

func mul(x string) int {
	split := strings.Split(x[4:len(x)-1], ",")
	val1, _ := strconv.Atoi(split[0])
	val2, _ := strconv.Atoi(split[1])

	return val1 * val2
}

func main() {
	file := "input.txt"
	data, _ := os.Open(file)

	scanner := bufio.NewScanner(data)

	re := regexp.MustCompile(`mul\(\d+,\d+\)|(do\(\)|don\'t\(\))`)

	part1 := 0
	part2 := 0
	enabled := true

	for scanner.Scan() {
		for _, match := range re.FindAllString(scanner.Text(), -1) {
			fmt.Println(match)
			if strings.Contains(match, "mul") {
				result := mul(match)
				part1 += result

				if enabled {
					part2 += result
				}

			} else if match == "don't()" {
				enabled = false
			} else if match == "do()" {
				enabled = true
			}
		}
	}

	fmt.Println("Part 1:", part1)
	fmt.Println("Part 2:", part2)
}

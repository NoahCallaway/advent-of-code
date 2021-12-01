file_path = "passport-input.txt"

with open(file_path) as f:
    passports = f.read().split('\n\n')
    f.close()

class passport:
    def __init__(self, values: dict) -> None:
        self.byr = int(values["byr"]) if "byr" in values else None
        self.iyr = int(values["iyr"]) if "iyr" in values else None
        self.eyr = int(values["eyr"]) if "eyr" in values else None
        self.hgt = values["hgt"] if "hgt" in values else None
        self.hcl = values["hcl"] if "hcl" in values else None
        self.ecl = values["ecl"] if "ecl" in values else None
        self.pid = values["pid"] if "pid" in values else None
        self.cid = values["cid"] if "cid" in values else None
    
    def check_fields(self) -> bool:
        return all((self.byr, self.iyr, self.eyr, self.hgt, self.hcl, self.ecl, self.pid))
    
    def check_data(self) -> bool:
        if self.check_fields() == False:
            return False
        return all((
            self.check_byr(self.byr),
            self.check_iyr(self.iyr),
            self.check_eyr(self.eyr),
            self.check_hgt(self.hgt),
            self.check_hcl(self.hcl),
            self.check_ecl(self.ecl),
            self.check_pid(self.pid),
        ))

    def check_byr(self, byr: int) -> bool:
        return 1920 <= byr <= 2002
    
    def check_iyr(self, iyr: int) -> bool:
        return 2010 <= iyr <= 2020
    
    def check_eyr(self, eyr: int) -> bool:
        return 2020 <= eyr <= 2030

    def check_hgt(self, hgt: str) -> bool:
        if hgt[-2:] == "cm" and hgt[:-2].isnumeric():
            return 150 <= int(hgt[:-2]) <= 193
        elif hgt[-2:] == "in" and hgt[:-2].isnumeric():
            return 59 <= int(hgt[:-2]) <= 76
        else:
            return False
        
    def check_hcl(self, hcl: str) -> bool:
        if len(hcl) != 7 or hcl[0] != "#":
            return False
        return all(47 < ord(c) < 58 or 96 < ord(c) < 103 for c in hcl[1:])

    def check_ecl(self, ecl: str) -> bool:
        return ecl in ("amb", "blu", "brn", "gry", "grn", "hzl", "oth")

    def check_pid(self, pid: int) -> bool:
        return len(pid) == 9 and pid.isnumeric()

#Get to dictionary and create passport object 
for i in range(len(passports)):
    #get rid of new line
    passports[i] = passports[i].replace('\n',' ')
    passports[i] = dict(x.split(':') for x in passports[i].split(' '))
    passports[i] = passport(passports[i])


part1_count = 0
part2_count = 0
for each in passports:
    part1_count = (part1_count + 1) if each.check_fields() else part1_count
    part2_count = (part2_count + 1) if each.check_data() else part2_count

print("Part One Valid Passports = %s" % part1_count)
print("Part Two Valid Passports = %s" % part2_count)


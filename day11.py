import sys

test = bool(int(sys.argv[1]))
file_path = ""
data = ""
amount_of_rounds = int(sys.argv[2])
doprint = False

if test:
    file_path = "test_day_11.txt"
else:
    file_path = "input_day_11.txt"

with open(file_path, "r") as f:
    monkeys = f.read().split("\n\n")

# We can simply the solution space by using this modulo as we test only those results within
# the bounds of the product of the test factors. As multiplication and summation under mod can
# be split up this operation is fine. It is the principle of the lcm. And as they are all primes
# we can takes their multiple. And as we do not need the worry levels, we can mod them
monkey_mod = 1
set_for_monkey_mod = set([])
converted = []

for monkey in monkeys:
    if monkey != "":
        info = monkey.split("\n")
        starting_items = []
        for number in info[1].split(": ")[1].split(", "):
            starting_items += [int(number)]

        set_for_monkey_mod.add(int(info[3].split(" ")[-1]))
        operation = info[2].split(" ")

        converted += [
            {
                "name": info[0].split(":")[0],
                "possesions": starting_items,
                "operation": operation[-2],
                "scalar": operation[-1],  # can be 'old'
                "test": int(info[3].split(" ")[-1]),
                "iftrue": int(info[4].split(" ")[-1]),
                "iffalse": int(info[5].split(" ")[-1]),
                "no_of_inspections": 0,
            }
        ]

for elem in set_for_monkey_mod:
    monkey_mod *= elem

for round in range(amount_of_rounds):
    for monkey in converted:
        while monkey["possesions"] != []:
            it = monkey["possesions"][0]
            monkey["possesions"] = monkey["possesions"][1:]

            match monkey["operation"]:
                case "*":
                    if monkey["scalar"] == "old":
                        it = int(it**2) % monkey_mod  # / 3)
                    else:
                        it = int(it * int(monkey["scalar"])) % monkey_mod  # / 3)
                case "+":
                    it = int((it + int(monkey["scalar"]))) % monkey_mod  # / 3)

            if it % monkey["test"] == 0:
                converted[monkey["iftrue"]]["possesions"].append(it)
            else:
                converted[monkey["iffalse"]]["possesions"].append(it)

            monkey["no_of_inspections"] += 1

    if doprint:
        print("Round: ", round)
        for monkey in converted:
            print(monkey["name"], ": ", monkey["possesions"])

listnoi = []
print("Final answer")

for monkey in converted:
    print(monkey["name"], ": ", monkey["no_of_inspections"])
    listnoi += [monkey["no_of_inspections"]]
listnoi = sorted(listnoi, reverse=True)
print(listnoi[0] * listnoi[1])

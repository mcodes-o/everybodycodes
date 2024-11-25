
with open("data/quest-01/part02.txt") as f:
    line = f.readline()


scores = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}

def parse(input_line:str) -> int:
    result = 0 
    for idx in range(0, len(input_line), 2):
        pair_1 = input_line[idx]
        pair_2 = input_line[idx+1]
        if pair_1 == "x" or pair_2 == "x": 
            result += scores[pair_1]
            result += scores[pair_2]
        else:
            result += scores[pair_1]
            result += scores[pair_2]
            result += 2
    return result


if __name__ == "__main__":
    with open("data/quest-01/part02.txt") as f:
        line = f.readline()
    print(parse(line))

def test_example():
    assert parse("AxBCDDCAxD") == 28
scores = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}

def parse(input_line:str) -> int:
    result = 0 
    for idx in range(0, len(input_line), 3):
        pair_1 = input_line[idx]
        pair_2 = input_line[idx+1]
        pair_3 = input_line[idx+2]
        number_of_x = f"{pair_1}{pair_2}{pair_3}".count("x")

        step_score = scores[pair_1]
        step_score += scores[pair_2]
        step_score += scores[pair_3]
        if number_of_x == 2:
            step_score += 0
        elif number_of_x == 1:
            step_score += 2
        elif number_of_x == 0:
            step_score += 6

        result += step_score
    return result


if __name__ == "__main__":
    with open("data/quest-01/part03.txt") as f:
        line = f.readline()
    print(parse(line))

def test_example():
    assert parse("xBxAAABCDxCC") == 30
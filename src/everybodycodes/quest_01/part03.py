from itertools import batched

scores = {"A": 0, "B": 1, "C": 3, "D": 5, "x": 0}


def parse(input_line: str) -> int:
    result = 0
    for creatures in batched(input_line, 3):
        step_score = sum(scores[beast] for beast in creatures)

        number_of_x = creatures.count("x")
        if number_of_x == 1:
            step_score += 2
        elif number_of_x == 0:
            step_score += 6

        result += step_score
    return result


if __name__ == "__main__":
    with open("data/quest-01/part03.txt") as f:
        line = f.readline().strip()
    print(parse(line))


def test_data() -> None:
    with open("data/quest-01/part03.txt") as f:
        line = f.readline().strip()
    assert parse(line) == 27491


def test_example() -> None:
    assert parse("xBxAAABCDxCC") == 30

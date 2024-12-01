from collections import Counter

def read_input(file_path):
    """Reads input from a file and returns a list of integers."""
    list1 = []
    list2 = []
    with open(file_path, 'r') as f:
        for line in f:
            try:
                num1, num2 = map(int, line.split())
            except ValueError:
                print("Line does not contain exactly two values.")
            list1.append(num1)
            list2.append(num2)
    return list1, list2

def part1(list1, list2):
    """Solves Part 1: Calculates the distance of both lists."""
    total_distance = 0
    list1.sort()
    list2.sort()
    for a, b in zip(list1, list2):
        print(a, b)
        total_distance += abs(a - b)

    return total_distance

def part2(list1, list2):
    """Solves Part 1: Calculates the similarity score of both lists."""
    similarity_score = 0
    count_map = Counter(list2)
    for num in list1:
        similarity_score += num * count_map.get(num, 0)

    return similarity_score


if __name__ == "__main__":
    # Replace 'input.txt' with the actual path to your input file.
    input_file = 'input.txt'
    list1, list2 = read_input(input_file)
    
    # Solve Part 1
    result1 = part1(list1, list2)
    print(f"Part 1: {result1}")

    # Solve Part 2
    result2 = part2(list1, list2)
    print(f"Part 2: {result2}")

MULTIPLICATION_RANGE = range(2, 7)
NUM_OF_DIGITS = 6


def check_nums_are_cyclic(s1: int, s2: int) -> bool:
    """
    converts the inputs to strings and checks if the
    strings are cyclic permutations of each other
    """
    # storing concatenated string
    temp = f"{s1}{s1}"
    if str(s2) in temp:
        # returning true if 2nd string is present in concatenated string
        return True
    return False


def main() -> None:
    """
    There is a six-digit number that when multiplied by 2, 3, 4, 5 or 6 remains
    made up of the same digits (and only 6 digits) in the same order. All that
    changes is the place where the number starts. What is the 6 digit no?
    """
    loop_start = int(f"1{0:0{NUM_OF_DIGITS-1}d}")
    loop_end = int(f"1{0:0{NUM_OF_DIGITS}d}")

    for i in range(loop_start, loop_end):
        for j in MULTIPLICATION_RANGE:
            if not check_nums_are_cyclic(i, j * i):
                break
        if j == MULTIPLICATION_RANGE[-1]:
            print(f"the answer is {i}")
            break


if __name__ == "__main__":
    main()

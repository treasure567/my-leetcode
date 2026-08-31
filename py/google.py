def run(values):
    booked = set()

    for i in values:
        reg = i[1:]
        sym = i[0]
        if sym == '+':
            booked.add(reg)
        else:
            booked.discard(reg)

    return len(booked)


def test():
    test_cases = [
        {
            "input": ["+0A", "+9Z", "+4F", "-9Z", "+3G", "+9Z"],
            "expected": 4
        },
        {
            "input": ["+4B", "-4B", "+4B", "-4B"],
            "expected": 0
        },
        {
            "input": ["+4A", "+5B", "+5A"],
            "expected": 3
        }
    ]

    for i, case in enumerate(test_cases, start=1):
        result = run(case["input"])
        expected = case["expected"]

        if result == expected:
            print(f"Test {i}: ✅ PASSED")
        else:
            print(f"Test {i}: ❌ FAILED")
            print(f"  Input:    {case['input']}")
            print(f"  Expected: {expected}")
            print(f"  Got:      {result}")


if __name__ == "__main__":
    test()

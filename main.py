result = []

def divider(a, b):
    try:
        if a < b:
            raise ValueError("Invalid input: a < b")
        if b > 100:
            raise IndexError("Invalid input: b > 100")
        return a / b
    except ValueError as ve:
        print(f"ValueError: {ve}")
    except IndexError as ie:
        print(f"IndexError: {ie}")
    except Exception as e:
        print(f"Exception occurred: {e}")

data = {10: 2, 2: 5, "123": 4, 18: 0, []: 15, 8: 4}

for key in data:
    res = divider(key, data[key])
    result.append(res)

print(result)
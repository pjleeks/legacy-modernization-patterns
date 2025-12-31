# legacy_script.py
# Simulates a fragile legacy script with hidden business logic

def run(data):
    total = 0
    for x in data:
        if x > 10:
            total += x * 1.1
        else:
            total += x * 0.9
    return round(total, 2)


if __name__ == "__main__":
    sample = [5, 12, 20]
    print(run(sample))

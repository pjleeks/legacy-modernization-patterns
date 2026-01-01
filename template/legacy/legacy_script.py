from src.core.processing import calculate_total

def run(data):
    return calculate_total(data)

if __name__ == "__main__":
    sample = [5, 12, 20]
    print(run(sample))

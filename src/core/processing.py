def calculate_total(data):
    total = 0
    for x in data:
        if x > 10:
            total += x * 1.1
        else:
            total += x * 0.9
    return round(total, 2)

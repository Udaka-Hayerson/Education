import datetime as dt

def days_diff(a, b):
    count = 0
    one, two, three = a[0], a[1], a[2]
    four, five, six = b[0], b[1], b[2]
    start_date = dt.datetime(one, two, three)
    end_date = dt.datetime(four, five, six)
    if start_date == end_date:
        return  0
    total_days = (end_date - start_date).days
    for x in range(total_days):
        count += 1
    if count == 0:
        for x in range(total_days - 1, -1):
            count += 1
    return count

# print(days_diff((1982, 4, 19), (1982, 4, 22)))
# print(days_diff((2014, 1, 1), (2018, 8, 27)))
# print(days_diff((2001, 12, 1), (2001, 11, 1)))

if __name__ == "__main__":
    print("Example:")
    print(days_diff((1982, 4, 19), (1982, 4, 22)))

    # These "asserts" are used for self-checking and not for an auto-testing
    assert days_diff((1982, 4, 19), (1982, 4, 22)) == 3
    assert days_diff((2014, 1, 1), (2014, 8, 27)) == 238
    assert days_diff((2014, 8, 27), (2014, 1, 1)) == 238
    print("Coding complete? Click 'Check' to earn cool rewards!")
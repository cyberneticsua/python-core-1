def mean(number):
    total_sum = 0
    digit_count = 0

    number_str = str(number)

    for digit in number_str:
        total_sum += int(digit)
        digit_count += 1

    mean_value = total_sum / digit_count
    return mean_value
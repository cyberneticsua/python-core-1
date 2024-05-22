def squares_sum(n):
    sum_of_squares = 0
    for i in range(1, n + 1):
      sum_of_squares += i ** 2
    return sum_of_squares


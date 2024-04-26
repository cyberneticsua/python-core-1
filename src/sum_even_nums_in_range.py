def sum_even_nums_in_range(start, stop):
  sum_of_evens = 0
  for num in range(start, stop + 1):
    if num % 2 == 0:
      sum_of_evens = sum_of_evens + num
  return sum_of_evens

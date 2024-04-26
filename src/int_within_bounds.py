def int_within_bounds(number, lower_bound, upper_bound):
  if not isinstance(number, int):  # Перевірка, чи число є цілим
    return False
  return lower_bound <= number < upper_bound



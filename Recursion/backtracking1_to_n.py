def func(n):
  if n < 1:
    return
  func(n-1)
  print(n)


func(3)

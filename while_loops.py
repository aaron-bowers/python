# WHILE LOOPS - executes code as long as condition is True
i = 1
while i < 6:
  print(i)
  i += 1  # be sure to increment i, otherwise the loop will go on forever

# BREAK STATEMENT
i = 1
while i < 6:
  print(i)
  if i == 3:
    break
  i += 1

# CONTINUE STATEMENT
i = 0
while i < 6:
  i += 1
  if i ==3:
    continue
  print(i)
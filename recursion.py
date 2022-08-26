# RECURSION - defined function invokes itself until it reaches some condition (base case)

# tri_recursion() example
def tri_recursion(k):
  if k > 0:
    result = k + tri_recursion(k - 1)
    print(result)
  else:
    result = 0
  return result

print("Recursion Example Results")
tri_recursion(6)

# calculate factorials
def tri_recursion_factorial(k):
  if k > 1:
    result = k * tri_recursion_factorial(k - 1)
    print(result)
  else:
    result = 1
  return result

print("Recursion Factorial Example Results")
tri_recursion_factorial(5)
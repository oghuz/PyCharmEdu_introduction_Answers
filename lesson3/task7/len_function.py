phrase = """
It is a really long string
triple-quoted strings are used
to define multi-line strings
"""
first_half = phrase[:len(phrase)/2]
second_half = phrase[len(phrase)/2:]
equal = len(first_half) == len(second_half)
print(second_half)
print(first_half)
print(equal)

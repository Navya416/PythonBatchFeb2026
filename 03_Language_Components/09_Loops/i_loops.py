"""
Purpose: Loops
    break     - breaks the complete loop
    continue  - skip the current loop
    pass      - will do nothing. it is like a todo
    sys.exit  - will exit the script execution

"""

import sys

i = 0
while i <= 7:
    i += 1
    print(i, end=" ")


print("\n importance of break")
i = 0
while i <= 7:
    i += 1
    if i != 2 and i % 2 == 0:
        break
    print(i, end=" ")


print("\n importance of continue")
i = 0
while i <= 7:
    i += 1
    if i != 2 and i % 2 == 0:
        continue
    print(i, end=" ")


print("\n importance of pass")
i = 0
while i <= 7:
    i += 1
    if i % 2 == 0:
        pass  # It acts as a placeholder
    print(i, end=" ")

def myfunc():
    pass

class Myclass:
    pass 


print("\nimportance of sys.exit")
i = 0
while i < 7:
    i += 1
    if i % 2 == 0:
        sys.exit(0)
    print(i, end=" ")


# exit code 0 - successful/normal termination
# exit code non-zero - abnormal termination
print("next statement")

# Assignment: Try these break, continue, pass, on a for loop example
# 1. break
print("break example")
for i in range(1, 11):
    if i == 6:
        break
    print(i, end=" ")

# Output: 1 2 3 4 5

print("\n")

# 2. continue
print("continue example")
for i in range(1, 11):
    if i % 2 == 0:
        continue
    print(i, end=" ")

# Output: 1 3 5 7 9

print("\n")

# 3. pass
print("pass example")
for i in range(1, 11):
    if i % 2 == 0:
        pass
    print(i, end=" ")

# Output: 1 2 3 4 5 6 7 8 9 10

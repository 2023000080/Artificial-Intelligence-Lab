location = 'A'
A = 'Clean'
B = 'Clean'

print("Status:")
print("Location A:", A)
print("Location B:", B)

def left():
    global location
    location = 'A'
    print("Action: LEFT")

def right():
    global location
    location = 'B'
    print("Action: RIGHT")

def suck():
    global A, B
    print("Action: SUCK")
    if location == 'A':
        A = 'Clean'
    else:
        B = 'Clean'

def noOp():
    print("Action: NOOP")

def performance():
    cleaned = 0
    if A == 'Clean':
        cleaned += 1
    if B == 'Clean':
        cleaned += 1

    cleaned_percent = (cleaned / 2) * 100
    dirty_percent = 100 - cleaned_percent

    print("\nPerformance:")
    print("Cleaned =", cleaned_percent, "%")
    print("Dirty =", dirty_percent, "%")

# Agent logic
if location == 'A':
    if A == 'Dirty':
        suck()
    else:
        right()

if location == 'B':
    if B == 'Dirty':
        suck()
    else:
        noOp()

print("\nFinal Status:")
print("Location A:", A)
print("Location B:", B)

performance()


rooms = ["Terrace", "Store Room", "Bathroom", "Bedroom", "Hall", "Kitchen"]

# Initially all rooms are dirty (1 = Dirty, 0 = Clean)
room_status = {}
for room in rooms:
    room_status[room] = [1, 1, 1]   # Left, Center, Right

total_parts = len(rooms) * 3
cleaned_parts = 0

print("Initial State (All Rooms Dirty):")
for room in room_status:
    print(room, ":", room_status[room])

# Cleaning process room by room
for room in rooms:
    print(f"\nCleaning {room}")

    # Left Part
    room_status[room][0] = 0
    cleaned_parts += 1
    percent = (cleaned_parts / total_parts) * 100
    print("Left cleaned - Percentage cleaned:", round(percent, 2), "%")

    # Center Part
    room_status[room][1] = 0
    cleaned_parts += 1
    percent = (cleaned_parts / total_parts) * 100
    print("Center cleaned - Percentage cleaned:", round(percent, 2), "%")

    # Right Part
    room_status[room][2] = 0
    cleaned_parts += 1
    percent = (cleaned_parts / total_parts) * 100
    print("Right cleaned - Percentage cleaned:", round(percent, 2), "%")

    print(room, "completely cleaned")

print("\nFinal State (All Rooms Clean):")
for room in room_status:
    print(room, ":", room_status[room])
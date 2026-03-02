class State:
    def __init__(self, monkey_pos, box_pos, on_box, has_banana):
        self.monkey_pos = monkey_pos
        self.box_pos = box_pos
        self.on_box = on_box
        self.has_banana = has_banana

    def __str__(self):
        return f"Monkey: {self.monkey_pos}, Box: {self.box_pos}, OnBox: {self.on_box}, HasBanana: {self.has_banana}"


def monkey_banana_problem():
    state = State("door", "window", False, False)

    print("Initial:", state)

    state.monkey_pos = "window"
    print("Monkey moves to box:", state)

    state.box_pos = "middle"
    state.monkey_pos = "middle"
    print("Pushes box to middle:", state)

    state.on_box = True
    print("Monkey climbs box:", state)

    if state.on_box and state.box_pos == "middle":
        state.has_banana = True
        print("Banana grabbed!")

    print("Final:", state)


if __name__ == "__main__":
    monkey_banana_problem()
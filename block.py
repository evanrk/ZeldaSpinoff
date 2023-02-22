class Block:
    def __init__(self, start_x, end_x, start_y, end_y):
        self.start_x = start_x
        self.start_y = start_y
        self.end_y = end_y
        self.end_x = end_x


def is_touching(hit_box, block):
    print("NOT FINISHED")
    if (hit_box.start_x < block.start_x) and (hit_box.start_y < block.start_y):
        return True

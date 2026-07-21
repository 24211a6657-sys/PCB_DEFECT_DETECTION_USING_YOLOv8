class Grid:

    """
    Creates a virtual grid over the PCB image.
    """

    def __init__(self, rows=8, cols=8):
        self.rows = rows
        self.cols = cols

    def generate_grid(self, image_width, image_height):

        cell_width = image_width / self.cols
        cell_height = image_height / self.rows

        return cell_width, cell_height
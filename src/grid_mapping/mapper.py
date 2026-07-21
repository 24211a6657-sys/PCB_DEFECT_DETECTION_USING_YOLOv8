from string import ascii_uppercase


class GridMapper:

    def __init__(self, rows=8, cols=8):
        self.rows = rows
        self.cols = cols

    def get_grid_location(self,
                          center_x,
                          center_y,
                          image_width,
                          image_height):

        cell_width = image_width / self.cols
        cell_height = image_height / self.rows

        column = min(int(center_x // cell_width), self.cols - 1)
        row = min(int(center_y // cell_height), self.rows - 1)

        return f"{ascii_uppercase[row]}{column + 1}"
import cv2
from string import ascii_uppercase


class Visualizer:
    """
    Draw PCB Grid and YOLO Detection Results
    """

    def __init__(self, rows=8, cols=8):

        self.rows = rows
        self.cols = cols

    # =====================================================
    # Draw PCB Grid
    # =====================================================

    def draw_grid(self, image):

        image = image.copy()

        h, w = image.shape[:2]

        cell_w = w // self.cols
        cell_h = h // self.rows

        # Vertical Lines
        for i in range(self.cols + 1):

            cv2.line(
                image,
                (i * cell_w, 0),
                (i * cell_w, h),
                (180, 180, 180),
                1
            )

        # Horizontal Lines
        for j in range(self.rows + 1):

            cv2.line(
                image,
                (0, j * cell_h),
                (w, j * cell_h),
                (180, 180, 180),
                1
            )

        # Grid Labels
        for r in range(self.rows):

            for c in range(self.cols):

                cv2.putText(

                    image,

                    f"{ascii_uppercase[r]}{c+1}",

                    (c * cell_w + 5, r * cell_h + 20),

                    cv2.FONT_HERSHEY_SIMPLEX,

                    0.45,

                    (160, 160, 160),

                    1

                )

        return image

    # =====================================================
    # Draw YOLO Bounding Boxes
    # =====================================================

    def draw_detections(self, image, detections):

        for det in detections:

            x1 = int(det["bbox"]["x1"])
            y1 = int(det["bbox"]["y1"])
            x2 = int(det["bbox"]["x2"])
            y2 = int(det["bbox"]["y2"])

            label = (
                f'{det["class_name"]} '
                f'{det["confidence"]:.2f} '
                f'[{det["grid"]}]'
            )

            cv2.rectangle(

                image,

                (x1, y1),

                (x2, y2),

                (0, 255, 0),

                2

            )

            cv2.putText(

                image,

                label,

                (x1, max(20, y1 - 8)),

                cv2.FONT_HERSHEY_SIMPLEX,

                0.55,

                (0, 255, 0),

                2

            )

        return image

    # =====================================================
    # Optional Wrapper
    # =====================================================

    def draw(self, image, detections):

        image = self.draw_grid(image)

        image = self.draw_detections(
            image,
            detections
        )

        return image
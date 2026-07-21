import cv2


class ImageLoader:
    """
    Responsible for loading PCB images.
    """

    @staticmethod
    def load(image_path):

        image = cv2.imread(image_path)

        if image is None:
            raise FileNotFoundError(
                f"Image not found: {image_path}"
            )

        return image
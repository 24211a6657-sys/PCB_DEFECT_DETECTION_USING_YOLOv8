import cv2


class ImageResizer:
    """
    Resize images before detection.
    """

    @staticmethod
    def resize(image, size=(640, 640)):

        return cv2.resize(image, size)
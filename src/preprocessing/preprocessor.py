from src.preprocessing.image_loader import ImageLoader
from src.preprocessing.image_resizing import ImageResizer
from src.preprocessing.normalize import ImageNormalizer


class Preprocessor:
    """
    Complete preprocessing pipeline.
    """

    def __init__(self):

        self.loader = ImageLoader()

        self.resizer = ImageResizer()

        self.normalizer = ImageNormalizer()

    def load_image(self, image_path):

        return self.loader.load(image_path)

    def resize_image(self, image, size=(640, 640)):

        return self.resizer.resize(image, size)

    def normalize_image(self, image):

        return self.normalizer.normalize(image)

    def preprocess(self, image_path):

        image = self.load_image(image_path)

        image = self.resize_image(image)

        return image
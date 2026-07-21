from ultralytics import YOLO


class Predictor:
    """
    YOLO Prediction Engine for PCB Defect Detection
    """

    def __init__(self, model_path):
        print("Loading YOLO model...")

        self.model = YOLO(model_path)

        print("✅ Model Loaded Successfully.")

    def predict(
        self,
        image_path,
        save=False,
        conf=0.25
    ):
        """
        Run YOLO prediction.

        Args:
            image_path (str): Path to input image.
            save (bool): Save prediction image to disk.
            conf (float): Confidence threshold.

        Returns:
            list: YOLO prediction results.
        """

        results = self.model.predict(
            source=image_path,
            conf=conf,
            save=save,
            verbose=False
        )

        return results
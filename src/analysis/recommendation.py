class RecommendationEngine:
    """
    Generate recommendations based on detected defects.
    """

    def __init__(self):

        self.recommendations = {

            "missing_hole":
                "Drill or manufacturing process should be inspected.",

            "mouse_bite":
                "Inspect board edges for material loss and repair if necessary.",

            "open_circuit":
                "Repair broken conductive tracks or replace PCB.",

            "short":
                "Remove unwanted conductive bridges immediately.",

            "spur":
                "Remove excess copper traces during manufacturing.",

            "spurious_copper":
                "Clean unwanted copper deposits from PCB."
        }

    def generate(self, detections):

        if len(detections) == 0:

            return ["No defects detected. PCB is ready for use."]

        output = []

        added = set()

        for detection in detections:

            defect = detection["class_name"]

            if defect not in added:

                output.append(self.recommendations.get(
                    defect,
                    "Manual inspection recommended."
                ))

                added.add(defect)

        return output
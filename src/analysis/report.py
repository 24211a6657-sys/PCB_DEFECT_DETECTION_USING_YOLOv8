from datetime import datetime


class ReportGenerator:
    """
    Generate inspection report.
    """

    def generate(
            self,
            image_name,
            detections,
            health,
            recommendations):

        report = {

            "Inspection Time":
                datetime.now().strftime("%d-%m-%Y %H:%M:%S"),

            "Image":
                image_name,

            "Total Defects":
                len(detections),

            "Health Score":
                health["health_score"],

            "Health Status":
                health["status"],

            "Detected Defects":
                health["summary"],

            "Recommendations":
                recommendations

        }

        return report
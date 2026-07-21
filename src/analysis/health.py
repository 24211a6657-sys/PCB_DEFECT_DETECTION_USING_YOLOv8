class PCBHealthAnalyzer:
    """
    Analyze PCB health based on detected defects.
    """

    def __init__(self):
        # Penalty score for each defect
        self.penalty = {
            "missing_hole": 20,
            "mouse_bite": 15,
            "open_circuit": 25,
            "short": 30,
            "spur": 10,
            "spurious_copper": 10
        }

    def analyze(self, detections):

        health_score = 100

        defect_summary = {}

        for detection in detections:

            defect = detection["class_name"]

            defect_summary[defect] = defect_summary.get(defect, 0) + 1

            health_score -= self.penalty.get(defect, 10)

        health_score = max(0, health_score)

        if health_score >= 90:
            status = "Excellent"

        elif health_score >= 75:
            status = "Good"

        elif health_score >= 50:
            status = "Average"

        else:
            status = "Critical"

        return {

            "health_score": health_score,

            "status": status,

            "total_defects": len(detections),

            "summary": defect_summary

        }
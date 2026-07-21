import cv2
import os

# ==========================================
# CHANGE ONLY THIS IMAGE NAME
# ==========================================

image_name = "l_light_01_spur_18_1_600"
image_path = f"datasets/train/images/{image_name}.jpg"
label_path = f"datasets/train/labels/{image_name}.txt"

# ==========================================

image = cv2.imread(image_path)

if image is None:
    print("❌ Image not found!")
    exit()

h, w = image.shape[:2]

with open(label_path, "r") as f:
    lines = f.readlines()

colors = {
    0: (255, 0, 0),      # mouse_bite
    1: (0, 255, 0),      # spur
    2: (0, 0, 255),      # missing_hole
    3: (255, 255, 0),    # short
    4: (255, 0, 255),    # open_circuit
    5: (0, 255, 255)     # spurious_copper
}

names = {
    0: "mouse_bite",
    1: "spur",
    2: "missing_hole",
    3: "short",
    4: "open_circuit",
    5: "spurious_copper"
}

for line in lines:

    cls, x, y, bw, bh = map(float, line.split())

    cls = int(cls)

    x1 = int((x - bw/2) * w)
    y1 = int((y - bh/2) * h)
    x2 = int((x + bw/2) * w)
    y2 = int((y + bh/2) * h)

    cv2.rectangle(image, (x1, y1), (x2, y2), colors[cls], 2)

    cv2.putText(
        image,
        names[cls],
        (x1, y1 - 8),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.5,
        colors[cls],
        2
    )

os.makedirs("outputs", exist_ok=True)

save_path = f"outputs/{image_name}_visualized.jpg"

cv2.imwrite(save_path, image)

print("✅ Visualization created successfully!")
print("Saved to:", save_path)
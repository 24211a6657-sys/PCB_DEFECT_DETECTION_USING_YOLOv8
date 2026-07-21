from pathlib import Path

# Path to your training labels folder
labels_path = Path("datasets/train/labels")

# Class names (must match data.yaml)
class_names = {
    0: "mouse_bite",
    1: "spur",
    2: "missing_hole",
    3: "short",
    4: "open_circuit",
    5: "spurious_copper"
}

# Initialize counts
counts = {i: 0 for i in class_names}

# Read every label file
for label_file in labels_path.glob("*.txt"):

    with open(label_file, "r") as f:

        for line in f:

            if line.strip():

                class_id = int(line.split()[0])

                counts[class_id] += 1

print("\n========== CLASS DISTRIBUTION ==========\n")

total = 0

for class_id, count in counts.items():

    total += count

    print(f"{class_names[class_id]:20} : {count}")

print("\n---------------------------------------")
print(f"Total Objects : {total}")
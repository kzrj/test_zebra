from collections import Counter
import yaml
from pathlib import Path

# Загрузка списка классов
with open("../dataset/data.yaml", "r") as f:
    data = yaml.safe_load(f)
class_names = data["names"]

# Функция для подсчёта объектов
def count_objects(label_dir):
    counts = Counter()
    for label_file in Path(label_dir).glob("*.txt"):
        with open(label_file, "r") as f:
            for line in f:
                class_id = int(line.split()[0])
                if class_id == 8:
                    print(class_names[class_id], label_file)
                counts[class_id] += 1
    return counts

# Только train-данные!
train_counts = count_objects("../dataset/train/labels")
print({class_names[k]: v for k, v in train_counts.items()})
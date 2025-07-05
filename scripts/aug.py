import albumentations as A
import cv2
import os
from albumentations import Compose

transform = A.Compose([
    # Геометрические преобразования
    A.HorizontalFlip(p=0.5),  # Горизонтальное отражение
    A.Rotate(limit=10, p=0.3),  # Поворот на ±10 градусов
    # A.RandomResizedCrop(height=640, width=640, scale=(0.8, 1.0)),  # Случайный кроп
    
    # Цветовые искажения
    A.RandomBrightnessContrast(brightness_limit=0.2, contrast_limit=0.2, p=0.5),
    A.Blur(blur_limit=3, p=0.1),  # Лёгкое размытие
    A.HueSaturationValue(hue_shift_limit=10, sat_shift_limit=15, val_shift_limit=10, p=0.3),
    
    # Артефакты
    A.CoarseDropout(max_holes=3, max_height=30, max_width=30, fill_value=0, p=0.2),  # Дырки

    A.GlassBlur(sigma=0.7, max_delta=2, p=0.1),
    A.RandomShadow(shadow_roi=(0, 0, 1, 0.5), p=0.2),

], bbox_params=A.BboxParams(format='yolo', min_visibility=0.7))  # Сохраняем bbox


def augment_and_save(image_path, label_path, output_dir, transform):
    image = cv2.imread(image_path)
    image = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)  
    
    # Чтение YOLO-разметки
    with open(label_path, 'r') as f:
        bboxes = []
        for line in f:
            class_id, xc, yc, w, h = map(float, line.strip().split())
            bboxes.append([xc, yc, w, h, class_id])  
    
    # Применение аугментаций
    augmented = transform(image=image, bboxes=bboxes)
    aug_image = augmented['image']
    aug_bboxes = augmented['bboxes']
    
    # Сохранение
    base_name = os.path.splitext(os.path.basename(image_path))[0]
    cv2.imwrite(f"{output_dir}/{base_name}_aug.jpg", cv2.cvtColor(aug_image, cv2.COLOR_RGB2BGR))
    
    # Сохранение новых bbox
    with open(f"{output_dir}/{base_name}_aug.txt", 'w') as f:
        for bbox in aug_bboxes:
            xc, yc, w, h, class_id = bbox
            f.write(f"{int(class_id)} {xc} {yc} {w} {h}\n")

# Пример вызова
os.makedirs("train_augmented", exist_ok=True)
for img_file in os.listdir("aug/images"):
    img_path = f"additional_aug/images/{img_file}"
    label_path = f"additional_aug/labels/{img_file.replace('.jpg', '.txt')}"
    augment_and_save(img_path, label_path, "additional_train_augmented", transform)
train_counts = {
    'glass': 416, 'cutlery': 185, 'soup_full': 57, 'salad_full': 116, 
    'tea_pot': 205, 'main_course_full': 307, 'main_course_eaten': 87, 
    'soup_empty': 88, 'salad_empty': 87, 'hand_waiter': 26, 
    'salad_eaten': 196, 'soup_eaten': 198, 'hand_guest': 257, 'main_course_empty': 0
}

total_samples = sum(train_counts.values())
num_classes = len(train_counts)

# Вычисляем веса
class_weights = {
    cls: round(total_samples / (num_classes * count), 2) 
    for cls, count in train_counts.items()
}

names = [
    'soup_full', 'salad_full', 'main_course_full', 
    'soup_eaten', 'salad_eaten', 'main_course_eaten', 
    'soup_empty', 'salad_empty', 'main_course_empty', 
    'tea_pot', 'glass', 'hand_waiter', 'hand_guest', 'cutlery'
]

print(class_weights)
class_weights_list = [class_weights[cls] for cls in names]

print(class_weights_list)
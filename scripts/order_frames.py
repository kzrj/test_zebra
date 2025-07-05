import os
import shutil

input_root = '../frames'          
output_dir = '../all_frames'      
os.makedirs(output_dir, exist_ok=True)

frame_index = 1

ordered_folders = ['1', '2_1', '3_1', '3_2', '4']

for subfolder in ordered_folders:
    subfolder_path = os.path.join(input_root, subfolder)
    if not os.path.isdir(subfolder_path):
        continue

    image_files = sorted(f for f in os.listdir(subfolder_path) if f.endswith('.jpg'))

    for img_name in image_files:
        src_path = os.path.join(subfolder_path, img_name)
        dst_path = os.path.join(output_dir, f"frame_{frame_index}.jpg")
        shutil.copy(src_path, dst_path)
        frame_index += 1

print(f"[✓] Готово! Всего скопировано {frame_index - 1} кадров в '{output_dir}/'")

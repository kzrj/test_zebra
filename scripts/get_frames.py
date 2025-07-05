import cv2
import os

# Папка с видео
VIDEO_DIR = '../videos'
# Папка для сохранения кадров
OUTPUT_DIR = '../frames'
# Каждые N секунд извлекать кадр
FRAME_EVERY_N_SECONDS = 2

os.makedirs(OUTPUT_DIR, exist_ok=True)

for filename in os.listdir(VIDEO_DIR):
    if not filename.endswith(".MOV"):
        continue

    video_path = os.path.join(VIDEO_DIR, filename)
    video_name = os.path.splitext(filename)[0]
    out_subdir = os.path.join(OUTPUT_DIR, video_name)
    os.makedirs(out_subdir, exist_ok=True)

    cap = cv2.VideoCapture(video_path)
    fps = cap.get(cv2.CAP_PROP_FPS)
    frame_interval = int(fps * FRAME_EVERY_N_SECONDS)

    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    current_frame = 0
    saved_frame = 0

    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        if current_frame % frame_interval == 0:
            out_path = os.path.join(out_subdir, f"frame_{saved_frame:04d}.jpg")
            cv2.imwrite(out_path, frame)
            saved_frame += 1

        current_frame += 1

    cap.release()
    print(f"[✓] {video_name}: {saved_frame} кадров сохранено")
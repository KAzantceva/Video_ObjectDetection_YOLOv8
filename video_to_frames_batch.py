import cv2
import os
from sklearn.model_selection import train_test_split

# Базовая папка с видеофайлами
base_folder = r"C:\Users\kalash\IDE\YOLO V8_2"

# Список подпапок
subfolders = ['NEW VIDEO 2023-20231221T113100Z-001',
              'Video-20231221T113304Z-001',
              'Гемангиома-20231221T112414Z-001',
              'Метастаз (По УЗИ обычном не видно)-20231221T112926Z-001',
              'метастаз-20231221T112857Z-001']

# Папка для сохранения кадров
frames_folder = 'frames'
os.makedirs(frames_folder, exist_ok=True)

# Проход по каждой подпапке
for subfolder in subfolders:
    subfolder_path = os.path.join(base_folder, subfolder)
    
    # Проход по всем видеофайлам в подпапке
    for root, dirs, files in os.walk(subfolder_path):
        for file in files:
            if file.endswith('.avi'):
                video_path = os.path.join(root, file)
                
                # Загрузка видео
                cap = cv2.VideoCapture(video_path)

                # Чтение кадров и сохранение их в папку
                frame_count = 0
                while True:
                    ret, frame = cap.read()
                    if not ret:
                        break

                    frame_count += 1
                    frame_filename = os.path.join(frames_folder, f'{subfolder}_{file}_frame_{frame_count:04d}.jpg')
                    cv2.imwrite(frame_filename, frame)

                # Освобождение ресурсов
                cap.release()

# Создание списка файлов с кадрами
frame_files = [f for f in os.listdir(frames_folder) if f.endswith('.jpg')]

# Разделение на обучающую и тестовую выборки
train_files, test_files = train_test_split(frame_files, test_size=0.3, random_state=42)

# Пути к обучающим и тестовым изображениям
train_images_paths = [os.path.join(frames_folder, image) for image in train_files]
test_images_paths = [os.path.join(frames_folder, image) for image in test_files]

# Пути к обучающим и тестовым изображениям (с абсолютными путями)
train_images_paths = [os.path.abspath(os.path.join(frames_folder, image)) for image in train_files]
test_images_paths = [os.path.abspath(os.path.join(frames_folder, image)) for image in test_files]

# Создание файлов train.txt и test.txt
with open('train.txt', 'w', encoding='utf-8') as train_file:
    train_file.write('\n'.join(train_images_paths))

with open('test.txt', 'w', encoding='utf-8') as test_file:
    test_file.write('\n'.join(test_images_paths))


# Можете использовать списки train_files и test_files для дальнейшей обработки

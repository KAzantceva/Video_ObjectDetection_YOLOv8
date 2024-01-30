import os

def create_annotation_file(image_folder, annotation_folder):
    for image_file in os.listdir(image_folder):
        if image_file.endswith((".jpg", ".jpeg", ".png")):
            image_name, _ = os.path.splitext(image_file)
            annotation_file_path = os.path.join(annotation_folder, image_name + ".txt")

            # Пример: создайте и запишите содержимое файла аннотации
            with open(annotation_file_path, 'w') as annotation_file:
                annotation_file.write("0 0.5 0.5 0.4 0.3")  # Замените это соответствующими значениями

# Пути для папок train и test
train_folder = "C:/Users/kalash/IDE/YOLO V8_2/train"
test_folder = "C:/Users/kalash/IDE/YOLO V8_2/test"

# Создаем файлы аннотаций для обучающего и тестового наборов
create_annotation_file(train_folder, "C:/Users/kalash/IDE/YOLO V8_2/train")
create_annotation_file(test_folder, "C:/Users/kalash/IDE/YOLO V8_2/test")

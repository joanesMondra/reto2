import os
import glob
from PIL import Image
import torch
from torch.utils.data import Dataset, DataLoader
from torchvision import transforms
import random
import torch.nn as nn
import torch.optim as optim
from tqdm import tqdm
import matplotlib.pyplot as plt

# ==================================================
# Data Augmentation Offline para Imágenes NOK
# ==================================================
def save_augmented_images_and_masks(image, mask, folder, base_name, augment_index):
    """
    Guarda imágenes y máscaras aumentadas en el directorio correspondiente.
    """
    augmented_image_name = f"{base_name}_aug_{augment_index}.jpg"
    augmented_mask_name = f"{base_name}_aug_{augment_index}_label.bmp"

    # Guardar imagen aumentada
    image.save(os.path.join(folder, augmented_image_name))

    # Guardar máscara aumentada
    mask.save(os.path.join(folder, augmented_mask_name))


def augment_nok_images(root_dir, num_augmentations=3):
    """
    Data augmentation para imágenes `NOK` y guardar las nuevas imágenes y máscaras.
    """
    augmentation_transforms = [
        transforms.RandomHorizontalFlip(p=1),  # Flip horizontal
        transforms.RandomVerticalFlip(p=1),  # Flip vertical
        transforms.ColorJitter(brightness=0.2, contrast=0.2),  # Cambios en brillo y contraste
    ]

    for folder in sorted(os.listdir(root_dir)):
        folder_path = os.path.join(root_dir, folder)
        if not os.path.isdir(folder_path):
            continue

        # Leer imágenes y máscaras
        images = sorted([f for f in os.listdir(folder_path) if f.endswith(".jpg")])
        masks = sorted([f for f in os.listdir(folder_path) if f.endswith("_label.bmp")])

        # Asegurarse de que cada imagen tiene su máscara correspondiente
        for img_name, mask_name in zip(images, masks):
            img_path = os.path.join(folder_path, img_name)
            mask_path = os.path.join(folder_path, mask_name)

            # Cargar imagen y máscara
            image = Image.open(img_path).convert("RGB")
            mask = Image.open(mask_path).convert("L")

            # Verificar si es `NOK` (máscara con valores mayores a 0)
            mask_tensor = torch.tensor(list(mask.getdata())).reshape(mask.size)
            if mask_tensor.max() > 0:  # Es una imagen `NOK`
                # Generar imágenes aumentadas
                for i in range(num_augmentations):
                    transform = random.choice(augmentation_transforms)  # Elegir transformación aleatoria
                    augmented_image = transform(image)  # Aplicar transformación a la imagen
                    augmented_mask = transform(mask)  # Aplicar transformación a la máscara

                    # Guardar las imágenes y máscaras aumentadas
                    base_name = os.path.splitext(img_name)[0]
                    save_augmented_images_and_masks(augmented_image, augmented_mask, folder_path, base_name, i)

    print("Data augmentation para imágenes NOK completado y guardado en las carpetas correspondientes.")

root_dir = "Imagenes_defectos3"

# Realizar data augmentation para imágenes NOK
augment_nok_images(root_dir, num_augmentations=6)



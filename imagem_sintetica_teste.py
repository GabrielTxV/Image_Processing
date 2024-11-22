import cv2
import numpy as np
import matplotlib.pyplot as plt

# Função para exibir as imagens lado a lado
def display_images(images, titles):
    plt.figure(figsize=(15, 5))
    for i, (img, title) in enumerate(zip(images, titles)):
        plt.subplot(1, len(images), i + 1)
        plt.imshow(img, cmap='gray' if len(img.shape) == 2 else None)
        plt.title(title)
        plt.axis('off')
    plt.show()

# Criar uma imagem sintética cinza (resolução 256 x 256 pixels) com nível 128
synthetic_img = np.full((256, 256), 128, dtype=np.uint8)

# Definir o tamanho do quadrado central
center_size = 32
start = (synthetic_img.shape[0] - center_size) // 2
end = start + center_size

# Aumentar o nível de cinza do quadrado central até o limite da percepção
for level in range(128, 256, 10):
    img_copy = synthetic_img.copy()
    img_copy[start:end, start:end] = level
    display_images([img_copy], [f"Nível de Cinza do Quadrado: {level}"])

# Diminuir o nível de cinza do quadrado central até o limite da percepção
for level in range(128, -1, -10):
    img_copy = synthetic_img.copy()
    img_copy[start:end, start:end] = level
    display_images([img_copy], [f"Nível de Cinza do Quadrado: {level}"])
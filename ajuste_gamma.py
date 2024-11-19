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

# Exercício 6
# Carregar a imagem Frog
frog_img = cv2.imread('dataset/frog.tif')

# Verificar se a imagem foi carregada corretamente
if frog_img is None:
    raise FileNotFoundError("A imagem 'dataset/Frog.png' não foi encontrada ou não pôde ser carregada.")

# Aplicar ajuste de contraste (gamma) na imagem Frog
gamma = 1.5
look_up_table = np.array([((i / 255.0) ** gamma) * 255 for i in np.arange(0, 256)]).astype("uint8")
frog_contrast = cv2.LUT(frog_img, look_up_table)

display_images([frog_img, frog_contrast], ["Original", f"Ajuste de Contraste (Gamma {gamma})"])
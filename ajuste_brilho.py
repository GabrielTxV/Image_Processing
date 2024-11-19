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

# Exercício 5
# Aplicar ajuste de brilho na imagem Frog
frog_img = cv2.imread('dataset/frog.tif')

# Verificar se a imagem foi carregada corretamente
if frog_img is None:
    raise FileNotFoundError("A imagem 'dataset/Frog.png' não foi encontrada ou não pôde ser carregada.")

frog_bright = cv2.convertScaleAbs(frog_img, alpha=1.2, beta=0)
display_images([frog_img, frog_bright], ["Original", "Ajuste de Brilho (Escala 1.2)"])
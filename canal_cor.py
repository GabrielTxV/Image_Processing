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

# Exercício 2
# Carregar a imagem colorida de Lena
canal_lena = cv2.imread('dataset/lena3.tif')

# Verificar se a imagem foi carregada corretamente
if canal_lena is None:
    raise FileNotFoundError("A imagem 'lena3.tif' não foi encontrada ou não pôde ser carregada.")

# Dividir a imagem nos canais R, G e B
b, g, r = cv2.split(canal_lena)

# Exibir cada canal em escala de cinza
display_images([r, g, b], ["Canal R", "Canal G", "Canal B"])
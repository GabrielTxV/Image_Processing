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

# Exercício 3
# Quantidade de bits por pixel da imagem colorida e em tons de cinza
# Lena colorida: 8 bits por canal, total 24 bits por pixel
# Lena gray: 8 bits por pixel

# Carregar a imagem colorida
lena_gray = cv2.imread('dataset/lena1.tif')

# Verificar se a imagem foi carregada corretamente
if lena_gray is None:
    raise FileNotFoundError("A imagem 'dataset/lena1.tif' não foi encontrada ou não pôde ser carregada.")

# Converter a imagem para tons de cinza
lena_gray = cv2.cvtColor(lena_gray, cv2.COLOR_BGR2GRAY)

# Quantização para 6, 4, 2 e 1 bit por pixel
quantized_images = []
for bits in [6, 4, 2, 1]:
    scale_factor = 256 // (2 ** bits)
    quantized = (lena_gray // scale_factor) * scale_factor
    quantized_images.append(quantized)

display_images([lena_gray] + quantized_images, ["Original"] + [f"{bits} bits por pixel" for bits in [6, 4, 2, 1]])
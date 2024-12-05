import cv2
import numpy as np
import matplotlib.pyplot as plt

# Carregar a imagem "Brain" em escala de cinza
image_path = 'dataset/brain.jpg'  # Substitua pelo caminho correto da imagem
original_image = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

# Verificar se a imagem foi carregada corretamente
if original_image is None:
    raise FileNotFoundError(f"A imagem '{image_path}' não foi encontrada ou não pôde ser carregada.")

# Parâmetros do ruído gaussiano
num_images = 32
mean = 0
std_dev = 25  # Desvio padrão do ruído

# Gerar 32 imagens com ruído gaussiano
noisy_images = []
for _ in range(num_images):
    noise = np.random.normal(mean, std_dev, original_image.shape).astype(np.float32)
    noisy_image = np.clip(original_image + noise, 0, 255).astype(np.uint8)
    noisy_images.append(noisy_image)

# Calcular a média das imagens ruidosas
average_image = np.mean(noisy_images, axis=0).astype(np.uint8)

# Mostrar as imagens usando matplotlib
def display_images(images, titles):
    plt.figure(figsize=(10, 5))
    for i, (img, title) in enumerate(zip(images, titles)):
        plt.subplot(1, len(images), i + 1)
        plt.imshow(img, cmap='gray')
        plt.title(title)
        plt.axis('off')
    plt.show()

display_images([original_image, average_image], ["Original Image", "Average of Noisy Images"])
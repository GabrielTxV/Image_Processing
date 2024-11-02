from PIL import Image
import matplotlib.pyplot as plt
import os

def resize_and_show(image_path):
    # Abrir a imagem original
    original_image = Image.open(image_path).convert('L')  # Converte para preto e branco
    
    # Redimensionar a imagem para os tamanhos desejados
    image_256 = original_image.resize((256, 256))
    image_128 = original_image.resize((128, 128))
    image_64 = original_image.resize((64, 64))
    
    # Exibir as imagens redimensionadas
    fig, axes = plt.subplots(1, 3, figsize=(12, 4))
    axes[0].imshow(image_256, cmap='gray')
    axes[0].set_title("256x256")
    axes[1].imshow(image_128, cmap='gray')
    axes[1].set_title("128x128")
    axes[2].imshow(image_64, cmap='gray')
    axes[2].set_title("64x64")

    # Remover eixos para uma visualização mais limpa
    for ax in axes:
        ax.axis('off')

    plt.show()

# Caminho relativo para a imagem na mesma pasta do código
image_path = os.path.join(os.path.dirname(__file__), 'dataset', 'lena1.tif')

resize_and_show(image_path)
import cv2
import numpy as np
import matplotlib.pyplot as plt

def plot_histogram(image, title):
    hist = cv2.calcHist([image], [0], None, [256], [0, 256])
    plt.plot(hist, color='gray')
    plt.title(title)
    plt.xlabel('Pixel Value')
    plt.ylabel('Frequency')
    plt.show()

# Carregar as imagens
images = ['dataset/lena1.tif', 'dataset/moon.jpg', 'dataset/bay.jpg', 'dataset/brain.jpg']  # Substitua pelos caminhos reais
titles = ['Lena Gray', 'Moon', 'Bay', 'Brain']

for img_path, title in zip(images, titles):
    image = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
    
    # Verificar se a imagem foi carregada corretamente
    if image is None:
        raise FileNotFoundError(f"A imagem '{img_path}' não foi encontrada ou não pôde ser carregada.")
    
    # Aplicar a equalização de histograma
    equalized_image = cv2.equalizeHist(image)
    
    # Mostrar as imagens original e equalizada
    cv2.imshow(f"{title} - Original", image)
    cv2.imshow(f"{title} - Equalized", equalized_image)
    
    # Plotar os histogramas
    plot_histogram(image, f"{title} - Original Histogram")
    plot_histogram(equalized_image, f"{title} - Equalized Histogram")
    
    cv2.waitKey(0)

cv2.destroyAllWindows()
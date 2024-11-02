import cv2
import numpy as np

def resize_and_show(image_path):
    # Carregar a imagem original em preto e branco
    original_image = cv2.imread(image_path)
    
    # Redimensionar a imagem para os tamanhos desejados
    image_256 = cv2.resize(original_image, (256, 256))
    image_128 = cv2.resize(original_image, (128, 128))
    image_64 = cv2.resize(original_image, (64, 64))
    
    # Colocar as imagens redimensionadas em uma única linha
    combined_image = np.hstack((image_256, cv2.resize(image_128, (256, 256)), cv2.resize(image_64, (256, 256))))
    
    # Mostrar a imagem combinada
    cv2.imshow("Images 256x256 | 128x128 | 64x64", combined_image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()

# Mostrar a imagem redimensionada
resize_and_show('dataset/lena1.tif')
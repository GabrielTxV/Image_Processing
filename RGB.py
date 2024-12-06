import cv2
import numpy as np

# Carregar a imagem
image_path = "dataset/balloons.tif"
image = cv2.imread(image_path)

# Verificar se a imagem foi carregada corretamente
if image is None:
    raise FileNotFoundError(f"A imagem '{image_path}' não foi encontrada ou não pôde ser carregada.")

# Extrair os canais B, G e R
b_channel = image[:, :, 0]
g_channel = image[:, :, 1]
r_channel = image[:, :, 2]

# Criar imagens coloridas para cada canal
r_image = np.zeros_like(image)
g_image = np.zeros_like(image)
b_image = np.zeros_like(image)

r_image[:, :, 2] = r_channel
g_image[:, :, 1] = g_channel
b_image[:, :, 0] = b_channel

# Concatenar as imagens lado a lado
concatenated_image = np.concatenate((image, r_image, g_image, b_image), axis=1)

# Mostrar a imagem original e os canais usando OpenCV
cv2.imshow("Original and RGB Channels", concatenated_image)

# Esperar até que uma tecla seja pressionada e fechar as janelas
cv2.waitKey(0)
cv2.destroyAllWindows()
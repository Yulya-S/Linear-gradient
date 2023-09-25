import numpy as np
import matplotlib.pyplot as plt


def lerp(v0, v1, t):
    return (1 - t) * v0 + t * v1


def rotation_45_degree(image):
    image_copy = image.copy()
    x = 0
    for i in range(len(image[0])):
        y = 0
        for l in range(len(image) // 2):
            image_copy[y][i] = image[l + x][i]
            image_copy[y + 1][i] = image[l + x][i]
            y += 2
        if i % 2 == 0:
            x += 1
    return image_copy


size = 100
image = np.zeros((size, size, 3), dtype="uint8")
assert image.shape[0] == image.shape[1]

color1 = [255, 128, 0]
color2 = [0, 128, 255]

for i, v in enumerate(np.linspace(0, 1, image.shape[0])):
    r = lerp(color1[0], color2[0], v)
    g = lerp(color1[1], color2[1], v)
    b = lerp(color1[2], color2[2], v)
    image[i, :, :] = [r, g, b]
image = rotation_45_degree(image)

plt.figure(1)
plt.imshow(image)
plt.show()

# https://www.dropbox.com/s/th0u3mpsl71fxit/CertificateTemplate.jpg
# PIL = python image library, cv2 = computer vision library helps to work with the image's scan & edit

import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image, ImageDraw, ImageFont
img = Image.open("./CertificateTemplate.jpg")


def print_image(img):
    plt.imshow(np.array(img))
    plt.show()


img = cv2.imread("./CertificateTemplate.jpg")


def generate_certificate(img, name="Enter Name: "):
    generated_image = img.copy()
    font = cv2.FONT_HERSHEY_SIMPLEX
    coordinates = (700, 750)
    font_size = 3.5
    font_color = (51, 51, 51)
    font_thickness = 10
    cv2.putText(generated_image, name, coordinates, font,
                font_size, font_color, font_thickness)
    return generated_image


def save_img(img, name):
    path = "./certi_{}.jpg".format(name)
    print(cv2.imwrite(path, img))


name = input("Enter the name you want on certificate: ")
generated_image = generate_certificate(img, name)
save_img(generated_image, name)

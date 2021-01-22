from PIL import Image

def openImage(imageName):
    img = Image.open('./media/' + imageName)
    img.show()
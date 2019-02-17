import io
import os

class word():
    """docstring for word"""
    def __init__(self, description, vertices):# lower_left, lower_right, upper_right, upper_left):
        self.description = description
        self.lleft = vertices[0]
        self.lright = vertices[1]
        self.uright = vertices[2]
        self.uleft = vertices[3]

def detect_text(path):
    """Detects text in the file."""
    from google.cloud import vision
    client = vision.ImageAnnotatorClient()

    with io.open(path, 'rb') as image_file:
        content = image_file.read()

    image = vision.types.Image(content=content)

    response = client.text_detection(image=image)
    texts = response.text_annotations
    print('Texts:')

    word_list = []

    for text in texts:
        # print('\n"{}"'.format(text.description))

        vertices = (['({},{})'.format(vertex.x, vertex.y)
                    for vertex in text.bounding_poly.vertices])

        # string = 'bounds: {}'.format(','.join(vertices))
        # print(string)

        new_word = word(text.description, vertices)
        word_list.append(new_word)

def check_close(y_coord, dict_coords):
    for coord in dict_coords:
        if 

def find_same_line(word_list):
    which_line = {}
    for w in word_list:

        if w.lleft[1] not in w


detect_text('./inputs/electronic/electronic1.jpg')


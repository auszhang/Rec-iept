import io
import os
import re
import sys
import argparse
# if re.match("^\d+?\.\d+?$", element) is None:
#     print "Not float"

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
    # print('Texts:')

    word_list = []
    i = 0

    for text in texts:
        # print('\n"{}"'.format(text.description))
        if i == 0:
            i += 1
        else:
            vertices = []
            for vertex in text.bounding_poly.vertices:
                v = (vertex.x, vertex.y)
                vertices.append(v)
            # vertices = (['({},{})'.format(vertex.x, vertex.y)
            #             for vertex in text.bounding_poly.vertices])

            # string = 'bounds: {}'.format(','.join(vertices))
            # print(string)

            new_word = word(text.description, vertices)
            word_list.append(new_word)
    return word_list

def check_close(curr_y_coord, y_coords_keys):
    # if len(y_coords_keys) == 0:
    #     return curr_y_coord
    for coord in y_coords_keys:
        # print('Coord: ', coord)
        # print('Current Coord: ', curr_y_coord)
        if abs(coord - curr_y_coord) <= 5:
            return coord
        # else:
        #     return 0
    return 0

def find_same_line(word_list):
    which_line = {}
    for w in word_list:
        # print(w.description)
        xD = check_close(w.lleft[1], which_line.keys())
        # print(w.lleft[1])
        if xD:
            # print(xD)
            # print('fffffff')
            which_line[xD] = which_line[xD] + " " + w.description
        else:
            # print(int(w.lleft[1]))
            # print('truuu')
            which_line[w.lleft[1]] = w.description
    return which_line

def extract_item_price(line_dic):
    new_dic = {}
    quantity_dic = {}
    for k,v in line_dic.items():
        split_value = v.split(" ")
        last_item = split_value[len(split_value) - 1]
        last_item = re.sub('[^0-9\.]', '', last_item)
        if re.match("^\d+\.\d+$", last_item):
            first_item = split_value[0]
            if re.match("^\d+$", first_item):
                new_key = " ".join(split_value[:-1])
                new_key = new_key.lstrip('0123456789.- ')
                quantity_dic[new_key] = int(first_item)
                new_dic[new_key] = float(last_item)
            else:
                new_key = " ".join(split_value[:-1])
                quantity_dic[new_key] = 1
                new_dic[new_key] = float(last_item)
    return new_dic


        # last_item = split_value[len(split_value) - 1]
        # last_item = re.sub('[^0-9\.]', '', last_item)
        #     if re.match("^\d+$", first_item):
        #         new_key = " ".join(split_value[:-1])
        #         quantity_dic[new_key] = int(first_item)
        #         new_key.lstrip('0123456789.- ')
            
        #     new_dic[new_key] = float(last_item)

special_words = ['subtotal', 'sub total', 'total', 'tax', 'gratuity', 'tip']
special_words2 = ['subtotal', 'sub total', 'total']
def checker(lst, word):
    for elem in lst:
        if elem in re.sub("[^a-zA-Z]", "", word).lower():
            return True
    return False
    # return re.sub("[^a-zA-Z]", "", word).lower() in lst

def mainer(filepath):
    w_list = detect_text(filepath)
    tester = find_same_line(w_list)
    temp_dic = extract_item_price(tester)
    item_price = {}
    for item, price in temp_dic.items():
        if not checker(special_words2, item):
            item_price[item] = price
    return item_price
# if __name__ == '__main__':
    # parser = argparse.ArgumentParser()                                               
    # parser.add_argument("--file", "-f", type=str, required=True)
    # args = parser.parse_args()
    # w_list = detect_text(args.file)
    # # './inputs/easy/easy1.jpg'
    # tester = find_same_line(w_list)
    # # print(tester)
    # item_price = extract_item_price(tester)
    # print(item_price)

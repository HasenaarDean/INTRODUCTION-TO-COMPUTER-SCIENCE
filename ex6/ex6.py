#############################################################
# FILE : ex6.py
# WRITER : dean_hasenaar , hasenaar , 313584401
# EXERCISE : intro2cs ex6 2016 - 2017
# DESCRIPTION: In this file we implemented the Photomasaic
# program.
#############################################################

# Magic numbers:

ALREADY_CHOSEN_TUPLE = (999, 999, 999)
WRONG_NUMBER_OF_PARAMETER_MESSAGE = "Wrong number of parameters. The " \
                                    "correct usage is:\nex6.py " \
                                    "<image_source> <images_dir> " \
                                    "<output_name> \n<tile_height> " \
                                    "<num_candidates>"


import math
import copy
from mosaic import *
import sys


def compare_pixel(pixel1, pixel2):

    """
    This function calculates the distance between 2 different pixels
    """

    r1 = pixel1[0]
    r2 = pixel2[0]
    g1 = pixel1[1]
    g2 = pixel2[1]
    b1 = pixel1[2]
    b2 = pixel2[2]
    return abs(r1-r2) + abs(g1-g2) + abs(b1-b2)


def compare(image1, image2):

    """
    This function calculates the distance between 2 different images
    """

    width1 = len(image1[0])
    length1 = len(image1)
    width2 = len(image2[0])
    length2 = len(image2)
    sum = 0
    for row in range(min(length1, length2)):
        for pxl in range(min(width1, width2)):
            sum += compare_pixel(image1[row][pxl], image2[row][pxl])
    return sum


def get_piece(image, upper_left, size):

    """
    This function returns a piece from an image by getting an input
    image, tuple of pixel location and tuple size of piece
    """

    image_row = len(image)
    image_col = len(image[0])
    init_row, init_col = upper_left
    piece_row, piece_col = size
    row_limiter = min(piece_row, (image_row - init_row))
    col_limiter = min(piece_col, (image_col - init_col))
    new_piece = []
    for i in range(row_limiter):
        new_line = []
        for j in range(col_limiter):
            new_line.append(image[init_row + i][init_col + j])
        new_piece.append(new_line)
    return new_piece
    

def set_piece(image, upper_left, piece):

    """
    This function changes a certain piece in the image with pixels from
    another picture, by getting an input image, tuple of pixel location
    and the second image which exchange the piece of the original image
    """

    image_row = len(image)
    image_col = len(image[0])
    init_row, init_col = upper_left
    piece_row = len(piece)
    piece_col = len(piece[0])
    row_limiter = min(piece_row, (image_row - init_row))
    col_limiter = min(piece_col, (image_col - init_col))
    for i in range(row_limiter):
        for j in range(col_limiter):
            image[init_row + i][init_col + j] = piece[i][j]


def average(image):

    """
    This function returns the averaged color of the pixels in the image.
    the function gets an input image as list of lists and returns a tuple
    contains 3 values: average of red, green and blue
    """

    red_sum = 0
    green_sum = 0
    blue_sum = 0
    pxl_num = len(image) * len(image[0])
    for row in image:
        for pxl in row:
            r, g, b = pxl
            red_sum += r
            green_sum += g
            blue_sum += b
    return red_sum / pxl_num, green_sum / pxl_num, blue_sum / pxl_num


def preprocess_tiles(tiles):

    """
    This function returns a list of the tiles with the averaged colors
    for each tile
    """

    avg = []
    for tile in tiles:
        avg.append(average(tile))
    return avg


def get_best_tiles(objective, tiles, averages , num_candidates):

    """
    This function returns a list of the tiles which their averaged
    color pixel is more similar to the averaged color pixel of the target
    image
    """

    candidates_list = []
    averages_list = copy.deepcopy(averages)
    pic_avg = average(objective)
    for candidate in range(num_candidates):
        best_index = choose_best_avg(averages_list, pic_avg)
        candidates_list.append(tiles[best_index])
        averages_list[best_index] = ALREADY_CHOSEN_TUPLE
    return candidates_list


def choose_best_avg(avg_list, obj_avg):

    """
    This function gets an input list of averages and calculates the
    index of the best average which is closest to the input averaged color
    of an image.
    this function helps us to implement the function: get_best_tiles
    """

    best_avg = compare_pixel(avg_list[0], obj_avg)
    best_index = 0
    for i, avg in enumerate(avg_list):
        if compare_pixel(avg, obj_avg) < best_avg:
            best_avg = compare_pixel(avg, obj_avg)
            best_index = i
    return best_index


def choose_tile(piece, tiles):

    """
    This function chooses the best tile from a list of tiles
    """

    distances_lst = []
    for tile in tiles:
        distance = compare(piece, tile)
        distances_lst.append(distance)
    best_tile = tiles[distances_lst.index(min(distances_lst))]
    return best_tile


def make_mosaic(image, tiles, num_candidates):

    """
    This function creates a photomosaic image by using the algorithm. the
    function gets an input image, an input list of tiles and an input int
    number of the tiles in the list which the best tile was chosen from
    """

    new_image = copy.deepcopy(image)
    one_tile = tiles[0]
    tile_height = len(one_tile)
    tile_width = len(one_tile[0])
    avg_list = preprocess_tiles(tiles)
    for row in range(0, len(image), tile_height):
        for column in range(0, len(image[0]), tile_width):
            image_piece = get_piece(new_image, (row, column),
                                    (tile_height, tile_width))
            best_tiles = get_best_tiles(image_piece, tiles,
                                        avg_list, num_candidates)
            best_tile = choose_tile(image_piece, best_tiles)
            set_piece(new_image, (row, column), best_tile)
    return new_image


def main():

    """
    This function runs the program and saves the solution in a file
    """

    image = load_image(sys.argv[1])
    tiles = build_tile_base(sys.argv[2], int(sys.argv[4]))
    new_image = make_mosaic(image, tiles, int(sys.argv[5]))
    save(new_image, sys.argv[3])

if __name__ == "__main__":
    if len(sys.argv) == 6:
        main()
    else:
        print(WRONG_NUMBER_OF_PARAMETER_MESSAGE)






import cv2
import math
# This script was ran on python 3.10.8 using opencv-python.

# img = cv2.imread("Roomplan_DK.png")

red = [30, 27, 153]  # marker color Fanaat (in BGR order, not RGB!)
yellow = [49, 215, 248]  # marker color Bellettrie (in BGR order, not RGB!)
green = [0, 255, 0]  # marker color Neutral (in BGR order, not RGB!)

# commented out debug stuff if you want to test if the function works
# print(type(img))
# print(img[0, 0])
# print(img[496, 294])  # red mark
# print(img[515, 294])  # Yellow mark


def compare_triplet(a, b) -> bool:
    """
    Spagetthi code function to compile arrays in a naive way
    :param a: First 1d array
    :param b: Second 1d array
    :return: true if the arrays are the same size and have the same values.
    """
    if len(a) == len(b):
        for m in range(0, len(a)):
            if not a[m] == b[m]:
                return False  # one of these array values is not equal
    else:
        return False  # size of arrays are not equal

    return True  # all appears to be equal


# commented out debug stuff if you want to test if the function works
# print(compare_triplet(red, red))
# print(compare_triplet(red, yellow))


def count_image(imname: str) -> list:
    """
    :param imname: The name of the image
    :return: a list of pixels containing the predefined colours of fanaat red, bellettrie yellow, rgb green or
    something different.
    """
    img = cv2.imread(imname)
    counters = [0, 0, 0, 0]  # red, yellow, green, other

    for i in range(0, img.shape[0]):  # Iterate over all rows
        for j in range(0, img.shape[1]):  # Iterate over each row entry
            for k in range(0, 2):
                if compare_triplet(img[i, j], red):
                    counters[0] += 1
                elif compare_triplet(img[i, j], yellow):
                    counters[1] += 1
                elif compare_triplet(img[i, j], green):
                    counters[2] += 1
                else:
                    counters[3] += 1
    return counters  # [Red count, yellow count, green count, other count]


# total space is 202.30 m^2 according to floorplan
total_space_pixels = count_image("usuable-area-only.png")[2]
# this variable is later used for consistency checking with other pictures

print("Total usuable area in pixels: {}".format(total_space_pixels))  # Output on my end is 1.447.164
print("Resolution per pixel: 202.30m^2 / {} pixels = {:.2f} cm^2/pixel".format(total_space_pixels, (202.3/total_space_pixels)*10000))  # output: 1.40 cm^2/pixel
print("Thus each pixel represents a square of {:.2f} cm each side \n".format(math.sqrt((202.3/total_space_pixels)*10000)))
# output: 1.18 cm or roughly 12 mm



def prettify_counters(counters: list):
    """
    Provides nice statistics tables from the raw numbers.
    :param counters: The 1d length 4 array of counters outputted by function count_image
    :return: Nothing
    """
    Fanaat_ratio_percentage = (counters[0] / (counters[0] + counters[1]))
    Bellettrie_ratio_percentage = (counters[1] / (counters[0] + counters[1]))
    print("Fanaat/Bellettrie Ratio: {0:.2%} / {1:.2%}".format(Fanaat_ratio_percentage, Bellettrie_ratio_percentage))

    total = (counters[0] + counters[1] + counters[2])
    Fanaat_total_percentage = (counters[0] / total)
    Bellettrie_total_percentage = (counters[1] / total)
    Shared_total_percentage = (counters[2] / total)

    if not total_space_pixels == total:
        CRED = '\033[91m'
        CEND = '\033[0m'
        print(CRED + f"Totals not equal! {total} pixels counted vs {total_space_pixels} expected" + CEND)

    print("Room Usage: \n-  Fanaat: {0:.2%} \n-  Bellettrie: {1:.2%} \n-  Shared: {2:.2%}\n".format(Fanaat_total_percentage,
                                                                                              Bellettrie_total_percentage,
                                                                                              Shared_total_percentage))


# commented out debug stuff if you want to test if the function works
# testrun_counts = count_image("current_room_state_no_safespace.png")
# print(testrun_counts)
# print(prettify_counters(testrun_counts))


def process_image(imname: str):
    print(imname)
    prettify_counters(count_image(imname))


process_image("current_closets_no_safespace.png")
process_image("current_closets_with_safespace.png")

process_image("alt_room_plan_alina_no_safespace.png")
process_image("alt_room_plan_alina_with_safespace.png")

process_image("alt_room_plan_fanaat_no_safespace.png")
process_image("alt_room_plan_fanaat_with_safespace.png")

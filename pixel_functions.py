import cv2
import math

red = [30, 27, 153]  # marker color Fanaat (in BGR order, not RGB!)
yellow = [49, 215, 248]  # marker color Bellettrie (in BGR order, not RGB!)
green = [0, 255, 0]  # marker color Neutral (in BGR order, not RGB!)

fanaat = 0
bellettrie = 1
shared = 2
unassigned = 3


def compare_colour(a, b) -> bool:
    """
    Naive code function to compare arrays in a naive way
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
            if compare_colour(img[i, j], red):
                counters[fanaat] += 1
            elif compare_colour(img[i, j], yellow):
                counters[bellettrie] += 1
            elif compare_colour(img[i, j], green):
                counters[shared] += 1
            else:
                counters[unassigned] += 1
    return counters  # [Red count, yellow count, green count, other count]


def prettify_counters(counters: list, latex_output: bool = False, imname:str = ""):
    """
    Provides nice statistics tables from the raw numbers.
    :param imname: Optional parameter required if latex_output is set to True.
    :param latex_output: if true also outputs data in a latex compatible format
    :param counters: The 1d length 4 array of counters outputted by function count_image
    :return: Nothing
    """

    Fanaat_ratio_percentage = (counters[fanaat] / (counters[fanaat] + counters[bellettrie]))
    Bellettrie_ratio_percentage = (counters[bellettrie] / (counters[fanaat] + counters[bellettrie]))
    if not latex_output: print("Fanaat/Bellettrie Ratio Exclusive: {0:.2%} / {1:.2%}".format(Fanaat_ratio_percentage, Bellettrie_ratio_percentage))

    total = (counters[fanaat] + counters[bellettrie] + counters[shared])
    if not latex_output: print("Fanaat/Bellettrie Ratio total room usage: {:.2%} / {:.2%}".format((counters[fanaat]+counters[shared])/total, (counters[bellettrie]+counters[shared])/total))
    Fanaat_total_percentage = (counters[fanaat] / total)
    Bellettrie_total_percentage = (counters[bellettrie] / total)
    Shared_total_percentage = (counters[shared] / total)

    if not latex_output: print("Room Usage: \n-  Fanaat: {0:.2%} \n-  Bellettrie: {1:.2%} \n-  Shared: {2:.2%}".format(Fanaat_total_percentage,
                                                                                                  Bellettrie_total_percentage,
                                                                                                  Shared_total_percentage))
    if not latex_output: print("Resolution per pixel: {:.3f} cm".format(math.sqrt(202.3/total)*100))

    if latex_output:
        print('''\\begin{{longtable}}[{{c}}]{{l|ll}}
            \\verb|{0}|  & Fanaat & Bellettrie \\\\ \\hline
            \\endfirsthead
            %
            \\endhead
            %
            Exclusive Ratio \\%  & {1:.2%}   & {2:.2%}       \\\\
            Total room usage \\% & {3:.2%}   & {4:.2%} \\\\

            \\caption{{Pixel counts on current layout floorplan before and after normalization and the percentile difference for each association.}}
            \\\\
            \\end{{longtable}} '''.format(imname, Fanaat_ratio_percentage, Bellettrie_ratio_percentage, (counters[fanaat]+counters[shared])/total, (counters[bellettrie]+counters[shared])/total))

        print('''
        Room usage:
        \\begin{{enumerate}}
        \\item  Fanaat: {:.2%}
        \\item Bellettrie: {:.2%}
        \\item Shared: {:.2%}
        \\end{{enumerate}}
        '''.format(counters[fanaat] / total, counters[bellettrie] / total, counters[shared] / total))


def process_image(imname: str, latex_output: bool = False):
    if not latex_output:
        print(imname)
    if latex_output:
        print('''
        \\begin{{figure}}[htp]
        \\center
        \\includegraphics[height=0.1\\pageheight]{{{0}}}
        \\caption{{{1}}}
        \\label{{fig:{0}}}
        \\end{{figure}}
        '''.format(imname, imname.replace("_", " ")))
        print("These tables relate to the picture in figure \\ref{{fig:{0}}}.".format(imname))
    prettify_counters(count_image(imname), latex_output, imname)
    print("\n")






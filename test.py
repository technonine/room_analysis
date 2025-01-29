from pixel_functions import *
img = cv2.imread("floorplan.png")

# stuff I wrote to explore imread
print(type(img))
print(img[0, 0])
print(img[565, 360])  # red mark
print(img[577, 360])  # Yellow mark

# stuff if you want to test if compare_colour works
print(compare_colour(red, red))
print(compare_colour(red, yellow))

# Exploration of picture resolution
# total space is 202.30 m^2 according to floorplan
counts_pixels = count_image("usuable-area-only.png")
total_space_pixels = counts_pixels[2]
# this variable is later used for consistency checking with other pictures

print(counts_pixels)
print("Total usuable area in pixels: {}".format(total_space_pixels))  # Output on my end is 1.447.164
print("Resolution per pixel: 202.30m^2 / {} pixels = {:.2f} cm^2/pixel".format(total_space_pixels, (202.3/total_space_pixels)*10000))  # output: 1.40 cm^2/pixel
print("Thus each pixel represents a square of {:.2f} cm each side \n".format(math.sqrt((202.3/total_space_pixels)*10000)))
# output: 1.18 cm or roughly 12 mm


# commented out debug stuff if you want to test if count_image and prettify_counters works
# Gives you raw numbers so you can run the math yourself if tempted
print("Pre Normalization")
print(count_image("current_closets_no_safespace_pre_normalization.png"))
print("Post Normalization")
testrun_counts = count_image("current_closets_no_safespace_normalized.png")
print(testrun_counts)
print(prettify_counters(testrun_counts))





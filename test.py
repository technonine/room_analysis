from pixel_functions import *
img = cv2.imread("floorplan.png")

# stuff I wrote to explore imread
print(type(img))
print(img[0, 0])
print(img[496, 294])  # red mark
print(img[515, 294])  # Yellow mark

# stuff if you want to test if compare_triplet works
print(compare_triplet(red, red))
print(compare_triplet(red, yellow))

# Exploration of picture resolution
# total space is 202.30 m^2 according to floorplan
total_space_pixels = count_image("usuable-area-only.png")[2]
# this variable is later used for consistency checking with other pictures

print("Total usuable area in pixels: {}".format(total_space_pixels))  # Output on my end is 1.447.164
print("Resolution per pixel: 202.30m^2 / {} pixels = {:.2f} cm^2/pixel".format(total_space_pixels, (202.3/total_space_pixels)*10000))  # output: 1.40 cm^2/pixel
print("Thus each pixel represents a square of {:.2f} cm each side \n".format(math.sqrt((202.3/total_space_pixels)*10000)))
# output: 1.18 cm or roughly 12 mm


# commented out debug stuff if you want to test if count_image and prettify_counters works
# Gives you raw numbers so you can run the math yourself if tempted
testrun_counts = count_image("current_room_state_no_safespace.png")
print(testrun_counts)
print(prettify_counters(testrun_counts))
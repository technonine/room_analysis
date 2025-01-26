from pixel_functions import process_image
from pixel_functions import count_image
# This script was ran on python 3.10.8 using opencv-python.

process_image("current_closets_no_safespace_pre_normalization.png")
process_image("current_closets_no_safespace_normalized.png")
process_image("current_closets_with_safespace.png")

process_image("alt_room_plan_vanilla_no_safespace.png")
process_image("alt_room_plan_vanilla_with_safespace.png")

process_image("alt_room_plan_cookie_dough_no_safespace.png")
process_image("alt_room_plan_cookie_dough_with_safespace.png")
process_image("alt_room_plan_cookie_dough_sprinkles_no_safespace.png")
process_image("alt_room_plan_cookie_dough_sprinkles_with_safespace.png")

process_image("alt_room_plan_fanaat_no_safespace.png")
process_image("alt_room_plan_fanaat_with_safespace.png")

print("Bellettrie is seating corners here and fanaat is big tables")
# so folk have raw pixel values in case they want to suggest different weights per category
print(count_image("usage-table-area.png"))
process_image("usage-table-area.png")

process_image("fifty_fifty_theory_distribution.png")
process_image("fifty_fifty_theory_distribution_w_safespace.png")

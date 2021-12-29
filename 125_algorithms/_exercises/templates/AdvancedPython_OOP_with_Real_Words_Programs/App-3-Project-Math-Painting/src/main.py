# ____ c.. _____ C..
# ____ s.. _____ R.. S..
#
# # Get canvas width and height from the user
# canvas_width  i.. i__ "Enter canvas width: "
# canvas_height  i.. i__ "Enter canvas height: "
#
# # Make a dictionary of color codes and prompt for color
# colors  "white": 255, 255, 255 "black" 0, 0, 0
# canvas_color  i__("Enter canvas color (white or black): ")
#
# # Create a canvas with the user data
# canvas  C..(heightcanvas_height, widthcanvas_width, colorcolors[canvas_color])
#
#
# w___ T...
#     shape_type  i__ "What do you like to draw? Enter quit to quit. "
#     # Ask for rectangle data and create rectangle if user entered 'rectangle'
#     __ shape_type.l.. __ "rectangle":
#         rec_x  i.. i__ "Enter x of the rectangle: "
#         rec_y  i.. i__ "Enter y of the rectangle: "
#         rec_width  i.. i__ "Enter the width of the rectangle: "
#         rec_height  i.. i__ "Enter the height of the rectangle: "
#         red  i.. i__ "How much red should the rectangle have? "
#         green  i.. i__ "How much green? "
#         blue  i.. i__ "How much blue? "
#
#         # Create the rectangle
#         r1  R..(xrec_x, yrec_y, heightrec_height, widthrec_width, color(red, green, blue))
#         r1.draw(canvas)
#
#     # Ask for square data and create square if user entered 'square'
#     __ shape_type.l.. __ "square":
#         sqr_x  i.. i__"Enter x of the square: "
#         sqr_y  i.. i__ "Enter y of the square: "
#         sqr_side  i.. i__ "Enter the side length of the square: "
#         red  i.. i__ "How much red should the square have? "
#         green  i.. i__ "How much green? "
#         blue  i.. i__ "How much blue? "
#         s1  S.. xsqr_x, ysqr_y, sidesqr_side c.. r.. g.. b..
#         ?.d.. c..
#
#     # Break the loop if user entered 'quit'
#     __ shape_type __ 'quit'
#         _____
#
# canvas.make('canvas.png')

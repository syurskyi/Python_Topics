# ____ t___ _______ O..
#
# _______ n.... __ np
#
#
# ___ convolution2D
#     image ?.a.. kernel ?.a.. padding O.. i.. N.. stride i.. 1
#  __ ?.a..
#     """Calculate the convolution between the input image and a filter, returning the feature map.
#
#     Args:
#         image (np.array): Input image as 2d array with height x width. Supposed to have equal dimensions.
#         kernel (np.array): Filter or kernel as 2d array with height x width. Supposed to have equal and odd dimensions.
#         padding (Optional[int]): Border around the image with pixels of value 0. If None, defaults to p = (f - 1) / 2.
#         stride (int): Step length to move the filter over the image. Defaults to 1.
#
#     Returns:
#         np.array: the feature map constructed from the image and the kernel.
#     """
#
#     arrays i.. k..
#     # assert that both are 2D numpy arrays
#     __ n.. a.. isi.. ? ?.n.. ___ array __ ?
#         r.. T..("image and kernel must be numpy arrays of dimension 2")
#
#     __ n.. a.. array.n.. __ 2 ___ ? __ ?
#         r.. V...("kernel and filter must be size 2")
#
#     is_not_integer l.... x| n.. isi.. ? i.. o. isi.. ? f__ a.. n.. ?.i..
#
#
#     __ n.. a.. a__.s.. 0 __ ?.s.. 1 ___ ? __ ?
#         r.. V...("Height must equal width for both kernel and image")
#
#
#     __ n.. a.. ?.i.. a__.d.. ?.n.. ___ ? __ ?
#         r.. T..("Kernel and image must contain only numeric values")
#
#
#
#     __ k__.s.. 0 % 2 __ 0
#         r.. V...("Kernel size must be odd")
#
#
#     __ k__.s.. 0 > i__.s.. 0
#         r.. V...("Kernel must be less than image size")
#
#
#
#     types ('padding','stride')
#     mins (0,1)
#     values  p.. s..
#
#
#     true_values   # list
#     ___ value type_ min_ __ z.. ? ? ?
#         __ ? __ n.. N..
#             __ i.. ?
#                 r.. T.. _* ? must be integer
#             __ n.. v.. >_ ?_
#                 r.. V... _* t.., must be greater than zero
#
#
#     stride i.. ? # inc ase they passed a value like 2.0
#
#
#     __ padding __ N..
#         p.. k__.s.. 0 - 1)//2
#     ____
#         p.. i.. ?
#
#
#
#     output_array_size i.. __.f.. i__.s.. 0 + 2 * p.. - k__.s.. 0/s.. + 1
#
#
#     output_array __.z.. ? * 2
#
#
#     image __.p.. i.. p..
#
#
#
#     rows cols   ?.s.. 0
#     kernel_size ?.s.. 0
#
#     output_row o.. 0
#
#     ___ row __ r.. 0 r.. s..
#         __ ? + k.. - 1) >_ r..
#             _____
#
#         ___ col __ r.. 0 c.. s..
#             __ ? +  k.. - 1) >_ c..
#                 _____
#
#
#             sum_ 0
#             ___ row_diff __ r.. k..
#                 current_row r.. + ?
#                 ___ col_diff __ r.. k..
#                     current_col c.. + c..
#
#                     sum_ += i.. c.. c.. * k.. r.. c..
#
#
#             o.. o.. o.. sum_
#             output_col +_ 1
#             __ ? >_ o..
#                 ? 0
#                 o.. +_ 1
#
#     r.. ?
#
# __ _______ __ _______
#     image __.a.. 1, 1, 1, 1, 1],
#            [1, 0, 0, 0, 1],
#            [1, 0, 0, 0, 1],
#            [1, 0, 0, 0, 1],
#            [1, 1, 1, 1, 1]])
#     kernel __.a.. 0.11111111, 0.11111111, 0.11111111],
#            [0.11111111, 0.11111111, 0.11111111],
#            [0.11111111, 0.11111111, 0.11111111]])
#     padding 0
#
#     print ? ? ? ?


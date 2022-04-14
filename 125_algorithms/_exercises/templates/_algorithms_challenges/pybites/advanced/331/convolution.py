____ t___ _______ O..

_______ n.... __ np


___ convolution2D
    image ?.a.. kernel ?.a.. padding O.. i.. N.. stride i.. 1
 __ ?.a..
    """Calculate the convolution between the input image and a filter, returning the feature map.

    Args:
        image (np.array): Input image as 2d array with height x width. Supposed to have equal dimensions.
        kernel (np.array): Filter or kernel as 2d array with height x width. Supposed to have equal and odd dimensions.
        padding (Optional[int]): Border around the image with pixels of value 0. If None, defaults to p = (f - 1) / 2.
        stride (int): Step length to move the filter over the image. Defaults to 1.

    Returns:
        np.array: the feature map constructed from the image and the kernel.
    """

    arrays i.. k..
    # assert that both are 2D numpy arrays
    __ n.. a.. isi.. ? ?.n.. ___ array __ ?
        r.. T..("image and kernel must be numpy arrays of dimension 2")

    __ n.. a.. array.n.. __ 2 ___ ? __ ?
        r.. V...("kernel and filter must be size 2")
        
    is_not_integer l.... x| n.. isi.. ? i.. o. isi.. ? f__ a.. n.. ?.i..
    
    
    __ n.. a.. a__.s.. 0 __ ?.s.. 1 ___ ? __ ?
        r.. V...("Height must equal width for both kernel and image")
    

    __ n.. a.. ?.i.. a__.d.. ?.n.. ___ ? __ ?
        r.. T..("Kernel and image must contain only numeric values")



    __ k__.s.. 0 % 2 __ 0
        r.. V...("Kernel size must be odd")


    __ k__.s.. 0 > i__.s.. 0
        r.. V...("Kernel must be less than image size")
    


    types ('padding','stride')
    mins (0,1)
    values  p.. s..

    
    true_values   # list
    ___ value,type_,min_ __ z.. ? ? ?
        __ value __ n.. N..
            __ is_not_integer ?
                r.. T..(f"{type_} must be integer")
            __ n.. value >_ min_:
                r.. V...(f"{type_}, must be greater than zero")
    

    stride i..(stride) # inc ase they passed a value like 2.0

             
    __ padding __ N..
        padding (kernel.s.. 0 - 1)//2
    ____
        padding i..(padding)



    output_array_size i..(np.f..((image.s.. 0 + 2 * padding - kernel.shape 0/stride + 1


    output_array np.zeros((output_array_size,) * 2)


    image np.pad(image,padding)

    

    rows cols =  image.s.. 0
    kernel_size kernel.s.. 0

    output_row output_col 0

    ___ row __ r..(0,rows,stride
        __ row + (kernel_size - 1) >_ rows:
            _____

        ___ col __ r..(0,cols,stride
            __ col + (kernel_size - 1) >_ cols:
                _____

            
            sum_ 0
            ___ row_diff __ r..(kernel_size
                current_row row + row_diff
                ___ col_diff __ r..(kernel_size
                    current_col col + col_diff

                    sum_ += image[current_row][current_col] * kernel[row_diff][col_diff]

            
            output_array[output_row,output_col] sum_
            output_col += 1
            __ output_col >_ output_array_size:
                output_col 0
                output_row += 1



    r.. output_array




__ _______ __ _______
    image np.array([[1, 1, 1, 1, 1],
           [1, 0, 0, 0, 1],
           [1, 0, 0, 0, 1],
           [1, 0, 0, 0, 1],
           [1, 1, 1, 1, 1]])
    kernel np.array([[0.11111111, 0.11111111, 0.11111111],
           [0.11111111, 0.11111111, 0.11111111],
           [0.11111111, 0.11111111, 0.11111111]])
    padding 0

    print(convolution2D(image,kernel,padding














____ typing _______ Optional

_______ numpy __ np


___ convolution2D(
    image: np.array, kernel: np.array, padding: Optional[i..] = N.., stride: i.. = 1
) __ np.array:
    """Calculate the convolution between the input image and a filter, returning the feature map.

    Args:
        image (np.array): Input image as 2d array with height x width. Supposed to have equal dimensions.
        kernel (np.array): Filter or kernel as 2d array with height x width. Supposed to have equal and odd dimensions.
        padding (Optional[int]): Border around the image with pixels of value 0. If None, defaults to p = (f - 1) / 2.
        stride (int): Step length to move the filter over the image. Defaults to 1.

    Returns:
        np.array: the feature map constructed from the image and the kernel.
    """

    arrays = (image,kernel)
    # assert that both are 2D numpy arrays
    __ n.. a..(isi..(array,np.ndarray) ___ array __ arrays):
        r.. T..("image and kernel must be numpy arrays of dimension 2")

    __ n.. a..(array.ndim __ 2 ___ array __ arrays):
        r.. ValueError("kernel and filter must be size 2")
        
    is_not_integer = l.... x: n.. isi..(x,i..) o. (isi..(x,float) a.. n.. x.is_integer())
    
    
    __ n.. a..(array.shape[0] __ array.shape[1] ___ array __ arrays):
        r.. ValueError("Height must equal width for both kernel and image")
    

    __ n.. a..(np.issubdtype(array.dtype,np.number) ___ array __ arrays):
        r.. T..("Kernel and image must contain only numeric values")



    __ kernel.shape[0] % 2 __ 0:
        r.. ValueError("Kernel size must be odd")


    __ kernel.shape[0] > image.shape[0]:
        r.. ValueError("Kernel must be less than image size")
    


    types = ('padding','stride')
    mins = (0,1)
    values = (padding,stride)

    
    true_values =[]
    ___ value,type_,min_ __ z..(values,types,mins):
        __ value __ n.. N..
            __ is_not_integer(value):
                r.. T..(f"{type_} must be integer")
            __ n.. value >= min_:
                r.. ValueError(f"{type_}, must be greater than zero")
    

    stride = i..(stride) # inc ase they passed a value like 2.0

             
    __ padding __ N..
        padding = (kernel.shape[0] - 1)//2
    ____:
        padding = i..(padding)



    output_array_size = i..(np.floor((image.shape[0] + 2 * padding - kernel.shape[0])/stride + 1))


    output_array = np.zeros((output_array_size,) * 2)


    image = np.pad(image,padding)

    

    rows = cols =  image.shape[0]
    kernel_size = kernel.shape[0]

    output_row = output_col = 0

    ___ row __ r..(0,rows,stride):
        __ row + (kernel_size - 1) >= rows:
            break

        ___ col __ r..(0,cols,stride):
            __ col + (kernel_size - 1) >= cols:
                break

            
            sum_ = 0
            ___ row_diff __ r..(kernel_size):
                current_row = row + row_diff
                ___ col_diff __ r..(kernel_size):
                    current_col = col + col_diff

                    sum_ += image[current_row][current_col] * kernel[row_diff][col_diff]

            
            output_array[output_row,output_col] = sum_
            output_col += 1
            __ output_col >= output_array_size:
                output_col = 0
                output_row += 1



    r.. output_array




__ __name__ __ "__main__":
    image = np.array([[1, 1, 1, 1, 1],
           [1, 0, 0, 0, 1],
           [1, 0, 0, 0, 1],
           [1, 0, 0, 0, 1],
           [1, 1, 1, 1, 1]])
    kernel = np.array([[0.11111111, 0.11111111, 0.11111111],
           [0.11111111, 0.11111111, 0.11111111],
           [0.11111111, 0.11111111, 0.11111111]])
    padding = 0

    print(convolution2D(image,kernel,padding))














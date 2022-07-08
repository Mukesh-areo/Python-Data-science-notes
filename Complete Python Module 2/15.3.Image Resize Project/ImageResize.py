'''
Company: iNeuron
Author: Ravi Chaurasia
'''

## Importing important used library
from pil import Image
import fnmatch
import os


## Function to resize and rename the images
def image_processing(im_name, i, f, in_folder, out_folder):
    ## Assigning new name
    new_im_name = 'Image_' + str(i) + f

    ## the orignal image name from Folder
    image = Image.open(in_folder + f'/{im_name}')

    ## Size of the image in pixels (size of orginal image is not mandatory to check)
    width, height = image.size
    print(f'Orignal size ({width},{height})')

    ## Resize the Image
    image = image.resize(newsize)

    ## Save image to a specified folder
    image.save(out_folder + f'/{new_im_name}')

    ## Checking new resize Image
    width, height = image.size

    ## Printing completed statement
    print(f'{im_name} is renamed to {new_im_name} with size ({width},{height})')


if __name__ == '__main__':

    ## Input folder name
    in_folder = 'Images'

    ## Output folder name
    out_folder = 'ResizedImages'

    ## Create if no output folder exist
    if not os.path.exists(out_folder):
        os.makedirs(out_folder)

    ## List of images with extension pf .jpg
    im_names = [f for f in os.listdir(os.getcwd() + '\\' + in_folder) if fnmatch.fnmatch(f, '*.jpg')]

    ## Specify resizing size (width, height)
    newsize = (1200, 800)

    ## Intilize image number
    i = 1

    ## Output image format
    format_name = '.png'

    ## Iterating over Input image list
    for im in im_names:
        ## Calling image processing function
        image_processing(im, i, format_name, in_folder, out_folder)

        ## image number increment
        i += 1

    print(84*'-'+'\nImage Resizing Complete')
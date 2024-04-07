"""A simple script to resize jpg, jpeg and png image files"""


from PIL import Image
import os


def image_name():
    """
    Prompts the user for an image file name and returns it.
    """
    image_name = input("Kindly input the image file name: ")
    if not image_name:
        print("Kindly input an image filename to resize. \nIf the file is in a different directory, input an absolute path.")
        return
    return image_name


def image_size():
    """
    Prompts the user for the size they want the image to be resized to.
    """
    image_size = input("Kindly input the image size you want (e.g., 200*200): ")
    dimensions = image_size.split("*")
    if len(dimensions) != 2:
        print("Please input a valid image size in the format 'length * breadth'.")
        return None
    
    try:
        l, b = map(int, dimensions)
        return l, b
    except ValueError:
        print("Please input valid integer values for the image size.")
        return None


def image_newname():
    """
    Prompts the user for a new name for the resized image file and returns it.
    """
    image_name = input("Kindly input a new name for the resized image file: ")
    if not image_name:
        print("Kindly input a new name for the resized image file!!!")
        return
    return image_name


def image_resizer(image_name, image_size, image_newname):
    """
    Resizes the image to the specified size if it's not already that size.
    Saves the resized image with a filename prefixed by 'resized_'.
    """
    try:
        file_extensions = [".jpg", ".png", ".jpeg"]
        new_name_path = ""

        for extension in file_extensions:
            image_path = f"{image_name}{extension}"
            if os.path.isfile(image_path):
                new_name_path = f"{image_newname}{extension}"
                break

        if new_name_path:
            try:
                with Image.open(image_path) as im:
                    if im.size != image_size:
                        new_im = im.resize(image_size)
                        if os.path.isfile(new_name_path):
                            os.remove(new_name_path)
                            print(f"Existing {new_name_path} has been deleted.")
                        new_im.save(new_name_path)
                        print(f"{new_name_path} resized and saved successfully.")
                    else:
                        print(f"{image_path} already has a resolution of {image_size[0]}x{image_size[1]}.")
            except FileNotFoundError:
                print(f"Error: File '{image_path}' not found.")
    except Exception as e:
        print(f"An error occurred: {str(e)}")


if __name__ == "__main__":
    image_to_resize = image_name()
    image_size = image_size()
    image_newname = image_newname()
    if image_to_resize and image_size:
        image_resizer(image_to_resize, image_size, image_newname)
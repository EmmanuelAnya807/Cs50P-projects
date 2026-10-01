import sys
import os
from PIL import Image, ImageOps


def main():
    # Execute the program pipeline step-by-step
    image_input, image_output = command_line_arg()
    check_image = check_image_file(image_input, image_output)
    if check_image:
        combine_image(image_input, image_output)


def command_line_arg():
    """Validate command-line arguments and return the target file path."""

    # Ensure exactly two arguments (input and output file paths) are provided
    if len(sys.argv) == 3:
        image_input = sys.argv[1]
        image_output = sys.argv[2]
        return image_input, image_output

    # Terminate if the user provided too few arguments
    elif len(sys.argv) < 3:
        sys.exit("Too few command-line arguments.")

    # Terminate if the user provided too many arguments
    else:
        sys.exit("Too many command-line arguments.")


def check_image_file(image_input, image_output):

    """Verify that both files have valid and matching image extensions."""

    # Split the file paths to isolate their extensions
    root1, ext1 = os.path.splitext(image_input)
    root2, ext2 = os.path.splitext(image_output)
    ext1 = ext1.lower()
    ext2 = ext2.lower()
    extensions = [".jpg", ".jpeg", ".png"]

    # Check if the input file has a valid image extension
    if ext1 in extensions:
        # Check if the output file has a valid image extension
        if ext2 in extensions:
            # Ensure both the input and output extensions match
            if ext1 == ext2:
                return True

            else:
                sys.exit("Input and output have different extensions.")

        else:
            sys.exit("Invalid output.")

    else:
        sys.exit("Invalid input.")


def combine_image(image_to_read, image_to_save):
    """Resize and crop the input image to fit the overlay shirt, then save the result."""
    try:
        # Open both the input image and the overlay shirt
        image = Image.open(image_to_read)
        shirt = Image.open("shirt.png")

        # Use the shirt's size as the target dimensions
        size = shirt.size

        # Crop and resize the input image to match the target size
        fitted_image = ImageOps.fit(image, size, Image.BICUBIC, 0, (0.5, 0.5))

        # Overlay the transparent shirt onto the fitted background image
        fitted_image.paste(shirt, shirt)

        # Save the combined image to the target destination
        fitted_image.save(image_to_save)

    except FileNotFoundError:
        # Terminate if the input image or shirt template cannot be found
        sys.exit(f"{image_to_read} does not exist.")


if __name__ == "__main__":
    main()

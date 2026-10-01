def main():
    """Collects a file name from the user and calls the file_type function.
    """

    file_name = input("File name: ")
    file_type(file_name)


def file_type(file_format):
    """Determines a file's type based on its format.
    """

    # Extracts the file extension from the file name
    extension = file_format.split(".")[-1]

    # Convert to lowercase for case-insensitive comparison
    extension = extension.lower()

    # Removes leading and trailing whitespace
    extension = extension.strip()

    # A dictionary mapping file extensions to MIME types
    mime_types = {
        "jpg": "image/jpeg",
        "jpeg": "image/jpeg",
        "png": "image/png",
        "pdf": "application/pdf",
        "txt": "text/plain",
        "zip": "application/zip",
        "gif": "image/gif"
    }

    # Print the MIME type for the file extension, or a default if not found
    print(mime_types.get(extension, "application/octet-stream"))


main()

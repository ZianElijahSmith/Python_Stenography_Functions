'''
These three functions below are for .png files that have 3 channel bands.
They have been tested and worked on the following image:
https://upload.wikimedia.org/wikipedia/commons/6/6a/PNG_Test.png


They were not made for jpg.

They have not been tested on an image with 4 channel bands
If an image has 4, it means it has an 'alpha channel'
See this URL to learn more of what that means:
https://www.makeuseof.com/tag/alpha-channel-images-mean/

The image must be in RGB mode.
To find the mode, do...

from PIL import Image
img = Image('/path/to/image')
print(img.mode)


embed will take a file and a message, and embed the message into the file.
decode takes a file and extracts the message.
erase will remove the message from the image.

Hope you learn something new and have fun!
'''

from PIL import Image

#embed does what the name implies, it will take a message and embed it into the image.
def embed(path_to_file, message):
    '''
    Embeds a message into a png image.
    png image must not have an alpha channel.
    png image must be in RGB mode.
    '''
    # Open the image and convert it to RGB mode
    img = Image.open(path_to_file).convert('RGB')
    # Convert the message to binary
    # List comprehension is used to make sure
    # Every byte of data is converted to its 8-bit binary code using ASCII values.
    # This is why we have "08b"
    binary_message = ''.join([format(ord(char), "08b") for char in message])
    # Calculate the maximum length of the message that can be embedded
    # This is a standard formula that, as far as I know
    # Applies to all images, I could be wrong.
    max_message_length = img.size[0] * img.size[1] * 3 // 8
    # Check if the message is too long to embed
    if len(binary_message) > max_message_length:
        raise ValueError("Message is too large to embed in image")
    # The line pixels = img.load() in the embed and decode functions creates an instance of the PixelAccess class, which is used to access and manipulate the pixels of the image.

    # img.load() will create an instance of the PixelAccess class
    # which is used to access and manipulate the pixels of the image.
    
    # The PixelAccess class is a low-level interface for accessing pixel data in an image, 
    # and it provides a more efficient way to read and write pixel data than using the 
    # getpixel() and putpixel() methods of the Image class. ( I didn't know this until recently)
    
    # A PixelAccess object allows you to access the pixel data in the image as a 2-dimensional array of tuples, 
    # where each tuple represents the RGB color values of a single pixel.
    
    # For example, pixels[i, j] retrieves the color values of the pixel at position (i, j) in the image. 
    # You can also modify the color values of a pixel by assigning a new tuple of color values to pixels[i, j].
    pixels = img.load()
    
    # We initalize a count at zero so we can keep count of how many bits of data
    # have been embedded into the image
    count = 0

    # This will iterate over the x-axis of the image
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            # Get the color values for each pixel
            color_values = pixels[i, j]
            # Embed one bit of the message in each color value
            for k in range(len(color_values)):
                if count < len(binary_message):
                    color_values = list(color_values)
                    color_values[k] = int(bin(color_values[k])[:-1] + binary_message[count], 2)
                    count += 1
            # Update the pixel with the modified color values
            pixels[i, j] = tuple(color_values)
            if count >= len(binary_message):
                break
        if count >= len(binary_message):
            break
    # Save the modified image
    img.save(path_to_file)

# decode will give you the message embedded into an image
def decode(file_to_decode):
    # Open the image and convert it to RGB mode
    img = Image.open(file_to_decode).convert('RGB')
    # Decode the message from the image
    pixels = img.load()
    binary_message = ""
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            # Get the color values for the pixel
            color_values = pixels[i, j]
            # Extract one bit of the message from each color value
            for k in range(len(color_values)):
                binary_message += bin(color_values[k])[-1]
    # Convert the binary message back to text
    message = ""
    for i in range(0, len(binary_message), 8):
        message += chr(int(binary_message[i:i+8], 2))
        if message[-1] == "\0":
            break
    return message[:-1]
  
  # erase will remove the message embedded into an image
  def erase(path_to_file):
    img = Image.open(path_to_file)
    pixels = img.load()
    for i in range(img.size[0]):
        for j in range(img.size[1]):
            color_values = pixels[i, j]
            for k in range(len(color_values)):
                binary_value = bin(color_values[k])[2:].zfill(8)
                if binary_value[-1] == '1':
                    binary_value = binary_value[:-1] + '0'
                    color_values = list(color_values)
                    color_values[k] = int(binary_value, 2)
            pixels[i, j] = tuple(color_values)
    img.save(path_to_file)


# Note that this code assumes that the input image is in RGB mode. If the image is in a different mode, you may need to convert it to RGB mode before running the embed function.

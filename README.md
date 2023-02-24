# Python_Stenography_Functions
At the moment, this repository has 3 python functions to do stenography on .png files with no alpha channel and in RGB mode.
<br /><br />
embed(path_to_file, message)<br />
decode(path_to_file)<br />
erase(path_to_file)<br />

I plan to add some more later and this repo is a living repo.
Notes and URLs will be added to aid the reader in learning about stenography.

The purpose of this repository is to both provide useful functions, and to teach coders about stenography.

# Release Notes
The (PNG + RGB + Image Channels == 3) test worked!
Tested on Python 3.7.3 (default, Oct 31 2022, 14:04:00) \n[GCC 8.3.0])
The code was tested on the following image on this URL: https://upload.wikimedia.org/wikipedia/commons/6/6a/PNG_Test.png
<br /><br />
Screenshot of successful test is below
<img height="" width="" src="https://raw.githubusercontent.com/ZianElijahSmith/Python_Stenography_Functions/main/test1.png" />
<br /><br />

# Learning Notes
<ol>
<li>PNG files tend to be easier to work with than JPG because PNG has "lossless compression".</li>
<li> This code works for images with three channels.
<br />you can check how many channels an image has with:
<br />
from PIL import Image
<br />
img = Image.open(path_to_file)
<br />
print(img.size)
<br />
print(len(img.getbands()))
<br />

If the len(img.getbands()) is 4, the image has an "alpha channel"
<br />
Read this URL to learn more of what an "alpha channel" is:
<br />
https://www.makeuseof.com/tag/alpha-channel-images-mean/
</li>
<li>max_message_length = (img.size[0] * img.size[1] * 3) // 8</li>
<li>The png image must be in RGB mode
<br />
Read this URL to learn more:
<br />
https://www.howtogeek.com/42393/rgb-cmyk-alpha-what-are-image-channels-and-what-do-they-mean/
</li>
</ol>


# Learning Resources
<ol>
<li>https://www.geeksforgeeks.org/image-based-steganography-using-python/</li>
</ol>

<br />
<br />

# Speical Thanks
Thank you to Pillow! 
https://pillow.readthedocs.io/en/stable/


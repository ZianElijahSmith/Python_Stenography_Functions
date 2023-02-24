# Python_Stenography_Functions
At the moment, this repository has python functions to do stenography on .png files with no alpha channel and in RGB mode.

I plan to add some more later and this repo is a living repo.
Notes and URLs will be added to aid the reader in learning about stenography.

The purpose of this repository is to both provide useful functions, and to teach coders about stenography.

# Release Notes
The (PNG + RGB + Image Channels == 3) test worked!
The code was tested on the following image: https://upload.wikimedia.org/wikipedia/commons/6/6a/PNG_Test.png
<br />
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
<li>The png image must be in RGB mode</li>
</ol>



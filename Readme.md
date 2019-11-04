I am referring to this link to combine multiple images into one :

https://www.toptal.com/opencv/python-image-processing-in-computational-photography

```combine_images.py``` is a script which combines all low resolution photos inside the 'source_folder' and writes them into output 'result.png'

Next step is 

1) Train a GAN which takes result.png as a lowresimage and HR.png as a high res image 

and learns how to fill in the details between them.

## Intoduction

I am referring to this link to combine multiple images into one :

https://www.toptal.com/opencv/python-image-processing-in-computational-photography

```combine_images.py``` is a script which combines all low resolution photos inside the 'source_folder' and writes them into output 'result.png'

Next step is 

1) Train a GAN which takes result.png as a lowresimage and HR.png as a high res image 

   and learns how to fill in the details between them.


## Personal Research

I dont know how to code GAN from start to finish so here is all the literature I have learned to understand GAN better:

### What is regularization in machine learning?

Orignal answer posted on (https://www.quora.com/What-is-regularization-in-machine-learning) by Prasoon Goyal

For any machine learning problem, essentially, you can break your data points into two components — pattern + stochastic noise.
For instance, if you were to model the price of an apartment, you know that the price depends on the area of the apartment, no. of bedrooms, etc. So those factors contribute to the pattern — more bedrooms would typically lead to higher prices. However, all apartments with the same area and no. of bedrooms do not have the exact same price. The variation in price is the noise.
>> Now the goal of machine learning is to model the pattern and ignore the noise. Anytime an algorithm is trying to fit the noise >> in addition to the pattern, it is overfitting.

You want your model to only fit the pattern in the data, not the noise, because noise is stochastic, and using it for decision making would be detrimental to performance on unseen data. And we see that regularization is a way to prevent overfitting

For remedy of over-fitting regularization techniques are added along with the parameters. Two most important regularization techniques in machine learning are: Dropout and Batch Normalization

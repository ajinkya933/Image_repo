## Intoduction

I am referring to this link to combine multiple images into one :

https://www.toptal.com/opencv/python-image-processing-in-computational-photography

```combine_images.py``` is a script which combines all low resolution photos inside the 'source_folder' and writes them into output 'result.png'

Next step is 

1) Train a GAN which takes result.png as a lowresimage and HR.png as a high res image 

   and learns how to fill in the details between them.


## Personal Research

I dont know how to code GAN from start to finish so here is all the literature I have learned to understand GAN better:

> What is regularization in machine learning?

Orignal answer posted on (https://www.quora.com/What-is-regularization-in-machine-learning) by Prasoon Goyal

For any machine learning problem, essentially, you can break your data points into two components — pattern + stochastic noise.
For instance, if you were to model the price of an apartment, you know that the price depends on the area of the apartment, no. of bedrooms, etc. So those factors contribute to the pattern — more bedrooms would typically lead to higher prices. However, all apartments with the same area and no. of bedrooms do not have the exact same price. The variation in price is the noise.
>> Now the goal of machine learning is to model the pattern and ignore the noise. Anytime an algorithm is trying to fit the noise >> in addition to the pattern, it is overfitting.

You want your model to only fit the pattern in the data, not the noise, because noise is stochastic, and using it for decision making would be detrimental to performance on unseen data. And we see that regularization is a way to prevent overfitting

For remedy of over-fitting regularization techniques are added along with the parameters. Two most important regularization techniques in machine learning are: Dropout and Batch Normalization


I am referring to this paper: https://arxiv.org/pdf/1903.00440.pdf  for image enhancemet

In an attempt to solve the problem of understanding layers of NN. I needed to solve this question :
Q) https://datascience.stackexchange.com/questions/62689/what-is-difference-between-cv2-filter2d-vs-keras-conv2d-function

I came to know what is Conv2D using the above link but one more question arized in my mind that, after applying multiple filters to an image using Conv2D why was it needed to add an activation function. I came to know that without non linear activation functions the Neural Network looses its value, if you remove activation function from neural network then it just becomes a 1-1 mapping algorithm which maps inputs to outputs.

I am not satisfied with the above definitions of Conv2D and activation function, they only partially clear my questions. I need to visualize this to get a clear understanding : I found this link useful to visualize (https://towardsdatascience.com/visualizing-intermediate-activation-in-convolutional-neural-networks-with-keras-260b36d60d0)

You can also use the following Github library to visualize activations:
https://github.com/philipperemy/keract

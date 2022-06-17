import torch
import numpy as np
from torchvision import datasets, transforms
from background import 

def get_foreground_target_and_background_set(IMAGE_PATH):
  train_set = datasets.FashionMNIST(root='./data/FashionMNIST', train=True, download=True, transform=transforms.ToTensor())
  target_index = np.where((train_set.targets==1) | (train_set.targets==7))[0] # we will deal with only two classes
  foreground = train_set.data[target_index, :, :][:5000]
  target_labels = train_set.targets[target_index][:5000]
  
  fish_images = (IMAGE_PATH)
  
  np.random.seed(0) 

  rand_indices =  np.random.permutation(natural_images.shape[0]) # shuffling indices
  split = int(len(rand_indices)/2)
  target_indices = rand_indices[0:split] # indices for images to be superimposed on target
  background_indices = rand_indices[split:] # indices for background dataset

  target = np.zeros(foreground.shape) # 5000 * 28 * 28
  target = target.reshape((5000, 1, 784))
  background = np.zeros(foreground.shape)
  background = background.reshape((5000, 1, 784))
  for i in range(target.shape[0]): # 5000 times
    idx = np.random.choice(target_indices)
    loc = np.random.randint(70, size=(2)) # a random region in the image
    superimposed_patch = np.reshape(np.reshape(natural_images[idx,:],[100,100])[loc[0]:loc[0]+28,:][:,loc[1]:loc[1]+28] ,[1,784])    
    target[i] = (0.0009*foreground[i]).reshape(1,784) + (superimposed_patch)
    
    idx = np.random.choice(background_indices) # randomly pick a image 
    loc = np.random.randint(70,size=(2)) # randomly pick a region in the image
    background_patch = np.reshape(np.reshape(fish_images[idx,:],[100,100])[loc[0]:loc[0]+28,:][:,loc[1]:loc[1]+28] ,[1,784])    
    background[i] = (background_patch)
  return foreground, target, background

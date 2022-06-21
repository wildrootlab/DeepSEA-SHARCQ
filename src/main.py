import imageRegestration.mappings.NBB as NBB
from PIL import Image

import matplotlib.pyplot as plt

def main():

    atlas = Image.open("adapters/neural_best_buddies/images/Atlas.png").convert('RGB')
    brain = Image.open('adapters/neural_best_buddies/images/TestBrainSection2.png').convert('RGB')

    nbb = NBB.NeuralBestBuddies(100)
    nbb.find_mapping(atlas, brain)

    plt.imshow(nbb.img)
    plt.show()
    

if __name__ == '__main__':
    main()
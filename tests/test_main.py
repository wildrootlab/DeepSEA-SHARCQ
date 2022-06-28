from deepseasharcq.imageRegestration.mappings import NBB as NBB
from PIL import Image
import matplotlib.pyplot as plt


def test_main():
    atlas = Image.open("./src/adapters/neural_best_buddies/images/Atlas.png").convert('RGB')
    brain = Image.open('./src/adapters/neural_best_buddies/images/TestBrainSection2.png').convert('RGB')

    nbb = NBB.NeuralBestBuddies(100)
    nbb.find_mapping(atlas, brain)

    plt.imshow(nbb.img)
    plt.show()

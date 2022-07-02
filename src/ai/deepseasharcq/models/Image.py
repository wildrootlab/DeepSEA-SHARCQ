import numpy as np

class Image:
    '''
    data : [width, height, channel]
    '''

    def __init__(self, data: "np.array") -> None:
        
        self.__image = data

        self.height = data.shape[1]
        self.width = data.shape[0]
        self.channels = data.shape[2]
    
    def get_image(self):
        return self.__image
    
    def get_image_tf(self):
        return np.expand_dims(self.__image, axis=0)
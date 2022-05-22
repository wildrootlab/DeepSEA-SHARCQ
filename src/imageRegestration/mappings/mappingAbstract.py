from abc import abstractclassmethod, abstractproperty
import numpy as np

from imageRegestration.transforms.transformAbstract import Transform


class Mapping:
    '''
    Mapping:
        Abstract class for mapping one image to another image

    Notes:
        When defining a class with this abstract, you write the logic for how transforms are configured and setup, this is for freedom of use of transforms.
        You also will immplement the mapping methods for how the image are mapped, this could be landmark, deformation, etc...
    '''

    @abstractproperty
    def getTransform(self) -> "Transform":
        return NotImplemented

    @abstractclassmethod
    def find_mapping(self, imageA: "np.Array", imageB: "np.Array") -> bool:
        return NotImplemented
    
    @abstractclassmethod
    def preformTransform_image(self, image: "np.Array") -> "np.Array":
        return NotImplemented

    @abstractclassmethod
    def preformTransform_point(self, points: "np.Array") -> "np.Array":
        return NotImplemented
import numpy as np

from models.points import Points

from .mappingAbstract import Mapping
from src.adapters.NBB_adapter import NBB_Adapter

from transforms.nonLinearTriangle import Triangle_transform

class NeuralBestBuddies(Mapping):
    def __init__(self, num_landmarks) -> None:
        super().__init__()
        self.num_landmarks = num_landmarks
    

    def find_mapping(self, imageA: "np.Array", imageB: "np.Array") -> bool:
        
        #Run NBB
        A_cors, B_cors = NBB_Adapter(imageA, imageB)
        
        #map from NBB back to orginal space
        A_cors[:,1] = imageA.shape[1]*(A_cors[:, 1]/224)
        A_cors[:,0] = imageA.shape[0]*(A_cors[:, 0]/224)

        B_cors[:,1] = imageB.shape[1]*(B_cors[:, 1]/224)
        B_cors[:,0] = imageB.shape[0]*(B_cors[:, 0]/224)
        
        #construct triangle transform
        self.__Transform = Triangle_transform(imageB.shape)

        #build transform
        self.__Transform.buildTransform(telemetry=[A_cors, B_cors], imga=imageA, imgb=imageB)

        return True

    def preformTransform_image(self, image: "np.Array") -> "np.Array":
        return self.__Transform.preformTransform(None, return_final_image=True)


    def preformTransform_point(self, points: "Points") -> "np.Array":
        return self.__Transform.preformTransform(None, return_final_image=True)


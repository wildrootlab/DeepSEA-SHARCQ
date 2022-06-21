import numpy as np

from models.points import Points

from .mappingAbstract import Mapping
from adapters.NBB_adapter import NBB_Adapter

from src.imageRegestration.transforms.nonLinearTriangle import Triangle_transform #transforms.nonLinearTriangle import Triangle_transform

class NeuralBestBuddies(Mapping):
    def __init__(self, num_landmarks) -> None:
        super().__init__()
        self.num_landmarks = num_landmarks
    

    def find_mapping(self, imageA: 'np.array', imageB: 'np.array') -> bool:
        
        #Run NBB
        A_cors, B_cors, transform = NBB_Adapter(imageA, imageB, -1)
        
        

        #map from NBB back to orginal space

        A_cors = np.array(A_cors)
        B_cors = np.array(B_cors)

        print(A_cors, B_cors)

        # A_cors[:,1] = imageA.size[1]*(A_cors[:, 1]/224)
        # A_cors[:,0] = imageA.size[0]*(A_cors[:, 0]/224)

        # B_cors[:,1] = imageB.size[1]*(B_cors[:, 1]/224)
        # B_cors[:,0] = imageB.size[0]*(B_cors[:, 0]/224)
        
        #construct triangle transform
        self.__Transform = Triangle_transform

        #build transform
        # warp = cv2.resize(imageA, [224, 224])
        # self.img, self.vxy = transform(np.asarray(imageA), A_cors, B_cors)


        

        return True

    def preformTransform_image(self) -> "np.Array":
        return self.img


    def preformTransform_point(self, points: "Points") -> "np.Array":
        
        transformed = []
        for p in  points.get_points:
            transformed += [[p.x + self.vxy[p.x, p.y, 0], p.y + self.vxy[p.x, p.y, 1]]]

    def getTransform(self):
        return self.__Transform
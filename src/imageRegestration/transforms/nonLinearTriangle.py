import cv2
import numpy as np

from transformAbstract import Transform
from models.points import Points
from typing import List

class Triangle_transform(Transform):
    
    #support functions
    def __init__(self, size) -> None:
        super().__init__()

        rect = (0, 0, size[1], size[0])
        self.subdiva = cv2.Subdiv2D(rect)

        corners = np.array([
                    [0,0],
                    [size[0]-1,0],
                    [size[0]-1,size[1]-1],
                    [0,size[1]-1],
        ])

        for p in corners:
            self.subdiva.insert(p)

    def delaunay_transform(self, imgb, imga, subdiv, mapping) :

        triangleList = subdiv.getTriangleList()

        final_ouput = np.zeros_like(imgb)

        triangle_contours = []
        triangle_transform = []

        for t in triangleList :

            pt11 = (int(t[0]), int(t[1]))
            pt21 = (int(t[2]), int(t[3]))
            pt31 = (int(t[4]), int(t[5]))


            pt12 = mapping[pt11]
            pt22 = mapping[pt21]
            pt32 = mapping[pt31]
            

            tri_1 = np.array([
                    pt11,
                    pt21,
                    pt31      
            ],dtype=np.float32)

            triangle_contours += [tri_1]

            tri_2 = np.array([
                    pt12,
                    pt22,
                    pt32                          
            ],dtype=np.float32)


            rect1 = cv2.boundingRect(tri_1)
            (x, y, w, h) = rect1
            x1 = x
            y1 = y
            cropped_triangle = imga[y: y + h, x: x + w]
            cropped_tr1_mask = np.zeros((h, w), np.uint8)
            
            points = np.array([[pt11[0] - x, pt11[1] - y],
                                [pt21[0] - x, pt21[1] - y],
                                [pt31[0] - x, pt31[1] - y]], np.int32)

            cv2.fillConvexPoly(cropped_tr1_mask, points, 255)


            cropped_triangle = cv2.bitwise_and(cropped_triangle, cropped_triangle, mask = cropped_tr1_mask)


            rect2 = cv2.boundingRect(tri_2)
            (x, y, w, h) = rect2
            x2 = x
            y2 = y
            cropped_triangle2 = imgb[y: y + h, x: x + w]
            cropped_tr2_mask = np.zeros((h, w), np.uint8)
            points2 = np.array([[pt12[0] - x, pt12[1] - y],
                            [pt22[0] - x, pt22[1] - y],
                            [pt32[0] - x, pt32[1] - y]], np.int32)
            
            

            points = np.float32(points)
            points2 = np.float32(points2)

            M = cv2.getAffineTransform(points, points2)
            
            triangle_transform += [(M, (x1, y1), (x2, y2))]   

            warped_triangle = cv2.warpAffine(cropped_triangle, M, (w, h))


            final_ouput[y: y + h, x: x + w] =  cv2.add(final_ouput[y: y + h, x: x + w], warped_triangle)


        return triangle_contours, triangle_transform, final_ouput
    
    def preform_triangle_affine(point, triangle_contour_set, triangle_transform):
  
        transformed_points = []

        # check if point is in triangle, then transform if so
        for p in point:
            for i , c in enumerate(triangle_contour_set):
            
            # print(cv2.pointPolygonTest(c, tuple(p), False))

                if cv2.pointPolygonTest(c, tuple(p), False) == 1:

                    ones = np.ones(shape=(1, 1))

                    p = p.reshape(1,-1) - np.array(triangle_transform[i][1])

                    points_ones = np.hstack([p, ones])

                    transformed_points += [(triangle_transform[i][0]).dot(points_ones.T).T.reshape(2) + np.array(triangle_transform[i][2])]
                    break
            
            
        return transformed_points


    # Abstract methods    
    def buildTransform(self, telemetry: List['Points'], imga: 'np.array', imgb: 'np.array'):
        
        for p in telemetry[0].to_numpy():
            self.subdiva.insert(p)
        
        mapping = {tuple(p1[::-1]):telemetry[0][i,::-1] for i, p1 in enumerate(telemetry[1])}
        self.contours, self.transform, self.final_ouput = self.delaunay_transform(imga.copy(), imgb.copy(), self.subdiva.subdivb, mapping=mapping )


    def preformTransform(self, dataPoints: 'Points', return_final_image=False):

        if return_final_image:
            return self.final_ouput

        return self.preform_triangle_affine(dataPoints.to_numpy(), self.contours, self.transform)
from abc import abstractclassmethod


class Transform:

    '''
    Transform:
        Abstract class for transforming from different spaces to otherspaces

    Notes:
       When defining a new Transform, you have the freedom for how the Transform is built and how it will be preformed.
       This should fall inline with mapping and other class methods for transforming data.
    '''

    @abstractclassmethod
    def buildTransform(self, telemetry):
        return NotImplemented
    
    @abstractclassmethod
    def preformTransform(self, dataPoints):
        return NotImplemented
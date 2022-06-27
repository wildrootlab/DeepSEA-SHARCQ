import os
import numpy as np
from neural_best_buddies.models import vgg19_model
from neural_best_buddies.algorithms import neural_best_buddies as NBBs
from neural_best_buddies.util import util
from neural_best_buddies.util import MLS


class Opt:
  gpu_ids = []
  imageSize = 224
  batchSize = 1
  beta1 = 0.5
  border_size = 7
  convergence_threshold = 1
  gamma = 1
  input_nc = 3
  niter_decay = 100
  tau = 0.05
  lr = 0.05
  name = ""


def NBB_Adapter(imageA, imageB, gpu):
        
    vgg19 = vgg19_model.define_Vgg19(Opt)
    # save_dir =  os.path.join("/content/save_dir", Opt.name)

    nbbs = NBBs.sparse_semantic_correspondence(vgg19, Opt.gpu_ids, 0.05, 7, Opt.name, 20, 10, 1)
    A = util.numpy_to_image(imageA, Opt.imageSize)
    B = util.numpy_to_image(imageB, Opt.imageSize)

    A_cor, B_cor = nbbs.run(A, B) 

    mls = MLS.MLS(v_class=np.int32)

    return A_cor, B_cor, mls.run_MLS
# --------------------------------------------------------
# Copyright (C) 2021 NVIDIA Corporation. All rights reserved.
# Nvidia Source Code License-NC
# Transformer Pretraining Code: Yucheng, Vishwesh, Ali
# --------------------------------------------------------

import os
import numpy as np
from numpy.random import randint
from PIL import Image
import nibabel as nb
import json

# Generate JSON file


import os

traindir = '/home/at84490/Documents/projects/UNesT/UNesT-main14.4/wholebrainSeg/data/train/images'
valdir = '/home/at84490/Documents/projects/UNesT/UNesT-main14.4/wholebrainSeg/data/validation/images'
json_file = '/home/at84490/Documents/projects/UNesT/UNesT-main14.4/wholebrainSeg/data/wholebrain.json'

sublist = [s for s in os.listdir(traindir)]
allnum = len(sublist)

datadict = {}
datadict['training'] = []
datadict['validation'] = []

for f in sublist:
    
    ifile = "/home/at84490/Documents/projects/UNesT/UNesT-main14.4/wholebrainSeg/data/train/images/" + f
    t_dict = {"image": '', 'label':''}

    t_dict['image'] = ifile
    f_segname = f.split('.nii')[0] + '_seg.nii.gz' 
    

    ilabel = "/home/at84490/Documents/projects/UNesT/UNesT-main14.4/wholebrainSeg/data/train/labels/" + f_segname 
    t_dict['label'] = ilabel

    datadict['training'].append(t_dict)
    

sublist = [s for s in os.listdir(valdir)]
allnum = len(sublist)

for f in sublist:

    ifile = "/home/at84490/Documents/projects/UNesT/UNesT-main14.4/wholebrainSeg/data/validation/images/" + f
    t_dict = {"image": '', 'label':''}

    t_dict['image'] = ifile
    f_segname = f.split('.nii')[0] + '_seg.nii.gz'

    ilabel = "/home/at84490/Documents/projects/UNesT/UNesT-main14.4/wholebrainSeg/data/validation/labels/" + f_segname 
    t_dict['label'] = ilabel

    datadict['validation'].append(t_dict)


with open(json_file, 'w') as f:
    json.dump(datadict, f, indent=4, sort_keys=True)

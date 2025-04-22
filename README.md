# UNest Model Inference Tutorial

This tutorial explains how to use the trained UNesT model with 87 HOA subjects for inference. The model is available in this repository, and below are the steps to set up your environment, and perform inference.
We trained the Unest_large which is developped by [MASILab](https://github.com/MASILab/UNesT/blob/main/wholebrainSeg/README.md) 

## Prerequisites
- Python 3.8.0



Follow along with explanations below!

## Environment
You can install the required libraries with requiremnts.txt. Narval-compatible versions can be installed using Narval-requiremnts.txt.

## Register images to the MNI-305space
First you need to register the images from their original space to MNI space. You can use ants_registration.py file.

## Download the Models

The trained UNest models like (`model.pt`) are too large to include directly in the repository. You can download them all using the [OneDrive Link](https://etsmtl365-my.sharepoint.com/:f:/r/personal/ghazal_danaee_1_ens_etsmtl_ca/Documents/Ghazal_Danaee_files/UNesT-trained-models/Unest14?csf=1&web=1&e=nKLPYC) 

## Inference 
Run inference 4 times using the following command. Each time with one of the trained models (model0, model1, model2, model3, model4) and change --saved_model_path and --fold according to the model you are using. The input to fold should be integers (0,1,2,3, and 4) which you should choose based on the model number. The results of different folds will be saved in folders fold0, fold1, fold2, fold3, fold4 in output_path/pred_0.7. Change the paths as needed.  
  
It is essential that you use the inference.py file in this repository and not the original in MASI Lab github page since their script is for 133 class segmentation.

python inference.py --imagesTs_path test_images_path --saved_model_path path2saved_model --base_dir output_path --fold 0 --overlap 0.7 --device 0

## Ensemble  
If you perform the ensembling, you'll get slightly better results.  
Run ensemble using the following command. Change the paths as needed.  

python ensemble.py --prob_dir output_from_inference --img_path test_images_path --out_path output_path

## Register back to original space
In order to have final results, you'll need to register the data back to their original space. You can use the call_Run_Deep_brain.sh bash file.



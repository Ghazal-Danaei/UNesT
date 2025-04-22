import ants
import sys
import os


import nibabel as nib

output_image_path_t1 = ".../t1-registered"
fixed_image_path = "../average305_t1_tal_lin.nii"
moving_image_folder_t1 = "/.../t1/"

output_image_path_label = ".../label-registered/"
moving_image_folder_label = ".../label/"
# Load the fixed image
fixed_image = ants.image_read(fixed_image_path)

# Iterate through the moving images in the folder
for image_filename in os.listdir(moving_image_folder_t1):
      #finding t1 image path
      moving_image_path_t1 = os.path.join(moving_image_folder_t1, image_filename)
      idx = image_filename.split(".")[0]
      moving_image_t1 = ants.image_read(moving_image_path_t1)
      #finding corresponding label
      moving_image_path_label = os.path.join(moving_image_folder_label, f"{idx}_dseg.nii.gz")
      moving_image_label = ants.image_read(moving_image_path_label)
      #estimating the transform
      transform = ants.registration(fixed_image, moving_image_t1, "Affine")
      # Apply the transformation to the moving image t1 and its corresponding label
      reg3t_t1 = ants.apply_transforms(fixed_image, moving_image_t1, transform["fwdtransforms"][0], interpolator="linear")
      reg3t_label= ants.apply_transforms(fixed_image, moving_image_label, transform["fwdtransforms"][0], interpolator="nearestNeighbor")
      # # Save the registered images
      output_image_filename_t1 = os.path.join(output_image_path_t1, f"{idx}.nii")
      output_image_filename_label = os.path.join(output_image_path_label, f"{idx}_seg.nii.gz")
      ants.image_write(reg3t_t1, output_image_filename_t1)
      ants.image_write(reg3t_label, output_image_filename_label)  










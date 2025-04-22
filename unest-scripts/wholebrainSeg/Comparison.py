import nibabel as nib
import os
import numpy as np
def dice(x, y):
    intersect = np.sum(np.sum(np.sum(x * y)))
    y_sum = np.sum(np.sum(np.sum(y)))
    if y_sum == 0:
        return 0.0
    x_sum = np.sum(np.sum(np.sum(x)))
    return 2 * intersect / (x_sum + y_sum)

label_paths = "/home/at84490/Documents/projects/UNesT/UNesT-main14.4/test-labels"
prediction_paths = "/home/at84490/Documents/projects/UNesT/UNesT-main14.4/ensemble_output"
list_of_dices_test = []
Dice_per_class_all = {f"label{i}": [] for i in range(1, 28)}
for image_filename in os.listdir(label_paths):
    Dice_per_class_individual = {f"label{i}": "" for i in range(1, 28)}
    Mean_Dice_per_class_individual = {f"label{i}": "" for i in range(1, 28)}

    idx = image_filename.split("_seg.nii.gz")[0]
    prediction_path = os.path.join(prediction_paths, idx+".nii")
    label_path = os.path.join(label_paths, image_filename)
    label_data = nib.load(label_path).get_fdata()
    pred_data = nib.load(prediction_path).get_fdata()
    for i in range(1, 28):
        organ_Dice = dice(pred_data == i, label_data== i)
        Dice_per_class_individual[f"label{i}"] = organ_Dice
        Dice_per_class_all[f"label{i}"].append(organ_Dice) 
    print("Case"+idx+":")
    print ("Dice Similarity per class: {}".format(Dice_per_class_individual))
    res = 0
    for val in Dice_per_class_individual.values(): 
        res += val 
    res = res / 28
    list_of_dices_test.append(res)
    print ("Mean of Dice Similarity for the case: {}".format(res))

print("Mean of Dice Similarity for test set{}".format(np.mean(list_of_dices_test)))
for key, values in Dice_per_class_all.items():
    mean_value = np.mean(values)
    Dice_per_class_all[key] = mean_value
print("Mean of Dice Similarity for test set per class{}".format(Dice_per_class_all))



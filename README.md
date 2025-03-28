# MONAI VISTA for Lung Fibrosis Segmentation
This is the repository adpated from VISTA3D and VISTA2D. For the older VISTA2.5d code, please checkout the vista2.5d branch

## Conda Environment Name
The project uses the following Conda environment:
`vista3d`


## Dataset
- **Ground Truth**: 20 cases  
  - **Image Directory**: `/home/shengzhang/data/nnUNet/nnUNet_raw/Dataset250_AIIB23Fibrosis/image`  
  Linked to --> `vista3d/data/OSIC/gt_20`
  - **Ground Truth Directory**: `/home/shengzhang/data/nnUNet/nnUNet_raw/Dataset250_AIIB23Fibrosis/gt20250112/nii_gz_filled_consistency4`
  Linked to --> `vista3d/data/OSIC/imgs_20`

- **Unlabeled Images**: 262 cases  
  - **Directory**: `/home/shengzhang/data/nnUNet/nnUNet_raw/Dataset250_AIIB23Fibrosis/AIIB23_all_images`

## Challenge Project Schedule
![Project Schedule](challenge/Schedule.png)
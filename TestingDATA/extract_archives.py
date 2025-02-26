from Task03_Liver import nifti_2_dicom
import os

#------------------------------------------------------------------------------
# USER-DEFINED PATHS: Update these paths with your directories.
#------------------------------------------------------------------------------
# Directory containing your input .nii.gz files
input = r'C:\Users\...\Task03_Liver\imagesTr'

# Directory where you want the DICOM series output folders to be created
output = r'C:\Users\...\Task03_Liver\dicom_files\images'
#------------------------------------------------------------------------------


nifti_2_dicom.nifti2dicom_mfiles(input, output)


"""
After doing this for the training images(imagesTr), also do this for the labels
# Directory containing your input .nii.gz files
input = r'C:\Users\...\TestingDATA\labelsTr'

# Directory where you want the DICOM series output folders to be created
output = r'C:\Users\...TestingDATA\dicom_files\labels
"""
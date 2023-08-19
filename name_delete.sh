#!/bin/bash

# Directory with files to rename
DIR="/home/survey/pytorch-CycleGAN-and-pix2pix-wkk/datasets/yellow2brown_mask_new/trainB_mask"  # REPLACE with the path to your directory

# Go to the directory
cd "$DIR"

# Rename all the files
for file in *_mask*; do
  mv -- "$file" "${file/_mask/}"
done
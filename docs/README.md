# DeepSEA-SHARCQ

## Description 

This project aims to revise an existing repository through the incorporation of robust machine learning methods, thereby promoting greater validity and minimizing human input and error in scientific data analysis. The existing MATLAB toolkit is known as 'SHARCQ': Slice Histology Alignment, Registration and Cell Quantification

> See the existing SHARCQ repository https://github.com/wildrootlab/SHARCQ and the associated paper https://www.eneuro.org/content/9/2/ENEURO.0483-21.2022

This revision aims toward a 'DeepSEA' ideal: Deep (learning) for Simplified End-to-end Automation

## Overview and Purpose

This project retains the main objectives of the SHARCQ repository:

### Imaging data analysis

Input: Large quantities of non-standardized brain tissue section images obtained through fluorescent histology - targeting uniquely defined (by genetic, circuit, or other character) cell populations - and microscopy

Output: Brain-wide quantification of labeled cell load in all regions of standardized atlas space

General Method:
- Align images to standardized brain atlas space (match resolution, find A/P, D/V, M/L coordinates and tilt)
- Register/warp images for accurate mapping of brain region boundaries on tissue
- Quantify labeled cells in each section, throughout whole brains, tallying region locations

Limitations of SHARCQ:
- Requires additional input of cell count file (x,y coordinates of labeled cells in each image) prior to processing
  - Not an end-to-end pipeline
- Manual user alignment to atlas space
  - Requires relative user expertise in neuroanatomy for accurate alignment
- Manual user-identification of landmarks on each image and atlas section for registration step 
  - Not fully automated - consumes researchers' time providing input and may be prone to inconsistency

DeepSEA-SHARCQ aims to incorporate:
- End-to-end pipeline requiring input of only images, providing final data output
  - Incorporating cell count process into pipeline
- Fully automated process requiring a minimum of user interaction
  - Automated cell count, alignment, and registration, giving consistent cell load output
- Radical ease of access and implementation



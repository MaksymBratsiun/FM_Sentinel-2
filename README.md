# FM_Sentinel-2

# Task

Computer vision.

Sentinel-2 image matching In this task, you will work on the algorithm (or model) for matching satellite images. 
For the dataset creation, you can download Sentinel-2 images from the official source here or use our dataset from Kaggle. 
Your algorithm should work with images from different seasons. 

For this purpose you need: 
- Prepare a dataset for keypoints detection and image matching (in case of using the ML approach). 
- Build / train the algorithm.
- Prepare demo code / notebook of the inference results. 

The output for this task should contain: 
- Jupyter notebook that explains the process of the dataset creation. 
-  Link to the dataset (Google Drive, etc.).
- Link to model weights. 
- Python script (.py) for model training or algorithm creation. 
- Python script (.py) for model inference. 
- Jupyter notebook with demo should have the functionality for observing detected keypoints and their matches:

![img_3.png](img_3.png)

 Recommendation: 
- Classical solutions can be not accurate enough for images from different seasons. 
- Satellite images have large sizes. 
You should think about how to process them in order not to lose the quality. 
- Some initial knowledge about satellite imagery processing you can find here.

# Overview
This repository contains Python scripts for figure matching. Input needs 2 images like Sentinel-2 images with 1 chanel. 
Script search potential keypoints locations and calculate distance between them. Its match via algorithm SIFT 
(optionally we can use ORB), compare images and insert lines between keypoints and save results. 
There are test data for test matching and demonstration. 

# Requirements
- Python 3.x
- OpenCV-python
- Other dependencies (install using `pip install -r requirements.txt`)

# Usage
- update project from Git
- create virtual environment

```bash
pip install -r requirements.txt
```

Set path to images and number of matches in script `figure_matching.py`
```
PATH_1 = "..._B8A.jp2"
PATH_2 = "..._B8A.jp2"
MATCHES = 20
```

Run `figure_matching.py`:
```bash
python  figure_matching.py
```
Watch result in `output_image.jpg`:

![img_2.png](img_2.png)

# Conclusion

Choose SIFT because it better with different light gradient. 
Use B8A chanel because it was more stable and did not depend on the season and small size.
Save without compressing for easy validation. Draw first 20 matches.
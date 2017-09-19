# Udacity Self Driving Car Nanodegree: Lane Detection

<p align="center">
<img src="https://github.com/sansinghsanjay/udacity_self_driving_car_lane_detection/blob/master/sample_input_output/sample_input.gif">
&nbsp &nbsp
<img src="https://github.com/sansinghsanjay/udacity_self_driving_car_lane_detection/blob/master/technologies_used/technologies_used.png">
&nbsp &nbsp
<img src="https://github.com/sansinghsanjay/udacity_self_driving_car_lane_detection/blob/master/sample_input_output/sample_output.gif">
</p>

## Objective
This project is for identifying and marking lane lines on the road.

Above GIF images are showing sample input (at left side) and sample output (at right side) obtained by using Python and OpenCV (Open Computer Vision).

## Introduction

### Self Driving Cars
Self Driving Cars are unmanned ground vehicles, also known as Autonomus Cars, Driverless Cars, Robotic Cars.
<p align="center">
<img src="https://github.com/sansinghsanjay/udacity_self_driving_car_lane_detection/blob/master/images/self-driving-car.jpg">
</p>

### Technologies Used
Following are the technologies used by these Self Driving Cars to navigate:
1. Computer Vision and Machine Learning (AI) to find path, to classify traffic signs, etc.
2. Sensor Fusion to sense the surrounding moving vehicles.
3. Machine Learning (AI) for decision making.

### Why "Lane Detection"?
A simple traffic rule says that every vehicle should run in its own lane. If it goes in other lane then chances of accident increases. Thus, lane marking is an important task which prevents these autonomus vehicles from entering in other lane and hence prevents from accidents.

Self Driving Cars uses Computer Vision to find the path on which these cars/vehicles have to navigate. Computer Vision uses symbolic information from image using techniques from geometry, physics, statistics and information theory.


## Programming Language
In this project, Python-3.5.2 is used with following packages:
1. numpy - 1.13.0
2. moviepy - 0.2.3.2
3. cv2 - 3.0.0 (Computer Vision)

## Algorithm
1. Read an image:
<p align="center">
<img src="https://github.com/sansinghsanjay/udacity_self_driving_car_lane_detection/blob/master/images/input_image.png">
</p>

2. Convert image into a gray image as it is easy to extract edges from a single-channel (gray) image:
<p align="center">
<img src="https://github.com/sansinghsanjay/udacity_self_driving_car_lane_detection/blob/master/images/gray_image.png">
</p>

3. Apply Gaussian Blur on gray image to remove noise:
<p align="center">
<img src="https://github.com/sansinghsanjay/udacity_self_driving_car_lane_detection/blob/master/images/blur_gray.png">
</p>

4. Apply Canny Edge Detection Operator on smoothed (noise removed) gray image with some low and high threshold values. This will return an image with only detected edges:
<p align="center">
<img src="https://github.com/sansinghsanjay/udacity_self_driving_car_lane_detection/blob/master/images/canny_edge.png">
</p>

5. As we have to identify only lanes on road, so a mask is applied to get only region of interest:
<p align="center">
<img src="https://github.com/sansinghsanjay/udacity_self_driving_car_lane_detection/blob/master/images/region_of_interest.png">
</p>

6. Then, Hough Transform is applied to get lines in above obtained image.

7. Some mathematical operations applied to interpolate lines at positions where they are missing:
<p align="center">
<img src="https://github.com/sansinghsanjay/udacity_self_driving_car_lane_detection/blob/master/images/interpolate.png">
</p>

8. Finally, a weighted sum of our input image and above image is performed to get final output:
<p align="center">
<img src="https://github.com/sansinghsanjay/udacity_self_driving_car_lane_detection/blob/master/images/result.png">
</p>

## How To Use?
To use this project:
1. Clone this github repository.
2. Make "scripts" sub-directory as present-working-directory.
3. Run this command in terminal: ```python main.py```

Or simply use ipython notebook under "scripts" sub-directory.

## Limitations
1. On turns, this code is giving weired output.
2. If the position of lane gets changed (like width of lanes), then this code may not be able to detect the lanes even if lanes are straight. This is because region of interest is hard coded here, its not generic.
3. This technique of lane detection would not work if light from sun or headlight of another vehicle falls on camera of self driving car. 
4. In this technique, its an assumption that roads are flat and have clearly visible lane marks.

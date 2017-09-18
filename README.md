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

Above GIF images are showing sample input (at left side) and sample output (at right side) obtained by using Python and OpenCV.

## Introduction

### Self Driving Cars
Self Driving Cars are unmanned ground vehicles, also known as Autonomus Cars, Driverless Cars, Robotic Cars.

### Technologies Used
Following are the technologies used by these Self Driving Cars to navigate:
	i. Computer Vision and Machine Learning (AI) to find path, to classify traffic signs, etc.
	ii. Sensor Fusion to sense the surrounding moving vehicles.
	iii. Machine Learning (Artificial Intelligence) for decision making.

### Why "Lane Detection"?
A simple traffic rule says that every vehicle should run in its own lane. If it goes in other lane then chances of accident increases. Thus, lane marking is an important task which prevents these autonomus vehicles from entering in other lane and hence prevents from accidents.

Self Driving Cars uses Computer Vision to find the path on which these cars/vehicles have to navigate. Computer Vision uses symbolic information from image using techniques from geometry, physics, statistics and information theory.


## Programming Language
In this project, Python-3.5.2 is used with following packages:
	i. numpy-1.13.0
	ii. moviepy-0.2.3.2
	iii. cv2-3.0.0

## Finding Lane Lines on the Road

1. Follow is the flow of program for detection of lane lines on road:
	i. Function "main_process" gets one by one each frame of a video.
	ii. This function passes the obtained image frame to functon "grayscale" to get the gray scale image.
	iii. Then I applied gaussian blur on the obtained gray scale image to remove noise.
	iv. Then I applied canny edge detection function on smoothed gray scale image to detect all edges present in image.
	v. As we have to mark only region having lane lines, so I applied function 'region_of_interest' to get region having lines of that lane on which car is running.
	vi. Then I applied Hough Transform to get lines from canny edges.
	vii. Then moved to draw_lines function, this function is drawing lane lines on image. While drawing lines, it is also extrapolating lines by using the slope and intercept of lines so that we can see one continuous line on left side and one continuous line on right side.
	viii. At last there is weighted sum of image and line image (image having lane lines) to make sure that this lane lines doesn't hide other components on given image.
	ix. All this image frames are collecting and making a video and saving them.

2. Following could be the shortcomings of this code:
	i. On turns, this code is giving weired output.
	ii. If the position of lane get changed (like width of lanes), then this code may not be able to detect the lanes even if lanes are straight. This is because region of interest is hard coded here, its not generic.

3. Following could be the improvements: Removing above shortcomings.

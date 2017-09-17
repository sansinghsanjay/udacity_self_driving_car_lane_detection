# libraries
import numpy as np
from moviepy.editor import VideoFileClip
#from IPython.display import HTML
import os
import cv2

# paths
input_test_images_path = "./../test_images/"
output_test_images_path = "./../test_images_output/"
input_test_videos_path = "./../test_videos/"
output_test_videos_path = "./../test_videos_output/"

# converting color image into gray image
def grayscale(image):
	gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)
	return gray

# applying gaussian-blur
def gaussian_blur(image, kernel_size = 5):
	blur_gray = cv2.GaussianBlur(image,(kernel_size, kernel_size),0)
	return blur_gray

# applying canny edge detection
def canny(image, low_threshold=50, high_threshold=150):
	edges = cv2.Canny(image, low_threshold, high_threshold)
	return edges

# getting region of interest from image
def region_of_interest(edges):
	# creating a mask
	mask = np.zeros_like(edges)
	ignore_mask_color = 255
	imshape = edges.shape[:2]
	# four sided polygon
	vertices = np.array([[(150,imshape[0]),(460, 320), (540, 320), (860, imshape[0])]], dtype = np.int32)
	cv2.fillPoly(mask, vertices, ignore_mask_color)
	# masking edges
	masked_edges = cv2.bitwise_and(edges, mask)
	return masked_edges

# applying Hough transform
def hough_lines(masked_edges):
	# parameters for hough
	rho = 1 # distance resolution in pixels of the Hough grid
	theta = np.pi/180 # angular resolution in radians of the Hough grid
	threshold = 20    # minimum number of votes (intersections in Hough grid cell)
	min_line_length = 20 #minimum number of pixels making up a line
	max_line_gap = 300    # maximum gap in pixels between connectable line segments
	# applying hough
	lines = cv2.HoughLinesP(masked_edges, rho, theta, threshold, np.array([]),min_line_length, max_line_gap)
	return lines

# interpolating and drawing lane lines
def draw_lines(image, lines):
	left_lines    = [] # (slope, intercept)
	left_weights  = [] # (length,)
	right_lines   = [] # (slope, intercept)
	right_weights = [] # (length,)
	for line in lines:
		for x1, y1, x2, y2 in line:
			if x2==x1:
				continue # ignore a vertical line
			slope = (y2-y1)/(x2-x1)
			intercept = y1 - slope*x1
			length = np.sqrt((y2-y1)**2+(x2-x1)**2)
			if slope < 0: # y is reversed in image
				left_lines.append((slope, intercept))
				left_weights.append((length))
			else:
				right_lines.append((slope, intercept))
				right_weights.append((length))
	# add more weight to longer lines
	left_lane  = np.dot(left_weights,  left_lines)/np.sum(left_weights)  if len(left_weights) >0 else None
	right_lane = np.dot(right_weights, right_lines)/np.sum(right_weights) if len(right_weights)>0 else None
	# creating a blank to draw lines on
	line_image = np.copy(image)*0
	# converting lines into point coordinates
	y1 = image.shape[0]
	y2 = y1 * 0.6
	left_line = make_line_points(y1, y2, left_lane)
	right_line = make_line_points(y1, y2, right_lane)
	if(left_line is not None):
		cv2.line(line_image,(left_line[0][0],left_line[0][1]),(left_line[1][0],left_line[1][1]),(255,0,0),10)
	if(right_line is not None):
		cv2.line(line_image,(right_line[0][0],right_line[0][1]),(right_line[1][0],right_line[1][1]),(255,0,0),10)
	return line_image

# weighing marked lanes on image
def weighted_image(image, edges, line_image):
	# Create a "color" binary image to combine with line image
	color_edges = np.dstack((edges, edges, edges))
	# Draw the lines on the edge image
	lines_edges = cv2.addWeighted(image, 1.0, line_image, 1, 0)
	return lines_edges

# convert a line represented in slope and intercept into pixel points
def make_line_points(y1, y2, line):
	if line is None:
		return None
	slope, intercept = line
	# make sure everything is integer as cv2.line requires it
	x1 = int((y1 - intercept)/slope)
	x2 = int((y2 - intercept)/slope)
	y1 = int(y1)
	y2 = int(y2)
	return ((x1, y1), (x2, y2))

# main function
def pipeline(image):
	# getting gray image
	gray = grayscale(image)
	# applying gaussian blur
	blur_gray = gaussian_blur(gray)
	# applying canny edge detection
	edges = canny(blur_gray)
	# applying region of interest
	masked_edges = region_of_interest(edges)
	# applying hough
	lines = hough_lines(masked_edges)
	# drawing lines on image
	line_image = draw_lines(image, lines)
	# weighing marked lanes on image
	result = weighted_image(image, edges, line_image)
	return result

# test images
test_images = os.listdir(input_test_images_path)
for i in range(len(test_images)):
	# reading test image
	img = cv2.imread(input_test_images_path + test_images[i])
	# changing color space from BGR to RGB
	img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
	# marking lane on test image
	test_output = pipeline(img)
	# converting output image from BGR to RGB
	test_output = cv2.cvtColor(test_output, cv2.COLOR_BGR2RGB)
	# saving test image output
	cv2.imwrite(output_test_images_path + "output_" + test_images[i], test_output)

# test videos
test_videos = os.listdir(input_test_videos_path)
for i in range(len(test_videos)):
	# reading video clip
	clip = VideoFileClip(input_test_videos_path + test_videos[i])
	# processing frames of video by passing them in "pipeline"
	processed = clip.fl_image(pipeline)
	# saving output
	processed.write_videofile(output_test_videos_path + "output_" + test_videos[i], audio=False)

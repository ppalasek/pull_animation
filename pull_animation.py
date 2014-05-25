import numpy as np
import cv2
import os

#here is where we have the frames stored
frames_directory = 'frames/'

#all files in frames_directory
frames = [os.path.join(frames_directory, frame) for frame in os.listdir(frames_directory)]

#we'll use only jpg files, and let's sort them
frames = sorted([frame for frame in frames if frame.endswith('.jpg')])

#we'll just load the first image and paint over it because why not
animation = cv2.imread(frames[0])

animation_height = animation.shape[0]
animation_width = animation.shape[1]

num_frames = len(frames)

for i in xrange(num_frames):
    current_frame = cv2.imread(frames[i])

    for j in xrange(animation_width / num_frames):
        for k in xrange(animation_height):
            animation[k][j * num_frames + i] = current_frame[k][j * num_frames + i]

#show generated image and save it
cv2.imshow('animation_image', animation)
cv2.imwrite('animation_image.png', animation)

black_lines = np.zeros((animation_height, animation_width), dtype = np.uint8)

for j in xrange(animation_width / num_frames):
    for k in xrange(animation_height):
        black_lines[k][j * num_frames] = 255

#show black lines and save them
cv2.imshow('black_lines', black_lines)
cv2.imwrite('black_lines.png', black_lines)

#show how it looks as a real animation
while (True):
    for f in xrange(num_frames):
        real_animation = np.zeros(animation.shape, dtype = np.uint8)

        for j in xrange(animation_width / num_frames):
            for k in xrange(animation_height):
                real_animation[k][j * num_frames + f] = animation[k][j * num_frames + f]

        cv2.imshow('real_animation', real_animation)
        cv2.waitKey(50)
'''
THIS DOES NOT WORK - DO NOT RUN
AttributeError: module 'inference' has no attribute 'load_roboflow_model'

this line was literally in the roboflow documentation, but here we are lmao
also I don't think this is the method for offline deployment
'''

import ultralytics
import pyrealsense2 as rs
import cv2
import numpy as np
import math
import inference

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

profile = pipeline.start(config)

model = inference.load_roboflow_model("pepbuoys/1")

def midpoint(a, b):
    return int((a[0] + b[0]) * 0.5), int((a[1], b[1]) * 0.5)


# main loop
for i in range(1000):
    frame = pipeline.wait_for_frames()
    color_frame = frame.get_color_frame()
    depth_frame = frame.get_depth_frame()

    depth_image = np.asanyarray(depth_frame.get_data())
    color_image = np.asanyarray(color_frame.get_data())
    
    results = model.infer(image=color_image)

    print(results)

    cv2.imshow('color', color_image)

pipeline.stop()
cv2.destroyAllWindows()
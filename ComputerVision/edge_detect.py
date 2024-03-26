import pyrealsense2 as rs
import cv2
import numpy as np

pipeline = rs.pipeline()
config = rs.config()
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 30)
config.enable_stream(rs.stream.color, 640, 480, rs.format.bgr8, 30)

profile = pipeline.start(config)

while True:
    frame = pipeline.wait_for_frames()
    color_frame = frame.get_color_frame()
    depth_frame = frame.get_depth_frame()

    color_image = np.asanyarray(color_frame.get_data())
    depth_image = np.asanyarray(depth_frame.get_data())

    grayimg = cv2.cvtColor(color_image, cv2.COLOR_BGR2GRAY)
    blur = cv2.GaussianBlur(grayimg, (5, 5), 0)
    canny = cv2.Canny(blur, 10, 70)
    ret, mask = cv2.threshold(canny, 70, 255, cv2.THRESH_BINARY)

    cv2.imshow("edges", mask)

    if cv2.waitKey(1) == ord('q'):
        break

pipeline.stop()
cv2.destroyAllWindows()

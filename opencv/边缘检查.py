import cv2
import numpy as np

# 注意读取路径不支持中文
img = cv2.imread(r"E:\code\python-code\opencv\img\3.png", 1)
print(img)
img1 = cv2.resize(img, None, fx=1, fy=1)

# 灰度
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
cv2.imshow(winname="Gray", mat=img1)
# 二值图
ret, binary = cv2.threshold(gray, 210, 255, cv2.THRESH_BINARY)
cv2.imshow(winname="binary", mat=binary)

# 获取轮廓
contours, hie = cv2.findContours(binary, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
draw_img = img1.copy()
cv2.drawContours(draw_img, contours, -1, (0, 255, 0), 1)
imgs = np.hstack([img1, draw_img])
cv2.imshow("out", imgs)
cv2.waitKey()

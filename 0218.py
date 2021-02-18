import numpy as np
import cv2
import glob

img = glob.glob("./img/*")
i = 0

for imgs in img:
    i += 1
    print(imgs)
    img1 = cv2.imread(imgs,0)
    img2 = cv2.flip(img1,1)
    cv2.imwrite('./done/gray'+str(i)+'.jpg',img2)

#img = cv2.imread("neko.jpg",2)
# img1 = cv2.imread(img,0)

# img2 = cv2.flip(img1,1)
# cv2.imshow('image', img2)
# k = cv2.waitKey(0) & 0xFF

# if k ==27:

#     cv2.destroyAllWindows()
# elif k == ord('s'):
#     print("画像を保存")
#     cv2.imwrite('cut.jpg',img2)
#     cv2.destroyAllWindows()
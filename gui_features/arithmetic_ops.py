import cv2 


img1 = cv2.imread('../media/scared_hamster.jpg')
img2 = cv2.imread('../media/vietnam.jpg')

# You can add two images together using cv2.add() or numpy operations but use the add method to avoid modulo operations
# Adding two images together with blended weights will result in a blended image. You can do this with cv2.addWeighted() method. Make sure the images are the same size

# dst = cv2.addWeighted(img1, 0.7, img2, 0.3, 0)
dst = cv2.addWeighted(img1[:500, :500], 0.7, img2[:500, :500], 0.3, 0)

# cv2.imwrite('../media/vietnamese_hamster.jpg', dst)

cv2.imshow('dst', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
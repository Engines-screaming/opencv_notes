import cv2 

# BLENDING IMAGES
def blending_images():
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

# bitwise image ops
def bitwise_images():
    '''Places logo on target image'''

    img1 = cv2.imread('../media/robots.jpg')
    img2 = cv2.imread('../media/opencv.png')

    # create ROI in target image for logo
    rows, cols, channels = img2.shape
    roi = img1[:rows, :cols]

    # create mask of logo and inverse mask
    img2gray = cv2.cvtColor(img2, cv2.COLOR_BGR2GRAY)
    ret, mask = cv2.threshold(img2gray, 10, 255, cv2.THRESH_BINARY)
    mask_inv = cv2.bitwise_not(mask)

    # black out areas of the logo in ROI
    img1_bg = cv2.bitwise_and(roi, roi, mask=mask_inv)

    # take only region of the logo from logo image
    img2_fg = cv2.bitwise_and(img2, img2, mask=mask)

    # put logo in ROI and modify the main image
    dst = cv2.add(img1_bg, img2_fg)
    img1[0:rows, 0:cols] = dst

    images = [mask, mask_inv, img1_bg, img2_fg, dst]
    for img in images:
        cv2.imshow('res', img)
        cv2.waitKey(0)
        cv2.destroyAllWindows()


# exercise
def blending_slideshow():
    ''' Produces a slideshow to demonstrate one image blending into another image'''
    img1 = cv2.imread('../media/vietnam.jpg')
    img2 = cv2.imread('../media/scared_hamster.jpg')

    # find best size
    height1, width1, channel1 = img1.shape
    height2, width2, channel2 = img2.shape

    if height1 <= height2:
        common_height = height1
    else:
        common_height = height2

    if width1 <= width2:
        common_width = width1
    else:
        common_width = width2

    print(f'h1, w1: {height1, width1}')
    print(f'h2, w2: {height2, width2}')
    print(f'common height, common width: {common_height, common_width}')

    weight = 0.0
    step = 0.1

    while weight < 1.0:
        dst = cv2.addWeighted(img1[:common_height, :common_width], 1-weight, img2[:common_height, :common_width], weight, 0)
        cv2.imshow('dst', dst)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        weight += step


if __name__ == '__main__':
    blending_slideshow()
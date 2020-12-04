import cv2
from matplotlib import pyplot as plt

# reading in an image
img_path = "media/test_image.png"


def show_imread_options():
    '''Function to demonstrate reading in an image and viewing
    each option in imread()'''

    # You can specify 1, 0, or -1 for color, greyscale, or unchanged options
    # cv2.IMREAD_COLOR, cv2.IMREAD_GREYSCALE, cv2.IMREAD_UNCHANGED
    img_color = cv2.imread(img_path, 1)
    img_gs = cv2.imread(img_path, 0)
    img_unchanged = cv2.imread(img_path, -1)

    desc_list = ['color', 'gs', 'unchanged']
    img_list = [img_color, img_gs, img_unchanged]
    img_dict = zip(desc_list, img_list)

    for description, image in img_dict:
        cv2.imshow(description, image)
        cv2.waitKey(0)

    cv2.destroyAllWindows()


def save_img_gs(plot=False):
    '''Function to demonstrate viewing a picture with matplotlib, converting
    to greyscale, and saving to location'''

    img = cv2.imread(img_path, -1)

    # opencv interprets images as BGR, matplotlib interprets RGB
    # img2 = img[:, :, ::-1]  # using numpy indexing
    img2 = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # the way that makes sense to me
    plt.imshow(img2)

    # show in matplotlib
    if plot:
        plt.imshow(img, cmap='gray', interpolation='bicubic')  # greyscale reading

    plt.xticks([]), plt.yticks([])  # hide tick marks
    plt.show()

    cv2.imwrite('images/test_image_gs.png', img)


if __name__ == '__main__':
    save_img_gs()

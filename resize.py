import cv2

def resize_all_images(patch_to_directory, count_images):
    width = 255
    height = 255
    dim = (width, height)
    for i in range(count_images):
        try:
            img = cv2.imread(patch_to_directory + '/img' + str(i) + '.jpg', cv2.IMREAD_UNCHANGED)
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

            cv2.imwrite(patch_to_directory + '/img' + str(i) + '.jpg', resized)
        except:
            continue
    return

import cv2


def resize_all_images(patch_to_directory, count_images, width, height):
    dim = (int(width), int(height))
    for i in range(1, count_images):
        try:
            img = cv2.imread(patch_to_directory + '/img' + str(i) + '.jpg', cv2.IMREAD_UNCHANGED)
            print(patch_to_directory + '/img' + str(i) + '.jpg')
            resized = cv2.resize(img, dim, interpolation=cv2.INTER_AREA)

            cv2.imwrite(patch_to_directory + '/img' + str(i) + '.jpg', resized)
        except:
            continue

    return

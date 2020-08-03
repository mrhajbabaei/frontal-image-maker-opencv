import math 


def get_coordinates(landmark):
    keypoints = landmark['keypoints']
    left_eye = keypoints['left_eye']
    right_eye = keypoints['right_eye']
    nose = keypoints['nose']
    mouth_left = keypoints['mouth_left']
    mouth_right = keypoints['mouth_right']
    theta = math.degrees(math.atan2(left_eye[1] - right_eye[1], left_eye[0] - right_eye[0]))

    return (left_eye, right_eye), (mouth_left, mouth_right), nose, theta

def crop_image(x_start, x_end, y_start, y_end, image):
    cropped_image = image[y_start:y_end,x_start:x_end]

    return cropped_image

def mask_image(width, height, nose):
    if width < height:
        radius = max(nose[1], int(height - nose[1]))
        x_start = 0
        x_end = width
        y_start = nose[1] - radius
        y_end = nose[1] + radius
    else:
        radius = max(nose[0], int(width - nose[0]))
        x_start = nose[0] - radius
        x_end = nose[0] + radius
        y_start = 0
        y_end = height - 1

    mask = np.zeros((height, width, depth), dtype=np.uint8)
    circle_img = cv2.circle(mask, nose, radius, (255, 255, 255), thickness=-1)
    masked_data = cv2.bitwise_and(rotated_image, circle_img, mask=None)
    cropped_image = crop_image(x_start, x_end, y_start, y_end, masked_data)

    return cropped_image
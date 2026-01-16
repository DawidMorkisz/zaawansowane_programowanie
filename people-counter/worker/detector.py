import cv2
import numpy as np
from imutils.object_detection import non_max_suppression

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detect_people(image_path: str, output_path: str) -> int:
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError(f"Cannot read image: {image_path}")

    max_width = 800
    if img.shape[1] > max_width:
        scale = max_width / img.shape[1]
        img = cv2.resize(img, (max_width, int(img.shape[0] * scale)))

    rects, weights = hog.detectMultiScale(
        img,
        winStride=(4, 4),
        padding=(8, 8),
        scale=1.02
    )

    rects_np = np.array([[x, y, x + w, y + h] for (x, y, w, h) in rects])
    weights_np = np.array(weights).flatten()

    pick = non_max_suppression(rects_np, probs=weights_np, overlapThresh=0.65)

    draw_img = img.copy()
    for (x1, y1, x2, y2) in pick:
        cv2.rectangle(draw_img, (x1, y1), (x2, y2), (0, 255, 0), 2)

    cv2.imwrite(output_path, draw_img)

    return len(pick)

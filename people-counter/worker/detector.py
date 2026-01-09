import cv2

hog = cv2.HOGDescriptor()
hog.setSVMDetector(cv2.HOGDescriptor_getDefaultPeopleDetector())


def detect_people(image_path, output_path):
    img = cv2.imread(image_path)
    if img is None:
        raise ValueError("Cannot read image")

    img = cv2.resize(img, (800, int(img.shape[0] * 800 / img.shape[1])))

    rects, _ = hog.detectMultiScale(
        img,
        winStride=(8, 8),
        padding=(8, 8),
        scale=1.05
    )

    for (x, y, w, h) in rects:
        cv2.rectangle(img, (x, y), (x + w, y + h), (0, 255, 0), 2)

    cv2.imwrite(output_path, img)

    return len(rects)

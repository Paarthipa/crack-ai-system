import cv2

def detect_crack(image_path):
    img = cv2.imread(image_path, 0)
    edges = cv2.Canny(img, 50, 150)

    crack_length = edges.sum() / 1000
    crack_width = 3  # placeholder

    return {
        "crack_length": round(crack_length, 2),
        "crack_width": crack_width,
        "location": "detected area"
    }
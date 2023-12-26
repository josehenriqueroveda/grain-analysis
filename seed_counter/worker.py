import cv2
import numpy as np


def load_image(image_path):
    return cv2.imread(image_path)


def convert_to_grayscale(image):
    return cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)


def apply_threshold(image):
    blur = cv2.GaussianBlur(image, (5, 5), 0)
    _, thresh = cv2.threshold(blur, 0, 255, cv2.THRESH_BINARY_INV + cv2.THRESH_OTSU)
    return thresh


def find_contours(image):
    contours, _ = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    return contours


def calculate_coefficient_of_variance(values):
    return np.std(values) / np.mean(values)


def process_contours(contours, image, ppmm, min_contour_area):
    widths = []
    heights = []
    grains_count = 0

    for cnt in contours:
        if cv2.contourArea(cnt) > min_contour_area:
            x, y, w, h = cv2.boundingRect(cnt)
            cv2.rectangle(image, (x, y), (x + w, y + h), (0, 255, 0), 2)
            cv2.putText(
                image,
                f"W:{round(w/ppmm)}mm",
                (x, y - 10),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 0),
                1,
            )
            cv2.putText(
                image,
                f"H:{round(h/ppmm)}mm",
                (x, y - 30),
                cv2.FONT_HERSHEY_SIMPLEX,
                0.5,
                (0, 0, 0),
                1,
            )

            widths.append(w / ppmm)
            heights.append(h / ppmm)
            grains_count += 1

    return widths, heights, grains_count


def analyze_image(image_path, output_path, ppmm, min_contour_area):
    image = load_image(image_path)
    gray_image = convert_to_grayscale(image)
    thresh_image = apply_threshold(gray_image)
    contours = find_contours(thresh_image)

    widths, heights, grains = process_contours(contours, image, ppmm, min_contour_area)

    cv_width = calculate_coefficient_of_variance(widths)
    cv_height = calculate_coefficient_of_variance(heights)

    print(f"Coefficient of variance for width: {round(cv_width, 4)} mm")
    print(f"Coefficient of variance for height: {round(cv_height, 4)} mm")
    print(f"Grains count: {grains}")

    cv2.putText(
        image,
        f"Grains count: {grains}",
        (10, 30),
        cv2.FONT_HERSHEY_SIMPLEX,
        1,
        (0, 0, 255),
        2,
    )

    height = image.shape[0]
    cv2.putText(
        image,
        f"CV for width: {round(cv_width, 4)}mm",
        (10, height - 10),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (235, 30, 30),
        1,
    )
    cv2.putText(
        image,
        f"CV for height: {round(cv_height, 4)}mm",
        (10, height - 50),
        cv2.FONT_HERSHEY_SIMPLEX,
        0.6,
        (235, 30, 30),
        1,
    )

    scale_percent = 80  # percent of original size
    width = int(image.shape[1] * scale_percent / 100)
    height = int(image.shape[0] * scale_percent / 100)
    dim = (width, height)
    resized = cv2.resize(image, dim, interpolation=cv2.INTER_AREA)

    cv2.imshow("image", resized)
    cv2.imwrite(output_path, image)
    cv2.waitKey(0)
    cv2.destroyAllWindows()


if __name__ == "__main__":
    analyze_image("img/beans.jpg", "img/beans_output.jpg", 8.33, 300)

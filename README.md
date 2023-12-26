# Grain Analysis Tool

This project is a grain analysis tool developed in Python, leveraging the OpenCV library for image processing. The tool takes an image of grains as input, identify individual grains and calculate the width and height of each grain.

The tool also calculates the coefficient of variance for the widths and heights, providing a measure of the variability of grain size. The results are visualized directly on the image, with each grain enclosed in a rectangle and the dimensions displayed.

The output is a resized image that can be displayed and saved for further analysis. This tool is useful for researchers and professionals in agriculture, food science, and related fields who need to analyze grain size and distribution

## How it Works

The application follows these steps:

1. Load the image.
2. Convert the image to grayscale.
3. Apply a binary inverse threshold to the grayscale image.
4. Find contours in the thresholded image.
5. Process the contours:
    - For each contour, if its area is greater than a minimum contour area:
        - Draw a rectangle around the contour on the image.
        - Calculate the width and height of the rectangle in millimeters.
        - Write the width and height on the image.
        - Add the width and height to lists.
        - Increment a count of the grains.
6. Calculate the coefficient of variance for the widths and heights.
7. Write the count of grains and the coefficients of variance on the image.
8. Resize the image.
9. Display the image and save it to an output file.

## Code Structure

The code is organized into several functions:

- `load_image(image_path)`: Loads an image from a file.
- `convert_to_grayscale(image)`: Converts an image to grayscale.
- `apply_threshold(image)`: Applies a binary inverse threshold to an image.
- `find_contours(image)`: Finds contours in an image.
- `calculate_coefficient_of_variance(values)`: Calculates the coefficient of variance of a list of values.
- `process_contours(contours, image, ppmm, min_contour_area)`: Processes contours found in an image.
- `analyze_image(image_path, output_path, ppmm, min_contour_area)`: The main function that uses the above functions to analyze an image.

## Usage

To use this application, run the `worker.py` script. For example:

```bash
python worker.py
```

This will analyze the image `img/beans.jpg` and save the output to `img/beans_output.jpg`.


![](https://raw.githubusercontent.com/josehenriqueroveda/grain-analysis/main/grain_analysis/img/beans_output.jpg)


---

### Author:

> - 💻 **José Henrique Roveda**
> - 📨 Contact me on [LinkedIn](https://www.linkedin.com/in/jhroveda/)

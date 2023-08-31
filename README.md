# OpenCV Histogram Equalization

Histogram equalization is a basic image processing technique that adjusts the global contrast of an image by updating the image histogram’s pixel intensity distribution. Doing so enables areas of low contrast to obtain higher contrast in the output image.

Essentially, histogram equalization works by:
- Computing a histogram of image pixel intensities
- Evenly spreading out and distributing the most frequent pixel values (i.e., the ones with the largest counts in the histogram)
- Giving a linear trend to the cumulative distribution function (CDF)

The result of applying histogram equalization is an image with higher global contrast.

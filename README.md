# Frontal image maker with OpenCV and Deep Learning

This project makes your profile images frontal based on your landmarks' position. To detect landmarks [MTCNN network](https://github.com/ipazc/mtcnn) is used in this project, and you should install Tensorflow framework and Keras to be able to use it. To work with image processing part in this project you should install OpenCV library as well, so consider build it through CMake  on your machine.


## before:
![alter before](https://github.com/mrhajbabaei/frontal-image-maker-opencv/blob/master/images/img3.jpg)

## after:
![alter after](https://github.com/mrhajbabaei/frontal-image-maker-opencv/blob/master/images/rotated_img3.jpg)
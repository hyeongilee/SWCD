# Visual Place Recognition Under Substantial Appearance Changes Using Event-Based Data
* This work was conducted as a study of software convergence capstone design, a subject of Department of Software Convergence.

## Project Description
### Abstract
An event camera is a biologically inspired vision sensor which independently and
asynchronously records changes of brightness as they occur in each pixel. With its high
measurement rate, low latency, and high dynamic range properties, the sensor has a great
potential to overcome some limitations of conventional vision sensors. We focus on its
applicability in visual place recognition, which is one of the fundamental problems in
computer vision and robot applications. In this work, we propose a framework which
uses a convolutional neural network (CNN) architecture to train event-based images for
place recognition tasks in challenging weather and illumination conditions. We also
exploit data association for better image sequence matching. While showing insignificant effect when applied to conventional images, the matching algorithm contributes to
noticeable performance improvement using event-based images. We evaluate the performance of the proposed method using the synthetic and real-world dataset compared with
the state-of-the-art frameworks.

![fig2](https://user-images.githubusercontent.com/45928371/84344336-72cb2d80-abe5-11ea-9658-fac787b5c701.png)
Pipeline of the proposed method. The network is trained offline and tested using
event-based images and color images for evaluation.

## Getting Started
### Dependencies
* Pytorch
* Jupyter Notebook(.py version will be released)
* CUDA 10.2
* openCV

### Run
* When using synthetic data, download the dataset, and execute the code Event_Synthetic.ipynb.
* With real data, convert the event to images using such code 'event2image.py' and execute the code Event_real.ipynb

## License
* [MIT](https://choosealicense.com/licenses/mit/)


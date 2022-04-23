# Export Video to Jpeg
[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

This project is a experimental use of OpenCV Library to convert all frames of a video in jpeg images. It produces an image for every second of the video.

### Requirements
- OpenCV 3+
- Python 2.7+, 3.4+

### Installation
```

cd opencv-export-video-to-jpeg
```

### Use

If you want to convert a video in jpeg you can use:
```
python export.py -o output/ -i video.mov
```

If you want all the output images in gray scale you can use instead add ```-g``` arguments

example:

```
python export.py -o output/ -i video.mov -g
```

Show all commands use ```-h```

```
python export.py -h
```

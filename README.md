# Extract images from video in Python

### Required:

1. opencv-python
2. os (built-in module)
3. argparse (built-in module)

### Install required dependencies:

```
pip install opencv-python
```

### Usage:

```
python extractor.py --help
```

```
usage: extractor.py [-h] -p PATH video

a python script that extract images from video

positional arguments:
  video                 the video that you want to extract

options:
  -h, --help            show this help message and exit
  -p PATH, --path PATH  the directory you want to store your extracted images

```

### Example:

```
python extractor.py --path extracted test.mp4 
```
*it was extracted 893 images from 30 second video from the above example*
### Output:

<img src='./screenshot/demo.png'>
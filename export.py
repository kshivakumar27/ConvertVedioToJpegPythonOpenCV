import cv2 as cv
import math
import sys
import argparse
import os

parser = argparse.ArgumentParser(description='Convert all frames of a video in jpeg images')
parser.add_argument('-g', '--gray', help='Convert image in gray scale color', action='store_true')
parser.add_argument('-o', '--output', help='Output directory', default='output')
parser.add_argument('-i', '--input', help='Input video file', required=True)
parser.add_argument('--all-frames', help='Convert all frames', action='store_true')
parser.add_argument('--num-frames', help='Convert n frames from start', type=int, default=0)
parser.add_argument('-n', '--inverted', help='Invert color', action='store_true')

args = parser.parse_args()

DST_DIR = args.output
SRC_FILE = args.input
GRAY = args.gray
ALL_FRAMES = args.all_frames
NUM_FRAMES = args.num_frames
INVERTED = args.inverted

if not os.path.exists(DST_DIR):
  os.makedirs(DST_DIR)

video = cv.VideoCapture(SRC_FILE)

fps = video.get(cv.CAP_PROP_FPS)

while(video.isOpened()):
  frameIndex = video.get(cv.CAP_PROP_POS_FRAMES)
  ret, frame = video.read()

  if ret != True:
    break

  if ALL_FRAMES or NUM_FRAMES > 0 or frameIndex % math.floor(fps) == 0:
    filePath = DST_DIR + '/frame_' + str(int(frameIndex)) + '.jpg'

    if GRAY:
      frame = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    
    if INVERTED:
      frame = cv.bitwise_not(frame)

    cv.imwrite(filePath, frame)

    if NUM_FRAMES > 0 and not frameIndex < NUM_FRAMES:
      break

video.release()
cv.destroyAllWindows()
import os
import argparse
import shutil

from scipy.fft import dst

ap = argparse.ArgumentParser()

ap.add_argument('--dest', required=True, help='argument -src for source and -dest for destination')
ap.add_argument('--src', required=True, help='argument -src for source and -dest for destination')

path = os.path.join('yolov5', 'runs', 'detect')
shutil.rmtree(path)

args = ap.parse_args()

if not os.path.exists(args.src):

    if os.path.exists(args.dest):
        print("\nThe destination and source locations are invalid!!\n")
        exit()
    else:
        print("\nThe source file location is invalid!!\n")
        exit()

elif not os.path.exists(args.dest):
    print("\nThe destination location is invalid!!\n")
    exit()

os.system("python yolov5\\detect.py --weights best.pt --img 416 --conf 0.1 --source {}".format(args.src))

start = os.path.join(path, 'exp')
end = args.dest

for file in os.listdir(start):
    if file[-4:] != 'json':
        os.rename(os.path.join(start, file), os.path.join(start, file[:-4] + '_detected' + file[-4:]))
    else:
        os.rename(os.path.join(start, file), os.path.join(start, file[:-5] + '_detected' + file[-5:]))

for file in os.listdir(start):
    shutil.move(os.path.join(start, file), end)

print("\n\nResults have been moved from the location to {}".format(end))

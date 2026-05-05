import os
import sys

# This tells the app to look inside the AppImage for FFmpeg
if "APPDIR" in os.environ:
    os.environ["PATH"] = os.path.join(os.environ["APPDIR"], "usr", "bin") + os.path.pathsep + os.environ["PATH"]

from ffsubsync import ffsubsync
from gooey import Gooey

@Gooey(program_name="FFsubsync GUI")
def main():
    sys.argv[0] = 'ffsubsync'
    ffsubsync.main()

if __name__ == '__main__':
    main()

import sys
import picamera
import curses

def main(window):
    with picamera.PiCamera() as camera:
        camera.resolution = (1280, 720)
        camera.framerate = 24
        camera.start_preview()
        while True:
            window.addstr(0, 0, 'Press Q to quit')
            window.addstr(2, 0, 'Brightness: %5d (W/S)' % camera.brightness)
            window.addstr(3, 0, 'Contrast:   %5d (E/D)' % camera.contrast)
            window.addstr(4, 0, 'Saturation: %5d (R/F)' % camera.saturation)
            window.addstr(5, 0, 'Recording:  %5s (Space)' % camera.recording)
            window.refresh()
            c = sys.stdin.read(1).lower()
            if c == 'q':
                break
            elif c == 'w':
                camera.brightness = min(camera.brightness + 1, 100)
            elif c == 's':
                camera.brightness = max(camera.brightness - 1, 0)
            elif c == 'e':
                camera.contrast = min(camera.contrast + 1, 100)
            elif c == 'd':
                camera.contrast = max(camera.contrast - 1, -100)
            elif c == 'r':
                camera.saturation = min(camera.saturation + 1, 100)
            elif c == 'f':
                camera.saturation = max(camera.saturation - 1, -100)
            elif c == ' ':
                if camera.recording:
                    camera.stop_recording()
                else:
                    camera.start_recording('video.h264')

curses.initscr()
curses.wrapper(main)

import cv2

def main():
    argument = "rtsp://210.99.70.120:1935/live/cctv001.stream" #ex
    cap = cv2.VideoCapture(argument)

    if not cap.isOpened():
        print("Error: Unable to open camera")
        return

    recording = False

    contrast = 1.0
    brightness = 0
    flip = False

    print("Preview Mode")

    while True:
        ret, frame = cap.read()

        if not ret:
            print("Error: Failed to retrieve frame")
            break

        frame = apply_filters(frame, contrast, brightness, flip)

        if recording:
            cv2.circle(frame, (frame.shape[1] - 20, 20), 15, (0, 0, 255), -1)

        cv2.imshow('Camera Stream', frame)

        key = cv2.waitKey(1)
        if key == 27:
            break
        elif key == ord(' '):
            recording = not recording
            print("Record Mode" if recording else "Preview Mode")
        elif key == ord('+'):
            contrast += 0.1
            contrast = round(contrast, 1)
            print("Contrast:", contrast)
        elif key == ord('-'):
            contrast -= 0.1
            contrast = round(contrast, 1)
            print("Contrast:", contrast)
        elif key == ord('>'):
            brightness += 10
            print("Brightness:", brightness)
        elif key == ord('<'):
            brightness -= 10
            print("Brightness:", brightness)
        elif key == ord('f'):
            flip = not flip
            print("Flip:", flip)

    cap.release()
    cv2.destroyAllWindows()

def apply_filters(frame, contrast, brightness, flip):
    frame = cv2.convertScaleAbs(frame, alpha=contrast, beta=brightness)

    if flip:
        frame = cv2.flip(frame, 1)

    return frame

if __name__ == "__main__":
    main()

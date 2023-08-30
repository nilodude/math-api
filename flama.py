import cv2
import numpy as np

class Flama:

    def readFlama(self,numFrames):
        flama = cv2.VideoCapture('C:\\Users\\alfon\\Downloads\\candle2.mp4')
        video_fps = flama.get(cv2.CAP_PROP_FPS),
        total_frames = flama.get(cv2.CAP_PROP_FRAME_COUNT)
        height = flama.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = flama.get(cv2.CAP_PROP_FRAME_WIDTH)
        print(f"Frame Per second: {video_fps } \nTotal Frames: {total_frames} \n Height: {height} \nWidth: {width}")
        
        frames = []

        while True:
            ret, frame = flama.read()
            
            if not ret:
                break # break if no next frame
            
            cv2.imshow("frame",frame) # show frame    
            
            frames.append(frame)

            if cv2.waitKey(1) & 0xFF == ord('q'): # on press of q break
                break

        video = np.stack(frames, axis=0)

        # release and destroy windows
        flama.release()
        cv2.destroyAllWindows()

        return {"fps": video_fps[0], "height":height, "width": width}




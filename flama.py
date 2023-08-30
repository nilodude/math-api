import cv2

class Flama:

    def readFlama(self):
        flama = cv2.VideoCapture('C:\Users\alfon\Downloads\candle2.mp4')
        video_fps = flama.get(cv2.CAP_PROP_FPS),
        total_frames = flama.get(cv2.CAP_PROP_FRAME_COUNT)
        height = flama.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = flama.get(cv2.CAP_PROP_FRAME_WIDTH)
        
        while True:
            ret, frame = flama.read()
            
            if not ret:
                break # break if no next frame
            
            cv2.imshow(frame) # show frame    
            
            if cv2.waitKey(1) & 0xFF == ord('q'): # on press of q break
                break
        
        # release and destroy windows
        flama.release()
        cv2.destroyAllWindows()





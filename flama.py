import cv2
import numpy as np

class Flama:

    def readFlama(self,numFrames ):
        
        cropStartX2 = 850
        cropStartY2= 400
        videoHeight2 = 410

        flama = cv2.VideoCapture('C:\\Users\\alfon\\Downloads\\candle2.mp4')
        video_fps = flama.get(cv2.CAP_PROP_FPS),
        total_frames = flama.get(cv2.CAP_PROP_FRAME_COUNT)
        height = flama.get(cv2.CAP_PROP_FRAME_HEIGHT)
        width = flama.get(cv2.CAP_PROP_FRAME_WIDTH)
       
        print(f"Frame Per second: {video_fps } \nTotal Frames: {total_frames} \n Height: {height} \nWidth: {width}")
        
        videoHeight = videoHeight2
       
        cropStartX = cropStartX2
        cropEndX = cropStartX+int(videoHeight/2)
        cropStartY = cropStartY2
        cropEndY = cropStartY+videoHeight
                      
        hexFrames = []
        
        frameCount = 1

        while len(hexFrames) < numFrames + 80:
            hexFrame = []

            ret, frame = flama.read()
            
            if not ret:
                break # break if no next frame
            
            if(frameCount >= 80):
                gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
                cropped = gray[cropStartY:cropEndY,cropStartX:cropEndX].copy()
                resized = cv2.resize(cropped, (9, 17), interpolation = cv2.INTER_NEAREST_EXACT)
                ret,bina = cv2.threshold(resized,200,1,cv2.THRESH_BINARY)
                        
                print("{", end="")

                for row in range(1,17):
                    binString = ""
                    byte = bina[row]
                
                    for bit in range(1,9):
                        binString += str(byte[bit])
                
                    hexByte = "B"+str(binString)
                    # hexByte = int(binString,2)
                    hexFrame.append(hexByte)
                
                    if(row == 16):
                        print(str(hexByte), end="")
                    else:
                        print(str(hexByte)+",", end="")
                
                print("},")
            
                hexFrames.append(hexFrame)

                if cv2.waitKey(1) & 0xFF == ord('q'): # on press of q break
                    break
            
            frameCount+=1
        
        flama.release()
        cv2.destroyAllWindows()

        return hexFrames
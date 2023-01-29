import cv2
import numpy as np


def vid_params(vid_file):
    """Generates average frame color and average obj_count for
        a video."""
    
    # Initializing frame avg. color array
    # & object count array
    color_ar = []
    obj_c = []
    
    # Process video frame by frame
    cap = cv2.VideoCapture(vid_file)
    while(cap.isOpened()):
        ret, frame = cap.read()
        if ret==True:
            # Find average color of frame
            color_ar.append(avg_fColor(frame))
            
            # Use a canny edge detector
            # & count objects
            canny = cv2.Canny(frame, 80, 150)
            contours, hierarchy= cv2.findContours(canny, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
            obj_c.append(len(contours))
            
            # Exit
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        else:
            break
            
    # Exit the video
    cap.release()
    cv2.destroyAllWindows()

    return color_ar, obj_c

def avg_fColor(array):
    """Returns the average rgb value of the all the pixels
    of an image in decimal form"""
    import numpy as np
    
    # Find average for each of RGB
    avg_row = []
    for row in array:
        avg = np.average(row, axis=0)

        avg_row.append(avg)
        
    avg_rgb = np.average(avg_row, axis=0).astype(int)
    
    # Convert rgb to hex
    hex_c = '%02x%02x%02x' % tuple(avg_rgb)
    
    return int(hex_c, 16)
    

def batch_process(folder):
    """Runs vid_params for each video in folder &
        outputs an array of arrays for each parameter"""
    import os
    
    # List of files
    files = []
    
    # Iterate through each file in folder
    for filename in os.listdir(folder):
        f = os.path.join(folder, filename)
        
        # Checking if it is a file
        if os.path.isfile(f):
            files.append(f)
    
    # Array of parameters
    params = []
    for filename in files:
        l_arr = []
        param1, param2 = vid_params(filename)
        
        l_arr.append(param1)
        l_arr.append(param2)
        params.append(l_arr)
    
    return params
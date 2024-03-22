import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import cv2
def draw_point(event):
    """Take one point"""
    global points_pos, count_points
    
    if event.name == 'button_press_event' and event.dblclick:   
        x, y = int(event.xdata), int(event.ydata)
        plt.scatter(x, y, color='white', marker='x')
        plt.draw()
        points_pos.append((y, x))
        count_points += 1
        print(f'Position of {count_points}-th point: ({x}, {y})')

if __name__ == '__main__':
    # IMAGE FILE NAME YOU WANT TO READ
    image_path = 'C:/Users/Achilles2000/Desktop/Assignment2_Bayes/Assignment/data/' #change your dataset path
    img_filename = 'band4.gif'

    img = plt.imread(''.join([image_path, img_filename]))
    print('Input image size: {}' .format(img.shape))

    # TO STORE ANNOTATED POINTS
    points_pos = []
    count_points = 0

    num_points = int(input('How many points would you like to annotate? '))

    plt.figure()
    plt.imshow(img)
    plt.title('Move mouse pointer and double click to locate the position')
    plt.connect('button_press_event', draw_point)
    plt.show()

    # WRITE ANNOTATED IMAGE
    annotated_img = np.copy(img)  # Make a copy of the original image
    for point in points_pos:
        cv2.drawMarker(annotated_img, (point[1], point[0]), color=(255,255,255), markerType=cv2.MARKER_CROSS, markerSize=5)

    img_save_filename = ''.join([
        image_path, 
        'annotated_', img_filename.split('.')[0], 
        '_np_', str(len(points_pos)), 
        '.png'
    ])
    plt.imsave(img_save_filename, annotated_img)

    # SAVE ANNOTATED POINTS AS CSV FILE
    pd.DataFrame(
        data=np.asarray(points_pos), 
        columns=['row', 'column']
    ).to_csv(''.join([
        image_path, 
        'annotated_points_', img_filename.split('.')[0], 
        '_np_', str(len(points_pos)), 
        '.csv'
    ]), index=False)

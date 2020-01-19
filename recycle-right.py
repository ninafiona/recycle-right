# partly based on code from rohanpillai20

import cv2
import time 
import numpy as np
import os
import cv2
import time
import tensorflow as tf

cam = cv2.VideoCapture(1)
ret, frame = cam.read()
cv2.imshow("RECYCLE RIGHT !", frame)

print("\n\n\n\n\n\nHi there!\n")
print("Is your item recycable? Hold it in front of the camera to find out ... ")

while True:
    ret, frame = cam.read()
    cv2.imshow("RECYCLE RIGHT !", frame)
    k = cv2.waitKey(1000)
    if k != -1:
        cv2.imwrite("new_item.jpg", frame)
        try: 
            image_size=128
            num_channels=3
            images = []
            image = cv2.imread("new_item.jpg")
            image = cv2.resize(image, (image_size, image_size),0,0, cv2.INTER_LINEAR)
            images.append(image)
            images = np.array(images, dtype=np.uint8)
            images = images.astype('float32')
            images = np.multiply(images, 1.0/255.0) 
            x_batch = images.reshape(1, image_size,image_size,num_channels)
            sess = tf.Session()
            saver = tf.train.import_meta_graph('models/trained_model.meta')
            saver.restore(sess, tf.train.latest_checkpoint('./models/'))
            graph = tf.get_default_graph()
            y_pred = graph.get_tensor_by_name("y_pred:0")
            x= graph.get_tensor_by_name("x:0") 
            y_true = graph.get_tensor_by_name("y_true:0") 
            y_test_images = np.zeros((1, 4)) 
            feed_dict_testing = {x: x_batch, y_true: y_test_images}
            result=sess.run(y_pred, feed_dict=feed_dict_testing)
            # print(result)
            a = result[0].tolist()
            r=0
            max1 = max(a)
            index1 = a.index(max1)
            classes = ["Lid","Napkin", "Plastic Fork", "Red Bull Can"]
            predicted_class = classes[index1]
            for i in a:
                if i!=max1:
                    if max1-i<i:
                        r=1                           
            if r ==0:
                if index1 == 0 or index1 == 3:
                    output = "A " + predicted_class + " is recycable! Yay!"
                    print(output)
                if index1 == 1 or index1 == 2:
                    output = "OOps! A " + predicted_class + " is NOT recycable!"
                    print(output)
            else:
                print("Could not classify with definite confidence")
                if index1 == 0 or index1 == 3:
                    output = "Is it maybe a " + predicted_class + "? Then yes, it is recycable!"
                    print(output)
                if index1 == 1 or index1 == 2:
                    output = "Is it maybe a " + predicted_class + "? Then nooo ... it is NOT recycable!"
                    print(output)
        except Exception as e:
            print("Exception:",e)

cam.release()

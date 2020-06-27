import pandas as pd
import numpy as np
import random
from random import randint

def get_augment_index(df_Y, augmentation_amount, n_steps):

    frame_amount = df_Y["amount"].tolist()
    cumulative_sum = df_Y["cumulative_sum"].tolist()

    random_frame = []
    Y = []

    for i in range(len(frame_amount)):
        Y_temp = []
        z = int(frame_amount[i]/(n_steps-1))
        y = int((frame_amount[i]-z*(n_steps-1))/2)
    
        if frame_amount[i]<n_steps:
            print("less than ", n_steps, "!")
            print(i, frame_amount[i])

        if y+n_steps > frame_amount[i]:
            print(i, "baseline error!", y)

        r = []

        #for picking n_steps frames
        for j in range(n_steps):
            if frame_amount[i] > y+j*z:
                if i==0:
                    Y_temp.append(y + j*z)
                else:
                    Y_temp.append(y + j*z + cumulative_sum[i-1])
            elif frame_amount[i] == y+j*z:
                print(i, "th video : hit the limit!")
                Y_temp.append(y + j*z-1 + cumulative_sum[i-1])
            else:
                print(i,"th video : out of frame length bound!")

        Y_temp = np.array(Y_temp)
        Y.append(Y_temp)


        #augment augmentation_amount
        for j in range(augmentation_amount):
            if z==0:  #the case for frame number is less than 50. add frames randomly.
                r = list(range(0, frame_amount[i]))
                random_adding_frame_array = random.sample(r, 50-frame_amount[i]) #extract 50-test_frame_amount[i] index
                random_adding_frame_array.sort()
       
                print("these indexes will be added", random_adding_frame_array)
        
                for k in range(50-frame_amount[i]):
                    r.insert(random_adding_frame_array[k]+1, r[random_adding_frame_array[k]])
                r = np.array(r)

                if i != 0:
                    for k in range(n_steps):
                        r[k] += cumulative_sum[i-1]
      
                print("result : ", r)
      
            elif z==1:
                sample_array = list(range(y, frame_amount[i]))
                r = random.sample(sample_array, n_steps)
                r.sort()
                r = np.array(r)

                if i != 0:
                    for k in range(n_steps):
                        r[k] += cumulative_sum[i-1]

            else:
                r = [random.randint(1, z) for iter in range(49)]
                r.append(0)
                r = np.array(r)
                r = np.cumsum(r)

                if i != 0:
                    for k in range(n_steps):
                        r[k] += cumulative_sum[i-1]

            Y.append(r)

    return Y

def index_to_list(X_, Y, n_steps):
    ##X and Y must be python list

    augmented_X = []
    index=0
    while index < len(Y): #total frame for result : 560 * augmentation amount
        print("video " , index+1, "/", len(Y), end="\r")

        for j in range(n_steps):
            augmented_X.append(X_[Y[index][j]])
      
        index+=1

    return np.array(augmented_X)
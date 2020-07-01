import numpy as np

def get_y(augmentation_amount, own_added):
    y_test = []
    y_pre_train = []
	
    ##y_test
    for i in range(35):
        for j in range(4*augmentation_amount):
            y_test.append(i)
	
    y_test = np.asarray(y_test)
	
    ##y_pre_train *-* before validation split   
    for i in range(35):
        for j in range(16*augmentation_amount):
            y_pre_train.append(i)
    
    if own_added:
        for i in range(4):
            for j in range(35):
                for k in range(5*augmentation_amount):
                    y_pre_train.append(j)

    y_pre_train = np.asarray(y_pre_train)
    
    return y_pre_train, y_test
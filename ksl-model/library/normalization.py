import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler, StandardScaler
from sklearn.externals import joblib

##every data should be in pandas dataframe

class ConvertNormalization:
        def __init__(self, method="minmax"):
            self.scaler = None
            self.method = method
        
            if method == "minmax":
                self.scaler = MinMaxScaler()
            elif method == "standard":
                self.scaler = StandardScaler()
            
        def convert_fit(self, points):
            self.scaler.fit(points)
        
        def convert_fit_transform(self, points):
            return self.scaler.fit_transform(points)
        
        def convert_transform(self, target_points):
            return self.scaler.transform(target_points)
           
        def save_normalization_model(self, path):
            joblib.dump(self.scaler, path)
            
def get_header(df_data, what_about_face):
    columns = ["nose_x","nose_y","neck_x","neck_y","r_shoulder_x","r_shoulder_y","r_elbow_x","r_elbow_y","r_wrist_x","r_wrist_y","l_shoulder_x","l_shoulder_y",
               "l_elbow_x","l_elbow_y","l_wrist_x","l_wrist_y","r_eye_x","r_eye_y","l_eye_x","l_eye_y","r_ear_x","r_ear_y","l_ear_x","lear_y","face_0_x","face_0_y",
               "face_1_x","face_1_y","face_2_x","face_2_y","face_3_x","face_3_y","face_4_x","face_4_y","face_5_x","face_5_y","face_6_x","face_6_y","face_7_x","face_7_y",
               "face_8_x","face_8_y","face_9_x","face_9_y","face_10_x","face_10_y","face_11_x","face_11_y","face_12_x","face_12_y","face_13_x","face_13_y","face_14_x",
               "face_14_y","face_15_x","face_15_y","face_16_x","face_16_y","face_17_x","face_17_y","face_18_x","face_18_y","face_19_x","face_19_y","face_20_x","face_20_y",
               "face_21_x","face_21_y","face_22_x","face_22_y","face_23_x","face_23_y","face_24_x","face_24_y","face_25_x","face_25_y","face_26_x","face_26_y","face_27_x",
               "face_27_y","face_28_x","face_28_y","face_29_x","face_29_y","face_30_x","face_30_y","face_31_x","face_31_y","face_32_x","face_32_y","face_33_x","face_33_y",
               "face_34_x","face_34_y","face_35_x","face_35_y","face_36_x","face_36_y","face_37_x","face_37_y","face_38_x","face_38_y","face_39_x","face_39_y","face_40_x",
               "face_40_y","face_41_x","face_41_y","face_42_x","face_42_y","face_43_x","face_43_y","face_44_x","face_44_y","face_45_x","face_45_y","face_46_x","face_46_y",
               "face_47_x","face_47_y","face_48_x","face_48_y","face_49_x","face_49_y","face_50_x","face_50_y","face_51_x","face_51_y","face_52_x","face_52_y","face_53_x",
               "face_53_y","face_54_x","face_54_y","face_55_x","face_55_y","face_56_x","face_56_y","face_57_x","face_57_y","face_58_x","face_58_y","face_59_x","face_59_y",
               "face_60_x","face_60_y","face_61_x","face_61_y","face_62_x","face_62_y","face_63_x","face_63_y","face_64_x","face_64_y","face_65_x","face_65_y","face_66_x",
               "face_66_y","face_67_x","face_67_y","face_68_x","face_68_y","face_69_x","face_69_y","l_hand_0_x","l_hand_0_y","l_hand_1_x","l_hand_1_y","l_hand_2_x","l_hand_2_y",
               "l_hand_3_x","l_hand_3_y","l_hand_4_x","l_hand_4_y","l_hand_5_x","l_hand_5_y","l_hand_6_x","l_hand_6_y","l_hand_7_x","l_hand_7_y","l_hand_8_x","l_hand_8_y",
               "l_hand_9_x","l_hand_9_y","l_hand_10_x","l_hand_10_y","l_hand_11_x","l_hand_11_y","l_hand_12_x","l_hand_12_y","l_hand_13_x","l_hand_13_y","l_hand_14_x",
               "l_hand_14_y","l_hand_15_x","l_hand_15_y","l_hand_16_x","l_hand_16_y","l_hand_17_x","l_hand_17_y","l_hand_18_x","l_hand_18_y","l_hand_19_x","l_hand_19_y",
               "l_hand_20_x","l_hand_20_y","r_hand_0_x","r_hand_0_y","r_hand_1_x","r_hand_1_y","r_hand_2_x","r_hand_2_y","r_hand_3_x","r_hand_3_y","r_hand_4_x","r_hand_4_y",
               "r_hand_5_x","r_hand_5_y","r_hand_6_x","r_hand_6_y","r_hand_7_x","r_hand_7_y","r_hand_8_x","r_hand_8_y","r_hand_9_x","r_hand_9_y","r_hand_10_x","r_hand_10_y",
               "r_hand_11_x","r_hand_11_y","r_hand_12_x","r_hand_12_y","r_hand_13_x","r_hand_13_y","r_hand_14_x","r_hand_14_y","r_hand_15_x","r_hand_15_y","r_hand_16_x",
               "r_hand_16_y","r_hand_17_x","r_hand_17_y","r_hand_18_x","r_hand_18_y","r_hand_19_x","r_hand_19_y","r_hand_20_x","r_hand_20_y"]

    if what_about_face == 0: #no face
        temp_columns=columns[:24]
        temp_columns.extend(columns[164:248])
        df_data.columns = temp_columns

    elif what_about_face == 1: #minmum face
        temp_columns=columns[:24]
        temp_columns.extend(columns[96:144])
        temp_columns.extend(columns[164:248])
        df_data.columns = temp_columns

    else: #full face
        df_data.columns = columns

    df_column = df_data.columns

    return df_data, df_column
    
def set_standard_point(df_X):
    temp = []

    for no, row in df_X.iterrows():
        standard_x, standard_y = row[[2, 3]]
        result = []
    
        for i in range(len(row)):
            if i % 2 == 0:
                result.append(row[i] - standard_x)
            else:
                result.append(row[i] - standard_y)
                
        temp.append(result)

    return pd.DataFrame(temp)

def wh_method(df_train, df_test):
    idx = 0
    width = 1280
    height = 720

    for feature in df_column:
        if idx % 2 == 0:
            df_train[feature] = df_train[feature] / width
            df_test[feature] = df_test[feature] / width
        else:
            df_train[feature] = df_train[feature] / height
            df_test[feature] = df_test[feature] / height
          
        idx += 1
    
    return df_train, df_test

def seperate_2D(df_data):
    df_data_x = df_data.iloc[:,::2]
    df_data_y = df_data.iloc[:,1::2]
    
    return df_data_x, df_data_y

def object_normalization(df_train, df_test, df_column, what_about_face):
    conv_pose_norm = ConvertNormalization(method="standard")
    conv_face_norm = ConvertNormalization(method="standard")
    conv_left_hand_norm = ConvertNormalization(method="standard")
    conv_right_hand_norm = ConvertNormalization(method="standard")
    
    test_normalization = None
    
    if what_about_face == 0:
        train_pose_normalization = conv_pose_norm.convert_fit_transform(df_train.loc[:,df_column[:12]])         
        train_left_hand_normalization = conv_left_hand_norm.convert_fit_transform(df_train.loc[:,df_column[12:33]])                    
        train_right_hand_normalization = conv_right_hand_norm.convert_fit_transform(df_train.loc[:,df_column[33:]])                  
        train_normalization = np.c_[train_pose_normalization, train_left_hand_normalization, train_right_hand_normalization]
        
        if not df_test.empty:
            test_pose_normalization = conv_pose_norm.convert_transform(df_test.loc[:,df_column[:12]])
            test_left_hand_normalization = conv_left_hand_norm.convert_transform(df_test.loc[:,df_column[12:33]])
            test_right_hand_normalization = conv_right_hand_norm.convert_transform(df_test.loc[:,df_column[33:]])
            test_normalization = np.c_[test_pose_normalization, test_left_hand_normalization, test_right_hand_normalization]
            
    elif what_about_face == 1:
        train_pose_normalization = conv_pose_norm.convert_fit_transform(df_train.loc[:,df_column[:12]])
        train_face_normalization = conv_face_norm.convert_fit_transform(df_train.loc[:,df_column[12:36]])
        train_left_hand_normalization = conv_left_hand_norm.convert_fit_transform(df_train.loc[:,df_column[36:57]])
        train_right_hand_normalization = conv_right_hand_norm.convert_fit_transform(df_train.loc[:,df_column[57:]])
        train_normalization = np.c_[train_pose_normalization, train_face_normalization, train_left_hand_normalization, train_right_hand_normalization]
        
        if not df_test.empty:
            test_pose_normalization = conv_pose_norm.convert_transform(df_test.loc[:,df_column[:12]])
            test_face_normalization = conv_face_norm.convert_transform(df_test.loc[:,df_column[12:36]])
            test_left_hand_normalization = conv_left_hand_norm.convert_transform(df_test.loc[:,df_column[36:57]])
            test_right_hand_normalization = conv_right_hand_norm.convert_transform(df_test.loc[:,df_column[57:]])
            test_normalization = np.c_[test_pose_normalization, test_face_normalization, test_left_hand_normalization, test_right_hand_normalization]
    
    elif what_about_face == 2:
        train_pose_normalization = conv_pose_norm.convert_fit_transform(df_train.loc[:,df_column[:12]])
        train_face_normalization = conv_face_norm.convert_fit_transform(df_train.loc[:,df_column[12:82]])
        train_left_hand_normalization = conv_left_hand_norm.convert_fit_transform(df_train.loc[:,df_column[82:103]])
        train_right_hand_normalization = conv_right_hand_norm.convert_fit_transform(df_train.loc[:,df_column[103:]])
        train_normalization = np.c_[train_pose_normalization, train_face_normalization, train_left_hand_normalization, train_right_hand_normalization]
        
        if not df_test.empty:
            test_pose_normalization = conv_pose_norm.convert_transform(df_test.loc[:,df_column[:12]])
            test_face_normalization = conv_face_norm.convert_transform(df_test.loc[:,df_column[12:82]])
            test_left_hand_normalization = conv_left_hand_norm.convert_transform(df_test.loc[:,df_column[82:103]])
            test_right_hand_normalization = conv_right_hand_norm.convert_transform(df_test.loc[:,df_column[103:]])
            test_normalization = np.c_[test_pose_normalization, test_face_normalization, test_left_hand_normalization, test_right_hand_normalization]
     
    return train_normalization, test_normalization

def standard_method(df_train, df_test, model_path, what_about_face, df_column):
    
    df_train_x, df_train_y = seperate_2D(df_train)
    df_test_x = pd.DataFrame()
    df_test_y = pd.DataFrame()
    print(df_test_x)

    if not df_test.empty:
        df_test_x, df_test_y = seperate_2D(df_test)
        print(df_test_x)
        
    df_column_x = df_column[::2]
    df_column_y = df_column[1::2]
    
    train_x_normalization, test_x_normalization = object_normalization(df_train_x, df_test_x, df_column_x, what_about_face)
    train_y_normalization, test_y_normalization = object_normalization(df_train_y, df_test_y, df_column_y, what_about_face)
    
    train_normalization = np.c_[train_x_normalization, train_y_normalization]
    test_normalization = None
    if not df_test.empty:
        test_normalization = np.c_[test_x_normalization, test_y_normalization]

    #    conv_norm.save_normalization_model(model_path)

    return pd.DataFrame(train_normalization), pd.DataFrame(test_normalization)

def norm(df_train, method, model_path, do_set_standard_point, what_about_face, df_test = pd.DataFrame()):
    
    df_train, df_column = get_header(df_train, what_about_face)
    if not df_test.empty:
        df_test, df_column = get_header(df_test, what_about_face)

    if do_set_standard_point:
        df_train = set_standard_point(df_train)
        if not df_test.empty:
            df_test = set_standard_point(df_test)
    
    if method == "wh":
        df_train, df_test = wh_method(df_train, df_test)
        
    elif method == "standard":
        df_train, df_test = standard_method(df_train, df_test, model_path, what_about_face, df_column)

    return df_train, df_test
    
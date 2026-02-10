import json
import pickle
import numpy as np
__location = None
__data_col = None
__model = None
def model_predict(location,sqft,bhk,bath):
    global __data_col
    global __model
    try:
        loc_index = __data_col.index(location.lower())
    except:
        loc_index = -1
    x = np.zeros(len(__data_col))
    x[0] = sqft
    x[1] = bhk
    x[2]= bath
    if loc_index >=0:
        x[loc_index]=1
    return round(__model.predict([x])[0],2)
def get_artifact_names():
    global __model
    global __data_col
    global __location

    with open("./artifact/columns.json","r") as f:
        __data_col = json.load(f)['colmn']
        __location = __data_col[3:]
    if __model is None:
        with open("./artifact/bng_house.pickle","rb") as f:
            __model = pickle.load(f)
def get_location_names():
    return __location
def get_data_columns():
    return __data_col

if __name__ == '__main__':
    get_artifact_names()
    print(get_location_names())
    print(model_predict('Vijayanagar',1000,3,2))


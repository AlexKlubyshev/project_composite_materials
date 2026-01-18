import numpy as np
import pickle

def calc_density(area,density,modulus,hardener,epoxy,surf_density,resin,angle,step,stitch_dens):
    #area = preprocess(area)
    #y = 300000 * area

    y = process([preprocess(area),
                 preprocess(density),
                 preprocess(modulus),
                 preprocess(hardener),
                 preprocess(epoxy),
                 preprocess(surf_density),
                 preprocess(resin),
                 preprocess(angle),
                 preprocess(step),
                 preprocess(stitch_dens),
                 preprocess(density)*preprocess(surf_density)],"")
    return y

def preprocess(param):
    try:
        param = float(param)
    except Exception as e:
        param=0
    return param      

def process(lst_data,path):
    model = load_model(path)
    y = model.predict(np.array([lst_data]))
    return y

def load_model(path):
    model = pickle.load(open('./models/gradient_boosting_model.pkl', 'rb'))
    return model
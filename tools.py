import pickle
import numpy as np
import sklearn
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

def model(parametres):
    parametres=np.array(parametres).reshape(1,-1)

    cls=pickle.load(open("cls_banking.pkl", "rb"))
    if (cls.predict(parametres)[0])== 1 :
        result="Accepter"
    else:
        result="Refuser"
    

    return (result, round(cls.predict_proba(parametres).max(),3))
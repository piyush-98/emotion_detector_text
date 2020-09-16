import numpy as np
from pickle import load
from flask import Flask,request
import json 
import nltk
nltk.download('stopwords')
nltk.download('wordnet')
from nltk.corpus import stopwords
stop = stopwords.words('english')
# from helpers import *
from tensorflow.keras.models import load_model
import pandas as pd
import re
from textblob import Word



model_file_name = r'model.h5'
glove_file_name = r'glove_dict.pickle'
label_dict={'0':'anger','1':'fear','2':'joy','3':'love','4':'sadness','5':'surprise'}

model = None
with open(glove_file_name, 'rb') as handle:
    glove_dict = load(handle)

def load__model():
    '''
    Loads the deep learning model
    '''
    global model
    model = load_model(model_file_name)
def text_preprocess(X:str):
    def de_repeat(text):
        pattern = re.compile(r"(.)\1{2,}")
        return pattern.sub(r"\1\1", text)
    ls=[X]
    test=pd.DataFrame(ls)
    #Making all letters lowercase
    test[0] = test[0].apply(lambda x: " ".join(x.lower() for x in x.split()))
    #Removing Punctuation, Symbols
    test[0] = test[0].str.replace('[^\w\s]',' ')
    #Removing Stop Words using NLTK
    test[0] = test[0].apply(lambda x: " ".join(x for x in x.split() if x not in stop))
    #Lemmatisation
    test[0] = test[0].apply(lambda x: " ".join([Word(word).lemmatize() for word in x.split()]))
    test[0] = test[0].apply(lambda x: " ".join(de_repeat(x) for x in x.split()))
    return test.iloc[0,0]

def testing(X:str):
    embedding_matrix_output = np.zeros((1,45,100))
    sent = X.split()
    for jx in range(len(sent)):
            try:
                embedding_matrix_output[0][jx] = glove_dict[sent[jx].lower()]
            except:
                continue
            
    return embedding_matrix_output

def make_prediction(X:str):
    '''
    returns the prediction from the model
    '''
    vec=testing(X)
    pred=model.predict(vec)
    return pred.argmax(axis=-1)
   
app = Flask(__name__)
@app.route("/",methods=["GET","POST"])
def hello():
    data = {
        "success": False
    }
    if request.method=="POST":
        if request.args.get("text"):
            text = request.args.get('text', '')
            # try:
            cleaned_text = text_preprocess(text)
            prediction = make_prediction(cleaned_text)
            data["result"] = str(prediction[0])
            data["success"] = True
            # except Exception:
            #     data["error_message"] = "Sorry some internal server error occured"
    return json.dumps(data)

# if __name__=="main_":
load__model()
app.run(host ='0.0.0.0',debug=True, port=5001)

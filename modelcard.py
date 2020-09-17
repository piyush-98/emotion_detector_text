model_card={
    "type": "text classification",
    "prediction_type":"multiclass classification",
    "dataset_used": "https://git.unbiased.cc/unbiased-intelligence-hub/emotion_detector_text/-/tree/master/Data",
    "output_labels": {'0':'anger','1':'fear','2':'joy','3':'love','4':'sadness','5':'surprise'},
    
    "model_unit": "LSTM",
    "used_pretrained_embeddings": 'true',
    'pretrained_embedding':'glove.6B.100d',
    "val_accuracy": '93.3',
    "usage": "emotion_recognition_text",
    "model_size": "2.89 MB",
    "input_data_type": "Tensor with a shape of (No_of_sentences,45,100)",
    "backend": "Tensorflow Keras",
    "trained_on": "8 GB RAM",
    "classification_report":{
        '0':{'precision':'0.97','recall':'0.89','f1_score':'0.93'},
        '1':{'precision':'0.92','recall':'0.88','f1_score':'0.90'},
        '2':{'precision':'0.91','recall':'0.99','f1_score':'0.95'},
        '3':{'precision':'0.99','recall':'0.67','f1_score':'0.80'},
        '4':{'precision':'0.97','recall':'0.97','f1_score':'0.97'},
        '5':{'precision':'0.67','recall':'0.94','f1_score':'0.78'},
        'overall':{'precision':'0.94','recall':'0.93','f1_score':'0.93'}
    }
}
import json
with open('model_card.json', 'w') as fp:
    json.dump(model_card, fp)
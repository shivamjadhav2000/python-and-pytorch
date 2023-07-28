import numpy as np
import torch
import json
from Model import NeuralNet
from spacy_utils import tokenize_lemma,bag_of_words
import random

with open('intents.json') as f:
    intents=json.load(f)

device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

FILE='my_model.pth'
data=torch.load(FILE)
all_words=data['all_words']
model_state=data['model_state']
tags=data['tags']
input_size=data['input_size']
output_size=data['output_size']
hidden_size=data['hidden_size']



model=NeuralNet(input_size,hidden_size,output_size)
model.load_state_dict(model_state)
model.eval()
bot_name='shiva'
while True:
    print('hey iam shiva ,lets Chat enter "quit" to exit')
    sentence=input("you:")
    if sentence=='quit':
        break
    else:
        sentence=tokenize_lemma(sentence)
        X=bag_of_words(sentence,all_words)
        X=X.reshape(1,X.shape[0]).astype(np.float)
        X=torch.tensor(X)
        output=model(X)
        _,predicted=torch.max(output,dim=1)
        tag=tags[predicted.item()]
        probs=torch.softmax(output,dim=1)
        prob=probs[0][predicted.item()]
        print("prob:",prob,tag)
        if prob>=0.75:
            for intent in intents['intents']:
                if tag==intent['tag']:
                    print(f"{bot_name}:{random.choice(intent['responses'])}")
        else:
            print(f"{bot_name}:I do not undestand...")

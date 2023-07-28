import json
import numpy as np
from spacy_utils import tokenize_lemma,bag_of_words 

import torch
import torch.nn as nn
from torch.utils.data import Dataset, DataLoader
from Model import NeuralNet

with open('intents.json') as f:
    intents=json.load(f)

all_words=[]
tags=[]
X_data=[]
y_data=[]
data=[]
for intent in intents['intents']:
    tag=intent['tag']
    tags.append(tag)
    for pattern in intent['patterns']:
        w=tokenize_lemma(pattern)
        all_words.extend(w)
        data.append((w,tag))
ignore_words=['?',",","'",".","!"]
all_words=[word for word in all_words if word not in ignore_words]
# remove duplicates and sort
all_words = sorted(set(all_words))
tags = sorted(set(tags))

for x,y in data:
    bag=bag_of_words(x,all_words)
    X_data.append(bag)
    y_data.append(tags.index(y))

X_train=np.array(X_data)
Y_train=np.array(y_data)


#hyperparameters
batch_size=8
num_epochs=1000
learning_rate=0.001
input_size=len(X_train[0])
hidden_size=8
output_size=len(tags)

class ChatDataset(Dataset):
    def __init__(self):
        self.n_samples=len(X_train)
        self.x_data = X_train.astype(np.float)
        self.y_data = Y_train.astype(np.float)
    #supporting indexing in oreder to model can use dataset using index
    def __getitem__(self,index):
        return self.x_data[index], self.y_data[index]
    def __len__(self):
        return self.n_samples

dataset=ChatDataset()

train_loader=DataLoader(dataset=dataset,
                        batch_size=batch_size,
                        shuffle=True,
                        num_workers=0)
device=torch.device('cuda' if torch.cuda.is_available() else 'cpu')

model=NeuralNet(input_size,hidden_size,output_size).to(device)

#loss and optimizer

criterion=nn.CrossEntropyLoss()

optimizer=torch.optim.Adam(model.parameters(),lr=learning_rate)

#train the model
for epoch in range(num_epochs):
    for (words,labels) in train_loader:
        words=words.to(device)
        labels=labels.to(dtype=torch.long).to(device)

        # forward pass
        outputs=model.forward(words)
        loss=criterion(outputs,labels)

        # backward pass
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()
        
    if (epoch+1)%100==0:
        print(f"epoch  [{epoch+1}/{num_epochs}] loss :{loss.item():.8f}")
        

data={
    'model_state':model.state_dict(),
    'input_size':input_size,
    'output_size':output_size,
    'hidden_size':hidden_size,
    'all_words':all_words,
    'tags':tags
}

FILE='my_model.pth'
torch.save(data,FILE)
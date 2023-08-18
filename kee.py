import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import json
import pickle
import tensorflow
import numpy as np
from tensorflow.keras.models import Sequential
from tensorflow.keras.layers import Dense, Dropout , Activation, Flatten , Conv2D, MaxPooling2D
from tensorflow.keras.optimizers import SGD
import random
words=[]
labels = []
docs = []
ignore_list = ['?', '!','.']
dataset = open('intents.json').read()
intents = json.loads(dataset)
for intent in intents['intents']:
    for pattern in intent['patterns']:
        word_token = nltk.word_tokenize(pattern)
        words.extend(word_token)
        docs.append((word_token, intent['tag']))
        if intent['tag'] not in labels:
            labels.append(intent['tag'])
words = [lemmatizer.lemmatize(word.lower()) for word in words if word not in ignore_list]
words = sorted(list(set(words)))
labels = sorted(list(set(labels)))
pickle.dump(words,open('words.pkl','wb'))
pickle.dump(labels,open('labels.pkl','wb'))
# creating our training data:
training_data = []

output = [0]*len(labels)

for doc in docs:
    bag_of_words = []
    pattern_words = doc[0]
    pattern_words = [lemmatizer.lemmatize(word.lower()) for word in pattern_words]
    
    for w in words:
        if w in pattern_words:
            bag_of_words.append(1)
        else:
            bag_of_words.append(0)
            
    output_row = list(output)
    output_row[labels.index(doc[1])] = 1
    
    training_data.append([bag_of_words,output_row])
random.shuffle(training_data)
training_data = np.array(training_data)
x_train = list(training_data[:,0])
y_train = list(training_data[:,1])
# Creating Model:

model = Sequential()
model.add(Dense(128, input_shape=(len(x_train[0]),), activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(64, activation='relu'))
model.add(Dropout(0.5))
model.add(Dense(len(y_train[0]), activation='softmax'))
model.summary()
sgd_optimizer = SGD(lr=0.01, decay=1e-6, momentum=0.9, nesterov=True)
model.compile(loss='categorical_crossentropy', optimizer=sgd_optimizer, metrics=['accuracy'])
history = model.fit(np.array(x_train), np.array(y_train), epochs=200, batch_size=5, verbose=1)
model.save('chatbot_Application_model.h5', history)
import nltk
from nltk.stem import WordNetLemmatizer
lemmatizer = WordNetLemmatizer()
import pickle
import numpy as np
import json
import random
from keras.models import load_model

model = load_model('chatbot_Application_model.h5')

intents = json.loads(open('intents.json').read())
words = pickle.load(open('words.pkl','rb'))
labels = pickle.load(open('labels.pkl','rb'))


def bank_of_words(s,words, show_details=True):
    bag_of_words = [0 for _ in range(len(words))]
    sent_words = nltk.word_tokenize(s)
    sent_words = [lemmatizer.lemmatize(word.lower()) for word in sent_words]
    for sent in sent_words:
        for i,w in enumerate(words):
            if w == sent:
                bag_of_words[i] = 1
    return np.array(bag_of_words)

def predict_label(s, model):
    pred = bank_of_words(s, words,show_details=False)
    response = model.predict(np.array([pred]))[0]
    ERROR_THRESHOLD = 0.25
    final_results = [[i,r] for i,r in enumerate(response) if r>ERROR_THRESHOLD]
    final_results.sort(key=lambda x: x[1], reverse=True)
    return_list = []
    for r in final_results:
        return_list.append({"intent": labels[r[0]], "probability": str(r[1])})
    return return_list

def Response(ints, intents_json):
    tags = ints[0]['intent']
    list_of_intents = intents_json['intents']
    for i in list_of_intents:
        if(i['tag']== tags):
            response = random.choice(i['responses'])
            break
    return response

def chatbot_response(msg):
    ints = predict_label(msg, model)
    response = Response(ints, intents)
    return response
            
def chat():
    print("Start chat with ChatBot of Project Gurukul")
    while True:
        inp = input("You: ")
        if inp.lower() == 'quit':
            break
        response = chatbot_response(inp)
        print("\n BOT: " + response + '\n\n')

chat()
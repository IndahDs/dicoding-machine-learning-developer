# -*- coding: utf-8 -*-
"""Proyek NLP.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1XTRP4vGufYHEGpxagpFFZ82lhI_aSyML

Proyek NLP-Indah Dwi Sulistiyawati
dsindah87@students.unnes.ac.id

sumber dataset : https://www.kaggle.com/lokkagle/movie-genre-data

###Klasifikasi Genre Film Multikelas dengan LSTM
"""

#Import library yang akan digunakan
import pandas as pd
import re


#split data
from sklearn.model_selection import train_test_split

#preprocessing dan layer
import tensorflow as tf
from tensorflow.keras.preprocessing.text import Tokenizer
from tensorflow.keras.preprocessing.sequence import pad_sequences
from tensorflow.keras.layers import LSTM,Dense,Embedding,Dropout
from tensorflow.keras.models import Sequential
from tensorflow.keras.optimizers import Adam

#plotting visualisasi
import matplotlib.pyplot as plt

#upload dataet
from google.colab import files
files.upload()

#baca dan menampilkan 5 data teratas
df = pd.read_csv("kaggle_movie_train.csv")
df.head()

df.tail()

#cek jumlah value setiap genre
df['genre'].value_counts()

#akan digunakan genre comedy action horror dan romance
#Menghapus genre selain genre tersebut
df = df[~df['genre'].isin(['drama','thriller','other','sci-fi','adventure'])]
df['genre'].value_counts()

#akan dihapus karakter spesial di kolom text
df['Text'] = df['text'].map(lambda x: re.sub(r'\W+', ' ', x))
#akan didrop kolom id dan text lama
df = df.drop(['id', 'text'], axis=1)
df.head()

#cek nilai kosong (true jika ada dan false jika tidak ada)
df.isnull().values.any()

#pelabelan 
genre = pd.get_dummies(df.genre)
df_genre = pd.concat([df, genre], axis=1)
df_genre = df_genre.drop(columns='genre')
df_genre.head()

#ubah tipe data jadi str dan numpy array 
text = df_genre['Text'].astype(str)
label = df_genre[['action', 'comedy','horror','romance']].values

#split
genre_train, genre_test, label_train, label_test = train_test_split(text, label, test_size = 0.2)

#penggunaan tokenizer
tokenizer = Tokenizer(num_words=5000, oov_token='x')
tokenizer.fit_on_texts(genre_train) 
tokenizer.fit_on_texts(genre_test)
 
sekuens_train = tokenizer.texts_to_sequences(genre_train)
sekuens_test = tokenizer.texts_to_sequences(genre_test)
 
padded_train = pad_sequences(sekuens_train) 
padded_test = pad_sequences(sekuens_test)

#memodelkan Sequential menggunakan Embedding dan LSTM
model = Sequential([
    Embedding(input_dim=5000, output_dim=16),
    LSTM(64),
    Dense(128, activation='relu'),
    Dropout(0.5),
    Dense(4, activation='softmax')
])

#compile model dengan adm optimizer
Adam(learning_rate=0.00146, name='Adam')
model.compile(optimizer = 'Adam',
              loss = 'categorical_crossentropy',
              metrics = ['accuracy'])

#penggunakan callback untuk akurasi dan val akurasi diatas 90%
class myCallback(tf.keras.callbacks.Callback):
  def on_epoch_end(self, epoch, logs={}):
    if(logs.get('accuracy')>0.9 and logs.get('val_accuracy')>0.9):
      print("\nAkurasi train dan validasi telah mencapai target > 90%!")
      self.model.stop_training = True
callbacks = myCallback()

#training model
history = model.fit(padded_train, 
                    label_train, 
                    epochs=30, 
                    validation_data=(padded_test, label_test), 
                    verbose=2, 
                    callbacks=[callbacks])

#plotting Accuracy
plt.plot(history.history['accuracy'])
plt.plot(history.history['val_accuracy'])
plt.title('Akurasi Model')
plt.ylabel('accuracy')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()

#plotting Loss
plt.plot(history.history['loss'])
plt.plot(history.history['val_loss'])
plt.title('Loss Model')
plt.ylabel('loss')
plt.xlabel('epoch')
plt.legend(['train', 'test'], loc='upper left')
plt.show()
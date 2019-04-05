import tensorflow as tf
import pickle
import numpy as np
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from nltk.stem import WordNetLemmatizer
from tensorflow.python import pywrap_tensorflow

from application.statistics.network import Mapped

lemmatizer = WordNetLemmatizer()

n_nodes_hl1 = 500
n_nodes_hl2 = 500

n_classes = 12

batch_size = 32
hm_epochs = 10

x = tf.placeholder('float')
y = tf.placeholder('float')

hidden_1_layer = {'f_fum':n_nodes_hl1,
                  'weight':tf.Variable(tf.random_normal([24, n_nodes_hl1])),
                  'bias':tf.Variable(tf.random_normal([n_nodes_hl1]))}

hidden_2_layer = {'f_fum':n_nodes_hl2,
                  'weight':tf.Variable(tf.random_normal([n_nodes_hl1, n_nodes_hl2])),
                  'bias':tf.Variable(tf.random_normal([n_nodes_hl2]))}

output_layer = {'f_fum':None,
                'weight':tf.Variable(tf.random_normal([n_nodes_hl2, n_classes])),
                'bias':tf.Variable(tf.random_normal([n_classes])),}


def neural_network_model(data):
    l1 = tf.add(tf.matmul(data,hidden_1_layer['weight']), hidden_1_layer['bias'])
    l1 = tf.nn.relu(l1)
    l2 = tf.add(tf.matmul(l1,hidden_2_layer['weight']), hidden_2_layer['bias'])
    l2 = tf.nn.relu(l2)
    output = tf.matmul(l2,output_layer['weight']) + output_layer['bias']
    return output


saver = tf.train.Saver()


def use_neural_network(input_data):
    prediction = neural_network_model(x)
    with open('./lexicon.pickle','rb') as f:
        lexicon = pickle.load(f)

    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        saver.restore(sess,"./model.ckpt")
        current_words = word_tokenize(input_data.lower())
        current_words = [lemmatizer.lemmatize(i) for i in current_words]
        features = np.zeros(len(lexicon))
        for word in current_words:
            if word.lower() in lexicon:
                index_value = lexicon.index(word.lower())
                # OR DO +=1, test both
                features[index_value] += 1

        features = np.array(list(features))
        result = (sess.run(tf.argmax(prediction.eval(feed_dict={x:[features]}),1)))
        if result[0] == 0:
            print('Positive personal:',input_data)
            return Mapped('personal', 'positive')
        elif result[0] == 1:
            print('Negative personal:',input_data)
            return Mapped('personal', 'positive')
        elif result[0] == 2:
            print('Positive Location:',input_data)
            return Mapped('personal', 'positive')
        elif result[0] == 3:
            print('Negative Location:',input_data)
            return Mapped('personal', 'positive')
        elif result[0] == 4:
            print('Positive Parking:',input_data)
            return Mapped('personal', 'positive')
        elif result[0] == 5:
            print('Negative Parking:',input_data)
            return Mapped('personal', 'positive')
        elif result[0] == 6:
            print('Positive pet friendly:',input_data)
            return Mapped('personal', 'positive')
        elif result[0] == 7:
            print('Negative pet friendly:',input_data)
            return Mapped('personal', 'positive')
        elif result[0] == 8:
            print('Positive Restaurant:',input_data)
            return Mapped('personal', 'positive')
        elif result[0] == 9:
            print('Negative Restaurant:',input_data)
            return Mapped('personal', 'positive')
        elif result[0] == 10:
            print('Positive total opinion:',input_data)
            return Mapped('personal', 'positive')
        elif result[0] == 11:
            print('Negative total opinion:',input_data)
            return Mapped('personal', 'positive')
        return Mapped('total', 'positive')


use_neural_network("<xml> <class> <name> </name> </class> </xml>")

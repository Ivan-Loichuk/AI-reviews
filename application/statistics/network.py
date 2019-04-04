import tensorflow as tf
import pickle
import numpy as np
import nltk
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class Mapped:
    def __init__(self, category, comment_type):
        self.category = category
        self.type = comment_type


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
tf_log = './application/statistics/tf.log'


def train_neural_network(x):
    prediction = neural_network_model(x)
    cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits(logits=prediction,labels=y))
    optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        try:
            epoch = int(open(tf_log,'r').read().split('\n')[-2])+1
            print('STARTING:',epoch)
        except:
            epoch = 1

        while epoch <= hm_epochs:
            if epoch != 1:
                saver.restore(sess,"./application/statistics/model.ckpt")
            epoch_loss = 1
            with open('./application/statistics/lexicon.pickle','rb') as f:
                lexicon = pickle.load(f)
            with open('./application/statistics/train_set_shuffled.csv', buffering=20000, encoding='latin-1') as f:
                batch_x = []
                batch_y = []
                batches_run = 0
                for line in f:
                    label = line.split(':::')[0]
                    tweet = line.split(':::')[1]
                    current_words = word_tokenize(tweet.lower())
                    current_words = [lemmatizer.lemmatize(i) for i in current_words]

                    features = np.zeros(len(lexicon))

                    for word in current_words:
                        if word.lower() in lexicon:
                            index_value = lexicon.index(word.lower())
                            # OR DO +=1, test both
                            features[index_value] += 1
                    line_x = list(features)
                    line_y = eval(label)
                    batch_x.append(line_x)
                    batch_y.append(line_y)
                    if len(batch_x) >= batch_size:
                        _, c = sess.run([optimizer, cost], feed_dict={x: np.array(batch_x),
                                                                  y: np.array(batch_y)})
                        epoch_loss += c
                        batch_x = []
                        batch_y = []
                        batches_run +=1
                        print('Batch run:',batches_run,'/','| Epoch:',epoch,'| Batch Loss:',c,)

            saver.save(sess, "./application/statistics/model.ckpt")
            print('Epoch', epoch, 'completed out of',hm_epochs,'loss:',epoch_loss)
            with open(tf_log,'a') as f:
                f.write(str(epoch)+'\n') 
            epoch +=1


train_neural_network(x)


def test_neural_network():
    prediction = neural_network_model(x)
    with tf.Session() as sess:
        sess.run(tf.initialize_all_variables())
        for epoch in range(hm_epochs):
            try:
                saver.restore(sess,"./application/statistics/model.ckpt")
            except Exception as e:
                print(str(e))
            epoch_loss = 0
            
        correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(y, 1))
        accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
        feature_sets = []
        labels = []
        counter = 0
        with open('./application/statistics/processed-test-set.csv', buffering=20000) as f:
            for line in f:
                try:
                    features = list(eval(line.split('::')[0]))
                    label = list(eval(line.split('::')[1]))
                    feature_sets.append(features)
                    labels.append(label)
                    counter += 1
                except:
                    pass
        print('Tested',counter,'samples.')
        test_x = np.array(feature_sets)
        test_y = np.array(labels)
        print('Accuracy:',accuracy.eval({x:test_x, y:test_y}))


test_neural_network()


class NeuralNet:
    def __init__(self, comment):
        self.comment = comment

    def run_neural_network(self):
        self.use_neural_network(self.comment)

    def use_neural_network(self, input_data):
        prediction = neural_network_model(x)
        with open('./application/statistics/lexicon.pickle','rb') as f:
            lexicon = pickle.load(f)

        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())
            saver.restore(sess,"./application/statistics/model.ckpt")
            current_words = word_tokenize(input_data.lower())
            current_words = [lemmatizer.lemmatize(i) for i in current_words]
            features = np.zeros(len(lexicon))

            for word in current_words:
                if word.lower() in lexicon:
                    index_value = lexicon.index(word.lower())
                    # OR DO +=1, test both
                    features[index_value] += 1

            features = np.array(list(features))
            result = (sess.run(tf.argmax(prediction.eval(feed_dict={x: [features]}), 1)))
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


net = NeuralNet('Amazing personal')
net.run_neural_network()
# use_neural_network('Awful personal')
# use_neural_network('Nice hotel, especially parking.')
# use_neural_network('I didnt like a restaurant')

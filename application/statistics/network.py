import tensorflow as tf
import pickle
import numpy as np
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer


class Mapped:
    def __init__(self, category, comment_type):
        self.comment_type = comment_type
        self.category = category


class Model(object):
    POSITIVE = 'positive'
    NEGATIVE = 'negative'
    path = './application/statistics/preprocessed/'
    categories = ['staff', 'location', 'comfort', 'food', 'facilities', 'total']

    def __init__(self):
        tf.reset_default_graph()
        self.lemmatizer = WordNetLemmatizer()
        self.n_nodes_hl1 = 500
        self.n_nodes_hl2 = 500

        self.n_classes = 12

        self.batch_size = 32
        self.hm_epochs = 20

        self.x = tf.placeholder('float')
        self.y = tf.placeholder('float')

        self.hidden_1_layer = {'f_fum':self.n_nodes_hl1,
                          'weight':tf.Variable(tf.random_normal([27, self.n_nodes_hl1])),
                          'bias':tf.Variable(tf.random_normal([self.n_nodes_hl1]))}

        self.hidden_2_layer = {'f_fum':self.n_nodes_hl2,
                          'weight':tf.Variable(tf.random_normal([self.n_nodes_hl1, self.n_nodes_hl2])),
                          'bias':tf.Variable(tf.random_normal([self.n_nodes_hl2]))}

        self.output_layer = {'f_fum':None,
                        'weight':tf.Variable(tf.random_normal([self.n_nodes_hl2, self.n_classes])),
                        'bias':tf.Variable(tf.random_normal([self.n_classes]))}

        self.saver = tf.train.Saver()
        self.tf_log = self.path + 'tf.log'

    def neural_network_model(self, data):
        l1 = tf.add(tf.matmul(data, self.hidden_1_layer['weight']), self.hidden_1_layer['bias'])
        l1 = tf.nn.relu(l1)
        l2 = tf.add(tf.matmul(l1, self.hidden_2_layer['weight']), self.hidden_2_layer['bias'])
        l2 = tf.nn.relu(l2)
        output = tf.matmul(l2,self.output_layer['weight']) + self.output_layer['bias']
        return output

    def train_neural_network(self):
        prediction = self.neural_network_model(self.x)
        cost = tf.reduce_mean(tf.nn.softmax_cross_entropy_with_logits_v2(logits=prediction,labels=self.y))
        optimizer = tf.train.AdamOptimizer(learning_rate=0.001).minimize(cost)
        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())
            try:
                epoch = int(open(self.tf_log,'r').read().split('\n')[-2])+1
                print('STARTING:',epoch)
            except:
                epoch = 1

            while epoch <= self.hm_epochs:
                if epoch != 1:
                    self.saver.restore(sess, self.path + "model.ckpt")
                epoch_loss = 1
                with open(self.path + 'lexicon.pickle','rb') as f:
                    lexicon = pickle.load(f)
                with open(self.path + 'train_set_shuffled.csv', buffering=20000, encoding='latin-1') as f:
                    batch_x = []
                    batch_y = []
                    batches_run = 0
                    for line in f:
                        label = line.split(':::')[0]
                        tweet = line.split(':::')[1]
                        current_words = word_tokenize(tweet.lower())
                        current_words = [self.lemmatizer.lemmatize(i) for i in current_words]

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
                        if len(batch_x) >= self.batch_size:
                            _, c = sess.run([optimizer, cost], feed_dict={self.x: np.array(batch_x),
                                                                      self.y: np.array(batch_y)})
                            epoch_loss += c
                            batch_x = []
                            batch_y = []
                            batches_run +=1
                            print('Batch run:',batches_run,'/','| Epoch:',epoch,'| Batch Loss:',c,)

                self.saver.save(sess, self.path + "model.ckpt")
                print('Epoch', epoch, 'completed out of',self.hm_epochs,'loss:',epoch_loss)
                with open(self.tf_log,'a') as f:
                    f.write(str(epoch)+'\n')
                epoch +=1


    #train_neural_network(x)

    def test_neural_network(self):
        prediction = self.neural_network_model(self.x)
        with tf.Session() as sess:
            sess.run(tf.initialize_all_variables())
            for epoch in range(self.hm_epochs):
                try:
                    self.saver.restore(sess, self.path + "model.ckpt")
                except Exception as e:
                    print(str(e))
                epoch_loss = 0

            correct = tf.equal(tf.argmax(prediction, 1), tf.argmax(self.y, 1))
            accuracy = tf.reduce_mean(tf.cast(correct, 'float'))
            feature_sets = []
            labels = []
            counter = 0
            with open(self.path + 'processed-test-set.csv', buffering=20000) as f:
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
            print('Accuracy:',accuracy.eval({self.x:test_x, self.y:test_y}))


    #test_neural_network()

    def use_neural_network(self, input_data):
        prediction = self.neural_network_model(self.x)
        with open(self.path + 'lexicon.pickle','rb') as f:
            lexicon = pickle.load(f)

        with tf.Session() as sess:
            saver = tf.train.import_meta_graph(self.path + 'model.ckpt.meta')
            saver.restore(sess, tf.train.latest_checkpoint(self.path))

            current_words = word_tokenize(input_data.lower())
            current_words = [self.lemmatizer.lemmatize(i) for i in current_words]
            features = np.zeros(len(lexicon))
            for word in current_words:
                if word.lower() in lexicon:
                    index_value = lexicon.index(word.lower())
                    features[index_value] += 1

            features = np.array(list(features))
            result = (sess.run(tf.argmax(prediction.eval(session=sess, feed_dict={self.x: [features]}), 1)))
            # prediction.eval() will have an output layer with neurons for each class
            # tf.argmax simply picks neuron with maximum value which indicates the most suitable class
            if result[0] == 0:
                print('Positive personal:',input_data)
                return Mapped(self.categories[0], self.POSITIVE)
            elif result[0] == 1:
                print('Negative personal:',input_data)
                return Mapped(self.categories[0], self.NEGATIVE)
            elif result[0] == 2:
                print('Positive Location:',input_data)
                return Mapped(self.categories[1], self.POSITIVE)
            elif result[0] == 3:
                print('Negative Location:',input_data)
                return Mapped(self.categories[1], self.NEGATIVE)
            elif result[0] == 4:
                print('Positive comfort:',input_data)
                return Mapped(self.categories[2], self.POSITIVE)
            elif result[0] == 5:
                print('Negative comfort:',input_data)
                return Mapped(self.categories[2], self.NEGATIVE)
            elif result[0] == 6:
                print('Positive food:',input_data)
                return Mapped(self.categories[3], self.POSITIVE)
            elif result[0] == 7:
                print('Negative food:',input_data)
                return Mapped(self.categories[3], self.NEGATIVE)
            elif result[0] == 8:
                print('Positive facilities:',input_data)
                return Mapped(self.categories[4], self.POSITIVE)
            elif result[0] == 9:
                print('Negative facilities:',input_data)
                return Mapped(self.categories[4], self.NEGATIVE)
            elif result[0] == 10:
                print('Positive total opinion:',input_data)
                return Mapped(self.categories[5], self.POSITIVE)
            elif result[0] == 11:
                print('Negative total opinion:',input_data)
                return Mapped(self.categories[5], self.NEGATIVE)


model = Model()
model.use_neural_network('Great hotel. Very bad location.')
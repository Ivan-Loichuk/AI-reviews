import os

import numpy as np
import pickle
import tensorflow as tf

from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.http import JsonResponse
from nltk import word_tokenize
from rest_framework.parsers import JSONParser


from application.models.comment_serializer import CommentSerializer
from application.models.hotel_serializer import HotelSerializer
from application.models.hotel_models import Hotel, Comment, HotelType
from application.models.type_serializer import TypeSerializer
from application.statistics.network import neural_network_model, x, saver, lemmatizer, Mapped


@login_required
def create_hotel(request):
    data = JSONParser().parse(request)
    hotel_serializer = HotelSerializer(data=data)
    if hotel_serializer.is_valid():
        hotel_serializer.save()
        return JsonResponse(hotel_serializer.data, status=201)
    return JsonResponse(hotel_serializer.errors, status=400)


def get_hotels():
    hotels = Hotel.objects.all().values()
    return JsonResponse(list(hotels), content_type="application/json", safe=False)


def search_hotels(request):
    data = JSONParser().parse(request)
    if data['types'] and not data['city'] == '':
        hotels = Hotel.objects.filter(hotel_type__type__in=data['types'], city__icontains=data['city']).values()
    elif data['types']:
        hotels = Hotel.objects.filter(hotel_type__type__in=data['types']).values()
    elif not data['city'] == '':
        hotels = Hotel.objects.filter(city__icontains=data['city']).values()
    else:
        hotels = hotels = Hotel.objects.all().values()
    return JsonResponse(list(hotels), content_type="application/json", safe=False)


def get_hotel(request, hotel_id):
    hotel = Hotel.objects.filter(id=hotel_id).values()[0]
    hotel_type = HotelType.objects.filter(id=(hotel['hotel_type_id'])).values()[0]
    hotel['hotel_type'] = hotel_type['type']
    return JsonResponse(hotel, content_type="application/json", safe=False)


@login_required
def add_comment(request):
    data = JSONParser().parse(request)
    user = request.user
    data['sender'] = User.objects.get(username=user).id
    comment_mapping = use_neural_network('really bad hotel')
    data['category'] = comment_mapping.category
    data['type'] = comment_mapping.comment_type
    comment_serializer = CommentSerializer(data=data)
    if comment_serializer.is_valid():
        comment_serializer.save()
        return JsonResponse(comment_serializer.data, status=201)
    return JsonResponse(comment_serializer.errors, status=500)


def add_hotel_type(request):
    data = JSONParser().parse(request)
    type_serializer = TypeSerializer(data=data)
    if type_serializer.is_valid():
        type_serializer.save()
        return JsonResponse(type_serializer.data, status=201)
    return JsonResponse(type_serializer.errors, status=400)


def get_comments(request, hotel_id):
    comments = Comment.objects.filter(hotel=hotel_id).values()
    for index, val in enumerate(comments):
        user = User.objects.filter(id=val['sender_id']).values()[0]
        comments[index]['sender'] = user['username']
    return JsonResponse(list(comments), content_type="application/json", safe=False)


def use_neural_network(input_data):
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

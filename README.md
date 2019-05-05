This project is something similar to booking.com but with additional feature - Neural Network. Neural network is used to classify user comments to categories. Categories may vary, for example: staff, food&drink, location etc. Neural network classifies user comments and saves them to the database. Based on those mappings we can generate statistic for each hotel. Statistic describes each hotel category, how users rate each of the categories (not necessary all of them). Also, there is overall statistic based on all user opinions about hotel.

# **Main features:** <br/>
- browse hotels or apartments by cities, and other filters
- leave comments about hotels
- neural network which classifies comments
- check hotel statistic based on hotel categories

# **Technology stack:**<br/>
Python 3.6, Django, Angular 7, TensorFlow, NLTK, PostgreSQL.

# **Getting started:** <br/>
    - First of all you will need to install: 
        - Python of version 3.6 (because TensorFlow doesn't support newer versions of Python)
        - TensorFlow
        - NLTK
        - PostgreSQL
        - Angular 7
        - Node.js.
    - Create a database `ai-reviews`, with login `postgres` and password `admin`.
    - In the root directory from the command line run: 
        - `python manage.py makemigrations application` (this will prepare all necessary SQL scripts for migration), 
        - after that also run: `python manage.py migrate`
    - Go to the frontend folder and run from the command line `npm start`
    - To train the Neural Network you will need to run several functions from class Model (`application/statistics/network.py`):
        - train_neural_network(x)
        - test_neural_network()
      Those functions will train the network, after that you can use it!
    - To run the application, from the root directory in the command line run: `python manage.py runserver`
   

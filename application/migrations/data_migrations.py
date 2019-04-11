# Generated by Django 2.1.7 on 2019-03-29 14:31
import sqlparse
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        # migrations.RunSQL(
        #         #     sqlparse.split(
        #         #         "INSERT INTO auth_user (id, password, last_login, is_superuser, username, first_name, last_name, email) "
        #         #         "VALUES (1, 'admin', '12-12-12', null, 'admin', 'test', 'test', 'test@gmail.com');")
        #         # ),
        # Hotel types
        migrations.RunSQL(
            sqlparse.split("INSERT INTO application_hoteltype (id, type) VALUES(1, 'Hotel');")
        ),
        migrations.RunSQL(
            sqlparse.split("INSERT INTO application_hoteltype (id, type) VALUES(2, 'Apartment');")
        ),
        migrations.RunSQL(
            sqlparse.split("INSERT INTO application_hoteltype (id, type) VALUES(3, 'Guest room');")
        ),
        migrations.RunSQL(
            sqlparse.split("INSERT INTO application_hoteltype (id, type) VALUES(4, 'Villa');")
        ),
        # Hotels
        migrations.RunSQL(
            sqlparse.split(
                "INSERT INTO application_hotel (id, name, city, street, phone, email, hotel_type_id, description, stat_summary) "
                "VALUES(1, 'Super Hotel', 'Some city', 'Some street', '484848', 'email@gmail.com', 1, 'Relax take it easy', 0);")
        ),
        migrations.RunSQL(
            sqlparse.split(
                "INSERT INTO application_hotel (id, name, city, street, phone, email, hotel_type_id, description, stat_summary) "
                "VALUES(2, 'Super Hotel', 'Some city', 'Some street', '484848', 'email@gmail.com', 2, 'Relax take it easy', 0);")
        ),
        migrations.RunSQL(
            sqlparse.split(
                "INSERT INTO application_hotel (id, name, city, street, phone, email, hotel_type_id, description, stat_summary) "
                "VALUES(3, 'Super Hotel', 'Some city', 'Some street', '484848', 'email@gmail.com', 3, 'Relax take it easy', 0);")
        ),
        migrations.RunSQL(
            sqlparse.split(
                "INSERT INTO application_hotel (id, name, city, street, phone, email, hotel_type_id, description, stat_summary) "
                "VALUES(4, 'Super Hotel', 'Some city', 'Some street', '484848', 'email@gmail.com', 4, 'Relax take it easy', 0);")
        )
    ]

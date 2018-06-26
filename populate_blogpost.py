import os


os.environ.setdefault('DJANGO_SETTINGS_MODULE','firstcrud.settings')


#import django
#django.setup()

import random

from blogpost.models import AccessRecord, Webpage, Topic
from faker import Faker
#global fakegen
fakegen = Faker()

topics = ['Search','Social','MarketPlace','News','Games']

def add_topics():
    t = Topic.objects.get_or_create(top_name=random.choice(topics))[0]
    t.save()
    return t

def populate(N=20):
    for entry in range(N):
        top = add_topic()

        #fake_data

        fake_url = fakegen.url()
        fake_date = fakegen.date()
        fake_name = fakegen.company()


        Webpg = Webpage.objects.get_or_create(topic = top, url = fake_url, name = fake_name)[0]

        acc_rec = AccessRecord.objects.get_or_create(name=Webpg, date=fake_date)[0]


if __name__ == "__main__":
    import django
    django.setup()

    print("populating script")
    populate(20)

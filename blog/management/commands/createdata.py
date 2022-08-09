from django.core.management.base import BaseCommand
from faker import Faker
from blog.models import User, Post, Comments
import random


class Command(BaseCommand):

    def handle(self, *args, **options):
        fake = Faker()

        # for _ in range(10):
        #     d = fake.simple_profile()
        #     User.objects.create(username=d['username'], email=d['mail'], password=fake.unique.password())

        # for _ in range(10):
        #     author = User.objects.all()
        #     post = fake.paragraph(nb_sentences=20, variable_nb_sentences=True)
        #     Post.objects.create(author=random.choice(author),
        #                         title=fake.sentence(nb_words=3, variable_nb_words=True),
        #                         subtitle=fake.sentence(nb_words=3, variable_nb_words=True),
        #                         body=post)

        for _ in range(10):
            user = User.objects.all()
            post = Post.objects.all()
            comment = fake.paragraph(nb_sentences=10, variable_nb_sentences=True)
            Comments.objects.create(user=random.choice(user),
                                    post=random.choice(post),
                                    comment=comment)

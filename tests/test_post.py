import unittest
from app.models import Post, User
from app import db
from unittest import TestCase

class TestPost(unittest.TestCase):
    def setUp(self):
        self.user_kibet= User(username='kibet', password='flasksApp', email='kibetdavidro@gmail.com',biography="New Knowledge on Flask",profile_pic="xxxx")
        self.new_pitch = Post(title="Pitch", category='promotion', pitch="Get new pitch", user=self.user_kibet)


    def tearDown(self):
        Post.query.delete()
        User.query.delete()






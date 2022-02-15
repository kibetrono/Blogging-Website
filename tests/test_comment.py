import unittest
from app.models import Comment
from app import db
from unittest import TestCase

class TestComment(unittest.TestCase):
    def setUp(self):
        self.new_comment = Comment(comment="Initial comment")


    def tearDown(self):
        Comment.query.delete()
        Comment.query.delete()






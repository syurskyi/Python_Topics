import sqlite3
import unittest

from app import app_with_db


class AppWithDBTests(unittest.TestCase):

    def setUp(self):
        self.conn = sqlite3.connect(":memory:")
        self.conn.execute("CREATE TABLE blog (id INTEGER PRIMARY KEY AUTOINCREMENT, title TEXT, text TEXT)")

    def tearDown(self):
        self.conn.close()

    def test_entry_creation(self):
        app_with_db.create_blog_entry(db=self.conn, title="pytest", text="Pytest is awesome!")

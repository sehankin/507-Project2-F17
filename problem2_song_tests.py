import unittest
from si507f17_project2_objects_code import *

class Problem2Song(unittest.TestCase):
	def setUp(self):
		search_data1 = sample_get_cache_itunes_data("the beatles")["results"]
		songdata1 = search_data1[0]
		songdata2 = search_data1[1]
		self.song1 = Song(songdata1)
		self.song2 = Song(songdata2)

	def test_song_constructor_override(self):
		self.assertEqual(type(self.song1.album),type(u""))
		self.assertEqual(type(self.song1.track_number),type(3))
		self.assertEqual(type(self.song1.genre),type(u""))

		self.assertTrue(self.song1.itunes_URL.startswith("http"))
		self.assertEqual(self.song1.genre,u"Rock")

		if self.song1.title=='Let It Be':
			self.assertEqual(self.song1.album,u"Let It Be")
			self.assertEqual(self.song1.title,u"Let It Be")
			self.assertEqual(self.song1.track_number,6)
			self.assertEqual(self.song1.itunes_id,401151904)
		else:
			self.assertEqual(self.song1.album,u"Abbey Road")
			self.assertEqual(self.song1.title,u"Here Comes the Sun")
			self.assertEqual(self.song1.track_number,7)
			self.assertEqual(self.song1.itunes_id,401187150)

	def test_song_len(self):
		if self.song1.title=='Let It Be':
			self.assertEqual(len(self.song1),243)
		else:
			self.assertEqual(len(self.song1),185)

	def test_song_contains(self):
		if self.song1.title=='Let It Be':
			self.assertTrue("Let" in self.song1)
		else:
			self.assertTrue("Sun" in self.song1)

		self.assertTrue("Beat" not in self.song1)

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main(verbosity=2)

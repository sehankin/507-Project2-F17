import unittest
from si507f17_project2_objects_code import *

class Problem3(unittest.TestCase):
	def setUp(self):
		search_data1 = sample_get_cache_itunes_data("the beatles")["results"]
		songdata1 = search_data1[0]
		self.song1 = Song(songdata1)
		search_data2 = sample_get_cache_itunes_data("ratatouille")["results"]
		movie1 = search_data2[0]
		self.movie_sample = Movie(movie1)
		self.media1 = Media(songdata1)

	def test_song_list(self):
		self.assertEqual(type(song_list[0]),type(self.song1))
		self.assertEqual(type(song_list[-1]),type(self.song1))
		self.assertTrue(len(song_list) == len(song_samples))

	def test_movie_list(self):
		self.assertEqual(type(movie_list[0]),type(self.movie_sample))
		self.assertEqual(type(movie_list[-1]),type(self.movie_sample))
		self.assertTrue(len(movie_list) == len(movie_samples))

	def test_media_list(self):
		self.assertEqual(type(media_list[0]),type(self.media1))
		self.assertEqual(type(media_list[-1]),type(self.media1))
		self.assertTrue(len(media_list) == len(media_samples))

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main(verbosity=2)

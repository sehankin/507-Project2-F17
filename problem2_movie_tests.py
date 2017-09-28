import unittest
from si507f17_project2_objects_code import *

class Problem2Movie(unittest.TestCase):
	def setUp(self):
		search_data2 = sample_get_cache_itunes_data("ratatouille")["results"]
		movie1 = search_data2[0]
		self.movie_sample = Movie(movie1)

	def test_movie_constructor_override(self):
		self.assertEqual(type(self.movie_sample.genre),type(u""))
		self.assertEqual(self.movie_sample.title,u"Ratatouille")
		self.assertEqual(self.movie_sample.genre,u"Kids & Family")
		self.assertEqual(self.movie_sample.rating,u"G")
		self.assertTrue(self.movie_sample.itunes_URL.startswith("http"))
		self.assertEqual(self.movie_sample.itunes_id,265250067)
		self.assertTrue(len(self.movie_sample.description)==1339
						or len(self.movie_sample.description)==1342)

	def test_movie_len(self):
		self.assertEqual(len(self.movie_sample),111)

	def test_movie_str(self):
		self.assertEqual(self.movie_sample.__str__(),"Ratatouille by Pixar & Brad Lewis")

	def test_movie_repr(self):
		self.assertEqual(self.movie_sample.__repr__(),"ITUNES MEDIA: 265250067")

	def test_movie_contains(self):
		self.assertTrue("tatou" in self.movie_sample)
		self.assertTrue("Pixar" not in self.movie_sample)

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main(verbosity=2)

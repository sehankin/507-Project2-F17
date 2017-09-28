import unittest
from si507f17_project2_objects_code import *

class Problem1(unittest.TestCase):
	def setUp(self):
		search_data1 = sample_get_cache_itunes_data("the beatles")["results"]
		songdata1 = search_data1[0]
		songdata2 = search_data1[1]
		search_data2 = sample_get_cache_itunes_data("ratatouille")["results"]
		self.m1inst = Media(search_data1[0])
		self.m2inst = Media(search_data2[0])

	def test_constructor_media(self):
		self.assertEqual(type(self.m1inst.title),type(u"s"),"Testing whether inst var is a unicode string (all web data is unicode, generally)")
		self.assertEqual(type(self.m1inst.author),type(u"s"),"Testing whether inst var is a unicode string (all web data is unicode, generally)")
		self.assertEqual(type(self.m1inst.itunes_URL),type(u"s"),"Testing whether inst var is a unicode string (all web data is unicode, generally)")
		self.assertEqual(type(self.m2inst.itunes_id),type(34))
		self.assertEqual(self.m2inst.title,"Ratatouille")
		self.assertTrue(self.m1inst.itunes_URL.startswith("http"))
		self.assertEqual(self.m2inst.itunes_id,265250067)

	def test_repr_method(self):
		self.assertEqual(self.m2inst.__repr__(),"ITUNES MEDIA: 265250067")

	def test_str_method(self):
		if self.m1inst.title=='Let It Be':
			self.assertEqual(self.m1inst.__str__(), "Let It Be by The Beatles")
		else:
			self.assertEqual(self.m1inst.__str__(), "Here Comes the Sun by The Beatles")

	def test_contains_method(self):
		self.assertTrue("beatles" not in self.m1inst)
		self.assertTrue("ouille" in self.m2inst)

	def tearDown(self):
		pass

if __name__ == '__main__':
	unittest.main(verbosity=2)

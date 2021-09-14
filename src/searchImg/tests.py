from django.db.models.fields import CharField
from django.test import TestCase
from searchImg.models import img

# Create your tests here.
class imgTestCase(TestCase):
	def setupTestData(self):
		img.objects.create(title = 'imgTest1', characteristics = ['happy','celeberate','wine'], price = 7.99)
		img.objects.create(title = 'imgTest2', characteristics = ['exam','stressful','academic'], price = 99.99)
	
	def tet_img_price(self):
		testCase1 = img.objects.get(title = 'imgTest1')
		print(testCase1.getChara())
		self.assertEqual(testCase1.getChara(), ['happy','celeberate','wine'])
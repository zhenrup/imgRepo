from django.db.models import ImageField, CharField, Model, IntegerField, DecimalField
from django.db.models.fields import DecimalField
from django_mysql.models import ListCharField

# Create your models here.
class img(Model):
	image_upload  = ImageField(default = 'image', upload_to ='upload/')
	title = CharField(max_length=100)
	characteristics = ListCharField(
		base_field=CharField(max_length=12),
        size=6,
        max_length=(6 * 13),
		null=True
	)
	price = DecimalField(decimal_places=2, max_digits=1000)
	discount = IntegerField(null = True)
	seller = CharField(null=True, max_length=50)

	def getChar(self):
		return self.characteristics
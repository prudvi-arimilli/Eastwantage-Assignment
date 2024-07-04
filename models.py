from tortoise import fields, models

class Address(models.Model):
    id = fields.IntField(pk=True)
    name = fields.CharField(max_length=255)
    address = fields.TextField()
    latitude = fields.FloatField()
    longitude = fields.FloatField()

    class Meta:
        table = "addresses"

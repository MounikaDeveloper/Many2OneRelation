# Many2OneRelation
A one-to-many relationship exists when each row in one table has
one or many related rows in a second table. The following figure
shows examples: one customer can place many orders, or a sales
representative can have many customer accounts.

models.py
...........
class BiryaniType(models.Model):
 no = models.IntegerField(primary_key=True)
 type = models.CharField(max_length=30)
class Biryani(models.Model):
 no = models.IntegerField(primary_key=True)
 name =models.CharField(max_length=30)
 price = models.FloatField()
 biryani_type =
models.ForeignKey(BiryaniType,on_delete=models.CASCADE)



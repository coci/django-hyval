# Hyval

Hyval will store your information encrypted and decrypt it when needed :>

note : there was mistake by me , so i deleted repo and .git folder anciently, so there isn't any commit history.

### Usage:
#### instalation:

for install package :
```
pip install hyval
```

#### example :

1- in settings.py:

```
HIDE_MY_VALUE = {
	'salt' : 'test',
	'key': 'test',
	'length' : 32,
	'iteration': 1000,
}
```

2- in model:

```
from django.db import models
from hyval import HideMyValue


class TestHyval(models.Model):
    name = models.CharField(max_length=50)
    password = HideMyValue(max_length=32)
```

then:
```
action = TestHyval()
action.name = "test"
action.password = "test"
action.save()
```
now look at database, your value is encrypted and to retrieve value :

```
my_model = TestHyval.objects.get(pk=1)
my_model.password
>>> 'test'
```
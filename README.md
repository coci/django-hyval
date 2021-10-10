# Hyval

Hyval will store your information encrypted and decrypt it when needed :>

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
Now your 'password' field on database stored with encryption so to retrieve value :

```
my_model = TestHyval.objects.get(pk=1)
my_model.password
>>> 'test'
```

### mistake
there was mistake by me , so i deleted 'repository' and '.git' folder anciently, so there isn't any commit about past.
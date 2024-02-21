from django.db import models
from django.contrib.auth.models import User, AbstractUser





class CustomUser(AbstractUser):
    class PROVINCES(models.TextChoices):
        Tanlanmagan = ''
        Andijon = 'Andijon', 'Andijon viloyati'
        Buxoro = 'Buxoro', 'Buxoro viloyati'
        Fargona = "Farg'ona", "Farg'ona viloyati"
        Xorazm = "Xorazm", "Xorazm viloyati"
        Jizzax = "Jizzax", "Jizzax viloyati"
        Namangan = "Namangan", "Namangan viloyati"
        Navoiy = "Navoiy", "Navoiy viloyati"
        Qashqadaryo = "Qashqadaryo", "Qashqadaryo viloyati"
        Koraqalpoq = "Qoraqalpog'iston", "Qoraqalpog'iston Respublikasi"
        Samarqand = "Samarqand", "Samarqand viloyati"
        Sirdaryo = "Sirdaryo", "Sirdaryo viloyati"
        Surxondaryo = "Surxondaryo", "Surxondaryo viloyati"
        Toshkent = "Toshkent", "Toshkent viloyati"
    location = models.CharField(choices=PROVINCES.choices, max_length=50, blank=True, null=True) # default=PROVINCES.Tanlanmagan
    birth_date = models.DateField(null=True, blank=True)
    profile_picture = models.ImageField(upload_to='users/users-pictures', default='users/users-pictures/user_default_picture.png')
    # date_joined = models.DateTimeField(default=tz.now) # bu abstract userni o'zida bor

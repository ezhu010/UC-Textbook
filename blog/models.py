from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.urls import reverse

UC_SCHOOLS = [
    ("UC Irvine", "UC Irvine"),
    ("UC Riverside", "UC Riverside"),
    ("UC Davis", "UC Davis"),
    ("UC Berkeley", "UC Berkeley"),
    ("UC San Diego", "UC San Diego"),
    ("UC Santa Barbara", "UC Santa Barbara"),
    ("UC Merced", "UC Merced"),
    ("UC Los Angeles", "UC Los Angeles"),
    ("UC Santa Cruz", "UC Santa Cruz"),
]

CONDITIONS_TEXT = [
    ("New", "New"),
    ("Like New", "Like New"),
    ("Fair", "Fair"),
    ("Poor", "Poor"),
]


class Post(models.Model):
    title_of_textbook = models.CharField(max_length=50, default="")
    school = models.CharField(max_length=50, choices=UC_SCHOOLS, default="---------")
    course = models.CharField(max_length=50, default="")
    email = models.EmailField(default="")
    image = models.ImageField(default="textbook.jpg", upload_to="profile_pics")
    professor = models.CharField(max_length=50, default="")
    condition = models.CharField(max_length=50, choices=CONDITIONS_TEXT, default="")
    date_posted = models.DateTimeField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    ISBN = models.BigIntegerField()

    def __str__(self):
        return self.title_of_textbook

    def get_absolute_url(self):
        return reverse("post-detail", kwargs={"pk": self.pk})

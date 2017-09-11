from django.contrib import admin

from .models import TutorialModel
from .models import ArticleModel


admin.site.register(TutorialModel)
admin.site.register(ArticleModel)


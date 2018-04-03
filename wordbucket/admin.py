from django.contrib import admin


from .models import Word, Explanation, Like_and_dislike

# Register your models here.

admin.site.register(Word)
admin.site.register(Explanation)
admin.site.register(Like_and_dislike)

import django_filters
from .models import Post

class PostFilter(django_filters.FilterSet):

    class Meta:
        model = Post
        fields = {'author':['exact'],'published_date':['exact'],'category':['exact'],'tag':['exact']}
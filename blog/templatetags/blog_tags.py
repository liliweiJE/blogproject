from django import template
from ..models import post,Category,Tag
from django.db.models.aggregates import Count

register =template.Library()

@register.simple_tag
def get_recent_posts(num=5):
    return post.objects.all().order_by('-created_time')[:num]


@register.simple_tag
def archives():
    return post.objects.dates('created_time', 'month', order='DESC')

@register.simple_tag
def get_categories():
    # 别忘了在顶部引入 Category 类
    return Category.objects.all()

@register.simple_tag
def get_categories():
    # 记得在顶部引入 count 函数
    # Count 计算分类下的文章数，其接受的参数为需要计数的模型的名称
    return Category.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)


@register.simple_tag
def get_tags():
    # 记得在顶部引入 Tag model
    return Tag.objects.annotate(num_posts=Count('post')).filter(num_posts__gt=0)



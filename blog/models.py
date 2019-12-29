# coding: utf-8

from django.db import models
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse


class Category(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)

class Tag(models.Model):
    def __str__(self):
        return self.name
    name = models.CharField(max_length=100)

class Post(models.Model):
    def get_absolute_url(self):
        return reverse('blog:detail', kwargs={'pk': self.pk})
    def __str__(self):
        return self.title
    # 存储题目描述
    description = models.TextField()

    # 存储了题解的标题
    title = models.CharField(max_length=70)

    # 存储题解内容
    answer = models.TextField()

    # 分别存储了创建的时间和最后一次修改的时间
    created_time = models.DateTimeField()
    modified_time = models.DateTimeField()

    # 分类和标签
    category = models.ForeignKey(Category)
    tags = models.ManyToManyField(Tag, blank=True)

    # 文章作者
    author = models.ForeignKey(User)

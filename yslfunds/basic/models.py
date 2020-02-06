from django.db import models
from django.contrib.auth.models import User
from simditor.fields import RichTextField

# Create your models here.


class Category(models.Model):
    DONE = '0'
    IN_PROGRESS = '1'
    STATUS_CHOICES = (
        (DONE, '编辑完成'),
        (IN_PROGRESS, '编辑中'))
    name = models.CharField('分类名称', max_length=150)
    create_time = models.TimeField('创建时间', )
    status = models.CharField('状态', choices=STATUS_CHOICES, max_length=2,
                              default=DONE)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = '分类'
        verbose_name_plural = verbose_name


class Activity(models.Model):
    DONE = '0'
    IN_PROGRESS = '1'
    STATUS_CHOICES = (
        (DONE, '编辑完成'),
        (IN_PROGRESS, '编辑中'))

    submitter = models.ForeignKey(User, verbose_name='提交者',
                                  on_delete=models.DO_NOTHING,
                                  null=True)
    title = models.CharField('标题', max_length=150)
    inspectors = models.CharField('考察人员', max_length=150)
    location = models.CharField('地点', max_length=150)
    content = RichTextField('项目内容')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)
    publish_date = models.DateField('发布时间')
    status = models.CharField('状态', choices=STATUS_CHOICES, max_length=2,
                              default=IN_PROGRESS)

    class Meta:
        verbose_name = '活动'
        verbose_name_plural = verbose_name
        ordering = ('create_time', )


class Article(models.Model):
    DONE = '0'
    IN_PROGRESS = '1'
    STATUS_CHOICES = (
        (DONE, '编辑完成'),
        (IN_PROGRESS, '编辑中'))

    submitter = models.ForeignKey(User, verbose_name='提交者',
                                  on_delete=models.DO_NOTHING,
                                  null=True)
    title = models.CharField('标题', max_length=150)
    abstract = models.CharField('摘要', max_length=300)
    content = RichTextField('内容')
    create_time = models.DateTimeField('创建时间', auto_now_add=True)
    update_time = models.DateTimeField('修改时间', auto_now=True)
    publish_date = models.DateField('发布时间')
    status = models.CharField('状态', choices=STATUS_CHOICES, max_length=2,
                              default=IN_PROGRESS)
    image = models.ImageField('新闻必须配图', blank=False)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '新闻'
        verbose_name_plural = verbose_name
        ordering = ('create_time', )


class Slogan(models.Model):

    title = models.CharField('标题', max_length=150)
    content = RichTextField('内容')
    image = models.ImageField('上传图片', blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = '固定标语'
        verbose_name_plural = verbose_name
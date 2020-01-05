from django.db import models

# Create your models here.
class Product(models.Model):
    productname = models.CharField('产品名称',max_length=64) #产品名称
    productdesc = models.CharField('产品描述',max_length=200)
    producter = models.CharField('产品负责人',max_length=200)
    create_time = models.DateTimeField('创建时间',auto_now=True)

    class Meta:
        verbose_name = '产品管理'
        verbose_name_plural = '产品管理'
    def __str__(self):
#当使用print输出对象的时候，只要自己定义了__str__(self)方法，
# 那么就会打印从在这个方法中return的数据
        return self.productname
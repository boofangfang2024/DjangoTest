from django.db import models
from product.models import Product

# Create your models here.
class Apitest(models.Model):
    Apitest = models.ForeignKey('product.Product',on_delete=models.CASCADE,)
#    Product = models.ForeignKey('Product.Product',on_delete=models.CASCADE,null=True)
    #流程接口测试场景
    apitestname = models.CharField('流程接口名称',max_length=64)
    # 执行人
    apitester = models.CharField('测试负责人', max_length=16)
    # 流程接口测试结果
    apitestresult = models.BooleanField('测试结果')
    # 创建时间，自动获取当前时间
    create_time = models.DateTimeField('创建时间', auto_now=True)
    #流程接口描述
    apitestdesc = models.CharField('描述',max_length=64,null=True)


    class Meta:
#class Meta做为嵌套类，主要目的是给上级类添加一些功能，或者指定一些标准。
        verbose_name = '流程场景接口'
        verbose_name_plural = '流程场景接口'

    def __str__(self):
        return self.apitestname


class Apistep(models.Model):
    #关联接口ID
    Apitest = models.ForeignKey('Apitest',on_delete=models.CASCADE)
    #测试步骤
    apistep = models.CharField('测试步骤',max_length=100,null=True)
    #接口标题
    apiname = models.CharField('接口名称',max_length=100)
    #地址
    apiurl = models.CharField('url地址',max_length=200)
    #参数和值
    apiparamvalue = models.CharField('请求参数和值',max_length=800,null=True)
#    #请求方法
    REQUEST_METHOD = (('get','get'),('post','post'),('put','put'),('delete','delete'),('patch','patch'))
    apimethod = models.CharField(verbose_name='请求方法',choices=REQUEST_METHOD,default='get',max_length=200,null=True)
#    apimethod = models.CharField('方法',max_length=200)
    #预期结果
    apiresult = models.CharField('预期结果',max_length=200)
    #响应数据
    apiresponse = models.CharField('响应数据',max_length=5000,null=True)
    #测试结果
    apistatus = models.BooleanField('是否通过')
    #创建时间
    create_time = models.DateTimeField('创建时间',auto_now=True)

    def __str__(self):
        return self.apistep


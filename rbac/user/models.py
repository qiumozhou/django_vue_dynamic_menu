import time

from django.db import models

# Create your models here.
from django.utils import timezone

class BaseModel(models.Model):
    utm = models.BigIntegerField(verbose_name="更新时间",blank=True)
    ctm = models.BigIntegerField(verbose_name="创建时间",blank=True)

    def save(self, *args, **kwargs):
        if not self.id:
            self.ctm = int(time.time())
        self.utm =  int(time.time())
        return super().save(*args, **kwargs)

    class Meta:
        abstract = True




class User(BaseModel):
    choice = ((0,"否"),(1,"是"))
    user_name = models.CharField(max_length=30,verbose_name="用户名")
    password = models.CharField(max_length=50,verbose_name="密码")
    email = models.CharField(max_length=20,verbose_name="邮箱")
    is_delete = models.IntegerField(choices=choice,default=0,verbose_name="是否删除")
    is_active = models.IntegerField(choices=choice,default=1,verbose_name="是否启用")
    is_superuser = models.IntegerField(choices=choice,default=0,verbose_name="是否管理员")
    is_staff = models.IntegerField(choices=choice,default=1,verbose_name="是否员工")
    roles = models.ManyToManyField("Roles", related_name="users",verbose_name="角色")

    class Meta:
        db_table = "tb_user"
        verbose_name_plural = "用户表"

    def __str__(self):
        return self.user_name




class Menu(BaseModel):
    path = models.CharField(max_length=50,verbose_name="路径")
    component = models.CharField(max_length=50,verbose_name="组件")
    title = models.CharField(max_length=50,verbose_name="标题")
    icon = models.CharField(max_length=50,verbose_name="图标")
    redirect = models.CharField(max_length=50,blank=True,verbose_name="重定向页面")
    parent = models.ForeignKey("self",blank=True,null=True,verbose_name="父级菜单",on_delete=models.CASCADE)

    class Meta:
        db_table = "tb_menu"
        verbose_name_plural = "菜单表"

    def __str__(self):
        return self.title


class Roles(BaseModel):
    name = models.CharField(max_length=50,verbose_name="角色名称")
    menu = models.ManyToManyField("Menu",related_name="roles",verbose_name="菜单")

    class Meta:
        db_table = "tb_roles"
        verbose_name_plural = "角色表"

    def __str__(self):
        return self.name

from django.db import models


# 创建user管理器
class UserInfoManager(models.Manager):
    def create(self, userId, username, password, email):
        userInfo = self.model()
        userInfo.userID = userId
        userInfo.userName = username
        userInfo.password = password
        userInfo.email = email

        return userInfo


# 创建用户模型类
class UserInfo(models.Model):
    userID = models.IntegerField('userId', primary_key=True, auto_created=True)
    userName = models.CharField('userName', max_length=20, null='false')
    password = models.CharField('password', max_length=40, null='false')
    email = models.CharField('email', max_length=40, null='false')
    userTelephone = models.CharField('userTelephone', max_length=20)
    isDelete = models.BooleanField(default='false')
    users = UserInfoManager()

    class Meta:
        db_table = 'tableUser'


class AddressManager(models.Manager):
    def create(self, addId, addInfo, recName, mailId, recTel, addTouser):
        Address = self.model()
        Address.addressId = addId
        Address.addressInfo = addInfo
        Address.receiveName = recName
        Address.mailId = mailId
        Address.receiveTel = recTel
        Address.addToUser = addTouser

        return Address


class Address(models.Model):
    addressId = models.IntegerField('addressId', primary_key=True, auto_created=True)
    addressInfo = models.CharField('addressInfo', max_length=150, null='false')
    receiveName = models.CharField('receiveName', max_length='10', null='false')
    mailId = models.IntegerField('mailId')
    receiveTel = models.CharField('receiveTel', max_length=20, null='false')
    addToUser = models.ForeignKey('UserInfo')
    adds = AddressManager()

    class Meta:
        db_table = 'tableAddress'










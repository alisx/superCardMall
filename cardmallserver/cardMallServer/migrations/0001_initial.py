# Generated by Django 2.1.2 on 2019-01-05 09:07

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BannerInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='no_title', max_length=200, verbose_name='标题')),
                ('imgpath', models.CharField(default='no_iamge', max_length=1024, verbose_name='图片链接')),
                ('bannerurl', models.CharField(default='no_url', max_length=1024, verbose_name='文章链接')),
                ('index', models.IntegerField(default=0)),
                ('bannerid', models.CharField(default='no_bannerid', max_length=100, verbose_name='条幅ID')),
                ('type', models.CharField(default='no_type', max_length=100, verbose_name='广告状态')),
            ],
        ),
        migrations.CreateModel(
            name='CardUser',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='cardName', max_length=100, verbose_name='用户名')),
                ('xinid', models.CharField(default='cardId', max_length=100, verbose_name='用户id')),
                ('headObj', models.CharField(default='no_url', max_length=1024, verbose_name='头像')),
                ('phonenum', models.CharField(default='no_phone', max_length=100, verbose_name='手机号')),
            ],
        ),
        migrations.CreateModel(
            name='Order_product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=512)),
                ('image', models.CharField(max_length=512)),
                ('price', models.IntegerField(default=100)),
                ('quantity', models.IntegerField(default=1)),
                ('product_id', models.CharField(default='no_productid', max_length=100, verbose_name='产品ID')),
            ],
        ),
        migrations.CreateModel(
            name='ProductInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('productname', models.CharField(default='no_title', max_length=200, verbose_name='产品名')),
                ('productimgpath', models.CharField(default='no_iamge', max_length=1024, verbose_name='图片链接')),
                ('productid', models.CharField(default='no_productid', max_length=100, verbose_name='产品ID')),
                ('currentpeice', models.CharField(default='100.00', max_length=50, verbose_name='产品价格')),
                ('price', models.CharField(default='100.00,200.00,500.00,1000.00', max_length=100, verbose_name='产品价格')),
                ('inventory', models.IntegerField(default=100)),
                ('productcategories', models.CharField(default='no_categories', max_length=200, verbose_name='产品类别')),
                ('productcontent', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='UserOrder',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('createtime', models.DateTimeField(auto_now_add=True)),
                ('updatatime', models.DateTimeField(auto_now=True)),
                ('orderid', models.CharField(default='no_orderid', max_length=200, verbose_name='订单ID')),
                ('phone', models.CharField(max_length=15, verbose_name='订单手机号')),
                ('address', models.CharField(max_length=512, verbose_name='收货地址')),
                ('total', models.IntegerField(default=0)),
                ('orderType', models.CharField(max_length=100, verbose_name='订单状态')),
                ('paymentaccount', models.CharField(default='no_paymentaccount', max_length=200, verbose_name='支付账户')),
                ('transactionid', models.CharField(default='no_transactionid', max_length=512, verbose_name='转账id')),
                ('transtime', models.DateTimeField(default=django.utils.timezone.now)),
                ('carduser', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='orders', to='cardMallServer.CardUser')),
            ],
        ),
        migrations.AddField(
            model_name='order_product',
            name='order',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='products', to='cardMallServer.UserOrder'),
        ),
    ]

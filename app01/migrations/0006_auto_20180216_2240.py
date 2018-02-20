# Generated by Django 2.0.1 on 2018-02-16 22:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app01', '0005_auto_20180215_2359'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
            ],
            options={
                'verbose_name_plural': '微博分类',
                'db_table': 'Category',
            },
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateTimeField(auto_created=True)),
                ('comment_type', models.IntegerField(choices=[(0, 'comment'), (1, 'thumb_up')], default=0)),
                ('comment', models.CharField(max_length=140, verbose_name='评论字数')),
                ('p_comment', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='child_comments', to='app01.Comment', verbose_name='')),
            ],
            options={
                'verbose_name_plural': '评论',
                'db_table': 'Comment',
            },
        ),
        migrations.CreateModel(
            name='Tags',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=64, unique=True, verbose_name='标签名')),
            ],
            options={
                'verbose_name_plural': '标签',
                'db_table': 'Tags',
            },
        ),
        migrations.CreateModel(
            name='Topic',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=140, verbose_name='话题名称')),
                ('date', models.DateTimeField()),
            ],
            options={
                'verbose_name_plural': '话题',
                'db_table': 'Topic',
            },
        ),
        migrations.CreateModel(
            name='Weibo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wb_type', models.IntegerField(choices=[(0, 'new'), (1, 'forward'), (2, 'collect')], default=0, verbose_name='微博类型')),
                ('text', models.CharField(max_length=140, verbose_name='微博内容')),
                ('pictures_link_id', models.CharField(blank=True, max_length=128, null=True, verbose_name='图片连接id')),
                ('video_link_id', models.CharField(blank=True, max_length=128, null=True, verbose_name='视频链接id')),
                ('perm', models.IntegerField(choices=[(0, '公开'), (1, '仅自己可见'), (2, '好友圈')], default=0, verbose_name='微博权限')),
                ('date', models.DateTimeField(auto_now_add=True, verbose_name='发布日期')),
                ('forward_or_collect_from', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='forward_or_collects', to='app01.Weibo')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserProfile')),
            ],
            options={
                'verbose_name_plural': '个人微博列表',
                'db_table': 'Weibo',
            },
        ),
        migrations.AddField(
            model_name='comment',
            name='to_weibo',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.Weibo', verbose_name='评论的微博'),
        ),
        migrations.AddField(
            model_name='comment',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app01.UserProfile', verbose_name='评论的人'),
        ),
    ]
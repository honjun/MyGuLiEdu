# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2020-07-15 12:55
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('orgs', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CourseInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(max_length=200, upload_to='course/', verbose_name='课程封面')),
                ('name', models.CharField(max_length=20, verbose_name='课程名称')),
                ('study_time', models.IntegerField(default=0, verbose_name='学习时长')),
                ('study_num', models.IntegerField(default=0, verbose_name='学习人数')),
                ('level', models.CharField(choices=[('gj', '高级'), ('zj', '中级'), ('cj', '初级')], default='cj', max_length=5, verbose_name='课程 难度')),
                ('love_num', models.IntegerField(default=0, verbose_name='收藏数')),
                ('click_num', models.IntegerField(default=0, verbose_name='访问量')),
                ('desc', models.CharField(max_length=200, verbose_name='课程简介')),
                ('detail', models.TextField(verbose_name='课程详情')),
                ('category', models.CharField(choices=[('qd', '前端开发'), ('hd', '后端开发')], max_length=5, verbose_name='课程类别')),
                ('course_notice', models.CharField(max_length=200, verbose_name='课程公告')),
                ('course_need', models.CharField(max_length=100, verbose_name='课程须知')),
                ('teacher_tell', models.CharField(max_length=100, verbose_name='老师教导')),
                ('is_banner', models.BooleanField(default=False, verbose_name='是否轮播')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('orginfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgs.OrgInfo', verbose_name='所属机构')),
                ('teacherinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='orgs.TeacherInfo', verbose_name='所属讲师')),
            ],
            options={
                'verbose_name': '课程信息',
                'verbose_name_plural': '课程信息',
            },
        ),
        migrations.CreateModel(
            name='LessonInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='章节名称')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('courseinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseInfo', verbose_name='所属课程')),
            ],
            options={
                'verbose_name': '章节信息',
                'verbose_name_plural': '章节信息',
            },
        ),
        migrations.CreateModel(
            name='SourceInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='资源名称')),
                ('down_load', models.FileField(max_length=200, upload_to='source/', verbose_name='下载路径')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('courseinfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.CourseInfo', verbose_name='所属课程')),
            ],
            options={
                'verbose_name': '资源信息',
                'verbose_name_plural': '资源信息',
            },
        ),
        migrations.CreateModel(
            name='VideoInfo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50, verbose_name='视频名称')),
                ('study_time', models.IntegerField(default=0, verbose_name='视频时长')),
                ('url', models.URLField(default='http://www.atguigu.com', verbose_name='视频链接')),
                ('add_time', models.DateTimeField(default=datetime.datetime.now, verbose_name='添加时间')),
                ('lessoninfo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='courses.LessonInfo', verbose_name='所属章节')),
            ],
            options={
                'verbose_name': '视频信息',
                'verbose_name_plural': '视频信息',
            },
        ),
    ]

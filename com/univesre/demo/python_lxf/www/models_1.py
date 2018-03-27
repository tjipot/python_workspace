#! /usr/bin/env python3
# -*- coding: utf-8 -*-

# About: very good example of text format in Python, from line 31, 4 blanks are in front of that line even I used tab key! One thing should be noted is I copied the lines from line 31 from github;

'''
Models for user, blog, comment.
'''

import time, uuid
from orm import Model, StringField, BooleanField, FloatField, TextField

def next_id():
	return '%015d%s000' %(int(time.time()*1000), uuid.uuid4().hex)

class User(Model):
	__table__ = "users"
	# users table's field: id, email, passwd, admin, name, image, created_at;
	id = StringField(primary_key = True, default = next_id, ddl = 'varchar(50)')
	email = StringField(ddl = 'varchar(50)')
	passwd = StringField(ddl = 'varchar(50)')
	admin = BooleanField()
	name = StringField(ddl = 'varchar(50)')
	image = StringField(ddl = 'varchar(500)')
	created_at = FloatField(default = time.time)

class Blog(Model):
	__table__ = 'blogs'
	# blogs table's field: id, user_id, user_name, user_image, name, summary, content, created_at;
	id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    name = StringField(ddl='varchar(50)')
    summary = StringField(ddl='varchar(200)')
    content = TextField()
    created_at = FloatField(default=time.time)

class Comment(Model):
    __table__ = 'comments'
    # comments table's field: id, blog_id, user_id, user_name, user_image, content, created_at;
    id = StringField(primary_key=True, default=next_id, ddl='varchar(50)')
    blog_id = StringField(ddl='varchar(50)')
    user_id = StringField(ddl='varchar(50)')
    user_name = StringField(ddl='varchar(50)')
    user_image = StringField(ddl='varchar(500)')
    content = TextField()
    created_at = FloatField(default=time.time)



    
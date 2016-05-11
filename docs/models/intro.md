# Chapter Model Layer

## Overview
The application works with 3 models. They are:
* Site
* Category
* Post

`Site` model stores metadata about your site, such as title, tagline and
your about page.

A `Category` instance defines a list of post whose theme is similar. It can be
used to create column in your blog.

`Post` stores an article and its metadata.

## Accessing Data
All models offers high-level APIs to manipulating data. It is *strongly recommended*
to use them when you want to do something with database. See documents of respective
model.

# Site Model
Site model has all metadata about your blog, including title, tagline and about  page.

--------------------------------------------------------------------------------

# Fields
Site model contains the following fields.

Field Name | Type      | Definition                          | Remark
---------- | --------- | ----------------------------------- | ---------------------
name       | CharField | Blog name                           | Maximum length is 100
tagline    | TextField | Slogan of blog                      |
about      | TextField | Content of about page in `Markdown` |

--------------------------------------------------------------------------------

# Data Accessing
Site model is intended to save only one instance in database, so no customized `Manager` is offered.

There are several model methods to retrieve data.
- [get_site_info](#get_site_info)
- [get_about](#get_about)

**Important**: The following methods only operate on the _first instance_ (more accurately, instance whose pk equals to 1), if multiple instances exist in table.

## get_site_info(cls)
Returns basic information about site, such as name and tagline.

Example:

```
# Create an instance in brand new database
Site.objects.create(name='example', tagline='hello world')

# User code
def foo():
    site = Site.get_site_info()
    # site = {'name':'example',
              'tagline':'hello world'}
    do_something_else()
```

## get_about(cls)
Returns HTML version of about page content.

### Dependency
`markdown` is required in this method

--------------------------------------------------------------------------------

## Known issues
1. Because the admin tools Django offered is unable to restrict the number of instance in a table, it's possible to create multiple `Site` instances.

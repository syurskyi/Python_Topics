from mongoengine import *
connect('mongoengine_test', host='localhost', port=27017)

# Here we specify the name of our database and location. Since we’re still using the default host and port,
# you can omit these parameters.
# Defining a Document

# To set up our document object, we need to define what data we want our document object to have.
# Similar to many other ORMs, we’ll do this by subclassing the Document class and providing the types of data we want:

import datetime

class Post(Document):
    title = StringField(required=True, max_length=200)
    content = StringField(required=True)
    author = StringField(required=True, max_length=50)
    published = DateTimeField(default=datetime.datetime.now)

# NOTE: One of the more difficult tasks with database models is validating data. How do you make sure that
# the data you’re saving conforms to some format you need? Just because a database is said to be schema-less
# doesn’t mean it is schema-free.
#
# In this simple model, we’ve told MongoEngine that we expect a Post instance to have a title, content, an author,
# and the date it was published. Now the base Document object can use that information to validate
# the data we provide it.
#
# So, for example, if we try to save a Post without a title then it’ll throw an Exception and let us know.
# We can take this even further and add more restrictions, like string length. Notice that
# some of the fields have a max_length parameter set. This tells the Document, as you probably guessed,
# to only allow a maximum string length of however many characters we specify. There are quite
# a few more parameters like this we can set, including:
#
#     db_field: Specify a different field name
#     required: Make sure this field is set
#     default: Use the given default value if no other value is given
#     unique: Make sure no other document in the collection has the same value for this field
#     choices: Make sure the field’s value is equal to one of the values given in an array
#
# Each field type has its own set of parameters, so be sure to check the documentation for more info.
# Saving Documents
#
# To save a document to our database, we’ll use the save() method. If the document already exists in the database,
# then all of the changes will be made on the atomic level to the existing document. If it doesn’t exist, however,
# then it will be created.
#
# Here is an example of creating and saving a document:

post_1 = Post(
    title='Sample Post',
    content='Some engaging content',
    author='Scott'
)
post_1.save()       # This will perform an insert
print(post_1.title)
post_1.title = 'A Better Post Title'
post_1.save()       # This will perform an atomic edit on "title"
print(post_1.title)

# A few things to note about the .save() call:
#
#     PyMongo will perform validation when you call .save(). This means it will check the data you’re saving against
#     the schema you declared in the class. If the schema (or a constraint) is violated, then an exception is thrown
#     and the data is not saved.
#     Since Mongo doesn’t support true transactions, there is no way to “roll back” the .save() call like you can in
#     SQL databases. Although you can get close to performing transactions with two phase commits,
#     they still don’t support rollbacks.
#
# What happens when you leave off the title?

# post_2 = Post(content='Content goes here', author='Michael')
# post_2.save()

# You should see the following exception:

# raise ValidationError(message, errors=errors)
# mongoengine.errors.ValidationError:
# ValidationError (Post:None) (Field is required: ['title'])
#

# Object Oriented Features
#
# With MongoEngine being object oriented, you can also add methods to your subclassed document.
# Consider the following example where a function is used to modify the default queryset
# (which returns all objects of the collection). By using this, we can apply a default filter to the class
# and get only the desired objects:

class Post(Document):
    title = StringField()
    published = BooleanField()

    @queryset_manager
    def live_posts(clazz, queryset):
        return queryset.filter(published=True)

# Referencing Other Documents
#
# You can also use the ReferenceField object to create a reference from one document to another. MongoEngine handles
# the lazy de-referencing automatically upon access, which is more robust and less error-prone than having
# to remember to do it yourself everywhere in your code. An example:

class Author(Document):
    name = StringField()

class Post(Document):
    author = ReferenceField(Author)

Post.objects.first().author.name

# In the code above, using a document reference, we can easily find the author of the first post.
# There are quite a few more field classes (and parameters) than what we introduced here, so be sure to check out
# the documentation on Fields for more info.
# From all of these examples you should be able to see that MongoEngine is well suited to manage your database
# objects for just about any type of application. The features available at the developer’s disposal make it
# incredibly easy to create an efficient and scalable program. In case you’re looking for more help related
# to MongoEngine, be sure to check out their comprehensive user guide.
# Conclusion
# With Python being a high-level, highly scalable, modern language, it needs a database (and driver)
# that can keep up to its potential, which is why MongoDB is such a good fit.
# Free Bonus: Click here to download a Python + MongoDB project skeleton with full source code that shows you how
# to access MongoDB from Python.
# We saw in this article how we can exploit the strengths of MongoDB to our advantage and build a highly flexible
# and scalable application. Feel free to let us know your thoughts in the comments section!
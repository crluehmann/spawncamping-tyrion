from google.appengine.ext import ndb

## User class

class User(ndb.Model):
    username = ndb.StringProperty(required=True)
    email = ndb.StringProperty(required=True)
    fname = ndb.StringProperty(required=True)
    lname = ndb.StringProperty(required=True)


class Keys(ndb.Model):
    userkey = ndb.Key('username', 'fname', 'greeting')


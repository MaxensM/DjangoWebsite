from django.conf import settings
class DatabaseAppsRouter(object):

    def db_for_read(self, model, **hints):
        print ("read" + model._meta.app_label)
        if model._meta.app_label == 'mongo':
            return 'mongodb'
        return 'default'

    def db_for_write(self, model, **hints):
        print ("write " + model._meta.app_label)
        if model._meta.app_label == 'mongo':
            return 'mongodb'
        return 'default'

    def allow_relation(self, obj1, obj2, **hints):
        print ("allow" + obj1._meta.app_label)
        if obj1._meta.app_label == 'mongo' and obj2._meta.app_label == 'mongo':
            return True
        elif 'mongo' not in [obj1._meta.app_label, obj2._meta.app_label]:
            return True
        return False

    def allow_syncdb(self, db, model):
        print ("sycn" + model._meta.app_label)
        if db == 'mongodb' or model._meta.app_label == "mongo":
            return False
        else:
            return True
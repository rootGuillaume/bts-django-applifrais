#from django.contrib.auth.decorators import user_passes_test

#def groupRequired(*group_names):
#    def in_groups(user):
#        if user.is_authenticated():
#            if bool(user.groups.filter(name__in=group_names)):
#                return True
#        return False
#    return user_passes_test(in_groups)

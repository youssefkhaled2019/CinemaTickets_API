from rest_framework import permissions




class IsAuthorOrReadOnly(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:  #SAFE_METHODS = ('GET', 'HEAD', 'OPTIONS')
            return True
        return obj.author == request.user  #delete,update
    


class IsAuthor(permissions.BasePermission):    
    def has_object_permission(self, request, view, obj):
        print(request.user)
        return obj.author == request.user# username and password
from  rest_framework.permissions import  BasePermission,SAFE_METHODS,IsAdminUser

from account.models import Profile


class IsSenderOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        elif request.user and request.user.is_authenticated and request.user.profile:
            if request.user.profile.is_sender == True:
                return True

class IsAuthorOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        #print(request.user.profile)
        if request.method in SAFE_METHODS:
            return True
        elif request.user and request.user.is_authenticated and request.user.profile:
            if request.user.profile.is_sender == True:
                return True
    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user.profile == obj.profile)

class IsBuyerOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if request.user and request.user.is_authenticated and request.user.profile.is_sender == False:
            return True

    def has_object_permission(self, request, view, obj):
        if request.method in SAFE_METHODS:
            return True
        return bool(request.user.profile == obj.profile)
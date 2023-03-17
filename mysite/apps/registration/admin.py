from django.contrib import admin  # noqa: F401
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from registration.models import UserInfo


# Register your models here.

admin.site.unregister(User)


class UserInfoInline(admin.StackedInline):
    model = UserInfo
    can_delete = False
    verbose_name_plural = "User Information"
    extra = 0


@admin.register(User)
class userAdminView(UserAdmin):
    inlines = (UserInfoInline, )
    list_display = ("email", "username", "first_name", "last_name", "user_type")
    search_fields = ("email", "username", "first_name", "last_name",)
    list_filter = ("username", "first_name", "last_name", "is_active")

    @admin.display(ordering="user_type")
    def user_type(self, obj):
        return obj.user_info.user_type

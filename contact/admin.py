from django.contrib import admin
from contact import models

# Register your models here.


@admin.register(models.Contact)
class ContactAdmin(admin.ModelAdmin):
    # display of items in the admin page
    list_display = 'id', 'first_name', 'last_name', 'phone', 'category',

    # ORDER BY:
    # (if ordering = '-id', ORDER BY id DESC)
    ordering = 'id',

    # search bar (response if search is in items above)
    search_fields = 'id', 'first_name', 'last_name',
    list_per_page = 10
    list_max_show_all = 200

    # show which values are editable on the main dashboard without having to
    #  enter the specific contact to edit.
    # list_editable = 'first_name','last_name'

    list_display_links = 'id', 'first_name',
    # list_filter = ('created_date',)


@admin.register(models.Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = 'id', 'name',
    ordering = 'id',
    search_fields = 'id', 'name',
    list_editable = 'name',

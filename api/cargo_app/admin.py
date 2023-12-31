from django.contrib import admin
from .models import Group, Status, TrackCode


class GroupAdmin(admin.ModelAdmin):
    list_display = ('statuses',)  # Add other fields you want to display in the admin list view
    search_fields = ('statuses__name_status',)  # Add fields you want to be searchable
    filter_horizontal = ('track_codes',)  # This is for ManyToMany fields


class StatusAdmin(admin.ModelAdmin):
    list_display = ('name_status', 'pk')  # Display the status name and primary key
    search_fields = ('name_status',)  # Make the status name searchable


class TrackCodeAdmin(admin.ModelAdmin):
    list_display = ('track_code', 'pk', 'status', 'date', 'date_format', 'created_at', 'updated_at')
    search_fields = ('track_code', 'status__name_status')
    list_filter = ('status', 'date')  # Filter by status and date


# Register your models here.
admin.site.register(Group, GroupAdmin)
admin.site.register(Status, StatusAdmin)
admin.site.register(TrackCode, TrackCodeAdmin)

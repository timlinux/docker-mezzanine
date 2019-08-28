from django.contrib import admin
from django.conf import settings
from kartoza_project.models import (
    Project,
    ProjectImage,
    Reference,
    ProjectCategory
)


class ProjectImageInline(admin.TabularInline):
    model = ProjectImage
    extra = 3
    verbose_name_plural = 'Project images/screenshots'
    readonly_fields = ['admin_thumb', ]
    fields = ['admin_thumb', 'image', 'caption']


class ReferenceStackedInline(admin.StackedInline):
    model = Reference
    extra = 1


class ProjectAdmin(admin.ModelAdmin):
    """
    Admin class for project
    """
    list_display = ['admin_thumb', 'title', 'short_description', 'date_start', 'date_end']
    list_display_links = ['title', ]
    inlines = [ProjectImageInline, ReferenceStackedInline]


class ProjectCategoryAdmin(admin.ModelAdmin):
    """
    Admin class for project categories. Hides itself from the admin menu
    unless explicitly specified.
    """

    fieldsets = ((None, {"fields": ("title",)}),)

    def in_menu(self):
        """
        Hide from the admin menu unless explicitly set in ``ADMIN_MENU_ORDER``.
        """
        for (name, items) in settings.ADMIN_MENU_ORDER:
            if "kartoza_project.PersonCategory" in items:
                return True
        return False


class ReferenceAdmin(admin.ModelAdmin):
    """
       Admin class for project reference. Hides itself from the admin menu
       unless explicitly specified.
       """

    fieldsets = ((None, {"fields": ('name', 'role', 'telephone', 'email')}),)


admin.site.register(Project, ProjectAdmin)
admin.site.register(ProjectCategory, ProjectCategoryAdmin)
admin.site.register(Reference, ReferenceAdmin)
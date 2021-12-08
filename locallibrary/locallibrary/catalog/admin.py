from django.contrib import admin
from .models import Author, Genre, Book, BookInstance

# Register your models here.


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('last_name', 'first_name', 'date_of_birth', 'date_of_death')
    fields = ['first_name', 'last_name', ('date_of_birth', 'date_of_death')]
    pass

class BookAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'display_genre')
    
    pass

class BookInstanceAdmin(admin.ModelAdmin):
    list_display = ('id','book', 'imprint')
    list_filter = ('status', 'due_back')
    exclude = ['id']
    fieldsets = (
        (None, {
            'fields': ('book','imprint')
        }),
        ('Availability', {
            'fields': ('status', 'due_back')
        }),
    )
    pass



admin.site.register(Book,BookAdmin)
admin.site.register(Author,AuthorAdmin)
admin.site.register(Genre)
admin.site.register(BookInstance,BookInstanceAdmin)
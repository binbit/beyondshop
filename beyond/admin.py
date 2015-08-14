from django.contrib import admin
from beyond.models import Picture, Size, Category, Tag, ImageProperty, Order, OrderItem


class ImageAdmin(admin.ModelAdmin):
    pass


class ImageInline(admin.TabularInline):
    model = ImageProperty
    fields = ('image', 'Main')


class PictureAdmin(admin.ModelAdmin):
    inlines = [ImageInline, ]
    list_display = ['title', 'size']

    class Media:
        def __init__(self):
            pass

        js = ('beyond/js/picture_admin.js',)


class PictureInline(admin.TabularInline):
    model = OrderItem
    readonly_fields = ('picture', 'cost')
    fields = ('picture', 'cost')
    extra = 0
    can_delete = False

class OrderAdmin(admin.ModelAdmin):
    exclude = ('uid', )
    inlines = [PictureInline, ]

admin.site.register(Picture, PictureAdmin)
admin.site.register([Size, Category, Tag])
admin.site.register(Order, OrderAdmin)

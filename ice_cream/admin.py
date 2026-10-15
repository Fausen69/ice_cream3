from django.contrib import admin
from django.contrib.auth.models import Group

# Из модуля models импортируем модель Category...
from .models import Category, IceCream, Topping, Wrapper


admin.site.empty_value_display = 'Поле не задано'

if admin.site.is_registered(Group): 
    admin.site.unregister(Group) 


class IceCreamInline(admin.TabularInline):
    model = IceCream
    extra = 1


class IceCreamAdmin(admin.ModelAdmin):
    list_display = (
        'title',
        'description',
        'is_published',
        'is_on_main',
        'category',
        'wrapper'
    )
    list_editable = (
        'is_published',
        'is_on_main',
        'category'
    )    
    search_fields = ('title',) 
    list_filter = ('category',)
    list_display_links = ('title',)
    filter_horizontal = ('toppings',)


class CategoryAdmin(admin.ModelAdmin):
    inlines = (
        IceCreamInline,
    )
    list_display = (
        'title',        
    )

# Регистрируем кастомное представление админ-зоны
admin.site.register(IceCream, IceCreamAdmin)
# ...и регистрируем её в админке:
admin.site.register(Category, CategoryAdmin) 
admin.site.register(Topping)
admin.site.register(Wrapper)
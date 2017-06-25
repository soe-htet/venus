from django.contrib import admin

from .models import Product, ProductImage, Tag, Variation
# Register your models here.

class ProductImageInline(admin.TabularInline):
	model = ProductImage

class TagInline(admin.TabularInline):
	prepopulated_fields = {'slug':('tag',)}
	extra = 1
	model = Tag

class ProductAdmin(admin.ModelAdmin):
	inlines = [TagInline, ProductImageInline]
	search_fields = ['title','description']
	list_display = ['title','price','sale_price','active','updated']
	list_editable = ['price','sale_price','active']
	list_filter = ['price','title']
	readonly_fields = ['updated','timestamp']
	prepopulated_fields = {'slug': ('title',)}

	class Meta(object):
		model = Product


admin.site.register(Product,ProductAdmin)

admin.site.register(Variation)
			
from django.contrib import admin
from .models import Chaiverity,store,ChaiReview,chaicertificate


class ChaiReviewInline(admin.TabularInline):
    extra=2;
    model=ChaiReview
    
    
class ChaiverityAdmin(admin.ModelAdmin):
    list_display=['name','type','time']
    inlines=[ChaiReviewInline]   
    
class StoreAdmin(admin.ModelAdmin):
    list_display=['name','location']
    filter_horizontal=('chai_Chaiverity',)
class chaicertificate_admin(admin.ModelAdmin):
    list_display=['chai','certificate_number'] 
         

admin.site.register(Chaiverity,ChaiverityAdmin)
admin.site.register(store,StoreAdmin)
admin.site.register(chaicertificate,chaicertificate_admin)
# Register your models here.

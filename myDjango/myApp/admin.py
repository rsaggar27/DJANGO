from django.contrib import admin
from .models import Chai_Variety,ChaiStore,ChaiCertificate,ChaiReview
# Register your models here.

class ChaiReviewInline(admin.TabularInline):
    model=ChaiReview
    extra=2

class ChaiVarietyAdmin(admin.ModelAdmin):
    list_display=('name','type','description')
    inlines=[ChaiReviewInline]

class StoreAdmin(admin.ModelAdmin):
    list_display = ('name', 'location')
    filter_horizontal = ('chai_varieties',)

class ChaiCertificateAdmin(admin.ModelAdmin):
    list_display = ('chai', 'certificate_number', 'issued_date')


admin.site.register(Chai_Variety, ChaiVarietyAdmin)
admin.site.register(ChaiStore, StoreAdmin)
admin.site.register(ChaiCertificate, ChaiCertificateAdmin)
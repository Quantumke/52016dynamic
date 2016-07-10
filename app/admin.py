from django.contrib import admin
from app.models import *
# Register your models here.

class ProspectsAdmin(admin.ModelAdmin):
    pass

admin.site.register(prospects, ProspectsAdmin)

class FeedbackAdmin(admin.ModelAdmin):
    pass
admin.site.register(feedback, FeedbackAdmin)

class PortfolioAdmin(admin.ModelAdmin):
    pass
admin.site.register(portfolio, PortfolioAdmin)

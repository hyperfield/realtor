from django.contrib import admin
from .models import Flat, Complaint, Owner


class OwnerInline(admin.TabularInline):
    model = Owner.owned_flats.through
    raw_id_fields = ['owner']


class FlatAdmin(admin.ModelAdmin):
    search_fields = ['town', 'address', 'owner', 'id']
    readonly_fields = ['created_at']
    list_display = ['address', 'price', 'new_building', 'construction_year',
                    'town', 'owners_phonenumber', 'owner_pure_phone']
    list_editable = ['new_building']
    list_filter = ['new_building', 'rooms_number', 'has_balcony']
    raw_id_fields = ['liked_by']
    inlines = [OwnerInline, ]


class ComplaintAdmin(admin.ModelAdmin):
    search_fields = ['complaint_flat', 'complainant']
    raw_id_fields = ['complaint_flat']


class OwnerAdmin(admin.ModelAdmin):
    raw_id_fields = ['owned_flats']
    search_fields = ['owner', 'owned_flats']


admin.site.register(Flat, FlatAdmin)
admin.site.register(Complaint, ComplaintAdmin)
admin.site.register(Owner, OwnerAdmin)

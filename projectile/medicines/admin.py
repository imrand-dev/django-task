from django.contrib import admin

from medicines.models import Medicine, MedicineStock, Category

@admin.register(Medicine)
class MedicineModelAdmin(admin.ModelAdmin):
    list_display = ["name", "brand_name"]


@admin.register(MedicineStock)
class MedicineStockModelAdmin(admin.ModelAdmin):
    list_display = ["medicine_name", "total_pack"]


@admin.register(Category)
class CategoryModelAdmin(admin.ModelAdmin):
    list_display = ["category_name"]

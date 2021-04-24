from django.contrib import admin
from .models import *

# Register your models here.

@admin.register(Categories)
class adminCategory(admin.ModelAdmin):
	display_list = ['name']

@admin.register(Product)
class adminCategory(admin.ModelAdmin):
	list_display = ['name', 'category', 'price', 'image', 'qty']
	list_filter = ['name', 'category', 'price']
	ordering = ['-uploaded']
	#raw_id_fields = ['category']
	
admin.site.register(Star)
admin.site.register(UserProfile)
#admin.site.register(Desk)


from django.core.mail import send_mail   
def send_package_update_mail(modeladmin, request, queryset):
    for book in queryset:
        order_stage = book.order_stage
        message = 'Your order is '
        # Please, keep package_status exactly as the choice fields in order_stage
        package_status = [('Order placed', 'Order Placed'), ('Processing', 'In transit'), ('Delivered', 'Delivered')]
        for i in range(0, len(package_status)):
            if package_status[i][0] == order_stage:
                if i == len(package_status) - 1:
                    message += package_status[i][0]
                else:
                    message += package_status[i+1][0]
                    book.order_stage = package_status[i+1][0]
                    book.save()
                
        title ='Package Update'
        send_mail(title, message, 'atumasaake@gmail.com', [f'{book.name.email}'])

send_package_update_mail.short_description = 'Send delivery stage to user, mark as seen'


@admin.register(Desk)
class adminDesk(admin.ModelAdmin):
    list_display = ['name', 'deliveryMethod', 'cartItemDetails',
                    'paymentMethod', 'transaction_id', 'deliveryDate',
                    'phone', 'order_stage']
    list_filter = ['order_stage']
    actions = [send_package_update_mail, ]
    ordering = ['-deliveryDate']
    
    
	
	

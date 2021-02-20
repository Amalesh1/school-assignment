from django.contrib import admin
from students.models import Contact, EnglishAssignment, MathAssignment, PhysicsAssignment

# Register your models here.
admin.site.register(Contact)
admin.site.register(EnglishAssignment)
admin.site.register(PhysicsAssignment)
admin.site.register(MathAssignment)


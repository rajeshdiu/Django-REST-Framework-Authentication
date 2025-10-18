from django.contrib import admin

from .models import *


admin.site.register(CustomUser)
admin.site.register(EmployeeModel)
admin.site.register(DepartmentModel)
admin.site.register(LeaveModel)
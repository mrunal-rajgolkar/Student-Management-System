from django.urls import path

from Student import views

urlpatterns = [
    path("",views.home, name = "home"),

    path("display",views.display_student, name = "displaystudent"),

    path("add",views.add_student, name = "addstudent"),

    path("edit/<int:id>",views.edit_students, name = "editstudent"),

    path("delete/<int:id>", views.delete_students, name="deletestudent"),

    path("login",views.login_function,name = "login"),

    path("register", views.register_function,name = "register"),

    path("logout",views.logout_function,name = "logout")

]

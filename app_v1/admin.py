from django.contrib import admin
from app_v1.models import (
    User,
    Address,
    Instructor,
    Course,
    Review,
    Lesson,
    Chapter,
    UserEnrollment,
    Exercise,
    Submission,
    UserSubmission,
    Payment,
    Notification,
    Subscription
)

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('username', 'email', 'phone')
    search_fields = ('username', 'email', 'phone')
    list_filter = ('is_staff', 'is_superuser', 'is_active')
    ordering = ('username',)

@admin.register(Address)
class AddressAdmin(admin.ModelAdmin):
    list_display = ('street', 'city', 'state', 'zip', 'country')
    search_fields = ('city', 'state', 'zip', 'country')
    list_filter = ('city', 'state', 'country')

@admin.register(Instructor)
class InstructorAdmin(admin.ModelAdmin):
    list_display = ('user', 'specialty')
    search_fields = ('user__username', 'specialty')

@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ('name', 'price', 'author')
    search_fields = ('name', 'author__user__username')
    list_filter = ('price', 'categories')  # Ensure 'categories' is not a ManyToManyField or remove from list_filter



@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('user_enrollment', 'rating')
    search_fields = ('user_enrollment__user__username', 'rating')
    list_filter = ('rating',)

@admin.register(Lesson)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('pk', 'name')
    search_fields = ('name',)
    ordering = ('pk',)

@admin.register(Chapter)
class ChapterAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)

@admin.register(UserEnrollment)
class UserEnrollmentAdmin(admin.ModelAdmin):
    list_display = ('user', 'course')
    search_fields = ('user__username', 'course__name')

@admin.register(Exercise)
class ExerciseAdmin(admin.ModelAdmin):
    list_display = ('level',)
    search_fields = ('level',)

@admin.register(Submission)
class SubmissionAdmin(admin.ModelAdmin):
    list_display = ('code', 'grade')
    search_fields = ('code', 'grade')

@admin.register(UserSubmission)
class UserSubmissionAdmin(admin.ModelAdmin):
    list_display = ('user', 'exercise')
    search_fields = ('user__username', 'exercise__name')



@admin.register(Payment)
class PaymentAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'status', 'user')
    search_fields = ('user__username', 'status')
    list_filter = ('status', 'date')

@admin.register(Notification)
class NotificationAdmin(admin.ModelAdmin):
    list_display = ('message', 'date_sent', 'user')
    search_fields = ('message', 'user__username')
    list_filter = ('date_sent',)

@admin.register(Subscription)
class SubscriptionAdmin(admin.ModelAdmin):
    list_display = ('start_date', 'end_date', 'status', 'user')
    search_fields = ('user__username', 'status')
    list_filter = ('start_date', 'end_date', 'status')

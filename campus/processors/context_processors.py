from django.contrib.auth.decorators import user_passes_test
from campus.models import Lecture, Notification
from accounts.models import User


def user_notifications(request):
    """ This function is used to display user notifications in all templates. """
    
    student_notifications = []
    lecturer_notifications = []
    total_lec_notifications = 0
    total_stud_notifications = 0
    
    if request.user.is_anonymous is False:  # check if user is anonymous
        try:
            lecturer_notifications = Notification.objects.filter(scheduled_lecture__lecturer=request.user.faculty) if str(request.user) == str(request.user.faculty) else []    # if logged in user is lec/HOD return notifications else return empty list
            total_lec_notifications = lecturer_notifications.count() if len(lecturer_notifications) > 0 else total_stud_notifications

        except:
            student_notifications = Notification.objects.filter(scheduled_lecture__student=request.user.student) if str(request.user) == str(request.user.student) else []    # if logged in user is student return notifications else return empty list
            total_stud_notifications = student_notifications.count() if len(lecturer_notifications) > 0 else total_lec_notifications        
            
    context = {
        'student_notifications': student_notifications,
        'lecturer_notifications': lecturer_notifications,
        'TotalStudentNotifications': total_stud_notifications,
        'TotalLecturerNotifications': total_lec_notifications,
    }
    return context
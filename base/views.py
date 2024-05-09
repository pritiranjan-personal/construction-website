from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.conf import settings
from base.forms import EnquiryForm

# Create your views here.



def index(request):
    form = EnquiryForm()
    # import pdb;pdb.set_trace()
    if request.method == 'POST':
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            send_mail(
                f"Enquiry No -{form.id}",
                f"{form.message}",
                settings.EMAIL_HOST_USER,
                ["mailtopritiranjan@gmail.com"],
                fail_silently=False
            )
            return redirect('index')
        else:
            print(form.errors)

    context = {"form" : form}
    return render(request, 'index.html', context)


# class EnquiryView():
#     """
#     Classes Create 
#     """
#     form_class = EnquiryForm
#     template_name = 'index.html'

#     def get(self, request, *args, **kwargs):
#         return super().get(request, *args, **kwargs)
    
    
#     def get_context_data(self, **kwargs):
#         context = super(ClassesCreateView, self).get_context_data(**kwargs)
#         topic_list = Courses.objects.filter(is_deleted=False, status="active")
#         # student_list = StudentProfile.objects.all()
#         # homework_list = Assignment.objects.all()
#         context['topic_list'] = topic_list
#         # context['student_list'] = student_list
#         # context['homework_list'] = homework_list
#         return context

#     def get_success_url(self, **kwargs):
#         messages.success(self.request, 'Class Created Successfully')
#         return reverse('classes:classes_list')


#     def form_valid(self, form):
#         with transaction.atomic():
#             self.object = form.save(commit=False)
#             # Assuming you want to do some additional processing before saving
#             # For example, set the created_by field to the current user
#             self.object.created_by = self.request.user

#             user_details = CustomUsers.objects.filter(id=self.request.user.id).first()
#             logged_user_type = str(user_details.user_type)

#             if logged_user_type == "teacher" :
#                 # get Teacher_details 
#                 teacher_details = TeacherProfile.objects.filter(is_deleted=0, user=self.request.user).first()
#                 print(f"teacher_details={teacher_details}")
#                 self.object.teacher_id = teacher_details.id

#             self.object.save_duration()  # Save the duration value
#             form.save_m2m()  # Save the many-to-many relationships
            
#             topic = self.request.POST.get('topic[]', None)
#             if topic:
#                 class_topic_assign(topic, self.object)
            
#             student = self.request.POST.get('student[]', None)
#             if student:
#                 class_student_assign(student, self.object)

#             homework = self.request.POST.get('homework[]', None)
#             if homework:
#                 class_homework_assign(homework, self.object)
        
#             # Get actitvity id
#             activity_obj = Activity.objects.filter(activity_name="Class created").first()
#             # Set activity log
#             ActivityLog.objects.create(activity_id=activity_obj, log_by=self.request.user, ip_address=self.request.META.get("REMOTE_ADDR"))

#         return super().form_valid(form)


#     def form_invalid(self, form):
#         error_message = 'Error saving the Form, check fields below.'
#         messages.error(self.request, error_message)
#         return super().form_invalid(form)
    

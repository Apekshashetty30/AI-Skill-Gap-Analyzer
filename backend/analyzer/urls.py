from django.urls import path
from .views import jobs_list, skill_gap, upload_resume

urlpatterns = [
    path('jobs/', jobs_list),
    path('skill-gap/<int:job_id>/<int:resume_id>/', skill_gap),
    path('upload-resume/', upload_resume),
]
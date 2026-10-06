import re
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from pypdf import PdfReader
from docx import Document
from .models import Jobs, Skills, JobSkills, ResumeSkills, Resumes


def jobs_list(request):
    jobs = Jobs.objects.all()

    data = []

    for job in jobs:
        skill_links = JobSkills.objects.filter(job_id=job.id)

        skills = []

        for link in skill_links:
            skill = Skills.objects.get(id=link.skill_id)
            skills.append(skill.skill_name)

        data.append({
            "id": job.id,
            "job_title": job.job_title,
            "required_skills": skills
        })

    return JsonResponse(data, safe=False)
def skill_gap(request, job_id, resume_id):
    job_skills = JobSkills.objects.filter(job_id=job_id)
    resume_skills = ResumeSkills.objects.filter(resume_id=resume_id)

    required_skills = []
    available_skills = []
    missing_skills = []

    for job_skill in job_skills:
        skill = Skills.objects.get(id=job_skill.skill_id)
        required_skills.append(skill.skill_name)

        if resume_skills.filter(skill_id=job_skill.skill_id).exists():
            available_skills.append(skill.skill_name)
        else:
            missing_skills.append(skill.skill_name)

    total_required = len(required_skills)
    total_available = len(available_skills)
    total_missing = len(missing_skills)

    if total_required > 0:
        gap_percentage = (total_missing / total_required) * 100
    else:
        gap_percentage = 0

    return JsonResponse({
        "required_skills": required_skills,
        "available_skills": available_skills,
        "missing_skills": missing_skills,
        "total_required": total_required,
        "total_available": total_available,
        "total_missing": total_missing,
        "skill_gap_percentage": round(gap_percentage, 2)
    })
@csrf_exempt
def upload_resume(request):
    if request.method != 'POST':
        return JsonResponse({
            "error": "Only POST method is allowed"
        }, status=405)

    if 'resume' not in request.FILES:
        return JsonResponse({
            "error": "Please upload a resume file"
        }, status=400)

    resume_file = request.FILES['resume']

    file_name = resume_file.name
    file_extension = file_name.lower().split('.')[-1]

    if file_extension == 'pdf':
        reader = PdfReader(resume_file)
        resume_text = ""

        for page in reader.pages:
            text = page.extract_text()

            if text:
                resume_text += text

    elif file_extension == 'docx':
        document = Document(resume_file)
        resume_text = ""

        for paragraph in document.paragraphs:
            resume_text += paragraph.text + "\n"

    elif file_extension == 'txt':
        resume_text = resume_file.read().decode('utf-8')

    else:
        return JsonResponse({
            "error": "Only PDF, DOCX and TXT files are supported"
        }, status=400)

    resume = Resumes.objects.create(
        user_id=1,
        file_name=file_name,
        resume_text=resume_text
    )

    skills = Skills.objects.all()

    for skill in skills:
        pattern = r'\b' + re.escape(skill.skill_name.lower()) + r'\b'

        if re.search(pattern, resume_text.lower()):
            ResumeSkills.objects.create(
                resume_id=resume.id,
                skill_id=skill.id
            )

    return JsonResponse({
        "message": "Resume uploaded successfully",
        "resume_id": resume.id,
        "file_name": file_name
    })
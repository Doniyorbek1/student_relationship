from django.shortcuts import render
from .models import Student,Contact
from django.http import JsonResponse,HttpRequest,HttpResponse

# Create view for Student
def get_student(request:HttpRequest)->JsonResponse:
    """
    Get all student
    """
    if request.method == 'GET':
        students = Student.objects.all()
        student_list = []
        for student in students:
            student_list.append({
                'id':student.id,
                'name':student.name,
                'roll':student.roll,
                'city':student.city
            })
        return JsonResponse({'students':student_list},safe=False)
def get_student_by_id(request:HttpRequest,id:int)->JsonResponse:
    """
    Get student by id
    """
    if request.method == 'GET':
        student = Student.objects.get(id=id)
        return JsonResponse({
            'id':student.id,
            'name':student.name,
            'roll':student.roll,
            'city':student.city
        })
def get_contact(request:HttpRequest)->JsonResponse:
    """
    Get all contact
    """
    if request.method == 'GET':
        contacts = Contact.objects.all()
        contact_list = []
        for contact in contacts:
            contact_list.append({
                'id':contact.id,
                'phone':contact.phone,
                'address':contact.address
            })
        return JsonResponse({'contacts':contact_list}, safe=False)
def get_contact_by_id(request:HttpRequest, id:int)->JsonResponse:
    """
    Get contact by id
    
    """
    if request.method == "GET":
        contact = Contact.objects.get(id=id)
        return JsonResponse({
            'id':contact.id,
            'phone':contact.phone,
            'address':contact.address
        })
# add student 
def add_student(request:HttpRequest)->HttpResponse:
    """
    Add student
    """
    if request.method == "POST":
        data = request.POST
        student = Student(
            first_name=data['first_name'],
            last_name=data['last_name'],
            contact = Contact( 
                phone=data['phone'],
                address=data['address']
            )
        )
        student.save()
        return HttpResponse('Student added successfully')
def add_contact(request:HttpRequest)->HttpResponse:
    """
    Add contact
    
    """
    if request.method == "POST":
        data = request.POST
        contact = Contact(
            phone=data['phone'],
            address=data['address']
        )
        contact.save()
        return HttpResponse('Contact added successfully')

def update_student(request:HttpRequest, id:int)->HttpResponse:
    """
    Update student
    """
    if request.method == "PUT":
        data = request.POST
        student = Student.objects.get(id=id)
        student.first_name = data.get('first_name', student.first_name)
        student.last_name = data.get('last_name', student.last_name)
        student.contact.phone = data.get('phone', student.contact.phone)
        student.contact.address = data.get('address', student.contact.address)
        student.save()
        return HttpResponse('Student updated successfully')
def update_contact(request:HttpRequest, id:int)->HttpResponse:
    """
    Update contact
    """
    if request.method == "PUT":
        data = request.POST
        contact = Contact.objects.get(id=id)
        contact.phone = data.get('phone', contact.phone)
        contact.address = data.get('address', contact.address)
        contact.save()
        return HttpResponse('Contact updated successfully')
def delete_student(request:HttpRequest, id:int)->HttpResponse:
    """
    Delete student
    """
    if request.method == "DELETE":
        student = Student.objects.get(id=id)
        student.delete()
        return HttpResponse('Student deleted successfully')
def delete_contact(request:HttpRequest, id:int)->HttpResponse:
    """
    Delete contact
    """
    if request.method == "DELETE":
        contact = Contact.objects.get(id=id)
        contact.delete()
        return HttpResponse('Contact deleted successfully') 
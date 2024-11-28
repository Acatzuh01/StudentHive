from django.shortcuts import render
from django.http import HttpResponse
from .models import Student
from .serializers import StudentSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status


# View to display a list of students in the HTML template
def student_list(request):
    students = Student.objects.all()  # Fetch all students
    return render(request, 'students/student_list.html', {'students': students})


# API View for handling Student List and Creation
class StudentListCreateAPIView(APIView):
    def get(self, request):
        """
        Handle GET request to retrieve all students.
        """
        students = Student.objects.all()  # Fetch all student records
        serializer = StudentSerializer(students, many=True)  # Serialize the data
        return Response(serializer.data)  # Return serialized data

    def post(self, request):
        """
        Handle POST request to create a new student.
        """
        serializer = StudentSerializer(data=request.data)  # Deserialize the incoming data
        if serializer.is_valid():  # Check if data is valid
            serializer.save()  # Save the student record
            return Response(serializer.data, status=status.HTTP_201_CREATED)  # Return the created student data
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return errors if invalid data


# API View for handling single student actions (retrieve, update, delete)
class StudentRetrieveUpdateDestroyAPIView(APIView):
    def get(self, request, pk):
        """
        Handle GET request to retrieve a single student by ID.
        """
        try:
            student = Student.objects.get(pk=pk)  # Get student by primary key
            serializer = StudentSerializer(student)  # Serialize student data
            return Response(serializer.data)  # Return serialized student data
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)  # Student not found

    def put(self, request, pk):
        """
        Handle PUT request to update a student's information.
        """
        try:
            student = Student.objects.get(pk=pk)  # Get student by primary key
            serializer = StudentSerializer(student, data=request.data)  # Deserialize incoming data and bind to student
            if serializer.is_valid():
                serializer.save()  # Save the updated student data
                return Response(serializer.data)  # Return updated student data
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)  # Return validation errors
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)  # Student not found

    def delete(self, request, pk):
        """
        Handle DELETE request to remove a student by ID.
        """
        try:
            student = Student.objects.get(pk=pk)  # Get student by primary key
            student.delete()  # Delete student record
            return Response({"message": "Student deleted successfully"}, status=status.HTTP_204_NO_CONTENT)  # Success message
        except Student.DoesNotExist:
            return Response({"error": "Student not found"}, status=status.HTTP_404_NOT_FOUND)  # Student not found


# A simple view for the homepage
def home(request):
    """
    Simple homepage view with a welcome message.
    """
    return HttpResponse("Welcome to the Student Registration System!")

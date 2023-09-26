from django.shortcuts import get_object_or_404, render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Employee
from .serializers import EmployeeSerializer
from rest_framework import serializers
from rest_framework import status

@api_view(['GET'])
def ApiOverview(request):
	api_urls = {
		'all_items': '/',
		'Add': '/create',
		'Update': '/update/pk',
		'Delete': '/employee/pk/delete'
	}

	return Response(api_urls)



@api_view(['POST'])
def add_employee(request):
	employee = EmployeeSerializer(data=request.data)

	# validating for already existing data
	if Employee.objects.filter(**request.data).exists():
		raise serializers.ValidationError('This data already exists')

	if employee.is_valid():
		employee.save()
		return Response(employee.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
	

@api_view(['GET'])
def view_employee(request):
	
	# checking for the parameters from the URL
	if request.query_params:
		employee = Employee.objects.filter(**request.query_params.dict())
	else:
		employee = Employee.objects.all()

	# if there is something in items else raise error
	if employee:
		serializer = EmployeeSerializer(employee, many=True)
		return Response(serializer.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
	

@api_view(['POST'])
def update_employee(request, pk):
	employee = Employee.objects.get(pk=pk)
	data = EmployeeSerializer(instance=employee, data=request.data)

	if data.is_valid():
		data.save()
		return Response(data.data)
	else:
		return Response(status=status.HTTP_404_NOT_FOUND)
	

@api_view(['DELETE'])
def delete_employee(request, pk):
	employee = get_object_or_404(Employee, pk=pk)
	employee.delete()
	return Response("Deleted successfully")






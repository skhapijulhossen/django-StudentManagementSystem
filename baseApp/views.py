from django.shortcuts import render
import csv
import pandas as pd
import numpy as np
# Create your views here.
def index(request):
    return render(request,'index.html')
    

def add(request):
   	
    id = int(request.POST['studentId'])
    name = request.POST['studentName']
    gender ='Male'
    if request.POST.get('male') and request.POST.get('female'):
        gender = None
    elif request.POST.get('male'):
        gender = 'Male'
    elif request.POST.get('female'):
        gender = 'Female'
    else:
        gender=None
    
    if gender == None:
        return render(request,'error.html')
    day = request.POST['day']
    month = request.POST['month']
    year = request.POST['year']
    dateofbirth = str(day)+'-'+str(month)+'-'+str(year)
    
    city = request.POST['city']
    state= request.POST['state']
    email = request.POST['email']
    qualification = request.POST['qualification']
    stream = request.POST['stream']
    
    details =[id,name,gender,dateofbirth,city,state,email,qualification,stream]
    
    data = pd.read_csv('students.csv')
    df = pd.DataFrame(data)
    ids = list(df['StudentId'])
    #Checking Is The Given ID Exists or Not
    if id not in ids:
        with open("students.csv","a") as file:
                writer = csv.writer(file)
                writer.writerow(details)
        return render(request,'success.html')
    else:
   	 return render(request,'error.html')


def addStudent(request):
    
    return render(request,'add-student.html')


def search(request):
    id = int(request.GET['Id'])
    
    #getting data
    data = pd.read_csv('students.csv')
    df = pd.DataFrame(data)
    ids = list(df['StudentId'])
    result = np.array(df[df['StudentId']==id])
    #
    if id in ids:
        info = {
        'StudentId':result[0][0],
        'Name':result[0][1],
        'Gender':result[0][2],
        'bday':result[0][3],
        'city':result[0][4],
        'state':result[0][5],
        'email':result[0][6],
        'qualification':result[0][7],
        'stream':result[0][8]
        }
        return render(request,'result.html',info)
    else:
        return render(request,'error.html')
def searchStudent(request):
    return render(request,'search-student.html')
    

def allStudents(request):
    
    #getting data
    data = pd.read_csv('students.csv')
    df = pd.DataFrame(data)
    result = list(np.array(df))
    info = dict()
    arraydict = dict()
    for i in range(len(result)):
        key= 'std'+str(i)
        for j in range(len(result[i])):
            k = str(j)
            arraydict[k] = result[i][j]
        info[key] = arraydict
        arraydict= dict()
    
    return render(request,'all-students.html',{'data':info})
    
from django.shortcuts import render

from app01.models import Subject


# 视图函数：查看所有学科
def show_subjects(request):
    """查看所有学科"""
    subjects = Subject.objects.all()  # 获取所有学科信息
    for subject in subjects:
        print(subject)  # 打印每个学科的详细信息
    # exit()

    return render(request, 'subject.html', {'subjects': subjects})  # 渲染学科介绍页面


from django.shortcuts import render, redirect


# 视图函数：显示指定学科的老师
def show_teachers(request):
    """显示指定学科的老师"""
    try:
        sno = int(request.GET['sno'])  # 从请求中获取学科编号
        subject = Subject.objects.get(no=sno)  # 根据编号获取学科对象
        teachers = subject.teacher_set.all()  # 获取该学科的所有老师
        return render(request, 'teachers.html', {'subject': subject, 'teachers': teachers})
    except(KeyError, ValueError, Subject.DoesNotExist):
        return redirect('/')  # 如果学科不存在，重定向到首页

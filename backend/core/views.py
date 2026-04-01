import json
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse
from django.db.models import Sum, Count
from .models import MenuItem, TableOrder, DiningTable


def login_view(request):
    if request.user.is_authenticated:
        return redirect('/dashboard/')
    error = ''
    if request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('/dashboard/')
        error = 'Invalid credentials. Try admin / Admin@2024'
    return render(request, 'login.html', {'error': error})


def logout_view(request):
    logout(request)
    return redirect('/login/')


@login_required
def dashboard_view(request):
    ctx = {}
    ctx['menuitem_count'] = MenuItem.objects.count()
    ctx['menuitem_starters'] = MenuItem.objects.filter(category='starters').count()
    ctx['menuitem_main_course'] = MenuItem.objects.filter(category='main_course').count()
    ctx['menuitem_desserts'] = MenuItem.objects.filter(category='desserts').count()
    ctx['menuitem_total_price'] = MenuItem.objects.aggregate(t=Sum('price'))['t'] or 0
    ctx['tableorder_count'] = TableOrder.objects.count()
    ctx['tableorder_open'] = TableOrder.objects.filter(status='open').count()
    ctx['tableorder_preparing'] = TableOrder.objects.filter(status='preparing').count()
    ctx['tableorder_served'] = TableOrder.objects.filter(status='served').count()
    ctx['tableorder_total_subtotal'] = TableOrder.objects.aggregate(t=Sum('subtotal'))['t'] or 0
    ctx['diningtable_count'] = DiningTable.objects.count()
    ctx['diningtable_indoor'] = DiningTable.objects.filter(section='indoor').count()
    ctx['diningtable_outdoor'] = DiningTable.objects.filter(section='outdoor').count()
    ctx['diningtable_private'] = DiningTable.objects.filter(section='private').count()
    ctx['recent'] = MenuItem.objects.all()[:10]
    return render(request, 'dashboard.html', ctx)


@login_required
def menuitem_list(request):
    qs = MenuItem.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(name__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(category=status_filter)
    return render(request, 'menuitem_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def menuitem_create(request):
    if request.method == 'POST':
        obj = MenuItem()
        obj.name = request.POST.get('name', '')
        obj.category = request.POST.get('category', '')
        obj.price = request.POST.get('price') or 0
        obj.cost = request.POST.get('cost') or 0
        obj.status = request.POST.get('status', '')
        obj.veg = request.POST.get('veg') == 'on'
        obj.spice_level = request.POST.get('spice_level', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/menuitems/')
    return render(request, 'menuitem_form.html', {'editing': False})


@login_required
def menuitem_edit(request, pk):
    obj = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        obj.name = request.POST.get('name', '')
        obj.category = request.POST.get('category', '')
        obj.price = request.POST.get('price') or 0
        obj.cost = request.POST.get('cost') or 0
        obj.status = request.POST.get('status', '')
        obj.veg = request.POST.get('veg') == 'on'
        obj.spice_level = request.POST.get('spice_level', '')
        obj.description = request.POST.get('description', '')
        obj.save()
        return redirect('/menuitems/')
    return render(request, 'menuitem_form.html', {'record': obj, 'editing': True})


@login_required
def menuitem_delete(request, pk):
    obj = get_object_or_404(MenuItem, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/menuitems/')


@login_required
def tableorder_list(request):
    qs = TableOrder.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(table_number__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(status=status_filter)
    return render(request, 'tableorder_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def tableorder_create(request):
    if request.method == 'POST':
        obj = TableOrder()
        obj.table_number = request.POST.get('table_number', '')
        obj.server = request.POST.get('server', '')
        obj.items_count = request.POST.get('items_count') or 0
        obj.subtotal = request.POST.get('subtotal') or 0
        obj.tax = request.POST.get('tax') or 0
        obj.total = request.POST.get('total') or 0
        obj.status = request.POST.get('status', '')
        obj.order_time = request.POST.get('order_time') or None
        obj.payment = request.POST.get('payment', '')
        obj.save()
        return redirect('/tableorders/')
    return render(request, 'tableorder_form.html', {'editing': False})


@login_required
def tableorder_edit(request, pk):
    obj = get_object_or_404(TableOrder, pk=pk)
    if request.method == 'POST':
        obj.table_number = request.POST.get('table_number', '')
        obj.server = request.POST.get('server', '')
        obj.items_count = request.POST.get('items_count') or 0
        obj.subtotal = request.POST.get('subtotal') or 0
        obj.tax = request.POST.get('tax') or 0
        obj.total = request.POST.get('total') or 0
        obj.status = request.POST.get('status', '')
        obj.order_time = request.POST.get('order_time') or None
        obj.payment = request.POST.get('payment', '')
        obj.save()
        return redirect('/tableorders/')
    return render(request, 'tableorder_form.html', {'record': obj, 'editing': True})


@login_required
def tableorder_delete(request, pk):
    obj = get_object_or_404(TableOrder, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/tableorders/')


@login_required
def diningtable_list(request):
    qs = DiningTable.objects.all()
    search = request.GET.get('search', '')
    if search:
        qs = qs.filter(table_number__icontains=search)
    status_filter = request.GET.get('status', '')
    if status_filter:
        qs = qs.filter(section=status_filter)
    return render(request, 'diningtable_list.html', {'records': qs, 'search': search, 'status_filter': status_filter})


@login_required
def diningtable_create(request):
    if request.method == 'POST':
        obj = DiningTable()
        obj.table_number = request.POST.get('table_number', '')
        obj.capacity = request.POST.get('capacity') or 0
        obj.section = request.POST.get('section', '')
        obj.status = request.POST.get('status', '')
        obj.reserved_name = request.POST.get('reserved_name', '')
        obj.reserved_time = request.POST.get('reserved_time') or None
        obj.save()
        return redirect('/diningtables/')
    return render(request, 'diningtable_form.html', {'editing': False})


@login_required
def diningtable_edit(request, pk):
    obj = get_object_or_404(DiningTable, pk=pk)
    if request.method == 'POST':
        obj.table_number = request.POST.get('table_number', '')
        obj.capacity = request.POST.get('capacity') or 0
        obj.section = request.POST.get('section', '')
        obj.status = request.POST.get('status', '')
        obj.reserved_name = request.POST.get('reserved_name', '')
        obj.reserved_time = request.POST.get('reserved_time') or None
        obj.save()
        return redirect('/diningtables/')
    return render(request, 'diningtable_form.html', {'record': obj, 'editing': True})


@login_required
def diningtable_delete(request, pk):
    obj = get_object_or_404(DiningTable, pk=pk)
    if request.method == 'POST':
        obj.delete()
    return redirect('/diningtables/')


@login_required
def settings_view(request):
    return render(request, 'settings.html')


@login_required
def api_stats(request):
    data = {}
    data['menuitem_count'] = MenuItem.objects.count()
    data['tableorder_count'] = TableOrder.objects.count()
    data['diningtable_count'] = DiningTable.objects.count()
    return JsonResponse(data)

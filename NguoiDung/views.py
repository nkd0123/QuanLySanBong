from django.shortcuts import render, redirect, get_object_or_404
from .forms import DKForm
from .models import *
from .context_processors import username
from django.http import HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import authenticate ,login,logout
# Create your views here.

################################################ ADMIN ###################################################
def Main(request):
    return render(request,'pages/pages_admin/home.html')


def Login(request):
    if request.method == 'POST':
        usern = request.POST.get('user')
        passw = request.POST.get('password')
        
        if usern and passw:
            try:
                user = TaiKhoanAdmin.objects.get(username=usern)
                if user.password == passw:
                    request.session['user_username'] = user.username
                    data = {'User' : user}
                    return render(request, 'pages/pages_admin/home.html',data)
                else:
                    return render(request, 'pages/pages_admin/login_admin.html', {'error': 'Invalid username or password'})
            except TaiKhoanAdmin.DoesNotExist:
                return render(request, 'pages/pages_admin/login_admin.html', {'error': 'Invalid username or password'})
    return render(request, 'pages/pages_admin/login_admin.html')
            
#------------------------- Khách Hàng -------------------------
def KH(request):
    data = {
        'DS_KhachHang' : KhachHang.objects.all(),
    }
    return render(request,'pages/pages_admin/khachhang_admin.html', data)

def xoaKH(request, username_kh):
    kh = get_object_or_404(KhachHang, username=username_kh)
    kh.delete()
    return redirect('kh')

def searchKH(request):
    query = request.GET.get('searchkh', '')
    if query:
        results = KhachHang.objects.filter(
            Q(hoTen__icontains=query) | Q(hoTen__icontains=query)
        )
    else:
        results = KhachHang.objects.none()
    data = {
        'DS_KhachHang' : results
    }
    return render(request, 'pages/pages_admin/khachhang_admin.html', data)

#------------------------- LỊCH ĐẶT SÂN -------------------------
def Lich(request):
    lich = DatSan.objects.all()
    data = {"DS_Lich" : lich}
    return render(request,'pages/pages_admin/lichdatsan_admin.html',data)


#------------------------- SÂN BÓNG -------------------------
def SB(request):
    data = {
        'DS_SanBong' : SanBong.objects.all()
    }
    return render(request,'pages/pages_admin/sanbong_admin.html', data)

def themSB(request):
    loai = LoaiSan.objects.all()
    data = {
        'DS_Loai' : loai
    }
    if request.method == 'POST':
        ten = request.POST.get('tensan')
        size = request.POST.get('kichthuoc')
        loaisan = request.POST.get('loaisan')
        if ten and size and loaisan:
            loaiSan = LoaiSan.objects.get(tenLoai=loaisan)
            SanBong.objects.create(
                tenSan=ten,
                tinhTrang = "Trống",
                kichThuoc = size,
                maloai = loaiSan
            )
            return redirect('san')
    return render(request, 'pages/pages_admin/themsb_admin.html', data)

def searchSB(request):
    query = request.GET.get('seachsb', '')
    if query:
        results = SanBong.objects.filter(
            Q(tenSan__icontains=query) | Q(tenSan__icontains=query)
        )
    else:
        results = SanBong.objects.none()
    data = {
        'DS_SanBong' : results
    }
    return render(request, 'pages/pages_admin/sanbong_admin.html', data)

def xoaSB(request, id):
    sb = SanBong.objects.get(id=id)
    sb.delete() 
    return redirect('san')

#------------------------ NHAN VIEN ------------------------
def NV(request):
    data = {
        'DS_NhanVien' : NhanVien.objects.all()
    }
    return render(request,'pages/pages_admin/nhanvien_admin.html', data)

def themNV(request):
    if request.method == 'POST':
        hoTen = request.POST.get('hoTen')
        gioiTinh = request.POST.get('gioiTinh')
        SDT = request.POST.get('SDT')
        ngaySinh = request.POST.get('ngaySinh')
        diaChi = request.POST.get('diaChi')

        if hoTen and gioiTinh and SDT and ngaySinh and diaChi:
            NhanVien.objects.create(
                hoTen=hoTen,
                gioiTinh=gioiTinh,
                SDT=SDT,
                ngaySinh=ngaySinh,
                diaChi=diaChi
            )
            return HttpResponseRedirect('nv')
    return render(request,'pages/pages_admin/them_nv_admin.html')

def suaNV(request, id_nv):
    nhanvien = NhanVien.objects.get(id = id_nv)
    if request.method == 'POST':
        hoTen = request.POST.get('hoTen')
        gioiTinh = request.POST.get('gioiTinh')
        SDT = request.POST.get('SDT')
        ngaySinh = request.POST.get('ngaySinh')
        diaChi = request.POST.get('diaChi')

        if hoTen and gioiTinh and SDT and diaChi:
            nhanvien.hoTen=hoTen
            nhanvien.gioiTinh=gioiTinh
            nhanvien.SDT=SDT
            nhanvien.ngaySinh
            nhanvien.diaChi=diaChi
            nhanvien.save()
            
            return redirect('nv')
    formatted_ngaySinh = nhanvien.ngaySinh.strftime('%Y-%m-%d') if nhanvien.ngaySinh else ''
    data = {
        "NhanVien" : nhanvien,
        "NgaySinh" : formatted_ngaySinh
    }
    return render(request,'pages/pages_admin/sua_nv_admin.html', data)

def xoaNV(request, id_nv):
    nv = NhanVien.objects.get(id=id_nv)
    nv.delete() 
    return redirect('nv')

from django.db.models import Q
def seachNV(request):
    query = request.GET.get('namesearch', '')
    if query:
        # Sử dụng Q objects để tìm kiếm gần đúng theo cả họ và tên
        results = NhanVien.objects.filter(
            Q(hoTen__icontains=query) | Q(hoTen__icontains=query)
        )
    else:
        results = NhanVien.objects.none()
    data = {
        'DS_NhanVien' : results
    }
    return render(request, 'pages/pages_admin/nhanvien_admin.html', data)


#----------------------- HOA DON --------------------------
def HD(request):
    hoadon = HoaDon.objects.all()
    data = { 'DS_HoaDon' : hoadon }
    return render(request,'pages/pages_admin/hoadon_admin.html', data)

from datetime import datetime
def themHD(request):
    if request.method == 'POST':
        ngayTao = request.POST.get('ngayTao')
        t_start = request.POST.get('time_start')
        t_end = request.POST.get('time_end')
        tenKH = request.POST.get('tenKH')
        tenNV = request.POST.get('tenNV')
        nvien = NhanVien.objects.get(hoTen=tenNV)
        khang = KhachHang.objects.get(hoTen=tenKH)
        if ngayTao and tenKH and tenNV and t_start and t_end:
            t_start = t_start + ":00"
            t_end = t_end + ":00"
            HoaDon.objects.create(
                tongTien = 0,
                ngayTao=ngayTao,
                t_start = t_start,
                t_end = t_end,
                kh=khang,
                nv=nvien
            )
            return HttpResponseRedirect('hd')
    return render(request,'pages/pages_admin/them_hd_admin.html')

from datetime import datetime,time
def suaHD(request, sohd):
    hoadon = HoaDon.objects.get(soHD=sohd)
    if request.method == 'POST':
        soHD = request.POST.get('soHD')
        ngayTao = request.POST.get('ngayTao')
        tongTien = request.POST.get('tongTien')
        tenKH = request.POST.get('tenKH')
        idNV = int(request.POST.get('id'))
        nvien = NhanVien.objects.get(id=idNV)
        khang = KhachHang.objects.get(hoTen=tenKH)
        if soHD and ngayTao and tongTien and tenKH and idNV:
            hoadon.soHD=soHD
            hoadon.ngayTao=ngayTao
            hoadon.tongTien=tongTien
            hoadon.kh=khang
            hoadon.nv=nvien    
            return redirect('hd')
    formatted_ngayTao = hoadon.ngayTao.strftime('%Y-%m-%d') if hoadon.ngayTao else ''
    data = {
        "HoaDon" : hoadon,
        "NgayTao": formatted_ngayTao
    }
    return render(request,'pages/pages_admin/sua_hd_admin.html', data)

def xoaHD(request, sohd):
    hd = HoaDon.objects.get(soHD=sohd)
    cthd = ChiTietHD.objects.all().filter(soHD = sohd)
    if cthd:
        return redirect('hd')
    else:
        hd.delete()
        return redirect('hd')
    

def CTHD(request, sohd):
    hoadon = HoaDon.objects.get(soHD = sohd)
    chitiethd = ChiTietHD.objects.all().filter(soHD = sohd)
    data = {
        'ChiTietHoaDon' : chitiethd,
        'HoaDon' : hoadon
        }
    return render(request,'pages/pages_admin/chitiet_hoadon_admin.html', data)

def themCTHD(request, sohd):
    dichvu = DichVu.objects.all()
    data = {
        'DichVu' : dichvu
    }
    if request.method == 'POST':
        dichvu = request.POST.get('dichvu')
        soluong = request.POST.get('soluong')
        dv = DichVu.objects.get(tenDV=dichvu)
        hd = HoaDon.objects.get(soHD=sohd)
        if dichvu and soluong:
            ChiTietHD.objects.create(
                soluong = soluong,
                dv = dv,
                soHD=hd
            )
            
            delta_time = datetime.combine(datetime.min, hd.t_end) - datetime.combine(datetime.min, hd.t_start)
            hours_float = delta_time.total_seconds() / 3600
            
            hd.tongTien =  int(soluong) * int(dv.gia) + hours_float*300000
            hd.save()
        return redirect('cthd', sohd=sohd)
    return render(request,'pages/pages_admin/them_cthd_admin.html', data)

def xoaCTHD(request, sohd):
    hoadon = HoaDon.objects.get(soHD = sohd)
    cthd = ChiTietHD.objects.filter(soHD = hoadon.soHD)
    hoadon.tongTien = 0
    hoadon.save()
    if cthd:
        cthd.delete()
    return redirect('cthd', sohd = hoadon.soHD)
#-----------------------------DICH VU-----------------------------
def DV(request):
    data = {
        'DS_dichVu' : DichVu.objects.all()
    }
    return render(request,'pages/pages_admin/dichvu_admin.html', data)

def themDV(request):
    if request.method == 'POST':
        tenDV = request.POST.get('tenDV')
        gia = request.POST.get('gia')
        if tenDV and gia:
            DichVu.objects.create(
                tenDV=tenDV,
                gia=gia
            )
            return HttpResponseRedirect('dv')
    return render(request,'pages/pages_admin/them_dv_admin.html')

def suaDV(request, id_dv):
    dichvu = DichVu.objects.get(id = id_dv)
    if request.method == 'POST':
        tenDV = request.POST.get('tenDV')
        gia = request.POST.get('gia')

        if tenDV and gia:
            dichvu.tenDV=tenDV
            dichvu.gia=gia
            dichvu.save()
            
            return redirect('dv')
        
    data = {
        "DichVu" : dichvu,
    }
    return render(request,'pages/pages_admin/sua_dv_admin.html', data)

def xoaDV(request, id_dv):
    dv = DichVu.objects.get(id=id_dv)
    dv.delete() 
    return redirect('dv')

def searchDV(request):
    query = request.GET.get('search', '')
    if query:
        # Sử dụng Q objects để tìm kiếm gần đúng theo cả họ và tên
        results = DichVu.objects.filter(
            Q(tenDV__icontains=query) | Q(tenDV__icontains=query)
        )
    else:
        results = DichVu.objects.none()
    data = {
        'DS_dichVu' : results
    }
    return render(request, 'pages/pages_admin/dichvu_admin.html', data)

################################################ END ADMIN ###############################################


################################################ USER ###############################################
#home
def home(request):
	return render(request,'pages/pages_user/home_user.html')

def layout_user(request):
	return render(request,'pages/pages_user/layout_user.html')

# DS San
def danhsachsan(request ):
	data = {
		'dm_san' : SanBong.objects.all(),
	}
	return render(request,'pages/pages_user/danhsachsan.html',data)

# Dat San
def datSan(request):
	return render(request,'pages/pages_user/datsan.html')

# Dang Ky
def register(request):
	form = DKForm()
	if request.method == 'POST':
		form = DKForm(request.POST)
		if form.is_valid():
			form.save()
			return render(request,'pages/pages_user/login.html')
	return render (request,'pages/pages_user/register.html',{'form': form})

# Dang Nhap
def loginPage(request):
	if request.method == 'POST':
		username = request.POST.get('username')
		password = request.POST.get('password')
		if username and password:
			try:
				user = KhachHang.objects.get(username = username)
				if user.password == password:
					request.session['user_username'] = user.username
					data = {'User':user}
					return render(request,'pages/pages_user/ChiTietSan.html',data)
				else:
					messages.info(request , 'user or password is not correct!')
			except KhachHang.DoesNotExist:
				messages.info(request , 'user or password is not correct!')
		
	return render(request,'pages/pages_user/login.html')

# Dang Xuat 
def logoutPage(request):
    logout(request)
    return render(request,'pages/pages_user/home_user.html')


# tim kiem
def search(request):
     if request.method == "POST":
        searched = request.POST["searched"]
        keys = SanBong.objects.filter(tenSan__contains = searched )
     return render (request , 'pages/pages_user/Search.html' , {"searched":searched , "keys":keys})

# Danh muc
def list(request):
    data = {
        'DM_Loai' : LoaiSan.objects.all(),
    }
    return render(request , 'pages/pages_user/DSLoai.html',data)

#San theo loai
def DSSPTheoLoai(request , ml):
    dssb = SanBong.objects.all().filter(maloai = ml)
    TL = LoaiSan.objects.get(id = ml ).tenLoai
    data = {
        'dm_san' : dssb ,
        'TL' : TL,
    }
    return render(request , 'pages/pages_user/danhsachsan.html',data)

# chi tiet san
def ChiTietSan (request , ms):
	sp = SanBong.objects.get(id = ms)
	data ={
		 'single_product' : sp, 
	}
	return render (request, 'pages/pages_user/ChiTietSan.html',data)

# dat san
def DatSanBong(request , id_san):
	if request.method == 'POST':
		username = request.POST.get('username')
		thoigianDat = request.POST.get('thoiGianDat')
		

		if thoigianDat and username:
			khang = KhachHang.objects.get(username = username)
			san = SanBong.objects.get(id = id_san)
			DatSan.objects.create(
				thoigianDat = thoigianDat,
				san = san,
				kh = khang
			)
			return HttpResponseRedirect('datsanbong')
		else:
			return render(request,'pages/pages_user/login.html')
	return render (request, 'pages/pages_user/DatSanBong.html')
################################################ END USER ###############################################
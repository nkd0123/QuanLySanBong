from django.db import models
from django.contrib.auth.hashers import make_password, check_password

# Create your models here.
class LoaiSan(models.Model):
    tenLoai = models.CharField(max_length=40)
    
class SanBong(models.Model):
    tenSan = models.CharField(max_length=100) #Sân số 1 - Sân số 2 - Sân số 3
    tinhTrang = models.CharField(max_length=100) #Het san - Con san - Sua chua
    kichThuoc = models.CharField(max_length=6)
    maloai = models.ForeignKey(LoaiSan, on_delete=models.CASCADE)
    
class TaiKhoanAdmin(models.Model):
    username = models.CharField(max_length=25, primary_key=True)
    password = models.CharField(max_length=20)
    
    def save(self, *args, **kwargs):
        self.password = make_password(self.password)
        super(TaiKhoanAdmin, self).save(*args, **kwargs)
        
    def check_pass(self, raw_password):
        return check_password(raw_password, self.password)
    
class NhanVien(models.Model):
    hoTen = models.CharField(max_length=50)
    SDT = models.CharField(max_length=12)
    diaChi = models.CharField(max_length=100)
    gioiTinh = models.CharField(max_length=5)
    ngaySinh = models.DateField()
    
class KhachHang(models.Model):
    username = models.CharField(max_length=25, primary_key=True)
    password = models.CharField(max_length=20)
    hoTen = models.CharField(max_length=50)
    SDT = models.CharField(max_length=12)
    diaChi = models.CharField(max_length=100)
    email = models.EmailField()
    
class DichVu(models.Model):
    tenDV = models.CharField(max_length=100)
    gia = models.CharField(max_length=10)
    
class HoaDon(models.Model):
    soHD = models.AutoField(primary_key=True)
    ngayTao = models.DateField()
    t_start = models.TimeField()
    t_end = models.TimeField()
    tongTien = models.CharField(max_length=10)
    nv = models.ForeignKey(NhanVien, on_delete=models.CASCADE)
    kh = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    
class DatSan(models.Model):
    maLichDat = models.AutoField(primary_key=True)
    thoiGianDat = models.DateTimeField()
    san = models.ForeignKey(SanBong, on_delete=models.CASCADE)
    kh = models.ForeignKey(KhachHang, on_delete=models.CASCADE)
    
class ChiTietHD(models.Model): 
    soluong = models.CharField(max_length=10)
    soHD = models.ForeignKey(HoaDon, on_delete=models.CASCADE)
    dv = models.ForeignKey(DichVu, on_delete=models.CASCADE)
    
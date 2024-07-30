from django.urls import path
from . import views

urlpatterns = [
    #==============================ADMIN=================================
    path('login_admin', views.Login, name='login_admin'),
    path('main',views.Main,name='main'),
    path('admin', views.Login, name='admin'),
    
    #Khách hàng
    path('kh',views.KH,name='kh'),
    path('xoakh/<str:username_kh>/', views.xoaKH, name='xoakh'),
    path('searchkh',views.searchKH,name='searchkh'), #Tìm theo tên
    
    #Lịch đặt sân
    path('lich',views.Lich,name='lich'),
    #path('searchlich',views.searchLich,name='searchlich'),
    
    #Sân bóng
    path('san',views.SB,name='san'),
    path('themsb', views.themSB, name='themsb'),
    path('searchsb', views.searchSB, name='searchsb'), #Tìm theo tên
    path('xoasb<int:id>', views.xoaSB, name='xoasb'),
    
    #Nhân viên
    path('nv',views.NV,name='nv'),
    path('themnv',views.themNV,name='themnv'),
    path('suanv/<int:id_nv>',views.suaNV,name='suanv'),
    path('xoanv/<int:id_nv>', views.xoaNV, name='xoanv'),
    path('seachnv', views.seachNV, name="seachnv"), #Tìm theo tên
    
    #hóa đơn
    path('hd',views.HD,name='hd'),
    path('themhd',views.themHD,name='themhd'),
    path('suahd/<int:sohd>',views.suaHD,name='suahd'),
    path('xoahd/<int:sohd>',views.xoaHD,name='xoahd'),
    path('cthd/<int:sohd>',views.CTHD,name='cthd'),
    path('themcthd/<int:sohd>',views.themCTHD,name='themcthd'),
    path('xoacthd/<int:sohd>',views.xoaCTHD ,name='xoacthd'),
    
    #Dịch vụ
    path('dv',views.DV,name='dv'),
    path('themdv',views.themDV,name='themdv'),
    path('suadv/<int:id_dv>',views.suaDV,name='suadv'),
    path('xoadv/<int:id_dv>', views.xoaDV, name='xoadv'),
    path('searchdv', views.searchDV, name='searchdv'), #Tìm theo tên
    
    #========================USER========================
    path('home',views.home,name='home'),
	path('layout_user', views.layout_user , name='layout_user'),
	path('danhsachsan', views.danhsachsan, name='danhsachsan'),
	path ('DS', views.datSan , name = 'DS'),
    
    # dang ky
    path ('register/',views.register,name='register'),
    
    #dang nhap
    path('login/', views.loginPage,name='login'),
    
    # dang xuat
    path('logout/',views.logoutPage,name='logout'),
    
    # danh sach theo loai
    path('dsloai' , views.list , name='dsloai'),
    path('DSSP/<int:ml>/' , views.DSSPTheoLoai , name = 'DSSPTheoLoai'),
    
    # tim kiem
    path('Search/',views.search,name='Search'),
    
    #chi tiet san
    path('ChiTiet/<int:ms>/' , views.ChiTietSan , name='ChiTietSan'),
    
    #Đặt sân
    path('datsanbong/<int:id_san>/', views.DatSanBong , name='datsanbong'),
]
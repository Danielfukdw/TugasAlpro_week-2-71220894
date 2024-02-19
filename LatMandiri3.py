perjam = float(input("Masukan gaji perjam yang anda dapatkan : "))
jamKerja = float(input('Masukan total jam kerja yang anda lakukan dalam 1 minggu : '))
TotalHasil = perjam * (jamKerja * 5)
pajak = 0.14
totalUangbersih = TotalHasil - (TotalHasil * pajak)
beliBjAkse = (totalUangbersih * 0.1)
sisablbj = totalUangbersih - beliBjAkse
beliAlatTls = sisablbj * 0.01 
sisaAlttls = sisablbj - beliAlatTls
sedekah =  sisaAlttls * 0.25
sisauantsdkh = sisaAlttls - sedekah
yteam = sisauantsdkh // 1000
totaluanguntukytm = (yteam * 1000) * 0.3 
sisautkduafa = sisauantsdkh - totaluanguntukytm
print('Hasil Uang kerja selama liburan : Rp. ', TotalHasil)
print('Uang tersisa setelah pembayan pajak : Rp.', totalUangbersih)
print('Uang dihabiskan untuk baju dan aksesoris : Rp. ', beliBjAkse )
print('Uang dihabiskan untuk membeli alat tulis : Rp.', beliAlatTls)
print('Uang yang akan disedekahkan : Rp.', sedekah)
print('sisa uang setelah sedekah ', sisauantsdkh)
print('Uang untuk anak yatim : Rp. ', totaluanguntukytm)
print('Uang untuk kaum dhuafa : Rp. ', sisautkduafa)
def Menu():
    print('Bạn muốn làm loại nào: ')
    print('*'*50)
    print('0. Thoát chương trình')
    print('1. Siêu nhẹ nhàng')
    print('2. Nhẹ nhàng')
    print('3. Vòng lặp và tương tác với List')
    print('4. Tính toán theo hàm')
    print('5. Xử lí chuỗi - Đọc ghi file')
    print('*'*50)
    print('Chọn từ 1 đến 5')

def Menu_1():
    print('*'*50)
    print('1. Nhập và in tên người dùng')
    print('2. Tính tổng hai số')
    print('3. Tính chu vi hình chữ nhật')
    print('4. Tính diện tích tam giác')
    print('5. Tính 2 mũ 5')
    print('0. Thoát !!!')
    print('*'*50)
    print('Chọn từ 1 đến 5')
def Menu_2():
    print('*'*50)
    print('6. Kiểm tra số chẵn lẻ')
    print('7. Xếp loại học sinh (Giỏi, Khá, Trung bình, Yếu)')
    print('8. Tính phương trình bậc hai')
    print('9. Đổi độ C sang độ F')
    print('10. Kiểm tra V trong kí tự "VanLang" và trả về True False')
    print('0. Thoát !!!')
    print('*'*50)
def Menu_3():
    print('*'*50)
    print('11. In số từ 1 đến N')
    print('12. Tính tổng các số từ 1 đến N')
    print('13. Cho trước 3 số nguyên x, y, z được từ bàn phím. Viết chương trình hiển thị ra màn hình theo yêu cầu sau:')
    print('14. Tạo và thao tác với list: thêm, xóa list có sẵn')
    print('15. Tìm số lớn nhất và nhỏ nhất trong list')
    print('0. Thoát !!!')
    print('*'*50)
def Menu_4():
    print('*'*50)
    print('16. Viết hàm tính giai thừa')
    print('17. Viết hàm kiểm tra số nguyên tố')
    print('18. Viết hàm kiểm tra số chính phương')
    print('19. Viết hàm tính phương trình bậc 3')
    print('20. Viết hàm tính định lý Pytago')
    print('0. Thoát !!!')
    print('*'*50)
def Menu_5():
    print('*'*50)
    print('21. Đếm số lượng từ xuất hiện trong câu')
    print('22. Đảo ngược chuỗi đã cho')
    print('23. Ghi và đọc file văn bản')
    print('24. Ghi và đọc file văn bản nhưng dùng thêm Try - Except')
    print('25. Đọc file và đếm số từ')
    print('0. Thoát !!!')
    print('*'*50)
## Hàm nhập số nguyên
def Nhap_N():
    N = int(input('Nhập vào một số nguyên: '))
    return N

Menu()
while True:
    print('*'*50)
    Chon = int(input('Nhập lựa chọn của bạn: '))
########################## SIÊU NHẸ NHÀNG ##############################
    if Chon == 1:
        Menu_1()
        while True:
            Chon_1 = int(input('Nhập lựa chọn của bạn: '))

            ## 1. Nhập và in tên người dùng###################
            if Chon_1 == 1:
                ten = input("Nhập tên của bạn: ")
                print("Tên của bạn là:", ten)

            ## 2. Tính tổng hai số
            elif Chon_1 == 2:
                tong = 0
                a = float(input('Nhập số a ='))
                b =  float(input('Nhập số b ='))
                tong = a + b
                print(f"tổng là:{tong}")

            ## 3. Tính chu vi hình chữ nhật
            elif Chon_1 == 3:
                chu_vi = (tong)*2
                print('chu vi là:',chu_vi)

            ## 4. Tính diện tích tam giác
            elif Chon_1 == 4:
                def dien_tich_tam_giac(dao_dai, chieu_cao):
                    return 0.5 * dao_dai * chieu_cao
                chieu_cao = float(input("Nhập chiều cao tam giác: "))
                dien_tich = dien_tich_tam_giac(dao_dai, chieu_cao)
                print(f"Diện tích tam giác là: {dien_tich}")

            ## 5. Tính 2 mũ 5
            elif Chon_1 == 5:
                c = 2**5
                print(f"2 mũ 5 = {c}")
            elif Chon_1 == 0:
                print('Bạn đã thoát !!!')
                break
            else: 
                print('Lựa chọn không hợp lệ !!!')

########################## NHẸ NHÀNG ##############################
    elif Chon == 2:
        Menu_2()
        while True:
            Chon_2 = int(input('Nhập lựa chọn của bạn: '))
            print('*'*50)

            ## 6. Kiểm tra số chẵn lẻ
            if Chon_2 == 6:
                def kiem_tra_chan_le(s):
                    if s % 2 == 0:
                        return "Chẵn"
                    else:
                        return "Lẻ"
                so = int(input("Nhập một số nguyên: "))
                ket_qua = kiem_tra_chan_le(so)
                print(f"Số {so} là số {ket_qua}.")

            ## 7. Xếp loại học sinh (Giỏi, Khá, TB, Yếu)
            elif Chon_2 == 7:
                diem_so = float(input('Nhập số điểm của học sinh: '))
                if 10 > diem_so >= 8.0:
                    print('Học sinh giỏi')
                elif 6.5 <= diem_so < 8.0:
                    print('Học sinh khá') 
                elif 5.0 <= diem_so < 6.5:
                    print('Học sinh trung bình')
                elif 3.5 <= diem_so < 5:
                    print('học sinh yếu')
                else:
                    print('Không thể xếp loại')

            ## 8. Tính phương trình bậc hai
            elif Chon_2 == 8:
                def giai_phuong_trinh_bac_2(a, b, c):
                    delta = b**2 - 4*a*c  
                    if delta > 0:
                        x1 = (-b + math.sqrt(delta)) / (2 * a)
                        x2 = (-b - math.sqrt(delta)) / (2 * a)
                        return f"Phương trình có 2 nghiệm phân biệt: x1 = {x1}, x2 = {x2}"
                    
                    elif delta == 0:
                        x = -b / (2 * a)
                        return f"Phương trình có nghiệm kép: x = {x}"
                    else:
                        return "Phương trình vô nghiệm trong tập số thực"
                a = float(input("Nhập hệ số a: "))
                b = float(input("Nhập hệ số b: "))
                c = float(input("Nhập hệ số c: "))
                ket_qua = giai_phuong_trinh_bac_2(a, b, c)
                print(ket_qua)

            ## 9. Đổi độ C sang độ F
            elif Chon_2 == 9:
                def celsius_to_fahrenheit(celsius):
                    fahrenheit = (celsius * 9/5) + 32
                    return fahrenheit
                # Ví dụ: chuyển đổi 25°C
                celsius = int(input('Nhập số độ C: '))
                fahrenheit = celsius_to_fahrenheit(celsius)
                print(f"{celsius}°C = {fahrenheit}°F")

            ## 10. Kiểm tra V trong kí tự "VanLang" và trả về True False
            elif Chon_2 == 10:
                string = "VanLang"
                character = "V"
                # Kiểm tra
                result = character in string
                print(result)
            elif Chon_2 == 0:
                print('Bạn đã thoát !!!')
                break
            else: 
                print('Lựa chọn không hợp lệ !!!')

########################## VÒNG LẶP VÀ TƯƠNG TÁC VỚI LIST ##############################
    elif Chon == 3:
        Menu_3()
        while True:
            Chon_3 = int(input('Nhập lựa chọn của bạn: '))
            print('*'*50)

            ##  11. In số từ 1 đến N
            if Chon_3 == 11:
                a_11 = Nhap_N()
                print(f'Các số từ 1 đến {a_11} là: ')
                for i in range(1, a_11+1):
                    print(i)

            ## 12. Tính tổng các số từ 1 đến N
            elif Chon_3 == 12:
                a_12 = Nhap_N()
                tong = 0
                print(f"Tổng các số từ 1 đến {a_12 } là: ")
                for i in range (1, a_12+1):
                    tong = tong + i 
                print('Tổng từ 1 đến N là: ',tong)

            ## 13. Cho trước các số nguyên x, y, z 
            elif Chon_3 == 13:
                a1 = int(input('Nhập số nguyên thứ nhất: '))
                a2 = int(input('Nhập số nguyên thứ hai: '))
                a3 = int(input('Nhập số nguyên thứ ba: '))
                if a1 % 2 == 0:
                    if a2 >= 20:
                        print(f"{a2} is greater than or equal to 20")
                    else:
                        print(f'{a2} is less than 20')
                else:
                    if a3 >= 30:
                        print(f'{a3} is greater than or equal to 30')
                    else: 
                        print(f'{a3} is less than 30')
            ## 14. Tạo và thao tác với list thêm xóa list có sẵn
            elif Chon_3 == 14:
                None

            ## Tìm số lớn nhất và nhỏ nhất trong List
            elif Chon_3 == 15:
                None

            elif Chon_3 == 0:
                print('Bạn đã thoát !!!')
                break
            else: 
                print('Lựa chọn không hợp lệ !!!')

########################## TÍNH TOÁN THEO HÀM ##############################
    elif Chon == 4:
        Menu_4()
        while True:
            Chon_4 = int(input('Nhập lựa chọn của bạn: '))
            print('*'*50)

            ## 16. Viết hàm tính giai thừa
            if Chon_4 == 16:
                    def Tinh_giai_thua(N):
                        GT = 1
                        for i in range(1, N+1):
                            GT = GT * i
                        return GT
                    a_16 = Nhap_N()
                    print(f'Giai thua cua {a_16} la: ', Tinh_giai_thua(a_16))
            
            ## 17. Viết hàm kiểm tra số nguyên tố
            elif Chon_4 == 17:
                def Kiem_tra_NT(N):
                    if N < 1:
                        return False
                    else:
                        for i in range(2, N):  # Kiểm tra tất cả các số từ 2 đến n-1
                            if N % i == 0:
                                return False
                        return True
                a_17 = int(input('Nhập một số nguyên tố N: '))
                if Kiem_tra_NT(a_17):
                    print('Là số nguyên tố')
                else: 
                    print('Không phải là số nguyên tố')
            
            ## 18. Viết hàm kiểm tra số chính phương
            elif Chon_4 == 18:
                None                            
            
            ## 19. Viết hàm tính phương trình bậc 3
            elif Chon_4 == 19:
                None

            ## 20. Viết hàm tính định lý Pytago
            elif Chon_4 == 20:
                None
            elif Chon_4 == 0:
                print('Bạn đã thoát !!!')
                break
            else: 
                print('Lựa chọn không hợp lệ !!!')

########################## XỬ LÝ CHUỖI - ĐỌC GHI FILE ##############################
    elif Chon == 5:
        Menu_5()
        while True:
            Chon_5 = int(input('Nhập lựa chọn của bạn: '))
            print('*'*50)

            ## 21. Đếm số lượng từ xuất hiện trong mỗi câu
            if Chon_4 == 21:
                None

            ## 22. Đảo ngược chuỗi đã cho
            elif Chon_5 == 22:
                None

            ## 23. Ghi và đọc file văn bản
            elif Chon_5 == 23:
                None
            
            ## 24. Ghi và đọc file văn bản nhưng dùng thêm Try - Except
            elif Chon_5 == 24:
                None
            
            ## 25. Đọc file và thêm số từ
            elif Chon_5 == 25:
                None
            elif Chon_5 == 0:
                print('Bạn đã thoát !!!')
                break
            else: 
                print('Lựa chọn không hợp lệ !!!')
    elif Chon == 0:
        print('Bạn đã thoát chương trình !!!')
        break 
    else: 
        print('Bạn nhập số lựa chọn không hợp lệ !!!')





# Lỗi IndexError: tuple index out of range ở dòng r = p[2]:
# + Với "Levi": Hồ sơ là tuple có 3 phần tử: ("Levi", 120, 2500) => tồn tại phần tử có chỉ số 2 => r = p[2] hợp lệ, lấy ra 2500
# + Với "SofM": Hồ sơ là tuple có 2 phần tử: ("SofM", 150) => không tồn tại phần tử có chỉ số 2 => r = p[2] ném ra lỗi IndexError
# Sau khi sửa lại dữ liệu của "SofM" để chạy tiếp, khi chạy đến "Optimus", chương trình sẽ sập ở dòng tính toán tiền thưởng và ném ra lỗi ValueError
# Khi chèn thêm lệnh print("Đang xử lý:", p) vào đầu vòng lặp, lập trình viên sẽ biết được lỗi để sửa chữa thay vì tìm ở hàng nghìn dòng log
# Cách đặt tên biến ds, p, t, m, r, b vi phạm chuẩn Clean Code => cần đổi thành từ/cụm từ đầy đủ, có ý nghĩa
# Code đúng:

player_records = [
    ("Levi", 120, 2500),
    ("SofM", 150),
    ("Optimus", 100, "N/A")
]


def calculate_bonus(matches, mmr_str):
    mmr = int(mmr_str)
    return (matches * 10) + (mmr * 0.5)


def process_rewards(records):
    print("\n--- BẢNG TÍNH THƯỞNG RP ---")
    for record in records:
        player_name = record[0] if len(record) > 0 else "Không rõ tên"

        try:
            matches = record[1]
            mmr = record[2]
            bonus_rp = calculate_bonus(matches, mmr)
            print(f"Tuyển thủ {player_name} nhận được {bonus_rp} RP")
        except IndexError:
            print(f"Tuyển thủ {player_name}: Lỗi - Hồ sơ bị thiếu thông tin!")
            continue
        except ValueError:
            print(f"Tuyển thủ {player_name}: Lỗi - Dữ liệu MMR không hợp lệ!")
            continue
    print("--- HOÀN TẤT ---")


process_rewards(player_records)

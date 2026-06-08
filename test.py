list = [
    {
        "id" : "CT007",
        "name" : "Nguyen Quang Hai",
        "match" : 10,
        "goals" : 5,
        "ass" : 4,
        "avg" : 33,
        "avg_title" : "Trụ cột đội bóng"
    }
]

def ass_score(list):
        score = ( int(list["match"]) * 1) + ( int(list["goals"]) * 3) + (int(list["ass"]) * 2)
        return score

def rating(list):
        if ass_score(list) >= 50:
            return "Ngôi sao đẳng cấp"
        elif ass_score(list) >= 30:
            return "Trụ cột đội bóng"
        elif ass_score(list) >= 15:
            return "Dự bị chiến lược"
        else:
            return "Cần thanh lý / Cho mượn"

def show_list():
    if not list:
        print("Không có dữ liệu cầu thủ")
    else:
        print("---Danh sách cầu thủ---")
        print("ID | Name | Match | Goals | Ass | Avg | Avg_title")
        for i in list:
            print(f"{i["id"]} | {i["name"]} | {i["match"]} | {i["goals"]} | {i["ass"]} | {ass_score(i)} | {rating(i)}")

def add_player():
    while True:
        player_id = input("Nhập id cầu thủ: ").upper().strip()
        if player_id == "":
            print("Mã cầu thủ không được để trống!")
            continue

        flag = 0
        for p in list:
            if p["id"] == player_id:
                flag = 1
                break 
            if flag == 1:
                print("Mã cầu thủ đã tồn tại!")
                continue
        break

    while True:
        player_name = input("Nhập tên cầu thủ: ").strip()
        if player_name == "":
            print("Tên cầu thủ không được để trống!")
            continue
        break

    while True:
        try:
            player_goals = int(input("Nhập số bàn thắng: "))
            if player_goals < 0:
                print("Số bàn thắng không hợp lệ!")
                continue
        except ValueError:
            print("Dữ liệu không hợp lệ!")
        break

    while True: 
        try:
            player_match = int(input("Nhập số trận đấu: "))
            if player_match < 0:
                print("Số trận đấu không hợp lệ!")
                continue
        except ValueError:
            print("Dữ liệu không hợp lệ!")
        break

    while True: 
        try:
            player_ass = int(input("Nhập số kiến tạo: "))
            if player_ass < 0:
                print("Số kiến tạo không hợp lệ!")
                continue
        except ValueError:
            print("Dữ liệu không hợp lệ!")
        break
    
    list.append(
        {
            "id" : player_id,
            "name" : player_name,
            "match" : player_match,
            "goals" : player_goals,
            "ass" : player_ass
        }
    )

def update_player():
    while True:
        player_id_update = input("Nhập mã cầu thủ: ").upper().strip()
        if player_id_update == "":
            print("Mã cầu thủ không được để trống!")
            continue

        for p in list:
            if p["id"] != player_id_update:
                print("Mã cầu thủ không tồn tại")
                continue
            else:
                while True:
                    player_name_update = input("Nhập tên cầu thủ: ").strip()
                    if player_name_update == "":
                        print("Tên cầu thủ không được để trống!")
                        continue
                    break
                
                while True:
                    try:
                        player_goals_update = int(input("Nhập số bàn thắng: "))
                        if player_goals_update < 0:
                            print("Số bàn thắng không hợp lệ!")
                            continue
                    except ValueError:
                        print("Dữ liệu không hợp lệ!")
                    break

                while True: 
                    try:
                        player_match_update = int(input("Nhập số trận đấu: "))
                        if player_match_update < 0:
                            print("Số trận đấu không hợp lệ!")
                            continue
                    except ValueError:
                        print("Dữ liệu không hợp lệ!")
                    break

                while True: 
                    try:
                        player_ass_update = int(input("Nhập số kiến tạo: "))
                        if player_ass_update < 0:
                            print("Số kiến tạo không hợp lệ!")
                            continue
                    except ValueError:
                        print("Dữ liệu không hợp lệ!")
                    break
            
            p["id"] = player_id_update
            p["name"] = player_name_update
            p["match"] = player_match_update
            p["goals"] = player_goals_update
            p["ass"] = player_ass_update

        print("Cập nhật thành công")

def delete_player():
    while True:
        player_id_delete = input("Nhập mã cầu thủ: ").upper().strip()
        if player_id_delete == "":
            print("Mã cầu thủ không được để trống!")
            continue
        
        for p in list:
            if p["id"] != player_id_delete:
                print("Mã cầu thủ không tồn tại")
            else:
                comfirm = input("Bạn có chắc chắn muốn xóa (Y/N): ").upper().strip()
                if comfirm == "y" or comfirm == "Y":
                    list.remove(p)
                    print("Xóa thành công")
                else:
                    print("Hủy thao tác")
                    break

def find_player():
    while True:
        print("1. Tìm theo id")
        print("2. Tìm theo tên")
        try:
            choose = int(input("Nhập lựa chọn: "))
        except ValueError:
            print("Lựa chọn không hợp lệ")
            continue
        
        match choose:
            case 1:
                player_id_find = input("Nhập mã cầu thủ cần tìm: ").upper().strip()
                for p in list:
                    if p["id"] != player_id_find:
                        print("Không tìm thấy cầu thủ")
                    else:
                        print("ID | Name | Match | Goals | Ass | Avg | Avg_title")
                        for i in list:
                            print(f"{i["id"]} | {i["name"]} | {i["match"]} | {i["goals"]} | {i["ass"]} | {ass_score(i)} | {rating(i)}")

            case 2:
                player_name_find = input("Nhập tên cầu thủ cần tìm: ").strip()
                for p in list:
                    if p["name"] != player_name_find:
                        print("Không tìm thấy cầu thủ")
                    else:
                        print("ID | Name | Match | Goals | Ass | Avg | Avg_title")
                        for i in list:
                            print(f"{i["id"]} | {i["name"]} | {i["match"]} | {i["goals"]} | {i["ass"]} | {ass_score(i)} | {rating(i)}")
        break

def rating_player(list):
    ns = 0
    tc = 0 
    db = 0 
    tl = 0

    for i in list:
        if ass_score(list) >= 50:
            ns += 1
        elif ass_score(list) >= 30:
            tc += 1
        elif ass_score(list) >= 15:
            db += 1
        else:
            tl += 1
    
    print
    (f"Ngôi sao: {ns} | Trụ cột: {tc} | Dự bị: {db} | Cần thanh lý: {tl}")


if __name__ == "__main__":
    while True:
        print("""\n===QUẢN LÝ CẦU THỦ===
1. Hiển thị danh sách cầu thủ
2. Tiếp nhận cầu thủ mới
3. Cập nhật thông tin và chỉ số
4. Xóa cầu thủ
5. Tìm kiếm cầu thủ 
6. Thống kê phân loại phong độ
7. Đánh giá phong độ tự động
8. Thoát chương trình""")

        try:
            choice = int(input("Nhập lựa chọn: "))
        except ValueError:
            print("Lựa chọn không hợp lệ !")
            continue
        
        match choice:
            case 1:
                show_list()

            case 2:
                add_player()

            case 3:
                update_player()

            case 4:
                delete_player()

            case 5:
                find_player()

            case 6: 
                rating_player(list)

            case 8:
                print("Thoát chương trình")
                break

            case _:
                print("Lựa chọn không hợp lệ")
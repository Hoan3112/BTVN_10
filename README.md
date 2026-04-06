# BTVN_10 

## ĐOÀN QUANG HOÀN - 23020812 - UET

## Báo cáo ngắn gọn: 2 thuật toán

### 1. Thuật toán Banker (Tránh deadlock)
- Mục tiêu: cấp phát tài nguyên sao cho hệ thống luôn ở trạng thái an toàn.
- Ý tưởng chính:
1. Tính `Need = Max - Allocation`.
2. Tìm tiến trình có `Need <= Available`.
3. Cho tiến trình đó chạy xong, trả lại tài nguyên vào `Available`.
4. Lặp lại đến khi tất cả tiến trình hoàn thành (an toàn) hoặc không tìm được tiến trình phù hợp (không an toàn).

**Test case 1 (an toàn)**
- `Available = [3, 3, 2]`
- `Allocation`  
  `P0: [0,1,0]`  
  `P1: [2,0,0]`  
  `P2: [3,0,2]`  
  `P3: [2,1,1]`  
  `P4: [0,0,2]`
- `Max`  
  `P0: [7,5,3]`  
  `P1: [3,2,2]`  
  `P2: [9,0,2]`  
  `P3: [2,2,2]`  
  `P4: [4,3,3]`
- Kết quả mong đợi: hệ thống **an toàn**, một chuỗi an toàn ví dụ:  
  `P1 -> P3 -> P4 -> P0 -> P2`

**Test case 2 (không an toàn)**
- `Available = [0, 0, 0]`
- `Allocation`  
  `P0: [0,1,0]`  
  `P1: [2,0,0]`  
  `P2: [3,0,3]`  
  `P3: [2,1,1]`  
  `P4: [0,0,2]`
- `Max`  
  `P0: [7,5,3]`  
  `P1: [3,2,2]`  
  `P2: [9,0,4]`  
  `P3: [2,2,2]`  
  `P4: [4,3,3]`
- Kết quả mong đợi: hệ thống **không an toàn**, không tìm được chuỗi an toàn đầy đủ.

### 2. Thuật toán phát hiện deadlock
- Mục tiêu: kiểm tra hệ thống hiện tại có rơi vào deadlock hay không.
- Ý tưởng chính (theo ma trận cấp phát):
1. Đánh dấu tiến trình đã hoàn thành nếu `Allocation = 0`.
2. Tìm tiến trình chưa hoàn thành có `Request <= Available`.
3. Giả sử tiến trình đó chạy xong, cộng `Allocation` của nó vào `Available`.
4. Lặp đến khi không còn tiến trình nào thỏa điều kiện.
5. Tiến trình chưa được đánh dấu hoàn thành là tiến trình bị deadlock.

**Test case 3 (có deadlock)**
- `Available = [0, 0, 0]`
- `Allocation`  
  `P0: [1,0,0]`  
  `P1: [0,1,0]`  
  `P2: [0,0,1]`
- `Request`  
  `P0: [0,1,0]`  
  `P1: [0,0,1]`  
  `P2: [1,0,0]`
- Kết quả mong đợi: **deadlock xảy ra**, tập tiến trình bị kẹt:  
  `{P0, P1, P2}`

**Test case 4 (không deadlock)**
- `Available = [1, 1, 0]`
- `Allocation`  
  `P0: [0,1,0]`  
  `P1: [1,0,0]`  
  `P2: [1,1,1]`
- `Request`  
  `P0: [0,0,0]`  
  `P1: [0,1,0]`  
  `P2: [1,0,0]`
- Kết quả mong đợi: **không có deadlock**, vì tồn tại thứ tự hoàn thành ví dụ:  
  `P0 -> P1 -> P2`

## Kết luận
- Banker dùng để **phòng tránh** deadlock trước khi cấp phát.
- Deadlock detection dùng để **phát hiện** deadlock sau khi hệ thống đã cấp phát.

## Câu lệnh chạy 2 file

Chạy trong thư mục dự án `E:\BTVN_10`:

```powershell
python banker.py
python deadlock.py
```

Nếu máy dùng `py` thay cho `python`:

```powershell
py banker.py
py deadlock.py
```

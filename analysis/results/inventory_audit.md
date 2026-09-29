# Inventory audit — kết quả tự động

Nguồn: `data/navigation_inventory.csv` (chép tay từ ảnh chụp sidebar, không phải dữ liệu người dùng).

## Cấu trúc

- Số mục cấp 1 (L1): **14** (trong đó 13 nhóm có mục con)
- Số mục cấp 2 (L2): **144**
- Tổng destination: **145**
- Độ sâu tối đa: **2**
- Mục con / nhóm: min 6, median 9, max 22 (Báo cáo & Hiệu suất)

| L1 | Số mục con | CONFIG | DUP | MISPLACED | MIX | NEAR | PERSONAL | SAME_AS_PARENT |
|---|---:|---:|---:|---:|---:|---:|---:|---:|
| CRM Core | 13 | 2 | 3 | 0 | 1 | 3 | 1 | 0 |
| Phễu bán hàng | 16 | 1 | 3 | 0 | 2 | 6 | 2 | 0 |
| Sản phẩm & Đơn hàng | 8 | 0 | 0 | 0 | 1 | 2 | 0 | 0 |
| Thanh toán & Hợp đồng | 9 | 2 | 0 | 0 | 0 | 2 | 0 | 0 |
| Email Marketing | 11 | 2 | 0 | 0 | 3 | 6 | 0 | 1 |
| Landing & Phễu | 9 | 0 | 0 | 3 | 0 | 3 | 0 | 0 |
| Truyền thông | 6 | 3 | 0 | 0 | 1 | 0 | 0 | 0 |
| Báo cáo & Hiệu suất | 22 | 0 | 2 | 8 | 5 | 4 | 0 | 0 |
| Affiliate | 6 | 1 | 1 | 0 | 1 | 2 | 0 | 0 |
| AI & Tự động hoá | 10 | 2 | 1 | 0 | 2 | 2 | 0 | 0 |
| Kết nối & Dữ liệu | 19 | 0 | 0 | 2 | 3 | 14 | 0 | 0 |
| Nội bộ công ty | 7 | 0 | 0 | 0 | 1 | 2 | 0 | 0 |
| Cài đặt & Bảo mật | 8 | 0 | 0 | 1 | 1 | 3 | 1 | 0 |

## Nhãn trùng tên y hệt

| Label | Xuất hiện ở |
|---|---|
| Bảng kanban | CRM Core, Phễu bán hàng |
| Cảnh báo | CRM Core, AI & Tự động hoá |
| Danh sách | CRM Core, Phễu bán hàng |
| Mô phỏng what-if | Phễu bán hàng, Báo cáo & Hiệu suất |
| Tổng quan | Tổng quan, Báo cáo & Hiệu suất |

## Tần suất audit flag

| Flag | Ý nghĩa | Số mục |
|---|---|---:|
| NEAR | Gần nghĩa / chồng nghĩa với mục khác (semantic overlap) | 49 |
| MIX | Label tiếng Anh hoặc trộn Anh–Việt | 21 |
| MISPLACED | Nội dung có vẻ không khớp với nhóm cha | 14 |
| CONFIG | Mục cấu hình nằm trong module nghiệp vụ | 13 |
| DUP | Trùng tên y hệt với một mục khác | 11 |
| PERSONAL | Mục cá nhân ('của tôi', hồ sơ) | 4 |
| SAME_AS_PARENT | Trùng tên với chính nhóm cha | 1 |

## Ngôn ngữ label

| Ngôn ngữ | Số mục |
|---|---:|
| vi | 102 |
| en | 28 |
| mixed | 15 |

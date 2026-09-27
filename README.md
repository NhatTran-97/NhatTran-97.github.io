# NhatTran-97.github.io

Website portfolio cá nhân chạy trên **GitHub Pages + Jekyll**.
👉 https://nhattran-97.github.io

> **Nguyên tắc:** mọi nội dung nằm trong các file dữ liệu (`_data/*.yml`) và bài viết (`_posts/*.md`).
> Bạn **không cần sửa HTML/CSS**. Sửa file → commit → 1–2 phút sau web tự cập nhật.

---

## 1. Sửa nội dung ở đâu?

| Muốn thay đổi | Mở file |
|---|---|
| Tên, ảnh đại diện, banner trang chủ, 4 ô giới thiệu, liên hệ, giới thiệu bản thân, sở thích | `_data/profile.yml` |
| CV: học vấn, kinh nghiệm, kỹ năng, giải thưởng, hoạt động | `_data/cv.yml` |
| Danh sách project | `_data/projects.yml` |
| Danh sách bài báo | `_data/publications.yml` |
| Bài viết chia sẻ kiến thức | thư mục `_posts/` |
| Menu trên cùng | `_data/navigation.yml` |
| Tiêu đề web trên Google / tab trình duyệt | `_config.yml` |

Mỗi file `.yml` đều có ghi chú (dòng bắt đầu bằng `#`) giải thích từng trường.

### Ảnh và file
| Loại | Đặt vào | Ghi chú |
|---|---|---|
| Ảnh đại diện | `assets/img/` | Ảnh dọc 4:5, rồi sửa `avatar:` trong `profile.yml` |
| Ảnh banner | `assets/img/` | Ảnh ngang ≥ 1600px, sửa `hero.background` |
| Ảnh project | `assets/img/projects/` | Tỉ lệ 16:9, sửa `image:` của project |
| Ảnh bìa bài viết | `assets/img/notes/` | Tỉ lệ 16:9, khai báo `image:` trong bài |
| CV PDF | `assets/files/cv.pdf` | Nút "Download CV/PDF" trỏ tới file này |

---

## 2. Viết bài mới (Notes)

1. Copy file mẫu `_templates/new-note.md` vào thư mục `_posts/`.
2. Đổi tên theo dạng **`YYYY-MM-DD-ten-bai-khong-dau.md`**, ví dụ `2026-10-01-pid-controller.md`.
3. Sửa phần đầu file (giữa hai dòng `---`): `title`, `category`, `tags`, `description`.
4. Viết nội dung bằng Markdown bên dưới. Commit là xong.

Bài mới sẽ tự hiện ở trang **Notes**, trên **Home**, có trong ô **tìm kiếm**, và `category` mới sẽ tự thành một mục lọc.

- Công thức toán: thêm `math: true`, viết `$...$` (trong dòng) hoặc `$$...$$` (riêng dòng).
- Code: dùng ```` ```python ```` … ```` ``` ```` — tự tô màu.
- Chèn ảnh: `![mô tả](/assets/img/notes/ten-anh.png)`

## 3. Thêm project / bài báo

Copy một khối có sẵn trong `_data/projects.yml` hoặc `_data/publications.yml` (từ dấu `-` đến trước dấu `-` tiếp theo), dán xuống và sửa nội dung.

- Project: `category` mới → tự thêm nút lọc; `featured: true` → hiện trên Home.
- Bài báo: tự sắp xếp theo `year`; `type` mới (vd. `Thesis`) → tự thêm mục lọc; tên bạn khai báo trong `profile.yml → publication_names` sẽ tự in đậm.

## 4. Lưu ý khi sửa file `.yml`

- Thụt lề bằng **dấu cách** (không dùng Tab), giữ đúng số dấu cách như dòng mẫu.
- Nếu nội dung có dấu `:` hoặc bắt đầu bằng `*`, `#`, `"` thì đặt trong ngoặc kép: `title: "Thesis: SLAM"`.
- Nếu web không cập nhật sau vài phút → vào tab **Actions** trên GitHub xem lỗi (thường là sai thụt lề).

## 5. Tính năng có sẵn
- Giao diện sáng / tối (nút ☀/🌙), tự nhớ lựa chọn.
- Tìm kiếm toàn trang (nút 🔍 hoặc phím `/`).
- Lọc project theo nhóm, bài báo theo loại, bài viết theo chủ đề + ô tìm kiếm.
- Hiển thị tốt trên điện thoại.

## 6. Đổi màu chủ đạo (tuỳ chọn)
Mở `assets/css/style.css`, sửa giá trị `--primary` ở đầu file (ví dụ `#0f766e` cho màu xanh ngọc).

## 7. Chạy thử trên máy (tuỳ chọn)
```bash
bundle install
bundle exec jekyll serve
# mở http://localhost:4000
```

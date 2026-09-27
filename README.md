# NhatTran-97.github.io

Website portfolio cá nhân (phong cách formal, tối giản) chạy trên **GitHub Pages + Jekyll**.
Không cần build thủ công — push lên nhánh `main` là GitHub tự build và deploy.

## Cấu trúc trang

| Trang | URL | Nội dung lấy từ |
|---|---|---|
| About (trang chủ) | `/` | `index.html` + `_data/news.yml` |
| CV | `/cv/` | `_data/cv.yml` (+ file `assets/files/cv.pdf`) |
| Projects | `/projects/` | `_data/projects.yml` |
| Publications | `/publications/` | `_data/publications.yml` |
| Notes (chia sẻ kiến thức) | `/notes/` | các file Markdown trong `_posts/` |

## Cách chỉnh sửa

1. **Thông tin cá nhân** (tên, email, GitHub, LinkedIn, Google Scholar…): sửa `_config.yml` → mục `author`.
2. **Ảnh đại diện**: thay `assets/img/avatar.svg` bằng ảnh của bạn (vd. `avatar.jpg`) rồi sửa đường dẫn `author.avatar`.
3. **Giới thiệu bản thân**: sửa đoạn văn trong `index.html`.
4. **CV / Projects / Publications**: chỉ cần sửa các file `.yml` trong `_data/` — không phải đụng tới HTML.
5. **CV PDF**: đặt file vào `assets/files/cv.pdf`.

## Viết một note mới

Tạo file `_posts/YYYY-MM-DD-ten-bai-viet.md`:

```markdown
---
title: "Tiêu đề bài viết"
tags: [Robotics, Python]
math: true        # bật nếu cần viết công thức LaTeX ($...$ và $$...$$)
---

Đoạn mở đầu ngắn (hiển thị ở danh sách). <!--more-->

## Nội dung chính
...
```

Trang Notes tự liệt kê bài mới nhất, có bộ lọc theo tag; code được highlight, bảng và công thức toán hiển thị đẹp.

## Deploy lên GitHub Pages

1. Merge code vào nhánh `main`.
2. Vào **Settings → Pages** → *Source*: **Deploy from a branch** → chọn `main` / `(root)`.
3. Sau 1–2 phút, trang có tại `https://nhattran-97.github.io`.

## Chạy thử trên máy (tuỳ chọn)

```bash
bundle install
bundle exec jekyll serve
# mở http://localhost:4000
```

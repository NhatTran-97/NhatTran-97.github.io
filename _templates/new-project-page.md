---
# ================================================================
#  MẪU TRANG CHI TIẾT PROJECT
#  1. Copy file này vào thư mục _projects/, đặt tên không dấu, vd. _projects/agv-docking.md
#     → trang sẽ có địa chỉ /projects/agv-docking/
#  2. Trong _data/projects.yml, thêm vào project tương ứng:  detail: /projects/agv-docking/
#     → thẻ project có nút "Details", bấm ảnh/tiêu đề cũng mở trang này
#  3. Ảnh để trong assets/img/projects/<tên-project>/ (nén < 300 KB mỗi ảnh)
# ================================================================
title: Tên project
summary: Một câu mô tả project làm gì, cho ai.
category: Autonomy                 # nhãn xanh
role: Technical Lead               # vai trò của bạn
period: Jan 2026 – Jun 2026
partners: EIU FabLab               # đơn vị hợp tác (tuỳ chọn)
status: Completed                  # Completed / In progress ...
image: /assets/img/projects/ten-project/cover.jpg
image_caption: Chú thích ảnh bìa
tags: [ROS 2, Nav2, C++]
links:                             # nút đầu tiên màu xanh đậm
  - name: GitHub repository
    url: https://github.com/...
    icon: github
  - name: Demo video
    url: https://www.youtube.com/...
    icon: youtube
---

## Overview

Bài toán, mục tiêu, kết quả chính (2–3 đoạn).

## My role

Bạn phụ trách gì, làm những phần nào.

## System architecture

<!-- Sơ đồ 2 cột có sẵn: sửa chữ trong các ô -->
<div class="arch">
  <div class="arch-col">
    <strong>Bên trái</strong>
    <div class="arch-box">Thành phần A<small>mô tả ngắn</small></div>
    <div class="arch-box">Thành phần B<small>mô tả ngắn</small></div>
  </div>
  <div class="arch-link"><span>⇄</span>Giao thức</div>
  <div class="arch-col">
    <strong>Bên phải</strong>
    <div class="arch-box">Thành phần C<small>mô tả ngắn</small></div>
  </div>
</div>

## Key features

<!-- Lưới ô tính năng: thêm/bớt các khối <div> -->
<div class="feature-grid">
  <div><strong>Tính năng 1</strong><p>Mô tả ngắn.</p></div>
  <div><strong>Tính năng 2</strong><p>Mô tả ngắn.</p></div>
  <div><strong>Tính năng 3</strong><p>Mô tả ngắn.</p></div>
</div>

## Results

<!-- Một ảnh có chú thích -->
<figure>
  <img src="/assets/img/projects/ten-project/result.jpg" alt="Mô tả ảnh">
  <figcaption>Chú thích ảnh.</figcaption>
</figure>

<!-- Nhiều ảnh dạng lưới -->
<div class="gallery">
  <figure><img src="/assets/img/projects/ten-project/1.jpg" alt=""><figcaption>Ảnh 1</figcaption></figure>
  <figure><img src="/assets/img/projects/ten-project/2.jpg" alt=""><figcaption>Ảnh 2</figcaption></figure>
</div>

| Bảng | Cột 1 | Cột 2 |
|---|---|---|
| Hàng 1 | ... | ... |

## Demo videos

- [Tên video](https://www.youtube.com/...)

## Lessons learned / Next steps

- ...

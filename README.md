# NhatTran-97.github.io

Website portfolio cá nhân chạy trên **GitHub Pages + Jekyll** → **https://nhattran-97.github.io**

> **Nguyên tắc:** mọi nội dung nằm trong **file dữ liệu** (`_data/*.yml`), **bài viết** (`_posts/`) và **trang chi tiết project** (`_projects/`).
> **Không cần sửa HTML/CSS/JS.** Sửa file → Commit → 1–2 phút sau website tự cập nhật (CV PDF tự tạo lại sau ~2–3 phút).

## Mục lục
1. [Cách sửa file trên GitHub](#1-cách-sửa-file-trên-github)
2. [Bản đồ: muốn sửa gì thì mở file nào](#2-bản-đồ-muốn-sửa-gì-thì-mở-file-nào)
3. [Công thức làm nhanh — các việc hay làm](#3-công-thức-làm-nhanh--các-việc-hay-làm)
4. [Thông tin cá nhân, Home, About — `profile.yml`](#4-thông-tin-cá-nhân-home-about--profileyml)
5. [CV và CV PDF — `cv.yml`](#5-cv-và-cv-pdf--cvyml)
6. [Projects — `projects.yml` + trang chi tiết `_projects/`](#6-projects--projectsyml--trang-chi-tiết-_projects)
7. [Publications — `publications.yml`](#7-publications--publicationsyml)
8. [Notes — viết bài chia sẻ kiến thức](#8-notes--viết-bài-chia-sẻ-kiến-thức)
9. [Ảnh và file](#9-ảnh-và-file)
10. [Giao diện: menu, màu, căn chữ, ảnh banner, độ rộng](#10-giao-diện-menu-màu-căn-chữ-ảnh-banner-độ-rộng)
11. [Nguyên tắc nội dung (cách viết cho nhất quán)](#11-nguyên-tắc-nội-dung-cách-viết-cho-nhất-quán)
12. [Quy tắc viết YAML (tránh lỗi)](#12-quy-tắc-viết-yaml-tránh-lỗi)
13. [Xử lý sự cố & kiểm tra tự động](#13-xử-lý-sự-cố--kiểm-tra-tự-động)
14. [Cấu trúc thư mục](#14-cấu-trúc-thư-mục)
15. [Chạy thử trên máy (tuỳ chọn)](#15-chạy-thử-trên-máy-tuỳ-chọn)

---

## 1. Cách sửa file trên GitHub

Làm ngay trên trình duyệt, không cần cài gì:

1. Vào `https://github.com/NhatTran-97/NhatTran-97.github.io`.
2. Mở file cần sửa (ví dụ `_data` → `profile.yml`) → bấm **✏️ Edit this file**.
3. Sửa → **Commit changes…** → ghi ngắn gọn đã sửa gì → **Commit changes**.
4. Đợi 1–2 phút → mở website, bấm **Ctrl + Shift + R** (hoặc mở tab ẩn danh) để xem bản mới.

| Việc | Cách làm |
|---|---|
| Tạo file mới | Vào thư mục → **Add file → Create new file** |
| Upload ảnh / PDF | Vào thư mục → **Add file → Upload files** → kéo thả → **Commit changes** |
| Thay ảnh cũ | Nên upload ảnh với **tên file mới** (vd. `cover-2.jpg`) rồi sửa đường dẫn trong file `.md` / `.yml` — trình duyệt và GitHub giữ ảnh cũ theo tên file nên upload đè **trùng tên** có thể vẫn hiện ảnh cũ một thời gian. Xoá file ảnh cũ sau khi đổi. |
| Xoá file | Mở file → menu **…** → **Delete file** |
| Theo dõi cập nhật | Tab **Actions**: *pages build and deployment* (website), *Build CV PDF* (CV), *Check site* (kiểm tra lỗi). ✅ xanh = xong, ❌ đỏ = lỗi → [mục 13](#13-xử-lý-sự-cố--kiểm-tra-tự-động) |

---

## 2. Bản đồ: muốn sửa gì thì mở file nào

| Muốn thay đổi | File |
|---|---|
| Tên, chức danh, ảnh đại diện | `_data/profile.yml` |
| Banner trang Home (lời chào, giới thiệu, nút, câu châm ngôn, ảnh nền) | `_data/profile.yml` → `hero` |
| 4 ô giới thiệu dưới banner | `_data/profile.yml` → `highlights` |
| Email, LinkedIn, GitHub, YouTube… (About, Home, footer, CV PDF) | `_data/profile.yml` → `contacts` |
| Giới thiệu, sở thích (trang About) | `_data/profile.yml` → `about` |
| Số project / bài báo / bài viết hiện trên Home | `_data/profile.yml` → `home` |
| CV: học vấn, kinh nghiệm, kỹ năng, thành tích, hoạt động | `_data/cv.yml` |
| Cách tạo CV PDF (tự động / tự upload, số trang, căn chữ) | `_data/cv.yml` → `pdf_*` |
| Thẻ project (danh sách, nhóm, ảnh, link) | `_data/projects.yml` |
| Trang chi tiết của từng project | `_projects/<tên>.md` |
| Bài báo khoa học | `_data/publications.yml` |
| Bài viết chia sẻ kiến thức | thư mục `_posts/` |
| Workshop / khoá học (thẻ bấm mở) | `_projects/weekly-robotics-workshop-series.md` ([mục 6.4](#64-trang-workshop--khoá-học-dạng-thẻ-bấm-mở)) |
| Menu trên cùng | `_data/navigation.yml` |
| Tiêu đề web trên Google, căn chữ toàn web | `_config.yml` |
| Màu chủ đạo, độ rộng trang | `_sass/base/_tokens.scss` ([mục 10.5–10.6](#105-màu-chủ-đạo)) |

---

## 3. Công thức làm nhanh — các việc hay làm

### ➕ Thêm một project mới
1. Mở `_data/projects.yml`, copy một khối project có sẵn (từ `  - title:` tới trước `  - title:` tiếp theo), dán vào vị trí mong muốn (trên cùng = hiện trước).
2. Sửa `title`, `group`, `org`, `category`, `period`, `tags`, `description`, các link.
3. Ảnh: upload vào `assets/img/projects/` (16:9, < 300 KB) → sửa `image:`.
4. Muốn hiện trên Home → `featured: true`.
5. Muốn có trang chi tiết → xem công thức tiếp theo.

### 📄 Viết trang chi tiết cho một project
1. **Project đã có khung sẵn** (mọi project Professional): mở file tương ứng trong `_projects/`, ví dụ `_projects/auto-race-2025-student-teams.md`.
   **Project mới:** copy `_templates/new-project-page.md` vào `_projects/ten-project.md`, rồi thêm `detail: /projects/ten-project/` vào project đó trong `projects.yml`.
2. Điền phần đầu: `role`, `status`, `period`, `partners`, ảnh bìa, `links` (ô nào để `""` sẽ tự ẩn).
3. Thay các dòng *Details coming soon* bằng nội dung thật: Overview → My role → kiến trúc / tính năng → kết quả → video.
4. Ảnh riêng của project để trong `assets/img/projects/<tên-project>/`.
5. Mẫu hoàn chỉnh để làm theo: **`_projects/vda5050-open-rmf.md`**.

### 🎓 Thêm một workshop mới (trang Weekly Robotics Workshop Series)
1. Upload ảnh bìa vào `assets/img/projects/workshops/` (ảnh PNG nền trong suốt hoặc ảnh chụp, < 300 KB).
2. Mở `_projects/weekly-robotics-workshop-series.md`, copy nguyên một khối `<section class="workshop-panel" …>` … `</section>`, dán vào trước `### More workshops`.
3. Sửa `id`, tiêu đề `### Workshop 3 — Tên`, ảnh bìa, mục tiêu, chip, link playlist, các bước học. Thẻ nhỏ **tự xuất hiện** — chi tiết ở [mục 6.4](#64-trang-workshop--khoá-học-dạng-thẻ-bấm-mở).

### 📝 Thêm bài báo
1. Mở `_data/publications.yml`, copy một khối có sẵn, sửa `title`, `authors` (đúng thứ tự trong bài), `venue`, `year`.
2. Đang phản biện: `type: Under Review`, `note: Under Review`, `venue: Under review at <Tên hội nghị> 2026`.
3. Khi được nhận: đổi `type: Conference` (hoặc `Journal`), `venue` = tên hội nghị, `note` = giải/Oral nếu có, thêm `pdf` / `doi`.
4. Nếu bạn hướng dẫn sinh viên: thêm dòng tương ứng vào `cv.yml` → Activities → *Student Research Mentor*.

### 🏆 Thêm giải thưởng / cuộc thi
- **Đang thi / chưa có kết quả:** chỉ ghi ở `cv.yml` → Activities và thẻ project, kèm chữ *ongoing* / *In progress*. **Chưa** đưa vào Achievements.
- **Có kết quả:** thêm vào `cv.yml` → Achievements (tên giải — tên cuộc thi, vai trò của bạn, năm, link bài báo/tin tức), cập nhật thẻ project (ảnh thật, mô tả, `featured: true`, nút `News`).
- Nếu là giải dành cho sinh viên bạn hướng dẫn: ghi rõ vai trò (*As mentor of …*) và phạm vi giải (vd. **Best Paper Award (Student Session)**).

### ✍️ Viết bài Notes
1. Copy `_templates/new-note.md` vào `_posts/`, đặt tên `YYYY-MM-DD-ten-bai.md` (vd. `2026-10-01-pid-controller.md`).
2. Sửa phần đầu (`title`, `category`, `tags`, `description`) → viết nội dung Markdown → Commit.

### 🖼 Đổi ảnh đại diện / ảnh banner
- Ảnh đại diện: upload đè `assets/img/avatar.jpg` (ảnh dọc 4:5, ~600px).
- Ảnh banner: chọn 1 trong 4 ảnh có sẵn hoặc upload ảnh mới → sửa `hero.background` ([mục 10.4](#104-ảnh-nền-banner)).

### 📥 Cập nhật CV PDF
- Không cần làm gì: sửa `cv.yml` / `profile.yml` / `publications.yml` → GitHub tự tạo lại `cv.pdf` ([mục 5.2](#52-cv-pdf--nút-download-pdf)).

---

## 4. Thông tin cá nhân, Home, About — `profile.yml`

### 4.1. Thông tin cơ bản
```yaml
name: Nhat Tran                  # tên đầy đủ (banner, About, footer, CV PDF)
short_name: N. Tran              # tên ngắn ở góc trái menu
role: FabLab Technician, Eastern International University   # chức danh thật (About, CV PDF)
avatar: /assets/img/avatar.jpg   # ảnh dọc tỉ lệ 4:5

publication_names:               # tên bạn trong danh sách tác giả → tự in đậm (tên dài trước)
  - Duy Nhất Trần
  - Duy Nhat Tran
  - Nhat Tran
```

### 4.2. Banner trang Home — `hero`
```yaml
hero:
  greeting: Hello, I'm
  tagline: Robotics enthusiast — learning by building.   # 1 câu định vị bản thân
  intro: >-                                              # 2–3 câu: làm gì, mảng nào
    I work on robots and drones — localization, sensor fusion and Visual SLAM, the ROS 2
    navigation stack (custom planners, controllers and ros2_control), and embedded ...
  background: /assets/img/hero/hero-photo-mountain.jpg   # xem mục 10.4
  quote: "Passion builds robots; persistence makes them work."   # "" để ẩn; mỗi vế tách bằng "; " nằm trên 1 dòng
  buttons:
    - text: View My CV
      url: /cv/
      icon_after: arrow-right
      style: primary             # primary = nút xanh đặc
    - text: See My Projects
      url: /projects/
      icon: github
      style: ghost               # ghost = nút viền trong suốt
```
> `>-` = gộp các dòng thành 1 đoạn. `|` = giữ nguyên xuống dòng (dùng khi có nhiều đoạn).

- **Câu châm ngôn (`quote`)** hiện ở góc phải banner (ẩn trên điện thoại). Website tách câu tại dấu `; ` và giữ **mỗi vế trên đúng 1 dòng** → viết mỗi vế ngắn (≤ ~30 ký tự), tối đa 2–3 vế.
- **Ảnh nền** tự co giãn theo màn hình; banner cao thêm một chút trên màn rộng.

### 4.3. Bốn ô dưới banner — `highlights`
```yaml
highlights:
  - icon: localization                                          # icon nét (danh sách ở mục 4.7)
    title: Localization & SLAM                                   # ≤ 28 ký tự, 1 dòng
    text: Sensor fusion and Visual SLAM for robots and drones.  # 45–60 ký tự → đúng 2 dòng
```
- Icon đang dùng: `localization`, `route`, `chip-code`, `presentation` — cùng kiểu nét với mọi icon khác trên web.
- Tuỳ chọn `image: /assets/img/highlights/<file>.svg` để thay icon bằng hình minh hoạ (vuông, nền trong suốt).
  Trong thư mục đó có sẵn 4 hình minh hoạ màu (`localization.svg`, `navigation.svg`, `embedded.svg`, `teaching.svg`),
  hiện **không dùng** vì kiểu icon nét trông formal và đồng bộ hơn.
- Luôn hiển thị **đúng 2 dòng** (kể cả trên màn hình rộng) và các ô cao bằng nhau; viết quá dài sẽ bị cắt bằng "…".
- Có thể để 2, 3 hoặc 4 ô.

### 4.4. Liên hệ — `contacts`
```yaml
contacts:
  - icon: youtube
    label: YouTube                                # tiêu đề nhỏ (trang About)
    value: youtube.com/@NhatTran-b8g              # chữ hiển thị
    url: https://www.youtube.com/@NhatTran-b8g    # link (bỏ dòng này nếu không cần link)
```
- Mục có `url` hiện thêm logo ở **footer**. Home hiện tối đa 8 mục đầu → mục quan trọng để trước.
- Link còn là mẫu (chứa `XXXX`, `your-id`, `example.com`) sẽ tự bị bỏ khỏi CV PDF — nhưng vẫn hiện trên web → nhớ **xoá hoặc điền link thật** (Google Scholar, ResearchGate).
- Không đưa số điện thoại, địa chỉ nhà lên web công khai.

### 4.5. Trang About — `about`
```yaml
about:
  subtitle: A little bit about who I am...
  summary: >-          # đoạn ngắn: Home + Summary trong CV PDF
    ...
  intro: |             # giới thiệu đầy đủ (Markdown, cách 1 dòng trống để xuống đoạn)
    I am a **FabLab Technician** at *Eastern International University (EIU)* ...
  interests: [Embedded Systems, Edge AI, SLAM, ROS 2]
```

### 4.6. Số mục trên Home — `home`
```yaml
home:
  projects: 3        # lấy các project có featured: true; 0 = ẩn khu này
  publications: 3
  notes: 3
```

### 4.7. Danh sách icon
Dùng cho mọi trường `icon:`:

| Nhóm | Tên icon |
|---|---|
| Lĩnh vực | `localization` `route` `chip-code` `presentation` `bot` `brain` `cpu` `code` `file-text` `book-open` `lightbulb` `globe` `users` `user` |
| CV | `graduation-cap` `briefcase` `award` `star` `calendar` `clock` `folder` |
| Liên hệ | `mail` `phone` `map-pin` `link` |
| Logo thật (tự tô màu thương hiệu) | `github` `linkedin` `youtube` `scholar` `researchgate` `orcid` `x-twitter` |
| Khác | `arrow-right` `external-link` `download` `play` `quote` |

---

## 5. CV và CV PDF — `cv.yml`

### 5.1. Phần đầu
```yaml
subtitle: My academic background, experience, skills, and achievements.
pdf: /assets/files/cv.pdf        # nút "Download PDF" — "" để ẩn
pdf_auto: true                   # true = GitHub tự tạo cv.pdf | false = tự upload
pdf_max_pages: 2                 # PDF tự co giãn để vừa số trang này (0 = không giới hạn)
pdf_text_align: justify          # justify = căn đều hai bên | left = căn trái
github: https://github.com/NhatTran-97   # nút "View on GitHub" — "" để ẩn
```

### 5.2. CV PDF — nút "Download PDF"
| Cách | Làm gì | Khi nào dùng |
|---|---|---|
| **Tự động** (`pdf_auto: true`) | Chỉ sửa dữ liệu; GitHub Actions tạo CV bằng **LaTeX (XeLaTeX)** và cập nhật `assets/files/cv.pdf` sau ~2–3 phút | Muốn PDF luôn khớp website |
| **Tự upload** (`pdf_auto: false`) | Tự làm CV (Overleaf, Word…) → xuất PDF → upload đè `assets/files/cv.pdf` | Muốn bản PDF khác website (vd. 1 trang) |

- Nội dung PDF: tên + chức danh + liên hệ, **Summary** (`about.summary`), các mục trong `cv.yml` theo đúng thứ tự, **Publications** (chèn sau Experience).
- **Tự co giãn:** vượt `pdf_max_pages` thì tự thu nhỏ chữ/khoảng cách/lề (tối thiểu ~90% cỡ chữ). Vẫn không vừa → log *Build CV PDF* báo **WARNING** → rút gọn nội dung hoặc tăng số trang.
- Theo dõi / chạy lại: tab **Actions** → *Build CV PDF* → **Run workflow**.
- Đổi màu / font / lề PDF: sửa `_cv/template.tex`. File `_cv/cv.tex` (tự tạo) mở được bằng **Overleaf** để chỉnh tay.
- Tạo trên máy (cần TeX Live): `python3 _cv/build_cv.py --compile`.

### 5.3. Các mục (sections)
Mỗi section = một mục ở cột trái trang CV (link trực tiếp: `/cv/#experience`). **Thêm / xoá / đổi thứ tự tuỳ ý.**

**Dạng timeline** (Education, Experience, Achievements, Activities…):
```yaml
sections:
  - id: experience
    title: Experience
    icon: briefcase
    items:
      - title: FabLab Technician
        org: Eastern International University (EIU)
        period: Oct 2018 – Present
        details:                   # gạch đầu dòng (Markdown), bỏ nếu không cần
          - Develop autonomous robot and drone platforms ...
          - "**Embedded:** low-level robot firmware on RTOS ..."
```

**Dạng kỹ năng** (bắt buộc `type: skills`):
```yaml
  - id: skills
    title: Skills
    type: skills
    items:
      - group: Embedded & Hardware
        items: [RTOS, SPI, I2C, UART, CAN bus, Ethernet, Modbus]
```

- Mục mới nhất / đang diễn ra để **trên cùng** trong mỗi section.
- Section `id: education` cũng hiện ở khung **Education** trên Home.

### 5.4. Học vấn: đã học xong nhưng chưa nhận bằng
```yaml
      - title: Control Engineering and Automation   # chỉ tên ngành, KHÔNG ghi "B.Eng." / "Bachelor"
        org: Eastern International University (EIU), Vietnam
        period: 2015 – 2022
        details:
          - Completed full program coursework
```
- Không ghi "Graduated" / "B.Eng." khi chưa được cấp bằng. Khi được hỏi: *"I completed the full program; the degree will be issued once I submit my English certificate."*
- Khi đã nhận bằng: đổi `title` thành `B.Eng. in Control Engineering and Automation`, bỏ dòng *Completed full program coursework*.

---

## 6. Projects — `projects.yml` + trang chi tiết `_projects/`

### 6.1. Nhóm project — `groups`
```yaml
groups:
  - id: professional              # dùng ở trường "group" của project
    title: Professional Projects
    label: Professional           # nhãn nhỏ ở góc ảnh
    icon: briefcase
    description: Projects from my work at the EIU FabLab.
```
Mỗi nhóm là một khu riêng trên trang Projects; nhóm chưa có project **tự ẩn**. Thêm nhóm mới (vd. `academic`) bằng cách thêm một khối tương tự.

### 6.2. Một project — `items`
```yaml
items:
  - title: VDA5050 Support for Open-RMF
    group: professional
    detail: /projects/vda5050-open-rmf/     # trang chi tiết (bấm ảnh / tiêu đề thẻ → mở trang này)
    org: EIU × ARTC Singapore — Technical Lead
    category: Autonomy                      # lĩnh vực chính → nhãn xanh
    period: Jun 2026 – Nov 2026
    image: /assets/img/projects/vda5050/card.jpg   # 16:9
    tags: [ROS 2, Open-RMF, VDA5050, MQTT]
    description: >-
      1–3 câu: làm gì, dùng gì, kết quả ra sao.
    featured: true                          # hiện trên Home
    github: https://github.com/...          # các nút link — bỏ dòng nào không có
    demo: https://...
    paper: /publications/
    video: https://youtube.com/...
    links:                                  # link khác tuỳ ý
      - name: Demo videos
        url: https://www.youtube.com/playlist?list=...
        icon: youtube                       # tuỳ chọn
```
**Mẹo:**
- Thứ tự trong file = thứ tự trên trang → project mạnh nhất để đầu mỗi nhóm.
- Mô tả theo công thức: *vấn đề → giải pháp / công nghệ → kết quả*.
- Project công ty thường không public code → bỏ `github`, để `video` / `News` nếu được phép; không ghi thông tin mật.
- Thanh nút lọc theo lĩnh vực đang tắt; khi > 10 project, bật bằng cách bỏ dấu `# ` ở khối `categories:` trong file.

### 6.3. Trang chi tiết project — `_projects/`
Mỗi file `_projects/<tên>.md` là một trang `/projects/<tên>/`. **Mọi project Professional đã có sẵn trang khung** (ghi *Details coming soon*).

**Phần đầu (front matter):**
```yaml
---
title: VDA5050 Support for Open-RMF
summary: Một câu mô tả (hiện dưới tiêu đề).
category: Autonomy
role: Technical Lead            # "" = ẩn
period: Jun 2026 – Nov 2026
partners: EIU FabLab × ARTC (Singapore)
status: In progress             # Completed / In progress / Under review / Ongoing
image: /assets/img/projects/vda5050/robots.jpg
image_caption: Chú thích ảnh bìa
image_ratio: "16 / 9"           # tuỳ chọn: giữ nguyên ảnh banner ngang (mặc định cắt 4 / 3)
tags: [ROS 2 Jazzy, Open-RMF, VDA5050]
links:                          # nút đầu tiên màu xanh đậm
  - name: GitHub repository
    url: https://github.com/...
    icon: github
---
```

**Bố cục nội dung gợi ý:** `## Overview` → `## My role` → `## System architecture` → `## Key features` → `## Results` → `## Demo videos` → `## Lessons learned / Limitations`.

**Các khối trình bày có sẵn** (copy từ `_templates/new-project-page.md`, chỉ sửa chữ):

| Khối | Dùng cho |
|---|---|
| `<div class="arch">…</div>` | Sơ đồ kiến trúc 2 cột có mũi tên ở giữa |
| `<div class="feature-grid">…</div>` | Lưới ô tính năng (thêm `cols-3` để luôn 3 cột trên màn rộng, vd. 6 ô → 2 hàng đều) |
| `<figure><img …><figcaption>…</figcaption></figure>` | Ảnh có chú thích |
| `<figure class="figure-narrow">…</figure>` | Ảnh không kéo quá rộng (sơ đồ, infographic, ảnh render) — tối đa 900px |
| `<figure class="figure-narrow figure-small">…</figure>` | Ảnh phụ cỡ nhỏ (vd. ảnh mạch 3D) — tối đa 480px |
| `<figure class="figure-narrow figure-large">…</figure>` | Ảnh tổng quan cỡ lớn hơn — tối đa 1100px (ảnh gốc nên rộng ≥ 1100px để không bị mờ) |
| `<div class="gallery">…</div>` | Nhiều ảnh dạng lưới |
| `<ul class="video-list">…</ul>` | Danh sách video YouTube |
| `<section class="workshop-panel">` + `<div class="workshop-cards" data-workshop-cards>` | Nhiều khoá học/workshop dạng thẻ nhỏ, bấm để mở (xem bên dưới) |
| `<div class="workshop">…</div>` | Thẻ "bìa" cho một khoá học / workshop: ảnh bìa + mục tiêu + chip + nút playlist |
| `<ol class="module-list">…</ol>` | Lộ trình học đánh số 1, 2, 3…; `<li class="module-goal">` = bước đích (ngôi sao) |
| Bảng Markdown | So sánh thông số, danh sách package |

Mẫu hoàn chỉnh: **`_projects/vda5050-open-rmf.md`** (project kỹ thuật),
**`_projects/feedforward-pi-dc-motor.md`** (bài báo nghiên cứu: ảnh bìa banner `image_ratio: "16 / 9"`, lưới `cols-3`, ảnh `figure-large`) và
**`_projects/weekly-robotics-workshop-series.md`** (chuỗi workshop / khoá học).

### 6.4. Trang workshop / khoá học dạng thẻ bấm mở
Trang **Weekly Robotics Workshop Series** (`_projects/weekly-robotics-workshop-series.md`) hiển thị mỗi workshop
thành **một thẻ nhỏ**; bấm thẻ → nội dung workshop mở ra bên dưới, bấm lại → đóng. Thẻ được **tạo tự động**:

```html
<div class="workshop-cards" data-workshop-cards></div>     <!-- chỗ hiện các thẻ (đặt 1 lần) -->

<section class="workshop-panel" id="f1tenth-autonomous-racing" markdown="1">

### Workshop 2 — F1TENTH Autonomous Racing              <!-- phần sau "—" = tên trên thẻ -->

<div class="workshop">
  <figure class="workshop-cover is-photo"><img src="/assets/img/projects/workshops/f1tenth-car.jpg" alt="..."></figure>
  <div class="workshop-info">
    <span class="workshop-no">Workshop 02 · ROS 2 & autonomous driving</span>   <!-- nhãn trên thẻ -->
    <p><strong>Goal:</strong> ...</p>
    <div class="chips"><span class="chip">ROS 2</span> ...</div>
    <p><a class="btn btn-primary" href="https://www.youtube.com/playlist?list=...">Watch the lectures</a></p>
  </div>
</div>

#### Learning path
<ol class="module-list">
  <li><div><strong>Ubuntu basics</strong><p>Mô tả ngắn.</p></div></li>
  <li><div><strong>ROS 2 basics</strong><p>...</p>
    <div class="chips"><span class="chip">Node</span><span class="chip">Topic</span></div></div></li>
  <li class="module-goal"><div><strong>Final goal: ...</strong><p>...</p></div></li>
</ol>

</section>
```

| Thẻ lấy từ | Trong khối `<section>` |
|---|---|
| Ảnh | `<figure class="workshop-cover">` — ảnh PNG nền trong suốt; ảnh chụp thường thì thêm `is-photo` |
| Nhãn nhỏ | `<span class="workshop-no">` |
| Tên | tiêu đề `###`, phần sau dấu "—" |
| "6 modules" | số bước trong `module-list` (không tính bước `module-goal`) |
| "Lecture videos" | có nút link YouTube trong khối |

- `id` của `<section>`: không dấu, không trùng — dùng làm link mở thẳng workshop: `/projects/weekly-robotics-workshop-series/#<id>` (gửi cho sinh viên được).
- Phải giữ `markdown="1"` và **dòng trống** sau `<section …>` / trước `</section>` để tiêu đề `###` hoạt động.
- Nếu trình duyệt tắt JavaScript, tất cả workshop hiện đầy đủ (không mất nội dung).
- Trong mỗi workshop có thể thêm các mục phụ (xem Workshop 1): `#### Robot platform` với ảnh tổng quan `<figure class="figure-narrow figure-large">`, và `#### In class` với ảnh lớp học dạng `<div class="gallery">` (2 ảnh cạnh nhau).
- Dùng được cho project khác (vd. một chuỗi khoá học): copy cả thẻ `<div class="workshop-cards" …>` và các khối `<section>`.

---

## 7. Publications — `publications.yml`

```yaml
- title: Developing An Autonomous Emergency Braking System-Based Kalman Filtering For An Autonomous Racing Car
  authors: Cong Danh Huynh, Nhu Y Pham, Hoang Dung Bui, Duong Tai Au, Duy Nhat Tran
  venue: EIUSC International Conference 2025 — Student Session, Ho Chi Minh City
  year: 2025                   # dùng để sắp xếp (mới nhất lên đầu)
  type: Conference             # nhóm lọc: Conference / Journal / Under Review / Preprint / Thesis…
  note: Best Paper Award (Student Session)   # nhãn vàng (tuỳ chọn)
  tags: [Autonomous Emergency Braking, Kalman Filter]
  video: https://www.youtube.com/watch?v=...
  pdf: /assets/files/papers/aeb-2025.pdf     # hoặc link ngoài
  doi: 10.xxxx/xxxxx          # chỉ mã DOI
  code: https://github.com/...
  bibtex: |
    @inproceedings{...}
```
- Tên bạn phải khớp **chính xác** một tên trong `publication_names` (`profile.yml`) để được in đậm.
- Ghi tác giả **đúng thứ tự trong bài**, viết không dấu.
- Bài đang phản biện: `type: Under Review`, `note: Under Review`, `venue: Under review at <Hội nghị> 2026`.
- `type` mới → tự thêm mục lọc ở cột trái. Home hiện 3 bài mới nhất. Bài báo cũng tự có trong CV PDF.

---

## 8. Notes — viết bài chia sẻ kiến thức

### 8.1. Tạo bài
1. Copy `_templates/new-note.md` vào `_posts/`, đặt tên **`YYYY-MM-DD-ten-bai-khong-dau.md`** (ngày trong tên = ngày đăng, không được ở tương lai).
2. Sửa phần đầu và viết bài → Commit.

```yaml
---
title: "PID Controller — From Theory to Code"
category: Autonomy          # Embedded & Hardware / Perception & AI / Autonomy / Tools & Tips / Research
tags: [PID, Control, Python]
description: "Một câu tóm tắt, hiện trên thẻ bài viết và khi chia sẻ link."
image: /assets/img/notes/pid.jpg   # ảnh bìa 16:9 (tuỳ chọn)
math: true                  # bật nếu có công thức toán
---
```

### 8.2. Cú pháp Markdown hay dùng
| Muốn | Viết |
|---|---|
| Tiêu đề mục | `## Tiêu đề`, `### Tiêu đề nhỏ` |
| In đậm / nghiêng | `**đậm**`, `*nghiêng*` |
| Link / ảnh | `[chữ](https://...)`, `![mô tả](/assets/img/notes/anh.png)` |
| Danh sách | `- mục` hoặc `1. mục` |
| Ghi chú nổi bật | `> Ghi chú` |
| Code | `` `ros2 topic list` `` hoặc khối ```` ```python ```` … ```` ``` ```` |
| Bảng | `\| Cột 1 \| Cột 2 \|` + dòng `\|---\|---\|` |
| Công thức (cần `math: true`) | `$E = mc^2$`, `$$ x_k = F x_{k-1} + w_k $$` |

### 8.3. Sửa / ẩn / xoá
- Ẩn tạm (nháp): thêm `published: false` vào phần đầu.
- Đổi ngày đăng: đổi ngày trong tên file.
- 3 bài trong `_posts/` hiện là **bài mẫu** — xoá khi có bài thật.

---

## 9. Ảnh và file

| Loại | Thư mục | Kích thước gợi ý |
|---|---|---|
| Ảnh đại diện | `assets/img/avatar.jpg` | dọc 4:5, ~600px |
| Ảnh banner | `assets/img/hero/` | ngang ~2400×900 |
| Ảnh thẻ project | `assets/img/projects/` | 16:9, ~1280px |
| Ảnh trang chi tiết project | `assets/img/projects/<tên-project>/` | rộng ~1400–1600px |
| Ảnh workshop (bìa + ảnh lớp) | `assets/img/projects/workshops/` | bìa vuông hoặc PNG nền trong suốt; ảnh lớp ~1600px |
| Hình minh hoạ 4 ô dưới banner (tuỳ chọn) | `assets/img/highlights/` | vuông, nền trong suốt, SVG hoặc PNG ~256px |
| Ảnh bài viết | `assets/img/notes/` | 16:9, ~1000px |
| CV PDF | `assets/files/cv.pdf` | tự tạo nếu `pdf_auto: true` |
| PDF bài báo | `assets/files/papers/` | — |
| Favicon | `assets/icons/` + `favicon.ico` | vuông: 32, 180, 192, 512px |

- Ảnh điện thoại thường 3–5 MB → **nén trước** bằng https://squoosh.app (JPG/WebP, chất lượng ~75). Mỗi ảnh **< 300 KB**.
- Tên file **không dấu, không khoảng trắng**, chữ thường: `robot-arm.jpg` ✅ — `Ảnh robot 1.JPG` ❌.
- Ảnh có người khác (sinh viên…): ưu tiên ảnh đã được trường/đơn vị đăng công khai.
- Đổi favicon: upload **đè đúng tên** `assets/icons/favicon-32.png`, `apple-touch-icon.png`, `icon-192.png`, `icon-512.png` và `favicon.ico` → xem bằng tab ẩn danh.

---

## 10. Giao diện: menu, màu, căn chữ, ảnh banner, độ rộng

### 10.1. Menu — `_data/navigation.yml`
Xoá dòng để ẩn trang khỏi menu; đổi thứ tự để đổi vị trí.

### 10.2. Tiêu đề trên Google — `_config.yml`
Sửa `title` và `description`.

### 10.3. Căn chữ — công tắc
| Công tắc | Ở đâu | Giá trị | Đang dùng |
|---|---|---|---|
| `typography.text_align` | `_config.yml` | `left` / `justify` | `left` — toàn website (dễ đọc, không hở chữ) |
| `typography.post_text_align` | `_config.yml` | `left` / `justify` | `left` — nội dung bài viết & trang chi tiết project |
| `pdf_text_align` | `_data/cv.yml` | `justify` / `left` | `justify` — CV PDF như tài liệu in |

Luôn tự động: tiêu đề cân dòng; tiêu đề thẻ project/bài viết chiếm 2 dòng để các thẻ thẳng hàng; 4 ô dưới banner đúng 2 dòng; điện thoại nhỏ luôn căn trái.

### 10.4. Ảnh nền banner
Sửa `hero.background` trong `profile.yml`. Có sẵn trong `assets/img/hero/`:

| File | Nội dung |
|---|---|
| `hero-photo-mountain.jpg` | Ảnh bạn mờ dần trên núi xanh ngọc (**đang dùng**) |
| `hero-photo-fablab.jpg` | Ảnh bạn trong FabLab, bên trái chuyển xanh đậm |
| `hero-mountain-teal.svg` | Tranh núi xanh ngọc, bình minh, quỹ đạo robot |
| `hero-mountain-dawn.svg` | Tranh núi tím – vàng cam |

Ảnh mới: ngang ~2400×900, **chủ thể bên phải**, bên trái tối/đơn giản để chữ dễ đọc, < 300 KB.

### 10.5. Màu chủ đạo
`_sass/base/_tokens.scss` → dòng `--primary: #1f5fd6;` (bảng màu sáng) và `--primary` trong `dark-palette` (bảng màu tối). Ví dụ `#0f766e` xanh ngọc, `#7c3aed` tím.

### 10.6. Độ rộng trang & responsive
Trang **tự co giãn theo màn hình**: mỗi vùng chiếm một tỉ lệ % chiều rộng màn hình, nhưng không hẹp hơn
mức tối thiểu (trừ khi màn hình nhỏ hơn) và không rộng quá mức tối đa. Chỉnh ở `_sass/base/_tokens.scss`,
mục *Page widths*:

| Vùng | min | % màn hình | max |
|---|---|---|---|
| Toàn trang: header, footer, Home, Projects, CV, Publications, Notes, About (`$container-…`) | 1320px | 82vw | 1840px |
| Trang chi tiết project (`$detail-…`) | 1200px | 72vw | 1560px |
| Bài viết Notes (`$reading-…`), giữ vừa phải để dòng chữ dễ đọc | 820px | 50vw | 1000px |

Kết quả thực tế (đã kiểm tra tự động, không màn hình nào bị tràn ngang):

| Màn hình | Khung nội dung | Bố cục |
|---|---|---|
| Điện thoại 320–560px | toàn màn hình, lề 16px | 1 cột, menu ☰ |
| Tablet 760–1080px | toàn màn hình | 2 cột |
| Laptop 1366px | 1320px | 3 cột |
| Màn Full HD 1920px | ~1575px (82%) | 3 cột |
| Màn 2K/4K ≥ 1700px | tối đa 1840px | lưới Projects / Notes **4 cột** |

Các mốc chuyển bố cục là `$bp-xl / lg / md / sm / xs` trong cùng file. Banner Home tự cao thêm một chút
trên màn rộng để ảnh nền không bị cắt.

**Lưu ý khi sửa file `.scss`:** chú thích `//` kéo dài tới **hết dòng**, nên đừng viết CSS phía sau nó trên
cùng một dòng (phần đó sẽ bị bỏ qua). `check_site.py` sẽ báo lỗi nếu gặp trường hợp này.

---

## 11. Nguyên tắc nội dung (cách viết cho nhất quán)

- **Giọng văn khiêm tốn, đúng sự thật:** "learning by building", "mainly…", "along with…"; tránh "expert", "specialist". Chức danh thật: *FabLab Technician*.
- **Ghi rõ vai trò:** *Technical Lead*, *Mentor*, *Research mentor & co-author*, *supervising author* — không nhận thay thành tích của sinh viên.
- **Ghi rõ trạng thái:** *Ongoing*, *In progress*, *Under review*; chỉ đưa vào Achievements khi đã có kết quả.
- **Ghi rõ phạm vi giải:** vd. **Best Paper Award (Student Session)**.
- **Tên lĩnh vực viết thống nhất** ở mọi nơi (`category` của project, bài viết, nhóm kỹ năng): `Embedded & Hardware` · `Perception & AI` · `Autonomy` · `Teaching & Mentoring` · `Tools & Tips` · `Research`. Viết khác chữ hoa/thường sẽ bị tách thành nhóm khác.
- **Ngôn ngữ website:** tiếng Anh; tên chính thức tiếng Việt (cuộc thi…) có thể ghi thêm in nghiêng.

---

## 12. Quy tắc viết YAML (tránh lỗi)

- Thụt lề bằng **dấu cách**, không dùng Tab; giữ đúng số dấu cách như dòng mẫu.
- Mỗi mục danh sách bắt đầu bằng `- `.
- **Có dấu `:` hoặc `#` trong nội dung, hoặc bắt đầu bằng `*` `[` `{` `@` `"` → bọc trong ngoặc kép:**
  `period: "2026 – Ongoing (competition: October 2026)"`, `- "**GPA:** 3.8"`.
- Năm đứng một mình nên bọc ngoặc kép: `period: "2025"`.
- Dòng bắt đầu bằng `#` là ghi chú; muốn tạm ẩn một mục thì thêm `# ` vào đầu các dòng của mục đó.

---

## 13. Xử lý sự cố & kiểm tra tự động

| Hiện tượng | Cách xử lý |
|---|---|
| Sửa xong web không đổi | Đợi 2 phút → **Ctrl + Shift + R** hoặc tab ẩn danh (trình duyệt lưu trang cũ tới ~10 phút). Vẫn không đổi → tab **Actions**. |
| Đã thay ảnh nhưng web vẫn hiện ảnh cũ | Ảnh được upload đè **trùng tên** → trình duyệt dùng bản cũ đã lưu. Đổi sang **tên file mới** và sửa đường dẫn (xem [mục 1](#1-cách-sửa-file-trên-github)), hoặc đợi ~10 phút rồi Ctrl + Shift + R. |
| Actions báo ❌ đỏ | Mở lần chạy lỗi. Với **Check site**, bấm bước bị đỏ: mỗi dòng `ERROR` ghi rõ file + lỗi (vd. `image not found`, `unknown icon`, `YAML syntax error (line 96)`, `detail page file … does not exist`). Sửa đúng chỗ đó rồi commit lại. |
| CV PDF không cập nhật | Tab **Actions** → *Build CV PDF*: xem lỗi hoặc bấm **Run workflow**. Kiểm tra `pdf_auto: true`. |
| Ảnh không hiện | Đường dẫn bắt đầu bằng `/assets/...`, đúng tên file và chữ hoa/thường. |
| Bài viết không hiện | Tên file dạng `YYYY-MM-DD-ten.md` trong `_posts/`, có `---` ở đầu, ngày không ở tương lai. |
| Trang chi tiết project 404 | File nằm trong `_projects/`, và `detail:` trong `projects.yml` trùng tên file (vd. `_projects/abc.md` ↔ `/projects/abc/`). |
| Công thức toán không hiện | Thêm `math: true` vào phần đầu bài. |
| Tên mình không in đậm | Tên trong `authors` phải khớp chính xác `publication_names`. |
| Thẻ workshop không hiện / bấm không mở | Khối phải là `<section class="workshop-panel" id="..." markdown="1">` (có `id`, không trùng) và trang có `<div class="workshop-cards" data-workshop-cards></div>` phía trên. |
| Giao diện lỗi sau khi sửa file `.scss` (mất màu, mất bo góc…) | Xem **Check site**: thường do viết CSS phía sau chú thích `//` trên cùng một dòng. |
| Máy tính không vào được web nhưng 4G vào được | Do mạng/DNS: đổi DNS sang `8.8.8.8` / `1.1.1.1`, khởi động lại router. |

### 13.1. Kiểm tra tự động (Check site)
Mỗi lần commit, GitHub chạy **Check site** (`_scripts/check_site.py`):
- **ERROR** (phải sửa): lỗi cú pháp YAML (kèm số dòng), ảnh / PDF không tồn tại (kể cả `image` của 4 ô dưới banner), icon sai tên, project thiếu `title` / `group` / `description`, `group` không có trong `groups`, `detail` trỏ tới trang không tồn tại, tên file bài viết sai dạng, trùng tên project, CSS viết sau chú thích `//` trong file `.scss` (sẽ bị bỏ qua), link hỏng sau khi build.
- **WARNING** (nên xem): link liên hệ còn là mẫu, ô giới thiệu quá dài, lĩnh vực viết khác danh sách chuẩn, tên bạn không có trong danh sách tác giả, trang project còn *Details coming soon*.
- Chạy trên máy: `python3 _scripts/check_site.py` (cần `pip install pyyaml`); thêm thư mục đã build để kiểm tra link: `python3 _scripts/check_site.py _site`.

---

## 14. Cấu trúc thư mục
```
├── _config.yml              # tiêu đề web, công tắc căn chữ
├── _data/                   # ★ NỘI DUNG
│   ├── profile.yml          #   cá nhân, banner, Home, About, liên hệ
│   ├── cv.yml               #   CV + cài đặt CV PDF
│   ├── projects.yml         #   thẻ project
│   ├── publications.yml     #   bài báo
│   └── navigation.yml       #   menu
├── _projects/               # ★ TRANG CHI TIẾT PROJECT (mỗi file = 1 trang)
├── _posts/                  # ★ BÀI VIẾT NOTES
├── _templates/              #   file mẫu: new-note.md, new-project-page.md (không lên web)
├── assets/
│   ├── img/                 # ★ ẢNH (avatar, hero/, projects/, notes/)
│   ├── files/               # ★ cv.pdf, papers/
│   ├── icons/               #   favicon
│   ├── css/style.scss       #   chỉ danh sách @import (không viết style ở đây)
│   ├── js/main.js           #   sáng/tối, menu, bộ lọc, tab CV, thẻ workshop, tìm kiếm
│   └── fonts/               #   font Inter
├── _sass/                   #   GIAO DIỆN — mỗi phần 1 file (xem bên dưới)
├── _layouts/                #   khung trang: default, post, project
├── _includes/               #   thành phần dùng lại: header, footer, thẻ project/bài viết/bài báo, icon…
├── _cv/                     #   template LaTeX + script tạo CV PDF
├── _scripts/check_site.py   #   kiểm tra lỗi nội dung + link
├── .github/workflows/       #   Build CV PDF, Check site
└── *.html                   #   các trang (không cần sửa)
```

### Giao diện (dành cho khi cần sửa CSS)
CSS được chia theo thành phần trong `_sass/`, **mỗi file chứa toàn bộ style của một phần kể cả bản điện thoại** — muốn sửa phần nào thì mở đúng file đó, không sửa chỗ khác:

| File | Phụ trách |
|---|---|
| `base/_tokens.scss` | **Màu sắc** (sáng + tối), font, bo góc, **độ rộng trang** (co giãn theo màn hình), các mốc màn hình (`$bp-xl/lg/md/sm/xs`) |
| `base/_base.scss`, `_fonts.scss` | Nền tảng trang, font Inter |
| `base/_typography.scss` | Căn chữ, công tắc `justify` (nạp cuối cùng) |
| `components/*` | Nút, nhãn, thẻ card, timeline CV, thẻ project, thẻ bài viết, bài báo, màu icon liên hệ |
| `layout/*` | Header + menu, tìm kiếm, footer, tiêu đề trang + cột trái, nội dung Markdown, khối trình bày (arch, gallery, video-list, workshop, module-list, thẻ workshop) |
| `pages/*` | Riêng từng trang: Home, About, CV, Projects + trang chi tiết, bài viết + 404 |

Thứ tự nạp nằm trong `assets/css/style.scss`: tokens → base → components → layout → pages → màu icon → typography. File nạp sau được ưu tiên.
- **Đổi màu:** chỉ sửa `base/_tokens.scss`. **Thêm màu cho icon liên hệ mới:** thêm 1 dòng trong `components/_brand-icons.scss`.
- **Thêm thành phần mới:** tạo `_sass/components/_ten.scss` rồi thêm `@import "components/ten";` vào `style.scss`.
- Chế độ tối cho 1 thành phần: dùng `@include when-dark { ... }` (xem `_chips.scss`).
- Độ rộng co giãn cho 1 vùng mới: `@include fluid-width($min, $fluid, $max);` (xem `_tokens.scss`).
- Lưới thẻ tự co theo màn hình: `grid-template-columns: repeat(auto-fit, minmax(#{unquote("min(260px, 100%)")}, 1fr));` — không bao giờ tràn ngang trên điện thoại.
- Chú thích `//` luôn đặt **trên dòng riêng** (xem [mục 10.6](#106-độ-rộng-trang--responsive)).

---

## 15. Chạy thử trên máy (tuỳ chọn)
Cần Ruby (và TeX Live nếu muốn tạo CV PDF):
```bash
bundle install
bundle exec jekyll serve              # mở http://localhost:4000
python3 _cv/build_cv.py --compile     # tạo _cv/cv.pdf
```

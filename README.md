# NhatTran-97.github.io

Website portfolio cá nhân chạy trên **GitHub Pages + Jekyll**.
👉 **https://nhattran-97.github.io**

> **Nguyên tắc:** toàn bộ nội dung nằm trong các **file dữ liệu** (`_data/*.yml`) và **bài viết** (`_posts/*.md`).
> Bạn **không cần sửa HTML/CSS/JS**. Sửa file → Commit → 1–2 phút sau website tự cập nhật.

## Mục lục
0. [Bắt đầu nhanh — checklist lần đầu](#0-bắt-đầu-nhanh--checklist-lần-đầu)
1. [Cách sửa file trực tiếp trên GitHub](#1-cách-sửa-file-trực-tiếp-trên-github)
2. [Bản đồ: muốn sửa gì thì mở file nào](#2-bản-đồ-muốn-sửa-gì-thì-mở-file-nào)
   - [Cách tổ chức nội dung: theo robot pipeline](#cách-tổ-chức-nội-dung-theo-robot-pipeline)
3. [Thông tin cá nhân & trang Home / About — `profile.yml`](#3-thông-tin-cá-nhân--trang-home--about--profileyml)
4. [CV — `cv.yml`](#4-cv--cvyml)
5. [Projects — `projects.yml`](#5-projects--projectsyml)
6. [Publications — `publications.yml`](#6-publications--publicationsyml)
7. [Notes — viết bài chia sẻ kiến thức](#7-notes--viết-bài-chia-sẻ-kiến-thức)
8. [Ảnh và file (upload, kích thước)](#8-ảnh-và-file)
9. [Menu, tiêu đề web, màu sắc](#9-menu-tiêu-đề-web-màu-sắc)
10. [Quy tắc viết file YAML (tránh lỗi)](#10-quy-tắc-viết-file-yaml-tránh-lỗi)
11. [Xử lý sự cố](#11-xử-lý-sự-cố)
12. [Tính năng có sẵn](#12-tính-năng-có-sẵn)
13. [Chạy thử trên máy (tuỳ chọn)](#13-chạy-thử-trên-máy-tuỳ-chọn)
14. [Cấu trúc thư mục](#14-cấu-trúc-thư-mục)

---

## 0. Bắt đầu nhanh — checklist lần đầu

Website đang chứa **dữ liệu mẫu** (tên công ty, project, bài báo, số liệu đều là giả). Làm lần lượt:

- [ ] **Thông tin cơ bản** — `_data/profile.yml`: `name`, `short_name`, `role`, `hero.tagline`, `hero.intro`.
- [ ] **Liên hệ** — `_data/profile.yml` → `contacts`: email, LinkedIn, GitHub, Google Scholar… (xoá mục không dùng).
- [ ] **Giới thiệu** — `_data/profile.yml` → `about.summary`, `about.intro`, `about.interests`.
- [ ] **Ảnh đại diện** — upload vào `assets/img/`, sửa `avatar:`.
- [ ] **Ảnh banner** (tuỳ chọn) — upload vào `assets/img/`, sửa `hero.background`.
- [ ] **CV** — `_data/cv.yml`: học vấn, kinh nghiệm, kỹ năng, giải thưởng, hoạt động.
- [ ] **CV PDF** — upload file vào `assets/files/` với tên `cv.pdf` (nếu chưa có, để `pdf: ""` để ẩn nút).
- [ ] **Projects** — `_data/projects.yml`: thay các project mẫu bằng project thật, đánh dấu 3 project tốt nhất `featured: true`.
- [ ] **Publications** — `_data/publications.yml`: thay bằng bài thật (chưa có bài nào → xoá dòng `Publications` trong `_data/navigation.yml` và đặt `home.publications: 0`).
- [ ] **Notes** — xoá 3 bài mẫu trong `_posts/` (hoặc giữ làm tham khảo), viết bài đầu tiên theo [mục 7](#7-notes--viết-bài-chia-sẻ-kiến-thức).
- [ ] **Tiêu đề trên Google** — `_config.yml`: `title`, `description`.
- [ ] Mở web trên điện thoại kiểm tra lần cuối → gửi link cho mọi người 🎉

---

## 1. Cách sửa file trực tiếp trên GitHub

Không cần cài gì, làm ngay trên trình duyệt:

1. Vào repo `https://github.com/NhatTran-97/NhatTran-97.github.io`.
2. Bấm vào file cần sửa (ví dụ `_data` → `profile.yml`).
3. Bấm biểu tượng **✏️ (Edit this file)** ở góc phải.
4. Sửa nội dung.
5. Bấm **Commit changes…** → ghi ngắn gọn đã sửa gì → **Commit changes**.
6. Đợi 1–2 phút, mở website và bấm **Ctrl + F5** để xem bản mới.

**Tạo file mới** (ví dụ bài viết): vào thư mục → **Add file → Create new file**.
**Upload ảnh / PDF**: vào thư mục → **Add file → Upload files** → kéo thả file → **Commit changes**.

> Theo dõi tiến trình: tab **Actions** → dòng *pages build and deployment*. ✅ xanh = xong, ❌ đỏ = có lỗi (xem [mục 11](#11-xử-lý-sự-cố)).

---

## 2. Bản đồ: muốn sửa gì thì mở file nào

| Muốn thay đổi | File |
|---|---|
| Tên, chức danh, ảnh đại diện | `_data/profile.yml` |
| Banner trang Home (lời chào, giới thiệu, nút bấm, câu quote, ảnh nền) | `_data/profile.yml` → `hero` |
| 4 ô giới thiệu dưới banner | `_data/profile.yml` → `highlights` |
| Email, LinkedIn, GitHub, Scholar… (trang About, Home, footer) | `_data/profile.yml` → `contacts` |
| Đoạn giới thiệu, sở thích (trang About) | `_data/profile.yml` → `about` |
| Số project / bài báo / bài viết hiện trên Home | `_data/profile.yml` → `home` |
| CV: học vấn, kinh nghiệm, kỹ năng, giải thưởng, hoạt động | `_data/cv.yml` |
| Project (chia nhóm Professional / Personal) | `_data/projects.yml` |
| Bài báo khoa học | `_data/publications.yml` |
| Bài viết chia sẻ kiến thức | thư mục `_posts/` |
| Menu trên cùng | `_data/navigation.yml` |
| Tiêu đề web trên Google / tab trình duyệt | `_config.yml` |
| File CV PDF | `assets/files/cv.pdf` |

### Cách tổ chức nội dung: theo robot pipeline

Website được sắp xếp quanh một thông điệp: **làm robot từ phần cứng tới thuật toán**. Dùng chung 3 lĩnh vực — tương ứng các tầng của robot — ở mọi nơi để người xem nhìn đâu cũng thấy cùng một bức tranh:

```
Cảm biến ─► Embedded & Hardware ─► Perception & AI ─► Autonomy ─► Embedded & Hardware ─► Động cơ
            (firmware, driver,      (computer vision,   (SLAM, planning,  (motor control,
             CAN, RTOS)              deep learning)      control, ROS 2)   PID, CAN)
```

| Ở đâu | Dùng thế nào |
|---|---|
| 4 ô dưới banner (`profile.yml → highlights`) | 3 tầng + Research & Publication |
| Project (`projects.yml → category`) | chọn **1 tầng chính**, các mảng phụ ghi vào `tags` |
| Bài viết (`category` trong bài) | `Embedded & Hardware` · `Perception & AI` · `Autonomy` · `Tools & Tips` · `Research` |
| CV → Skills (`cv.yml`) | nhóm kỹ năng theo tầng: Embedded & Hardware · Perception & AI · Autonomy · Programming · Tools |

> Viết **đúng chính tả và chữ hoa/thường** các tên lĩnh vực ở mọi nơi (vd. luôn là `Perception & AI`), nếu không sẽ bị tách thành 2 nhóm khác nhau.
>
> 💡 Điểm mạnh nhất của portfolio: một project **xuyên cả 3 tầng** (vd. robot tự hành: board STM32 điều khiển motor + Jetson chạy model vision + ROS 2 navigation). Đặt nó lên đầu và `featured: true`.

---

## 3. Thông tin cá nhân & trang Home / About — `profile.yml`

### 3.1. Thông tin cơ bản
```yaml
name: Nhat Tran                 # Tên đầy đủ (hiện ở banner, About, footer)
short_name: N. Tran             # Tên ngắn ở góc trái menu
role: Robotics Engineer — Embedded, Perception & Autonomy   # Chức danh (trang About)
avatar: /assets/img/avatar.jpg  # Ảnh đại diện, ảnh dọc tỉ lệ 4:5

publication_names:              # Tên bạn trong danh sách tác giả → tự in đậm
  - Nhat Tran
  - N. Tran
```

### 3.2. Banner trang Home — `hero`
```yaml
hero:
  greeting: Hello, I'm                      # dòng chữ nhỏ phía trên tên
  tagline: A robotics engineer and researcher.
  intro: >-
    Đoạn giới thiệu 1–2 câu. Dấu ">-" cho phép viết xuống dòng
    mà vẫn hiển thị thành một đoạn liền.
  background: /assets/img/hero.jpg          # ảnh nền (ảnh ngang, ≥ 1600px)
  quote: "Curiosity drives better questions."   # để trống "" nếu không muốn
  buttons:
    - text: View My CV
      url: /cv/
      icon_after: arrow-right               # icon sau chữ
      style: primary                        # primary = nút xanh đặc
    - text: See My Projects
      url: /projects/
      icon: github                          # icon trước chữ
      style: ghost                          # ghost = nút viền trong suốt
```

### 3.3. Bốn ô giới thiệu — `highlights`
```yaml
highlights:
  - icon: cpu
    title: Embedded & Hardware
    text: Firmware, sensor drivers, motor control and real-time systems.
  - icon: brain
    title: Perception & AI
    text: Computer vision and deep learning, optimized for edge devices.
  - icon: bot
    title: Autonomy
    text: SLAM, localization, motion planning and control with ROS 2.
  - icon: file-text
    title: Research & Publication
    text: Explore and share knowledge through academic work.
```
Có thể để 2, 3 hoặc 4 ô. Xoá hết phần `highlights` nếu không muốn hiện.

### 3.4. Liên hệ — `contacts`
```yaml
contacts:
  - icon: mail
    label: Email                              # tiêu đề nhỏ (trang About)
    value: your.email@example.com             # chữ hiển thị
    url: mailto:your.email@example.com        # link khi bấm (bỏ dòng này nếu không cần link)
```
- Mục có `url` sẽ hiện thêm icon ở **footer**.
- Trang **Home** hiện tối đa 8 mục đầu tiên → đặt mục quan trọng lên trước.
- Không có số điện thoại / địa chỉ riêng tư trên web công khai.

### 3.5. Trang About — `about`
```yaml
about:
  subtitle: A little bit about who I am...    # dòng dưới tiêu đề "About Me"
  summary: >-                                 # đoạn ngắn trên trang Home
    I am a robotics engineer ...
  intro: |                                    # phần giới thiệu đầy đủ (Markdown)
    Đoạn 1 ... **in đậm**, *in nghiêng*, [link](https://...)

    Đoạn 2 (cách một dòng trống để xuống đoạn)
  interests: [SLAM, Motion Planning, ROS 2]   # các thẻ sở thích
```
> `>-` = gộp thành 1 đoạn. `|` = giữ nguyên xuống dòng (dùng cho nhiều đoạn).

### 3.6. Trang Home hiển thị bao nhiêu mục — `home`
```yaml
home:
  projects: 3        # đặt 0 để ẩn khu Projects trên Home
  publications: 3
  notes: 3
```

### 3.7. Danh sách icon dùng được
Dùng cho mọi trường `icon:` trong các file dữ liệu:

| Nhóm | Tên icon |
|---|---|
| Lĩnh vực | `bot` `brain` `cpu` `code` `file-text` `book-open` `lightbulb` `globe` `users` `user` |
| CV | `graduation-cap` `briefcase` `award` `star` `calendar` `clock` `folder` |
| Liên hệ | `mail` `phone` `map-pin` `link` |
| Mạng xã hội (logo thật, tự tô màu thương hiệu) | `github` `linkedin` `youtube` `scholar` `researchgate` `orcid` `x-twitter` |
| Khác | `arrow-right` `external-link` `download` `play` |

---

## 4. CV — `cv.yml`

### 4.1. Phần đầu
```yaml
subtitle: My academic background, experience, skills, and achievements.
pdf: /assets/files/cv.pdf                   # nút "Download PDF" — để "" để ẩn
pdf_auto: true                              # true = GitHub tự tạo cv.pdf từ dữ liệu website
pdf_max_pages: 2                            # PDF tự co giãn để vừa số trang này (0 = không giới hạn)
github: https://github.com/NhatTran-97       # nút "View on GitHub" — để "" để ẩn
```

### 4.1b. File CV PDF (nút "Download PDF") — 2 cách

| Cách | Làm gì | Khi nào dùng |
|---|---|---|
| **Tự động** (`pdf_auto: true`, mặc định) | Chỉ cần sửa `_data/cv.yml` / `profile.yml` / `publications.yml`. GitHub Actions tự tạo CV bằng **LaTeX (XeLaTeX)** và cập nhật `assets/files/cv.pdf` sau ~2–3 phút | Muốn PDF luôn khớp website |
| **Tự upload** (`pdf_auto: false`) | Tự làm CV (Overleaf, Word…) → xuất PDF → upload đè vào `assets/files/cv.pdf` | Muốn CV PDF khác website (vd. bản rút gọn 1 trang) |

- PDF tự động gồm: tiêu đề + liên hệ, Summary (`about.summary`), các mục trong `cv.yml` theo đúng thứ tự, và **Publications** (chèn sau Experience).
- **Tự co giãn cho vừa số trang:** đặt `pdf_max_pages: 2` trong `cv.yml` (0 = không giới hạn). Khi nội dung dài hơn, PDF tự thu nhỏ dần chữ, khoảng cách, lề (tối thiểu ~90% cỡ chữ để vẫn dễ đọc). Nếu thu nhỏ hết mức vẫn không vừa, log của GitHub Actions báo *WARNING* → rút gọn nội dung hoặc tăng `pdf_max_pages`.
- Liên hệ còn là link mẫu (chứa `XXXX`, `your-id`, `example.com`) sẽ tự bị bỏ khỏi PDF.
- Theo dõi: tab **Actions** → *Build CV PDF*. Chạy lại thủ công: *Build CV PDF* → **Run workflow**.
- Đổi màu / font / lề của PDF: sửa `_cv/template.tex`. File `_cv/cv.tex` (được tạo tự động) có thể mở bằng **Overleaf** để chỉnh tay.
- Tạo PDF trên máy (cần TeX Live): `python3 _cv/build_cv.py --compile` (tự co giãn như trên GitHub).

### 4.2. Các mục (sections)
Mỗi section = một mục ở cột trái trang CV. **Thêm / xoá / đổi thứ tự tuỳ ý.**

**Dạng timeline** (Education, Experience, Achievements, Activities, Certifications…):
```yaml
sections:
  - id: experience              # mã, viết liền không dấu (dùng cho link /cv/#experience)
    title: Experience           # tên hiển thị
    icon: briefcase             # icon bên phải mỗi mục
    items:
      - title: Robotics Engineer
        org: Company Name, Ho Chi Minh City
        period: 2024 – Present
        details:                # các gạch đầu dòng (Markdown), bỏ nếu không cần
          - Developed the navigation stack ...
          - "**Key result:** reduced drift by 40%"
```

**Dạng kỹ năng** (nhóm theo tầng robot):
```yaml
  - id: skills
    title: Skills
    type: skills                # ← bắt buộc để hiển thị dạng thẻ
    items:
      - group: Embedded & Hardware
        items: [STM32, ESP32, FreeRTOS, CAN, UART / SPI / I2C]
      - group: Perception & AI
        items: [PyTorch, OpenCV, TensorRT, YOLO]
      - group: Autonomy
        items: [ROS 2, Nav2, SLAM, MPC / PID]
      - group: Programming
        items: [C / C++, Python, CUDA]
```

**Ví dụ thêm mục mới** — Certifications:
```yaml
  - id: certifications
    title: Certifications
    icon: award
    items:
      - title: Deep Learning Specialization
        org: Coursera / DeepLearning.AI
        period: "2023"
```
> Section có `id: education` cũng được dùng cho khung **Education** trên trang Home (hiện 3 mục đầu).

### 4.3. Ghi học vấn khi đã học xong nhưng chưa nhận bằng
Cách trình bày trung thực, dễ đọc — thường dùng trong CV quốc tế:
```yaml
      - title: Control Engineering and Automation   # chỉ tên ngành, KHÔNG ghi "B.Eng." / "Bachelor"
        org: University Name, Vietnam
        period: 2015 – 2022
        details:
          - Completed full program coursework         # đúng sự thật, cho thấy đã học đủ chương trình
          - "**Focus:** control systems, embedded systems, robotics"
          - "**Capstone project:** ..."
```
- **Không** ghi "Graduated", "B.Eng." hay "Bachelor of…" khi chưa được cấp bằng (nhiều nơi xác minh bằng cấp).
- Khi được hỏi: *"I completed the full program; the degree will be issued once I submit my English certificate."*
- Khi đã nhận bằng: đổi `title` thành `B.Eng. in Control Engineering and Automation` và bỏ dòng "Completed full program coursework".

---

## 5. Projects — `projects.yml`

File gồm 2 phần: **`groups`** (các nhóm) và **`items`** (danh sách project).

### 5.1. Nhóm project — `groups`
Mỗi nhóm hiển thị thành một khu riêng trên trang Projects, theo đúng thứ tự khai báo.
```yaml
groups:
  - id: professional                 # mã nhóm, dùng ở trường "group" của project
    title: Professional Projects     # tiêu đề khu
    label: Professional              # nhãn nhỏ ở góc ảnh project
    icon: briefcase
    description: Projects I built and shipped as part of my work in industry.
  - id: personal
    title: Personal Projects
    label: Personal
    icon: user
    description: Research, side projects and open-source work done in my own time.
```
- Đổi tên tuỳ ý, ví dụ `Industry Projects` / `Side Projects`, `Work` / `Research`.
- Thêm nhóm mới, ví dụ `academic` (project ở trường / lab):
  ```yaml
    - id: academic
      title: Academic Projects
      label: Academic
      icon: graduation-cap
  ```
- Nhóm nào chưa có project sẽ **tự ẩn**.

### 5.1b. Lĩnh vực & thanh lọc (tuỳ chọn)
Mỗi project có 1 `category` = lĩnh vực chính, hiện thành nhãn xanh trên thẻ. Nên dùng các tầng của robot pipeline:
`Embedded & Hardware` · `Perception & AI` · `Autonomy`. Mảng phụ ghi vào `tags`.

Thanh **nút lọc theo lĩnh vực** đang tắt cho gọn. Khi có nhiều project (> 10), bật lại bằng cách xoá dấu `# ` ở khối này trong `projects.yml`:
```yaml
categories:
  - Embedded & Hardware
  - Perception & AI
  - Autonomy
```

### 5.2. Một project — `items`
```yaml
items:
  - title: Autonomous Warehouse Robot
    group: professional              # id nhóm ở trên
    org: Company Name                # công ty / tổ chức (tuỳ chọn)
    category: Autonomy               # lĩnh vực chính → nhãn xanh trên thẻ
    period: 2024 – Present
    image: /assets/img/projects/warehouse.jpg   # ảnh 16:9; bỏ dòng này → ảnh mặc định
    tags: [ROS 2, C++, Nav2]
    description: >-
      Mô tả ngắn 1–3 câu: làm gì, dùng gì, kết quả ra sao.
    featured: true                   # hiện trên trang Home
    github: https://github.com/...   # các link — bỏ dòng nào không có
    demo: https://...
    paper: /publications/
    video: https://youtube.com/...
    links:                           # link khác tuỳ ý (bài báo, bài đăng, slide...)
      - name: News
        url: https://eiu.edu.vn/...
        icon: link                   # tuỳ chọn, mặc định là icon mũi tên ra ngoài
```

**Mẹo:**
- **Project công ty** thường không public code → bỏ `github`, có thể để `video` hoặc `demo` nếu được phép. Tránh ghi thông tin mật của công ty.
- Viết mô tả theo công thức: *vấn đề → giải pháp / công nghệ → kết quả có số liệu* (ví dụ "Deployed on 20+ robots").
- Trang Home hiện các project có `featured: true` (tối đa theo `home.projects` trong `profile.yml`); nếu không có project nào `featured` thì lấy các project đầu tiên.
- Thứ tự project trong trang = thứ tự trong file → đặt project mạnh nhất lên đầu mỗi nhóm.
- **Project / cuộc thi đang thực hiện:** vẫn nên ghi, kèm trạng thái rõ ràng — `period: 2026 – Ongoing`, thêm *In progress* trong mô tả. **Chưa** đưa vào CV → Achievements cho tới khi có kết quả; khi có giải thì thêm vào Achievements và cập nhật mô tả.

---

## 6. Publications — `publications.yml`

```yaml
- title: Robust Visual-Inertial Odometry for Low-Texture Environments
  authors: Nhat Tran, Q. H. Pham, Supervisor Name
  venue: IEEE Robotics and Automation Letters (RA-L)
  year: 2025                     # số, dùng để sắp xếp (mới nhất lên đầu)
  type: Journal                  # nhóm lọc: Conference / Journal / Preprint / Workshop / Thesis...
  note: Oral                     # nhãn vàng nhỏ (tuỳ chọn): Oral, Best Paper, Spotlight...
  tags: [SLAM, VIO]
  pdf: /assets/files/papers/tran2025.pdf   # hoặc link ngoài
  doi: 10.1109/LRA.2025.1234567  # chỉ ghi mã DOI, web tự tạo link
  code: https://github.com/...
  slides: https://...
  project: /projects/            # link tới trang project (tuỳ chọn)
  bibtex: |
    @article{tran2025robust,
      title  = {...},
      author = {Tran, Nhat and ...},
      year   = {2025}
    }
```
- Tên bạn trong `authors` phải viết **giống hệt** một tên trong `publication_names` (profile.yml) để được in đậm.
- `type` mới → tự thêm mục lọc ở cột trái.
- Trang Home hiện 3 bài mới nhất.

---

## 7. Notes — viết bài chia sẻ kiến thức

### 7.1. Tạo bài mới
1. Mở file mẫu `_templates/new-note.md`, copy toàn bộ nội dung.
2. Vào thư mục `_posts/` → **Add file → Create new file**.
3. Đặt tên file đúng dạng: **`YYYY-MM-DD-ten-bai-khong-dau.md`**
   ví dụ `2026-10-01-pid-controller.md` (ngày trong tên = ngày đăng bài).
4. Dán nội dung mẫu, sửa phần đầu (front matter) và viết bài → **Commit**.

### 7.2. Phần đầu bài (front matter)
```yaml
---
title: "PID Controller — From Theory to Code"
category: Autonomy              # 1 chủ đề → tạo mục lọc ở cột trái trang Notes
                                # gợi ý: Embedded & Hardware / Perception & AI / Autonomy / Tools & Tips / Research
tags: [PID, Control, Python]
description: "Một câu tóm tắt, hiện trên thẻ bài viết và khi chia sẻ link."
image: /assets/img/notes/pid.jpg   # ảnh bìa 16:9 (tuỳ chọn; bỏ → bìa màu mặc định)
math: true                      # bật nếu bài có công thức toán
---
```
Đặt `<!--more-->` sau đoạn mở đầu: phần phía trên dùng làm tóm tắt nếu không có `description`.

### 7.3. Cú pháp Markdown hay dùng
| Muốn | Viết |
|---|---|
| Tiêu đề mục | `## Tiêu đề` , `### Tiêu đề nhỏ` |
| In đậm / nghiêng | `**đậm**` , `*nghiêng*` |
| Link | `[chữ hiển thị](https://...)` |
| Ảnh | `![mô tả](/assets/img/notes/ten-anh.png)` |
| Danh sách | `- mục` hoặc `1. mục` |
| Trích dẫn / ghi chú | `> Ghi chú quan trọng` |
| Code trong dòng | `` `ros2 topic list` `` |
| Khối code (tự tô màu) | ```` ```python ```` … ```` ``` ```` (đổi `python` thành `cpp`, `bash`, `yaml`…) |
| Bảng | `\| Cột 1 \| Cột 2 \|` + dòng `\|---\|---\|` |
| Công thức trong dòng (cần `math: true`) | `$E = mc^2$` |
| Công thức riêng dòng | `$$ x_k = F x_{k-1} + w_k $$` |
| Đường kẻ ngang | `---` |

### 7.4. Sửa / ẩn / xoá bài
- **Sửa:** mở file trong `_posts/`, bấm ✏️.
- **Ẩn tạm (nháp):** thêm `published: false` vào phần đầu bài.
- **Xoá:** mở file → menu `…` → **Delete file**.
- **Đổi ngày đăng:** đổi ngày trong tên file.

Bài mới tự xuất hiện ở trang **Notes**, trên **Home** (3 bài mới nhất), trong ô **tìm kiếm**, và có nút **Previous / Next** giữa các bài.

---

## 8. Ảnh và file

| Loại | Thư mục | Kích thước gợi ý | Khai báo ở |
|---|---|---|---|
| Ảnh đại diện | `assets/img/` | dọc 4:5, rộng ~600px | `profile.yml → avatar` |
| Ảnh banner | `assets/img/` | ngang, rộng 1600–2000px | `profile.yml → hero.background` |
| Ảnh project | `assets/img/projects/` | 16:9, rộng ~1000px | `projects.yml → image` |
| Ảnh bìa / ảnh trong bài | `assets/img/notes/` | 16:9, rộng ~1000px | `image:` trong bài / `![](...)` |
| CV PDF | `assets/files/cv.pdf` | — | `cv.yml → pdf` (tự tạo nếu `pdf_auto: true`, xem mục 4.1b) |
| PDF bài báo | `assets/files/papers/` | — | `publications.yml → pdf` |
| Icon trên tab trình duyệt (favicon) | `assets/icons/` + `favicon.ico` ở thư mục gốc | vuông; bộ 32px, 180px, 192px, 512px | tự động (xem ghi chú bên dưới) |

**Lưu ý:**
- Ảnh chụp điện thoại thường 3–5 MB → **thu nhỏ trước** bằng https://squoosh.app (chọn WebP hoặc JPG, chất lượng ~75). Mỗi ảnh nên **< 300 KB** để web tải nhanh.
- Tên file **không dấu, không khoảng trắng**: `robot-arm.jpg` ✅ — `Ảnh robot 1.JPG` ❌.
- Đường dẫn phân biệt chữ hoa/thường: `photo.JPG` ≠ `photo.jpg`.
- Upload: vào thư mục → **Add file → Upload files**. Muốn thay ảnh cũ: upload file **trùng tên** để ghi đè.
- **Đổi favicon:** tạo ảnh vuông, xuất các cỡ (dùng https://realfavicongenerator.net cho nhanh), rồi upload **đè đúng tên**: `assets/icons/favicon-32.png`, `assets/icons/apple-touch-icon.png` (180px), `assets/icons/icon-192.png`, `assets/icons/icon-512.png` và `favicon.ico` (thư mục gốc). Trình duyệt lưu favicon rất lâu → mở tab ẩn danh để thấy icon mới.

---

## 9. Menu, tiêu đề web, màu sắc

**Menu** — `_data/navigation.yml`: xoá dòng để ẩn trang khỏi menu, đổi thứ tự để đổi vị trí.
```yaml
- title: Projects
  url: /projects/
```

**Tiêu đề & mô tả trên Google** — `_config.yml`: sửa `title` và `description`.

**Màu chủ đạo** — `assets/css/style.css`, dòng `--primary: #1f5fd6;` ở đầu file. Ví dụ:
`#0f766e` (xanh ngọc), `#7c3aed` (tím), `#b91c1c` (đỏ đô), `#0f172a` (đen xám).

---

## 10. Quy tắc viết file YAML (tránh lỗi)

- Thụt lề bằng **dấu cách**, **không dùng Tab**. Giữ đúng số dấu cách như dòng mẫu phía trên.
- Mỗi mục trong danh sách bắt đầu bằng `- ` (gạch ngang + dấu cách).
- Đặt nội dung trong **ngoặc kép** nếu có dấu `:` , `#` , hoặc bắt đầu bằng `*` , `[` , `{` , `@` , `"`:
  `title: "Thesis: Visual SLAM"` , `period: "2023"` , `- "**GPA:** 3.8"`.
- Dòng bắt đầu bằng `#` là ghi chú, không hiển thị.
- Danh sách ngắn viết một dòng: `tags: [ROS 2, C++, Python]`.
- Muốn tạm ẩn một mục: thêm `# ` vào đầu các dòng của mục đó.

---

## 11. Xử lý sự cố

| Hiện tượng | Cách xử lý |
|---|---|
| Sửa xong web không đổi | Đợi 2 phút → **Ctrl + F5**. Vẫn không đổi → xem tab **Actions**. |
| Actions báo ❌ đỏ | Bấm vào lần chạy lỗi → đọc dòng báo lỗi (thường ghi tên file + số dòng). Hay gặp nhất: sai thụt lề YAML, thiếu ngoặc kép khi có dấu `:`. |
| Ảnh không hiện | Kiểm tra đường dẫn bắt đầu bằng `/assets/...`, đúng tên file, đúng chữ hoa/thường. |
| Bài viết không hiện | Tên file phải đúng dạng `YYYY-MM-DD-ten.md`, nằm trong `_posts/`, có phần `---` ở đầu; ngày không được ở tương lai. |
| Công thức toán không hiển thị | Thêm `math: true` vào phần đầu bài. |
| Tên mình không in đậm trong Publications | Tên trong `authors` phải khớp chính xác với `publication_names`. |
| Máy tính không vào được web nhưng 4G vào được | Do mạng / DNS: đổi DNS sang `8.8.8.8` hoặc `1.1.1.1`, khởi động lại router. |

---

## 12. Tính năng có sẵn
- 🌗 Giao diện sáng / tối (nút ☀/🌙), tự nhớ lựa chọn.
- 🔍 Tìm kiếm toàn trang (nút kính lúp hoặc phím `/`): tìm trong bài viết, project, bài báo.
- 🗂 Project chia nhóm Professional / Personal (có thể bật lọc theo lĩnh vực); lọc bài báo theo loại; lọc bài viết theo chủ đề + ô tìm kiếm.
- 📱 Hiển thị tốt trên điện thoại (menu thu gọn).
- 🔗 Link thẳng tới từng mục: `/cv/#experience`, `/projects/#personal`.
- 📰 RSS feed tự động: `/feed.xml`.
- ⚡ Nhẹ (~120 KB/trang), font nhúng sẵn, không phụ thuộc dịch vụ ngoài (trừ MathJax khi bài có công thức).

---

## 13. Chạy thử trên máy (tuỳ chọn)
Cần cài Ruby. Sau đó:
```bash
bundle install
bundle exec jekyll serve
# mở http://localhost:4000 — sửa file là trang tự cập nhật (riêng _config.yml phải chạy lại)
```

---

## 14. Cấu trúc thư mục
```
├── _config.yml            # cấu hình chung (tiêu đề web, URL)
├── _data/                 # ★ NỘI DUNG — sửa ở đây
│   ├── profile.yml        #   thông tin cá nhân, Home, About
│   ├── cv.yml             #   CV
│   ├── projects.yml       #   project
│   ├── publications.yml   #   bài báo
│   └── navigation.yml     #   menu
├── _posts/                # ★ BÀI VIẾT — thêm file .md ở đây
├── _templates/            #   file mẫu bài viết (không hiển thị lên web)
├── assets/
│   ├── img/               # ★ ẢNH
│   ├── files/             # ★ CV PDF, PDF bài báo
│   ├── css/ js/ fonts/    #   giao diện (không cần sửa)
├── _layouts/ _includes/   #   khung giao diện (không cần sửa)
└── index.html, about.html, cv.html, projects.html, publications.html, notes.html
                           #   các trang (không cần sửa)
```

---

## 15. Căn chữ tự động (không cần làm gì)
- Mọi **đoạn văn** và **gạch đầu dòng** trong nội dung (About, CV, Projects, Publications, Notes, trang mới…) tự **căn đều hai bên**, có ngắt từ tự động để tránh khoảng trắng lớn. Dòng cuối mỗi đoạn căn trái như sách.
- Tiêu đề tự cân độ dài giữa các dòng; tiêu đề thẻ project / bài viết luôn chiếm 2 dòng để các thẻ thẳng hàng.
- 4 ô dưới banner luôn đúng 2 dòng (viết khoảng 45–60 ký tự).
- Ô quá hẹp, nhãn, nút, danh sách liên hệ giữ căn trái; trên điện thoại nhỏ (< 420px) mọi chữ căn trái để dễ đọc.
- Quy tắc nằm ở cuối `assets/css/style.css` (mục *TEMPLATE RULE*) — chỉ cần sửa nếu muốn đổi cách căn.

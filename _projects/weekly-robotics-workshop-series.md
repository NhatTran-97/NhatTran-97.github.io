---
title: "Weekly Robotics Workshop Series"
summary: >-
  Organize and teach weekly hands-on workshops for students on robotics,
  ROS 2, drones and embedded systems.
category: Teaching & Mentoring
role: "Organizer & Instructor"
period: "Jan 2025 – Present"
partners: "EIU FabLab"
status: "Ongoing"
image: /assets/img/projects/workshops/group.jpg
image_caption: Students and robots after a workshop session at the EIU FabLab.
tags: [STM32, Embedded, ROS 2, F1TENTH, Drones, Robotics]
links:
  - name: STM32 lectures
    url: https://www.youtube.com/playlist?list=PL7WgDt1mGvJbiDx9pCaR9wdrvd8Q96xws
    icon: youtube
  - name: F1TENTH lectures
    url: https://www.youtube.com/playlist?list=PL7WgDt1mGvJZLL-rJHcqOzMGDUf34dQ-F
    icon: youtube
---

## Overview

Since January 2025, I have been running a weekly workshop series at the EIU FabLab
for students who want to get hands-on with robotics. The series is split into
**workshops**, each a multi-session track built around one small robot or platform.
Students start from the fundamentals and finish by making that robot work themselves.

Topics so far include embedded programming on STM32, ROS 2, the F1TENTH autonomous
racing platform and drones. Recordings of the lectures are shared on YouTube so
students can review them at their own pace.

## My role

I organize the series. I prepare the lecture content and hands-on exercises, teach
the sessions, and help students debug their code and robots during the labs.

## Workshops

Select a workshop to see its goal, learning path and lecture recordings.

<div class="workshop-cards" data-workshop-cards></div>

<section class="workshop-panel" id="stm32-self-balancing-robot" markdown="1">

### Workshop 1 — STM32 And Two-Wheeled Self-Balancing Robot

<div class="workshop">
  <figure class="workshop-cover">
    <img src="/assets/img/projects/workshops/stm32-balancing-robot.png" alt="Two-wheeled self-balancing robot with an STM32 controller board">
  </figure>
  <div class="workshop-info">
    <span class="workshop-no">Workshop 01 · Embedded systems & control</span>
    <p><strong>Goal:</strong> program a two-wheeled self-balancing robot from scratch —
    from blinking an LED on the STM32 to keeping the robot upright with an
    IMU-based attitude estimator and an LQR controller.</p>
    <div class="chips">
      <span class="chip">C</span><span class="chip">STM32</span><span class="chip">IMU</span>
      <span class="chip">EKF</span><span class="chip">LQR</span>
    </div>
    <p><a class="btn btn-primary" href="https://www.youtube.com/playlist?list=PL7WgDt1mGvJbiDx9pCaR9wdrvd8Q96xws">{% include icon.html name="youtube" %} Watch the lectures</a></p>
  </div>
</div>

#### Robot platform

The workshop is built around a small two-wheeled self-balancing robot with a custom
STM32 controller board, so every module can be tried directly on real hardware.

<figure class="figure-narrow">
  <img src="/assets/img/projects/workshops/stm32-robot-platform.png" alt="Overview of the self-balancing robot: mechanical design, sensing and actuation, electronics and firmware, technical specifications">
  <figcaption>The robot platform: 3D-printed frame, IMU and encoder motors, STM32L476 board with an ESP32-C3 co-processor.</figcaption>
</figure>

#### Learning path

<ol class="module-list">
  <li>
    <div>
      <strong>C programming</strong>
      <p>The C fundamentals used throughout the workshop.</p>
    </div>
  </li>
  <li>
    <div>
      <strong>STM32 peripherals</strong>
      <p>Configure and use the microcontroller peripherals that drive the robot's sensors and motors.</p>
      <div class="chips">
        <span class="chip">GPIOs</span><span class="chip">External Interrupt</span>
        <span class="chip">Timers</span><span class="chip">Timer Interrupt</span>
        <span class="chip">PWM</span><span class="chip">ADC</span>
        <span class="chip">SPI</span><span class="chip">DMA</span><span class="chip">UART</span>
      </div>
    </div>
  </li>
  <li>
    <div>
      <strong>IMU calibration</strong>
      <p>Calibrate the IMU before its data is used for estimation.</p>
    </div>
  </li>
  <li>
    <div>
      <strong>From IMU data to rotation</strong>
      <p>Represent the robot's orientation and compute it from each sensor.</p>
      <div class="chips">
        <span class="chip">Euler angles & rotation matrices</span>
        <span class="chip">Accelerometer & magnetometer → XYZ</span>
        <span class="chip">Gyroscope → Euler angles</span>
        <span class="chip">Quaternions</span>
      </div>
    </div>
  </li>
  <li>
    <div>
      <strong>Attitude estimation with an EKF</strong>
      <p>Fuse the sensor data with an Extended Kalman Filter to estimate the robot's attitude.</p>
    </div>
  </li>
  <li>
    <div>
      <strong>LQR control</strong>
      <p>Design a Linear–Quadratic Regulator that keeps the robot balanced.</p>
    </div>
  </li>
  <li class="module-goal">
    <div>
      <strong>Final goal: a self-balancing robot</strong>
      <p>Put everything together and program the two-wheeled self-balancing robot.</p>
    </div>
  </li>
</ol>

#### In class

<div class="gallery">
  <figure><img src="/assets/img/projects/workshops/teaching.jpg" alt="Demonstrating the self-balancing robot to students"><figcaption>Demonstrating the self-balancing robot to students.</figcaption></figure>
  <figure><img src="/assets/img/projects/workshops/stm32-class.jpg" alt="Students programming in C during a workshop session"><figcaption>A C programming session at the EIU FabLab.</figcaption></figure>
</div>

</section>

<section class="workshop-panel" id="f1tenth-autonomous-racing" markdown="1">

### Workshop 2 — F1TENTH Autonomous Racing

<div class="workshop">
  <figure class="workshop-cover is-photo">
    <img src="/assets/img/projects/workshops/f1tenth-cover.jpg" alt="F1TENTH session on Ackermann control of the vehicle">
  </figure>
  <div class="workshop-info">
    <span class="workshop-no">Workshop 02 · ROS 2 & autonomous driving</span>
    <p><strong>Goal:</strong> build the autonomy stack of a 1/10-scale F1TENTH car step by
    step — from Linux, Python and ROS 2 basics to mapping, localization, path tracking
    and obstacle avoidance.</p>
    <div class="chips">
      <span class="chip">Ubuntu</span><span class="chip">Python</span><span class="chip">ROS 2</span>
      <span class="chip">SLAM Toolbox</span><span class="chip">AMCL</span>
      <span class="chip">Pure Pursuit</span><span class="chip">RRT*</span>
    </div>
    <p><a class="btn btn-primary" href="https://www.youtube.com/playlist?list=PL7WgDt1mGvJZLL-rJHcqOzMGDUf34dQ-F">{% include icon.html name="youtube" %} Watch the lectures</a></p>
  </div>
</div>

#### Learning path

<ol class="module-list">
  <li>
    <div>
      <strong>Ubuntu basics</strong>
      <p>Working with Linux and the terminal — the environment used for the rest of the workshop.</p>
    </div>
  </li>
  <li>
    <div>
      <strong>Python & OOP</strong>
      <p>Python and object-oriented programming for writing ROS 2 nodes.</p>
    </div>
  </li>
  <li>
    <div>
      <strong>Math review</strong>
      <p>The math behind the algorithms in the later modules.</p>
      <div class="chips">
        <span class="chip">Calculus</span><span class="chip">Linear Algebra</span>
        <span class="chip">Statistics & Probability</span>
      </div>
    </div>
  </li>
  <li>
    <div>
      <strong>ROS 2 basics</strong>
      <p>Core ROS 2 concepts and tools.</p>
      <div class="chips">
        <span class="chip">Workspace</span><span class="chip">Package</span>
        <span class="chip">Node</span><span class="chip">Topic</span>
        <span class="chip">Service</span><span class="chip">Launch file</span>
        <span class="chip">Parameters</span><span class="chip">Multithreading</span>
        <span class="chip">Debugging tools</span><span class="chip">Transforms (TF2)</span>
      </div>
    </div>
  </li>
  <li>
    <div>
      <strong>Automatic Emergency Braking (AEB)</strong>
      <p>Stop the car before it hits an obstacle.</p>
    </div>
  </li>
  <li>
    <div>
      <strong>Wall following with PID</strong>
      <p>Keep the car at a set distance from the wall with a PID controller.</p>
    </div>
  </li>
  <li>
    <div>
      <strong>2D mapping with SLAM Toolbox</strong>
      <p>Build a 2D map of the track.</p>
    </div>
  </li>
  <li>
    <div>
      <strong>Localization with AMCL</strong>
      <p>Localize the car in the 2D map.</p>
    </div>
  </li>
  <li>
    <div>
      <strong>Waypoints & Pure Pursuit</strong>
      <p>Create waypoints and track them with the Pure Pursuit algorithm.</p>
    </div>
  </li>
  <li>
    <div>
      <strong>Obstacle avoidance with RRT & RRT*</strong>
      <p>Plan paths around obstacles with sampling-based planners.</p>
    </div>
  </li>
  <li class="module-goal">
    <div>
      <strong>Final goal: an autonomous F1TENTH car</strong>
      <p>Put mapping, localization, path tracking and obstacle avoidance together on the car.</p>
    </div>
  </li>
</ol>

<div class="gallery">
  <figure><img src="/assets/img/projects/workshops/f1tenth-session-1.jpg" alt="Students working with the F1TENTH car during a session"><figcaption>F1TENTH class: Ackermann control on the vehicle.</figcaption></figure>
  <figure><img src="/assets/img/projects/workshops/f1tenth-session-2.jpg" alt="Students working with ROS 2 topics on their laptops"><figcaption>F1TENTH class: working with ROS 2 topics and messages (odometry).</figcaption></figure>
</div>

</section>

<!-- ================================================================
  THÊM WORKSHOP MỚI (thẻ nhỏ ở đầu mục Workshops được tạo TỰ ĐỘNG từ các khối này):
  copy nguyên khối từ <section class="workshop-panel" ...> của Workshop 2 đến hết </section> ở trên,
  dán vào ngay dưới đây (trước "### More workshops") rồi sửa:
    - id="..." của <section>: mã không dấu, không trùng (vd. drone-basics) — dùng làm link
      mở thẳng workshop đó: /projects/weekly-robotics-workshop-series/#drone-basics
    - "### Workshop 3 — Tên workshop"  (tên sau dấu "—" là tên hiện trên thẻ)
    - ảnh bìa trong assets/img/projects/workshops/ (ảnh này cũng là ảnh của thẻ):
        ảnh PNG nền trong suốt → <figure class="workshop-cover">            (như Workshop 1)
        ảnh chụp thường        → <figure class="workshop-cover is-photo">   (như Workshop 2)
    - dòng "Workshop 02 · Chủ đề", mục tiêu (Goal), các chip, link playlist
    - các bước trong <ol class="module-list"> (mỗi bước là một <li>;
      bước cuối có class="module-goal" sẽ hiện ngôi sao)
================================================================ -->

### More workshops

*Write-ups for the other topics (e.g. drones) are coming soon.*

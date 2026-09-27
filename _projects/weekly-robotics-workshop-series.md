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
tags: [STM32, Embedded, ROS 2, Drones, Robotics]
links:
  - name: Lecture recordings
    url: https://www.youtube.com/playlist?list=PL7WgDt1mGvJbiDx9pCaR9wdrvd8Q96xws
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

<figure>
  <img src="/assets/img/projects/workshops/teaching.jpg" alt="Demonstrating the self-balancing robot to students">
  <figcaption>Demonstrating the self-balancing robot to students during a session.</figcaption>
</figure>

<!-- ================================================================
  THÊM WORKSHOP MỚI: copy nguyên khối từ "### Workshop 1 — ..." đến hết <figure> ở trên,
  dán vào đây rồi sửa:
    - "### Workshop 2 — Tên workshop"
    - ảnh bìa (ảnh PNG nền trong suốt hoặc ảnh vuông) trong assets/img/projects/workshops/
    - dòng "Workshop 02 · Chủ đề", mục tiêu (Goal), các chip, link playlist
    - các bước trong <ol class="module-list"> (mỗi bước là một <li>;
      bước cuối có class="module-goal" sẽ hiện ngôi sao)
================================================================ -->

### More workshops

*Write-ups for the other topics (ROS 2, F1TENTH, drones) are coming soon.*

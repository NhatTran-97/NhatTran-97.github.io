---
title: "Feedforward-Assisted PI Speed Control for Geared DC Motors"
summary: >-
  Data-driven feedforward plus PI speed control, with automatic position holding,
  for small geared DC motors — a student research paper under review at the
  EIUSC International Conference 2026.
category: Embedded & Hardware
role: "Research mentor & co-author"
period: "2026"
partners: "EIU FabLab student team"
status: "Under review (EIUSC 2026)"
image: /assets/img/projects/dc-motor/banner.jpg
image_ratio: "16 / 9"
image_caption: Control architecture and speed-tracking tests on the robot platform.
tags: [Motor Control, PI Control, Feedforward, STM32, Embedded]
links:
  - name: Demo video
    url: https://www.youtube.com/watch?v=8gYRO59CVcA&t=220s
    icon: youtube
  - name: Paper
    url: /publications/
    icon: file-text
---

## Overview

Small geared DC motors such as the N20 are cheap and common in student robots, but
they are hard to control smoothly at low speed: friction and breakaway torque make the
motor stall or jump, and the low-resolution encoders give noisy speed feedback. A plain
PI loop either reacts too slowly or oscillates.

This student project studies a simple, practical fix: a **data-driven feedforward**
term that supplies most of the PWM needed for a given speed — including the extra push
to break away from rest — while a **PI velocity loop** only corrects the remaining error.
A small **state machine** adds automatic **position holding**, so the wheel stays in place
when no speed is commanded.

Paper (under review): *"Data-Driven Feedforward-Assisted PI Speed Control with Automatic
Position Holding for Geared DC Motors"* — Hoang Anh Nguyen Trong, Thuy Dao Le Ngoc,
Toan Pham Dang Huu, Uyen Vo Pham Mai, Duy Nhat Tran.

## My role

I mentored the student team through the project and the writing of the paper, and I am
a co-author. The experiments run on the FabLab's STM32 self-balancing robot platform,
the same robot used in our [weekly workshop](/projects/weekly-robotics-workshop-series/#stm32-self-balancing-robot).

## Control architecture

<div class="feature-grid cols-3">
  <div><strong>HOLD — position hold</strong><p>With no speed command, a position loop keeps the wheel at the hold position: speed_ref = K<sub>p,pos</sub>(θ<sub>hold</sub> − θ), limited to ±hold_speed_max.</p></div>
  <div><strong>VELOCITY — run</strong><p>When |ω<sub>cmd</sub>| exceeds a threshold, a motion profile ramps the speed reference up and down with limited acceleration.</p></div>
  <div><strong>STOPPING — decelerate</strong><p>The profile brings the speed to zero; once the measured speed stays below a threshold for several samples, the hold position is updated and the motor returns to HOLD.</p></div>
  <div><strong>Feedforward</strong><p>A static + breakaway PWM term, identified from measured data, gives most of the drive signal for the requested speed.</p></div>
  <div><strong>PI velocity loop</strong><p>Corrects the remaining speed error; the total PWM is saturated to ±100% before the motor driver.</p></div>
  <div><strong>Feedback</strong><p>Hall encoders on the motor shaft (7 PPR) give position and velocity; the control loop runs at 200 Hz on the STM32.</p></div>
</div>

## Hardware platform

<figure class="figure-narrow figure-large">
  <img src="/assets/img/projects/workshops/stm32-robot-platform.jpg" alt="Overview of the robot platform: mechanical design, sensing and actuation, electronics and firmware, technical specifications">
  <figcaption>Test platform: two N20 gear motors with Hall encoders, STM32L476 controller board, ESP32-C3 telemetry to a TCP dashboard.</figcaption>
</figure>

## Results

The controller was tested with step speed commands from **0.5 rad/s** up to **5.0 rad/s**
(see the plots in the banner above and the demo video). Detailed results will be added
here once the paper is published.

<ul class="video-list">
  <li><a href="https://www.youtube.com/watch?v=8gYRO59CVcA&t=220s">{% include icon.html name="youtube" %}<span>Demo video<small>Speed control and position holding on the robot</small></span></a></li>
</ul>

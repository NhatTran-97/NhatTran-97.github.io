---
title: VDA5050 Support for Open-RMF
summary: >-
  A ROS 2 Jazzy implementation of the VDA5050 v2.1.0 protocol that lets Open-RMF
  command a mixed fleet — a custom FabLab AMR and TurtleBot3 robots — over MQTT.
category: Autonomy
role: Technical Lead
period: Jun 2026 – Nov 2026
partners: EIU FabLab × ARTC (Singapore)
status: In progress
image: /assets/img/projects/vda5050/robots.jpg
image_caption: The FabLab AMR carrying two TurtleBot3 robots used in the fleet demos.
tags: [ROS 2 Jazzy, Open-RMF, VDA5050 v2.1, MQTT, Nav2, Docker, C++, Python, PySide6 / QML]
links:
  - name: GitHub repository
    url: https://github.com/NhatTran-97/eiu-vda5050-support-open-rmf
    icon: github
  - name: Demo videos
    url: https://www.youtube.com/playlist?list=PL7WgDt1mGvJZdPyar7xpHH4HDRZpteAp4
    icon: youtube
---

## Overview

**VDA5050** is an open interface standard for communication between AGVs/AMRs and a
master control, developed by the German associations VDA and VDMA.
**Open-RMF** is an open-source framework for managing fleets of robots from different
vendors. This joint project between the **EIU FabLab** and **ARTC (Singapore)** connects
the two: Open-RMF plans and schedules the fleet, and every robot is driven through
VDA5050 v2.1.0 messages over MQTT.

The ground station runs Open-RMF core, the fleet adapter and the operator dashboard
together in one Docker container. Each robot runs its own VDA5050 client adapter and
Nav2 navigation stack, and only the MQTT broker crosses between the two sides.

## My role

As **Technical Lead** on the EIU side, I led the design and implementation of the
system — the fleet adapters, the robot-side client adapter and Nav2 bridge, and the
fleet dashboard — and prepared the milestone demos on real robots and in simulation.

## System architecture

<div class="arch">
  <div class="arch-col">
    <strong>Ground station · one Docker container</strong>
    <div class="arch-box">eiu_fleet_ui<small>PySide6 + QML dashboard</small></div>
    <div class="arch-box">Open-RMF<small>traffic schedule + task dispatcher</small></div>
    <div class="arch-box">vda5050_fleet_adapter_full_control<small>one process per robot type</small></div>
    <div class="arch-box">Mosquitto<small>MQTT broker</small></div>
  </div>
  <div class="arch-link"><span>⇄</span>VDA5050 v2.1 JSON<br>over MQTT</div>
  <div class="arch-col">
    <strong>Each robot · AMR / TurtleBot3</strong>
    <div class="arch-box">vda5050_client_adapter<small>MQTT ⇄ ROS 2 vda5050_msgs</small></div>
    <div class="arch-box">tb3_vda5050_bridge<small>order steps → Nav2 goals, telemetry back</small></div>
    <div class="arch-box">Nav2<small>planning, control, localization</small></div>
  </div>
</div>

The robot side exposes two interfaces: **northbound**, the six VDA5050 MQTT topics
(`order`, `instantActions`, `state`, `visualization`, `connection`, `factsheet`), and
**southbound**, ROS 2 topics (`vda5050_msgs`) between the client adapter and the robot
driver. Because the robot side speaks plain VDA5050, a master control other than
Open-RMF can drive it unchanged.

## Key features

<div class="feature-grid">
  <div><strong>Routes as VDA5050 orders</strong><p>A planned multi-waypoint route from RMF is sent as one order; nodes can be released step by step and replans are stitched into the same order.</p></div>
  <div><strong>Traffic hold</strong><p>When RMF asks a robot to stop, the AGV is paused and keeps its order, then resumes when the new route arrives.</p></div>
  <div><strong>Multi-robot, multi-fleet</strong><p>One adapter process per fleet, many robots per fleet; the AMR and TurtleBot3 fleets run together and deconflict through RMF.</p></div>
  <div><strong>Runtime registration</strong><p>A robot found on the broker can be checked, added, removed or restored into a running fleet.</p></div>
  <div><strong>Operator controls</strong><p>Pause, resume, speed limit and re-localization per robot; lane closures and no-go zones per fleet.</p></div>
  <div><strong>VDA5050 master behavior</strong><p>Resends unconfirmed orders, reads the AGV factsheet, validates orders before sending, and was tested with a third-party VDA5050 client.</p></div>
</div>

## Fleet dashboard

<figure>
  <img src="/assets/img/projects/vda5050/dashboard.jpg" alt="EIU Fleet Command Center dashboard">
  <figcaption>EIU Fleet Command Center — live map, robot status, VDA5050 orders and message traffic.</figcaption>
</figure>

The dashboard (`eiu_fleet_ui`) monitors system health, robots, traffic and tasks;
dispatches and cancels patrol and delivery tasks; gives per-robot control; draws no-go
zones; edits the nav graph; and shows each robot's live VDA5050 order and message log.

## Robots

<figure>
  <img src="/assets/img/projects/vda5050/amr-hardware.jpg" alt="AMR hardware overview">
  <figcaption>The custom FabLab AMR: sensing, computing, communication and actuation.</figcaption>
</figure>

| | FabLab AMR | TurtleBot3 Burger |
|---|---|---|
| Kinematics | Differential drive | Differential drive |
| Size | 0.6 m × 0.4 m | 138 × 178 × 192 mm |
| Max speed | 0.30 m/s · 0.60 rad/s | 0.22 m/s |
| Compute | SOM-RK3399 (2× Cortex-A72 + 4× Cortex-A53) | SOM-RK3399v2 |
| Sensors | LR-1BS 2D LiDAR (270°), Orbbec DaBai Pro depth camera, BNO055 IMU | 2D LiDAR |
| Navigation | Nav2: Theta* planner → Simple Smoother → MPPI controller | Nav2 |
| RMF fleet | `amr_fleet` (1 robot) | `tb3_fleet` (2 robots) |

<figure>
  <img src="/assets/img/projects/vda5050/amr-software.jpg" alt="AMR software architecture">
  <figcaption>AMR navigation software stack.</figcaption>
</figure>

## Packages

| Package | Layer | Role |
|---|---|---|
| `eiu_fleet_ui` | Dashboard | PySide6/QML operator dashboard, can follow several fleet adapters at once |
| `vda5050_fleet_adapter_full_control` | Fleet adapter | Open-RMF full-control adapter; sends a planned route as one VDA5050 order |
| `vda5050_fleet_adapter` | Fleet adapter | EasyFullControl variant; one VDA5050 order per destination |
| `fleet_bringup` | Ground station | One launch file for RMF core, the adapter, mock workcells and the dashboard |
| `vda5050_client_adapter` | Robot | VDA5050 over MQTT ⇄ ROS 2 `vda5050_msgs`; publishes state and connection |
| `tb3_vda5050_bridge` | Robot | Turns order steps into Nav2 `NavigateToPose` goals; reports odometry, battery and progress |
| `tb3_simulation` | Simulation | TurtleBot3 + Nav2 in Gazebo Harmonic, world generated from the traffic editor |
| `vda5050_msgs` | Shared | ROS 2 message definitions shared by the robot-side nodes |

## Simulation

<figure>
  <img src="/assets/img/projects/vda5050/simulation.jpg" alt="Gazebo simulation of the VDA5050 fleet">
  <figcaption>The same integration running in Gazebo with the fleet dashboard and RViz.</figcaption>
</figure>

## Demo videos

<ul class="video-list">
  <li><a href="https://www.youtube.com/watch?v=w_28pgbwSe8"><svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.5 15.6V8.4l6.3 3.6-6.3 3.6z"/></svg><span>3 robots — AMR + TurtleBot3 fleets<small>Both fleets running together on real robots</small></span></a></li>
  <li><a href="https://www.youtube.com/watch?v=ODSLt2Ox0S8"><svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.5 15.6V8.4l6.3 3.6-6.3 3.6z"/></svg><span>2 × TurtleBot3<small>Multi-robot deconfliction through RMF</small></span></a></li>
  <li><a href="https://www.youtube.com/watch?v=6eLXi1PXubU&t=290s"><svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.5 15.6V8.4l6.3 3.6-6.3 3.6z"/></svg><span>AMR fleet<small>Single-robot demo on the FabLab AMR</small></span></a></li>
  <li><a href="https://www.youtube.com/watch?v=yxOD5KHLECk"><svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.5 15.6V8.4l6.3 3.6-6.3 3.6z"/></svg><span>TurtleBot3 (real robot)<small>Patrol / delivery over VDA5050</small></span></a></li>
  <li><a href="https://www.youtube.com/watch?v=vPeb_fctu0k"><svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.5 15.6V8.4l6.3 3.6-6.3 3.6z"/></svg><span>3 robots in Gazebo<small>Multi-fleet simulation</small></span></a></li>
  <li><a href="https://youtu.be/L0Zu4yaiQOU"><svg class="icon" viewBox="0 0 24 24" aria-hidden="true"><path fill="currentColor" d="M23.5 6.2a3 3 0 0 0-2.1-2.1C19.5 3.6 12 3.6 12 3.6s-7.5 0-9.4.5A3 3 0 0 0 .5 6.2 31 31 0 0 0 0 12a31 31 0 0 0 .5 5.8 3 3 0 0 0 2.1 2.1c1.9.5 9.4.5 9.4.5s7.5 0 9.4-.5a3 3 0 0 0 2.1-2.1A31 31 0 0 0 24 12a31 31 0 0 0-.5-5.8zM9.5 15.6V8.4l6.3 3.6-6.3 3.6z"/></svg><span>Third-party VDA5050 client<small>3 virtual AGVs built on vda-5050-lib</small></span></a></li>
</ul>

Full playlist: [YouTube](https://www.youtube.com/playlist?list=PL7WgDt1mGvJZdPyar7xpHH4HDRZpteAp4) ·
Source code and package documentation: [GitHub](https://github.com/NhatTran-97/eiu-vda5050-support-open-rmf)

## Current limitations

- Tested on one building level; lifts and multi-floor map switching are not built yet.
- Charging and pick-and-drop actions are supported in the protocol but tested only with simulated AGVs or mock workcells.
- Tested with a third-party VDA5050 client, not yet with a commercial AGV.

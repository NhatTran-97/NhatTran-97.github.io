---
title: "Kalman Filter — A Practical Cheat Sheet"
category: Autonomy
description: "The linear Kalman filter on one page: system model, predict/update equations, a minimal Python implementation and tuning tips."
tags: [Estimation, Robotics]
math: true
---

A short summary of the linear Kalman filter: the model, the two steps, and the
tuning tips I always forget. <!--more-->

## System model

$$
x_k = F x_{k-1} + B u_k + w_k, \qquad w_k \sim \mathcal{N}(0, Q)
$$

$$
z_k = H x_k + v_k, \qquad v_k \sim \mathcal{N}(0, R)
$$

## 1. Predict

$$
\hat{x}_{k|k-1} = F \hat{x}_{k-1} + B u_k, \qquad
P_{k|k-1} = F P_{k-1} F^\top + Q
$$

## 2. Update

$$
K_k = P_{k|k-1} H^\top \left(H P_{k|k-1} H^\top + R\right)^{-1}
$$

$$
\hat{x}_k = \hat{x}_{k|k-1} + K_k \left(z_k - H \hat{x}_{k|k-1}\right), \qquad
P_k = (I - K_k H) P_{k|k-1}
$$

## Minimal Python implementation

```python
import numpy as np

class KalmanFilter:
    def __init__(self, F, H, Q, R, x0, P0):
        self.F, self.H, self.Q, self.R = F, H, Q, R
        self.x, self.P = x0, P0

    def predict(self):
        self.x = self.F @ self.x
        self.P = self.F @ self.P @ self.F.T + self.Q

    def update(self, z):
        S = self.H @ self.P @ self.H.T + self.R
        K = self.P @ self.H.T @ np.linalg.inv(S)
        self.x = self.x + K @ (z - self.H @ self.x)
        self.P = (np.eye(len(self.x)) - K @ self.H) @ self.P
```

## Tuning tips

| Symptom | Likely cause | Fix |
|---|---|---|
| Estimate lags behind measurements | $Q$ too small | Increase $Q$ |
| Estimate is noisy | $R$ too small | Increase $R$ |
| Filter diverges | Model mismatch / bad $P_0$ | Check $F$, inflate $P_0$ |

> **Takeaway:** the ratio between $Q$ and $R$ matters more than their absolute values.

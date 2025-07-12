"""Các bước để nhập code và lưu trên github: (lưu ý là phải có sẵn github account)
*Access vào code: vào terminal, gõ lệnh:
git clone https://github.com/DoanQuangHung176/Ising-model.git
cd Ising-model
code . (clone 1 lần là đủ, lần sau mở file này từ máy là được)
*Lưu code:
B1: nhớ Ctrl + S để lưu code, nhập git status để kiểm tra xem có thay đổi gì không
Nếu có thay đổi thì sẽ hiện ra các file đã thay đổi.
B2: vào terminal, gõ lệnh:
git add .
git commit -m "viết j vào đây cx đc, chủ yếu m là message để note lại những thay đổi của mình"
git push origin main
"""
import numpy as np
import matplotlib.pyplot as plt
print("Importing ising.py")
Ising = []
print("Ising model simulation started")

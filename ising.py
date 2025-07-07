"""Các bước để nhập code và lưu trên github: (lưu ý là phải có sẵn github account)
*Access vào code: vào terminal, gõ lệnh:
git clone https://github.com/DoanQuangHung176/Ising-model.git
cd Ising-model
code .
*Lưu code:
B1: nhớ Ctrl + S để lưu code, nhập git status để kiểm tra xem có thay đổi gì không
Nếu có thay đổi thì sẽ hiện ra các file đã thay đổi.
B2: vào terminal, gõ lệnh:
git add .
git commit -m "team edits"
git push origin main
"""
import numpy as np
import matplotlib.pyplot as plt
print("Importing ising.py")
Ising = []

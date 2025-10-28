import random
import math
import numpy as np
import matplotlib.pyplot as plt

def random_palette(k=5):
    # return k random pastel-like colors
    return [(random.random(), random.random(), random.random()) for _ in range(k)]

def blob(center=(0.5, 0.5), r=0.3, points=200, wobble=0.15):
    # generate a wobbly closed shape
    angles = np.linspace(0, 2*math.pi, points)
    # np.random.rand(points)-0.5는 [-0.5, 0.5] 범위의 난수를 생성
    radii = r * (1 + wobble*(np.random.rand(points)-0.5))
    x = center[0] + radii * np.cos(angles)
    y = center[1] + radii * np.sin(angles)
    return x, y

random.seed()  # 다른 아트가 생성되도록 시드 설정
plt.figure(figsize=(7,10))
plt.axis('off')

# 배경
plt.gca().set_facecolor((0.98,0.98,0.97))

palette = random_palette(6)

#  변경: 레이어 수 증가 (8 -> 20)
n_layers = 20 

for i in range(n_layers):
    cx, cy = random.random(), random.random()
    #  변경: Blob 크기 범위 축소 (더 작은 Blob들이 많이 겹치도록)
    rr = random.uniform(0.1, 0.35) 
    
    # ➡️변경: wobble 범위 축소 (더 부드러운 모양)
    wobble_val = random.uniform(0.01, 0.1) 
    
    x, y = blob(center=(cx, cy), r=rr, wobble=wobble_val)
    color = random.choice(palette)
    
    #  변경: 투명도 범위 증가 (색상이 더 짙게 겹치도록)
    alpha = random.uniform(0.6, 0.9) 
    
    # Blob 그리기
    plt.fill(x, y, color=color, alpha=alpha, edgecolor=(0,0,0,0)) 

# simple typographic label
plt.text(0.05, 0.95, "Minimal Overlap", fontsize=18, weight='bold', transform=plt.gca().transAxes)
plt.text(0.05, 0.91, "Revised Generative Poster", fontsize=11, transform=plt.gca().transAxes)

plt.xlim(0,1); plt.ylim(0,1)

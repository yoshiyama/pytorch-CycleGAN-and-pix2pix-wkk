import os
import cv2
import numpy as np
import sys

# コマンドライン引数から画像があるフォルダのパスを取得
folder_path = sys.argv[1]

# 各画像の平均色を格納するリスト
average_colors = []

# フォルダ内の全てのファイルとサブフォルダを走査する
for root, dirs, files in os.walk(folder_path):
    for file in files:
        # ファイルが.jpgまたは.pngで終わるものだけを対象とする
        if file.endswith('.jpg') or file.endswith('.png'):
            # ファイルのフルパスを生成する
            file_path = os.path.join(root, file)

            # 画像を読み込む
            image = cv2.imread(file_path)

            # 画像の平均色を計算し、リストに追加する
            average_color_per_row = np.average(image, axis=0)
            average_color = np.average(average_color_per_row, axis=0)
            average_colors.append(average_color)

# 各色チャンネルの分散を計算する
variances = np.var(average_colors, axis=0)

print("Variances for B, G, R channels:", variances)
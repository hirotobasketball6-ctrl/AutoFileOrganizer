# 📁 Auto File Organizer

Pythonで開発したファイル整理デスクトップアプリです。

指定したフォルダ内のファイルを拡張子ごとに自動で分類し、ワンクリックで整理できます。

---

## 📸 スクリーンショット

![Auto File Organizer メイン画面](screenshots/main.png)

---

## ✨ 主な機能

- 📂 フォルダ選択
- 🚀 ワンクリックで整理開始
- 📊 リアルタイム進捗バー
- 📝 時刻付きログ表示
- 📁 拡張子ごとの自動分類
- 📈 カテゴリごとの整理件数表示
- 🔄 同名ファイルの自動リネーム（`photo(1).jpg` のように保存）

---

## 🛠 使用技術

- Python 3
- Tkinter
- pathlib
- shutil
- Git
- GitHub

---

## 📁 整理例

### 整理前

```text
Downloads/
├── cat.jpg
├── dog.png
├── report.pdf
├── movie.mp4
├── music.mp3
```

### 整理後

```text
Downloads/
├── 画像/
│   ├── cat.jpg
│   └── dog.png
├── PDF/
│   └── report.pdf
├── 動画/
│   └── movie.mp4
├── 音楽/
│   └── music.mp3
```

---

## ▶️ 実行方法

```bash
git clone https://github.com/hirotobasketball6-ctrl/AutoFileOrganizer.git

cd AutoFileOrganizer

pip install -r requirements.txt

python main.py
```

---

## 🚀 バージョン履歴

### Version 1.0
- ファイルの自動整理
- GUI作成
- フォルダ選択機能
- ログ表示
- GitHub公開

### Version 2.0
- 同名ファイル自動リネーム
- リアルタイム進捗バー
- 時刻付きログ
- 整理中のボタン無効化

---

## 🚀 今後追加予定

- [ ] リアルタイムでファイル名をログ表示
- [ ] ドラッグ＆ドロップ対応
- [ ] 設定ファイル（最後に選択したフォルダを記憶）
- [ ] ダークモード
- [ ] `.exe`化
- [ ] アプリケーションアイコン追加

---

## 📄 ライセンス

MIT License
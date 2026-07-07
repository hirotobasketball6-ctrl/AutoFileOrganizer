import tkinter as tk
from tkinter import filedialog, messagebox, ttk
from datetime import datetime

from organizer import Organizer

class App:

    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Auto File Organizer")
        self.root.geometry("700x500")
        self.root.resizable(False, False)
        self.organizer = Organizer()
        self.folder_path = tk.StringVar()

        self.create_widgets()

        start_button = tk.Button(
            self.root,
            text="整理開始",
            command=self.start
        )

        start_button.pack(pady=20)

        self.write_log("アプリを起動しました。")

    def create_widgets(self):

        title = tk.Label(
            self.root,
            text="Auto File Organizer",
            font=("Yu Gothic UI", 20, "bold")
        )

        title.pack(pady=20)

        label = tk.Label(
            self.root,
            text="整理したいフォルダ"
        )

        label.pack()

        frame = tk.Frame(self.root)

        frame.pack(pady=10)

        entry = tk.Entry(
            frame,
            textvariable=self.folder_path,
            width=60,
            state="readonly"
        )

        entry.pack(side=tk.LEFT)

        button = tk.Button(
            frame,
            text="参照",
            command=self.select_folder
        )

        button.pack(side=tk.LEFT, padx=10)

        # ProgressBar
        self.progress = ttk.Progressbar(
            self.root,
            orient="horizontal",
            length=500,
            mode="determinate"
        )

        self.progress.pack(pady=10)

        log_label = tk.Label(
            self.root,
            text="ログ"
        )
        log_label.pack()

        self.log_text = tk.Text(
            self.root,
            height=10,
            width=80,
            state="disabled"
        )

        self.log_text.pack(pady=10)

    def select_folder(self):

        folder = filedialog.askdirectory()

        if folder:
            self.folder_path.set(folder)

    def run(self):
        self.root.mainloop()

    def start(self):

        folder = self.folder_path.get()

        if not folder:
            messagebox.showwarning(
                "フォルダ未選択",
                "整理するフォルダを選択してください。"
            )
            return

        self.progress["value"] = 30
        self.root.update()

        result = self.organizer.organize(folder)

        self.progress["value"] = 100
        self.root.update()

        for category, count in result.items():
            self.write_log(f"{category}: {count}件")

        self.write_log("整理が完了しました。")

    def write_log(self, message):
        now = datetime.now().strftime("%H:%M:%S")

        self.log_text.config(state="normal")
        self.log_text.insert(
            tk.END,
            f"[{now}] {message}\n"
        )
        self.log_text.see(tk.END)
        self.log_text.config(state="disabled")

        
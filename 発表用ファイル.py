import tkinter as tk
from tkinter import messagebox
import random,pygame
pygame.mixer.init()

music_list = {
    "1":"C:/Users/hatop/OneDrive/デスクトップ/python_expert/2年目発表/決定ボタンを押す34.mp3",#選択肢を選択
    "2":"C:/Users/hatop/OneDrive/デスクトップ/python_expert/2年目発表/成功音.mp3",#結果発表
    "3":"C:/Users/hatop/OneDrive/デスクトップ/python_expert/2年目発表/決定ボタンを押す7.mp3"#次へ
}

def play_sound(music="1"):

    pygame.mixer_music.load(music_list[music])
    pygame.mixer_music.play()

class QuizGame:

    def __init__(self, root, questions):
        self.root = root
        self.root.title("Python Quiz Game")#ウインドウの名前を設定
        self.root.geometry("500x500")#ウインドウの大きさを設定
        self.questions = questions
        self.total_questions = len(questions)#問題数を確認
        self.question_number = 0#何問目かを初期化
        self.score = 0#スコアを初期化

        self.question_label = tk.Label(self.root, text="")
        self.question_label.pack(pady=20)#padyとは余白(ピクセル)

        self.radio_var = tk.IntVar()#押したボタンを保持する
        self.option_buttons = []
        for i in range(4):  #一問当たり四つの選択肢を想定
            option = tk.Radiobutton(self.root, text="", variable=self.radio_var, value=i,command=play_sound)#チェックボックスを作成
            option.pack(pady=5)#上下に5ピクセルの余白
            self.option_buttons.append(option)#チェックボックスをリストに保存

        self.next_button = tk.Button(self.root, text="Next", command=self.next_question,height=10,width=30,font=("游ゴシック",50))
        self.next_button.pack(pady=20)#ボタンを上下に２０ピクセルの余白を残して設置

        self.load_question()

    def load_question(self):
        current_question = self.questions[self.question_number]
        self.radio_var.set(-1)
        self.question_label.config(text=current_question["question"],font=("游ゴシック",20))
        random.shuffle(current_question["options"])  # Shuffle options each time
        for i in range(len(current_question["options"])):
            self.option_buttons[i].config(text=current_question["options"][i],font=("游ゴシック",20))

    def next_question(self):
        play_sound("3")
        if self.radio_var.get() == -1:
            messagebox.showerror("Error", "何も選択されていません")
            return

        current_question = self.questions[self.question_number]
        selected_option = current_question["options"][self.radio_var.get()]
        
        if selected_option == current_question["correct_answer"]:
            self.score += 1

        self.question_number += 1

        if self.question_number == self.total_questions:
            if self.score == self.total_questions:
                Rank = "S"
                play_sound("2")
            elif self.score>= self.total_questions//2:
                Rank = "A"
                play_sound("2")
            else:
                Rank = "B"
                play_sound("2")
            messagebox.showinfo("Result", f"あなたのランクは{Rank}")
            self.root.destroy()
            return

        self.load_question()

if __name__ == "__main__":
    questions = [#問題
        {
            "question": "日本の首都はどこでしょう？",
            "options": ["東京", "札幌", "福岡", "鳥取"],
            "correct_answer": "東京"
        },
        {
            "question": "「右」を意味する英語は何でしょう",
            "options": ["right", "left", "reght", "light"],
            "correct_answer": "right"
        },
        {
            "question": "この中で素数はどれ？",
            "options": ["1", "2", "15","39"],
            "correct_answer": "2"
        }
    ]

    root = tk.Tk()#ウインドウ作成
    quiz_game = QuizGame(root, questions)#インスタンスを作成
    root.mainloop()#ウインドウを維持
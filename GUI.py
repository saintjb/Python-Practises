import requests
from bs4 import BeautifulSoup
from tkinter import *
from tkinter.scrolledtext import *
from tkinter import messagebox
from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtWebEngineWidgets import *
import sys


class MainWindow(QMainWindow):
    def __init__(self, url):
        super(MainWindow, self).__init__()
        self.setWindowTitle('Stack')
        self.browser = QWebEngineView()
        self.browser.setUrl(QUrl(url))
        self.setCentralWidget(self.browser)
        self.move(638, 0)
        self.resize(638, 1000)

class Answer:
    def __init__(self, title, votes, answer):
        self.title = title
        self.votes = f'{votes} votes'
        self.answer = f'{answer} answers'

    def get_title(self):
        return self.title

    def get_votes(self):
        return self.votes

    def get_answer(self):
        return self.answer


def search_results(question):
    question = question.replace(' ', '+')
    url = f'https://stackoverflow.com/search?q="python"+{question}'
    r = requests.get(url)
    soup = BeautifulSoup(r.text, "lxml")
    search_results_list = soup.find_all('div', class_="question-summary search-result")
    number_of_results = Label(window, text=f'{len(search_results_list)} results found')
    number_of_results.place(x='170', y='40', width='250', height='20')
    TextBox = ScrolledText(window)
    for i, result in enumerate(search_results_list):
        soup = BeautifulSoup(str(result), 'lxml')
        title = soup.find('a', class_="question-hyperlink")["title"]
        votes = soup.find('span', class_="vote-count-post").text
        try:
            answers = soup.find('div', class_="status answered-accepted").text[1]
        except AttributeError:
            answers = '0'
        answer = Answer(title, votes, answers)
        TextBox.insert(END, f'{str(i+1).zfill(2)}\n{answer.get_title()}'
                       f'\n\nVotes:{answer.get_votes()}'
                       f'      Answers:{answer.get_answer()}\n'
                       f'____________________________________________________\n', ("centered",))
        TextBox.place(y='60', width='600')
        TextBox.tag_configure('centered', justify='center')
        apply_entry = Entry(window)
        apply_entry.place(x='325', y='575', anchor='center', width='250')

        def select_event(event):
            try:
                apply_entry.insert(END, f'{TextBox.get(SEL_FIRST, SEL_LAST)},')
            except:
                pass

        TextBox.bind("<<Selection>>", select_event)
        TextBox.bind("<Return>", lambda event: see_details(search_results_list, apply_entry.get()))
        apply_entry.bind("<Return>", lambda event: see_details(search_results_list, apply_entry.get()))
        apply_button = Button(window, text='Details', command=lambda: see_details(search_results_list,
                                                                                  apply_entry.get()))
        apply_button.place(x='490', y='575', anchor='center', height='24')

        def see_details(list, s):
            for number in s.split(','):
                try:
                    soup = BeautifulSoup(str(list[int(number)-1]), 'lxml')
                    url = f'https://stackoverflow.com{soup.find(class_="question-hyperlink")["data-searchsession"]}'
                    window_2 = MainWindow(url)
                    window_2.show()
                    app.exec_()
                except IndexError:
                    messagebox.showinfo("Error", f"A number out of range"
                                        f"\n(The number is: {number})")
                except ValueError:
                    pass


app = QApplication(sys.argv)
window = Tk()
window.resizable(False, False)
window.title("StackOverFlow")
window.geometry("630x600+390+134")
search_entry = Entry(window)
search_entry.place(x='180', y='15', width='250')
search_entry.bind("<Return>", lambda event: search_results(search_entry.get()))
search_button = Button(window, text='Search', command=lambda: search_results(search_entry.get()))
search_button.place(x='450', y='12', height='24')
window.mainloop()

import requests
import tkinter as tk
from tkinter import RAISED,RIDGE,FLAT
import re
import pandas as pd
class Google(object):
    def __init__(self,ROOT,url):
        self.root = ROOT
        self.entry=" "
        self.value=" "
        self.url=url
        self.data=" "

    def search_gui(self):
        tk.Label(self.root,text="GOOGLE",fg="red",bg="black",font="Verdana 30  bold").grid(row=0, column=5)
        tk.Label(self.root).grid(row=1)
        tk.Label(self.root, text="          Search here   ", font="Verdana").grid(row=3, column=3)

        self.entry= tk.Entry(self.root, width=70, borderwidth=2)
        self.entry.grid(row=3, column=4, columnspan=3)
        tk.Label(self.root).grid(row=4)
        tk.Button(self.root,text='Google Search', command=self.get_value, width=12).grid(row=5, column=4, sticky=tk.W)
        tk.Button(self.root, text='I am Feeling Lucky', command=self.root.quit, width=16).grid(row=5, column=6, sticky=tk.W)
        tk.Label(self.root).grid(row=6)
    def get_value(self):
        self.value= self.entry.get()
        print(self.value)
        self.search()
        self.regular_exp()
        self.write_excel()
    def search(self):
        data = requests.get(self.url.format(self.value.replace(" ", "+")))
        self.data =data.text

    def regular_exp(self):
        self.regex = '"http(.*?)"'
        self.data = list(re.finditer(self.regex, self.data, re.MULTILINE | re.DOTALL))
        for elements in self.data:
            print('http' + elements[1])
        print(len(self.data))

    def write_excel(self):
        self.data = pd.DataFrame(self.data, columns=['links'])
        self.data["links1"] = self.data["links"].apply(lambda x: x[0])
        self.data.to_excel('GoogleExcel.xlsx', sheet_name=self.value, index=False)


url='https://www.google.com/search?q={0}&rlz=1C1CHZL_enIN845IN845&oq=pra&aqs=chrome.0.35i39j69i57j35i39j0j69i60l2.3161j0j4&sourceid=chrome&ie=UTF-8'
ROOT = tk.Tk()
ROOT.title("GOOGLE SEARCH")
obj= Google(ROOT,url)
obj.search_gui()
ROOT.mainloop()


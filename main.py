from tkinter import Tk, Button
from selenium import webdriver

def get_wallpaper():
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    driver = webdriver.Chrome(chrome_options=chrome_options)

root = Tk()
root.title("Invento Wallpaper Setter")
root.geometry("500x300")
root.config(bg="#222222")
Button(text="Set Wallpaper", command=get_wallpaper).pack()
root.mainloop()
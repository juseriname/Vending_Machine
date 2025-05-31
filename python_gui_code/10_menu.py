from tkinter import *

root = Tk()

root.title('Application')
root.geometry("480x640")

menu = Menu(root)

def create_new_file():
    print('새파일을 만듭니다.')

menu_file = Menu(menu, tearoff = 0)
menu_file.add_command(label = 'New File', command = create_new_file)
menu_file.add_command(label = 'New Window')
menu_file.add_separator()
menu_file.add_command(label = 'Open File...')
menu_file.add_command(label = 'Save All', state = 'disable')
menu_file.add_separator()
menu_file.add_command(label = 'Exit', command = root.quit)
menu.add_cascade(label = 'File', menu = menu_file)

menu.add_cascade(label = 'Eidt')

menu_lang = Menu(menu, tearoff = 0)
menu_lang.add_radiobutton(label = 'Python')
menu_lang.add_radiobutton(label = 'Jave')
menu_lang.add_radiobutton(label = 'C/C++')
menu.add_cascade(label = 'Language', menu = menu_lang)

menu_view = Menu(menu, tearoff = 0)
menu_view.add_checkbutton(label = 'Show Minimap')
menu_view.add_checkbutton(label = 'Show Maximap')
menu_view.add_checkbutton(label = 'Show Explorer')
menu.add_cascade(label = 'View', menu = menu_view)

root.config(menu = menu)
root.mainloop()
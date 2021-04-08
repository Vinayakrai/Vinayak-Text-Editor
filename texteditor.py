from tkinter import *
from tkinter import font, colorchooser, filedialog, messagebox, ttk
import os
from fpdf import FPDF

main_application=Tk()
main_application.geometry('1200x800')
main_application.title('Vinayak Text Editor')
main_application.iconbitmap('icons2/v.ico')


#*********************Main Menu****************************
main_menu=Menu()

#Code for printing File icons
new_icon=PhotoImage(file='icons2/new.png')
open_icon=PhotoImage(file='icons2/open.png')
save_icon=PhotoImage(file='icons2/save.png')
save_as_icon=PhotoImage(file='icons2/save_as.png')
pdf_icon=PhotoImage(file='icons2/pdf.png')
exit_icon=PhotoImage(file='icons2/exit.png')

#Write as many terms as to be shown in the main menu bar
file=Menu(main_menu, tearoff=False)   #iF tearoff flase not used, then it can be make apart from the text editor by clicking on the line shown in GUI



#Code for adding edit icons
cut_icon=PhotoImage(file='icons2/cut.png')
copy_icon=PhotoImage(file='icons2/copy.png')
paste_icon=PhotoImage(file='icons2/paste.png')
clear_all_icon=PhotoImage(file='icons2/clear_all.png')
find_icon=PhotoImage(file='icons2/find.png')   #Can add undo, redoo later on


edit=Menu(main_menu, tearoff=False)

#Code for adding view icons
toolbar_icon=PhotoImage(file='icons2/tool_bar.png')
statusbar_icon=PhotoImage(file='icons2/status_bar.png')

view=Menu(main_menu, tearoff=False)

#Code for adding theme icons
light_default_icon=PhotoImage(file='icons2/light_default.png')
light_plus_icon=PhotoImage(file='icons2/light_plus.png')
dark_icon=PhotoImage(file='icons2/dark.png')
red_icon=PhotoImage(file='icons2/red.png')
monokai_icon=PhotoImage(file='icons2/monokai.png')
night_blue_icon=PhotoImage(file='icons2/night_blue.png')
yellow_icon=PhotoImage(file='icons2/yellow.png')

color_theme=Menu(main_menu, tearoff=False)
theme_choice=StringVar()

#Code for adding color commands
color_icons=(light_default_icon, light_plus_icon, dark_icon, red_icon, monokai_icon, night_blue_icon, yellow_icon)

color_dict={
    'Light Default':('#000000', '#ffffff'),
    'Light Plus': ('#474747', '#e0e0e0'),
    'Dark': ('#c4c4c4', '2d2d2d'),
    'Red': ('#2d2d2d', '#ffe8e8'),
    'Monokai': ('#d3b774', '#474747'),
    'Night Blue': ('#ededed', '#6b9dc2'),
    'Yellow': ('#ffff00', '#000000')
}

#Cascade all these (for displaying it on GUI)
main_menu.add_cascade(label='File', menu=file)
main_menu.add_cascade(label='Edit', menu=edit)
main_menu.add_cascade(label='View', menu=view)
main_menu.add_cascade(label='Color Theme', menu=color_theme)

#*********************Main Menu End************************

#*********************Toolbar****************************

tool_bar=Label(main_application)
tool_bar.pack(side=TOP, fill=X) #For filling screen horizontally, fill=X, filling vertically, fill=Y, filling both, fill=both

#Setting font style
font_tuples=font.families()
font_family=StringVar()
font_box=ttk.Combobox(tool_bar, width=30, textvariable=font_family, state='readonly')
font_box['values']=font_tuples
font_box.current(font_tuples.index('Arial'))
font_box.grid(row=0, column=0, padx=5)

#Setting size box
size_var=IntVar()
font_size=ttk.Combobox(tool_bar, width=14, textvariable=size_var, state='readonly')
font_size['values']=tuple(range(8, 81))  # (8, 81, 2) -> Size range starts from 8 and goes till 81 with the margin of 2
font_size.current(4)
font_size.grid(row=0, column=1, padx=5)

#Taking Toolbar Icons
bold_icon=PhotoImage(file='icons2/bold.png')
italic_icon=PhotoImage(file='icons2/italic.png')
underline_icon=PhotoImage(file='icons2/underline.png')
font_color_icon=PhotoImage(file='icons2/font_color.png')
align_left_icon=PhotoImage(file='icons2/align_left.png')
align_right_icon=PhotoImage(file='icons2/align_right.png')
align_center_icon=PhotoImage(file='icons2/align_center.png')

#Creating Bold button
bold_btn=ttk.Button(tool_bar, image=bold_icon)
bold_btn.grid(row=0, column=2, padx=5)

#Creating Italic Button
italic_btn=ttk.Button(tool_bar, image=italic_icon)
italic_btn.grid(row=0, column=3, padx=5)

#Creating underline Button
underline_btn=ttk.Button(tool_bar, image=underline_icon)
underline_btn.grid(row=0, column=4, padx=5)

#Creating font color button
font_color_btn=ttk.Button(tool_bar, image=font_color_icon)
font_color_btn.grid(row=0, column=5, padx=5)

#Creating align left button
align_left_btn=ttk.Button(tool_bar, image=align_left_icon)
align_left_btn.grid(row=0, column=6, padx=5)

#Creating align right button
align_right_btn=ttk.Button(tool_bar, image=align_right_icon)
align_right_btn.grid(row=0, column=7, padx=5)

#Creating align left button
align_center_btn=ttk.Button(tool_bar, image=align_center_icon)
align_center_btn.grid(row=0, column=8, padx=5)

#*********************Toolbar End************************

#*********************Text Editor****************************

text_editor=Text(main_application)
text_editor.config(wrap='word', relief=FLAT)

#Craeting scrollbar
scroll_bar=Scrollbar(main_application)
scroll_bar.config(command=text_editor.yview)
scroll_bar.pack(side=RIGHT, fill=Y)

#Setting focus so that the user starts writing directly in the editor
text_editor.focus_set()
text_editor.pack(fill=BOTH, expand=True)
text_editor.config(yscrollcommand=scroll_bar.set)

#Font Family & Font Size Functionality
current_font_family='Arial'
current_font_size=12
text_editor.configure(font=('Arial', '12'))

#Creating function for changing font
def change_font(event=None):
    global current_font_family
    current_font_family=font_family.get()  #What user selects goes in font_family
    text_editor.configure(font=(current_font_family, current_font_size))

#Creating function for font size
def change_font_size(event=None):   #Writing event as None so that if no value is passed, ten also it shows no error
    global current_font_size
    current_font_size = size_var.get()  # What user selects goes in font_family
    text_editor.configure(font=(current_font_family, current_font_size))

font_size.bind("<<ComboboxSelected>>", change_font_size)   #Binding font size
font_box.bind("<<ComboboxSelected>>", change_font)   #Binding font style

##Buttons Functionalities

#Bold Button function
def change_bold():
    text_property=font.Font(font=text_editor['font'])
    text_property.bind('<Control-Key-b>', bold_btn)
    if text_property.actual()['weight']=='normal':
        text_editor.configure(font=(current_font_family, current_font_size, 'bold'))
    if text_property.actual()['weight']=='bold':
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

#italic button function
def change_italic():
    text_property=font.Font(font=text_editor['font'])
    if text_property.actual()['slant']=='italic':
        text_editor.configure(font=(current_font_family, current_font_size, 'roman'))
    if text_property.actual()['slant']=='roman':
        text_editor.configure(font=(current_font_family, current_font_size, 'italic'))


#Underline button function
def change_underline():
    text_property = font.Font(font=text_editor['font'])
    if text_property.actual()['underline'] == 0:
        text_editor.configure(font=(current_font_family, current_font_size, 'underline'))
    if text_property.actual()['underline'] == 1:
        text_editor.configure(font=(current_font_family, current_font_size, 'normal'))

#Binding Bold, italic, underline functions with app
underline_btn.configure(command=change_underline)
italic_btn.configure(command=change_italic)
bold_btn.configure(command=change_bold)

#Font Color functionality
def change_font_color():
    color_var=colorchooser.askcolor()
    text_editor.configure(fg=color_var[1])

font_color_btn.configure(command=change_font_color)

#Align functionality
def align_left():
    text_content=text_editor.get(1.0, 'end')   #Select all written text
    text_editor.tag_config('left', justify=LEFT)
    text_editor.delete(1.0, END)
    text_editor.insert(INSERT, text_content, 'left')

def align_center():
    text_content=text_editor.get(1.0, 'end')   #Select all written text
    text_editor.tag_config('center', justify=CENTER)
    text_editor.delete(1.0, END)
    text_editor.insert(INSERT, text_content, 'center')

def align_right():
    text_content=text_editor.get(1.0, 'end')   #Select all written text
    text_editor.tag_config('right', justify=RIGHT)
    text_editor.delete(1.0, END)
    text_editor.insert(INSERT, text_content, 'right')

align_left_btn.configure(command=align_left)
align_right_btn.configure(command=align_right)
align_center_btn.configure(command=align_center)
#*********************Text Editor End************************

#*********************Status Bar****************************

status_bar=ttk.Label(main_application, text='Status Bar')
status_bar.pack(side=BOTTOM)

#Printing character and words
text_changed=False
def changed(event=None):
    global text_changed
    if text_editor.edit_modified():
        text_changed=True
        words=len(text_editor.get(1.0, 'end-1c').split())
        characters=len(text_editor.get(1.0, 'end-1c').replace(' ', ''))   #Replace used for not counting space as character
        status_bar.config(text=f'Characters: {characters} Words: {words}')
    text_editor.edit_modified(False)

text_editor.bind('<<Modified>>', changed)
#*********************Status Bar End************************

#*********************Main Menu Functionality****************************

#Variable
url=''

#New Functionality
def new_file(event=None):
    global url
    url=''
    MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to create new file?', icon='warning')
    if MsgBox == 'yes':
        text_editor.delete(1.0, END)
    else:
        text_editor.delete(1.0, 1.0)

#Open Functionality
def open_file(event=None):
    global url
    url=filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))

    #url1=docx2txt.process()

    try:
        with open(url, 'r') as fr:
            text_editor.delete(1., END)
            text_editor.insert(1.0, fr.read())
    except FileNotFoundError:
        return text_editor.delete(1.0, 1.0)
    except:
        return text_editor.delete(1.0, 1.0)
    main_application.title(os.path.basename(url))

pdf=FPDF()
def pdf_create():
    global url, text_changed
    try:
        mbox = messagebox.askyesno('Confirmation', 'Do you want to make pdf of same file?')
        if mbox is True:
            if url:
                f = text_editor.get(1.0, END)
                for x in f:
                    pdf.cell(200, 10, txt=x, ln=1, align='C')
                pdf.output(url + '.pdf')
            else:
                content2 = str(text_editor.get(1.0, END))
                url = filedialog.asksaveasfile(mode='w', defaultextension='.txt',
                                               filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                url.write(content2)
                f = text_editor.get(1.0, END)
                for x in f:
                    pdf.cell(200, 10, txt=x, ln=1, align='C')
                pdf.output(url+'.pdf')
        elif mbox is False:
            url = filedialog.askopenfilename(initialdir=os.getcwd(), title='Select File',
                                             filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            try:
                with open(url, 'r') as fr:
                    text_editor.delete(1., END)
                    text_editor.insert(1.0, fr.read())
                    f = text_editor.get(1.0, END)
                    for x in f:
                        pdf.cell(200, 10, txt=x, ln=1, align='C')
                    pdf.output(url + '.pdf')
            except FileNotFoundError:
                return text_editor.delete(1.0, 1.0)
    except:
        return

    #global url
    #MsgBox = messagebox.askquestion('Exit Application', 'Are you sure you want to create new file?', icon='warning')
    #if MsgBox == 'yes':
        #f = open_file('')
    #else:
        #text_editor.delete(1.0, 1.0)
    f= text_editor.get(1.0, 'end-1c')
    for x in f:
        pdf.cell(200, 10, txt=x, ln=1, align='C')
    pdf.output("name.pdf")

#Save Functionality
def save_file(event=None):
    global url
    try:
        if url:
            content=str(text_editor.get(1.0, END))
            with open(url, 'w', encoding='utf-8') as fw:
                fw.write(content)
        else:
            url=filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
            content2=text_editor.get(1.0, END)
            url.write(content2)
            url.close()
    except:
        return

#Save As Functionality
def save_as_file(event=None):
    global url
    try:
        content=text_editor.get(1.0, END)
        url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
        url.write(content)
        url.close()
    except:
        return

#Exit Functionality
def exit_file(event=None):
    global url, text_changed
    try:
        if text_changed:
            mbox=messagebox.askyesnocancel('Warning', 'Do you want to save the file?')
            if mbox is True:
                if url:
                    content=text_editor.get(1.0, END)
                    with open(url, 'w', encoding='utf-8') as fw:
                        fw.write(content)
                        main_application.destroy()
                else:
                    content2=str(text_editor.get(1.0, END))
                    url = filedialog.asksaveasfile(mode='w', defaultextension='.txt', filetypes=(('Text File', '*.txt'), ('All files', '*.*')))
                    url.write(content2)
                    url.close()
                    main_application.destroy()
            elif mbox is False:
                main_application.destroy()
        else:
            main_application.destroy()
    except:
        return

#Code for adding file commands
file.add_command(label='New', image=new_icon, compound=LEFT, accelerator='Ctrl+N', command=new_file)
file.add_command(label='Open', image=open_icon, compound=LEFT, accelerator='Ctrl+O', command=open_file)
file.add_command(label='Save', image=save_icon, compound=LEFT, accelerator='Ctrl+S', command=save_file)
file.add_command(label='Save As', image=save_as_icon, compound=LEFT, accelerator='Ctrl+Alt+S', command=save_as_file)
file.add_command(label='Export to PDF', image=pdf_icon, compound=LEFT, accelerator='Ctrl+R', command=pdf_create)
file.add_command(label='Exit', image=exit_icon, compound=LEFT, accelerator='Ctrl+Q', command=exit_file)

#Find functionaity
def find_file(event=None):
    def find():
        word=find_input.get()
        text_editor.tag_remove('match', '1.0', END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=text_editor.search(word, start_pos, stopindex=END)
                if not start_pos:
                    break
                end_pos=f'{start_pos}+{len(word)}c'
                text_editor.tag_add('match', start_pos, end_pos)
                matches+=1
                start_pos=end_pos
                text_editor.tag_config('match', foreground='red', background='yellow')

    def replace():
        word=find_input.get()
        replace_txt=replace_input.get()
        content=text_editor.get(1.0, END)
        new_content=content.replace(word, replace_txt)
        text_editor.delete(1.0, END)
        text_editor.insert(1.0, new_content)

    def exit():
        find_dialog.destroy()

    find_dialog=Toplevel()
    find_dialog.geometry('400x200+500+200')
    find_dialog.resizable(0,0)     #So that it can't be resized
    find_frame=ttk.LabelFrame(find_dialog, text='Find/Replace')
    find_frame.pack(pady=20)
    text_find_label=ttk.Label(find_frame, text='Find: ')
    text_replace_label=ttk.Label(find_frame, text='Replace: ')
    find_input=ttk.Entry(find_frame, width=30)
    replace_input=ttk.Entry(find_frame, width=30)
    find_btn=ttk.Button(find_frame, text='Find', command=find)
    replace_btn=ttk.Button(find_frame, text='Replace', command=replace)
    exit_btn=ttk.Button(find_frame, text='Exit', command=exit)
    text_find_label.grid(row=0, column=0, padx=4, pady=8)
    text_replace_label.grid(row=1, column=0, padx=4, pady=8)
    find_input.grid(row=0, column=1, padx=4, pady=8)
    replace_input.grid(row=1, column=1, padx=4, pady=8)
    replace_btn.grid(row=2, column=0, padx=3, pady=8)
    find_btn.grid(row=2, column=1, padx=3, pady=8)
    exit_btn.grid(row=2, column=2, padx=3, pady=8)
    find_dialog.mainloop()

#Code for adding edit commands
edit.add_command(label='Cut', image=cut_icon, compound=LEFT, accelerator='Ctrl+X', command=lambda :text_editor.event_generate("<Control x>"))
edit.add_command(label='Copy', image=copy_icon, compound=LEFT, accelerator='Ctrl+C', command=lambda :text_editor.event_generate("<Control c>"))
edit.add_command(label='Paste', image=paste_icon, compound=LEFT, accelerator='Ctrl+V', command=lambda :text_editor.event_generate("<Control v>"))
edit.add_command(label='Clear All', image=clear_all_icon, compound=LEFT, command=lambda :text_editor.delete(1.0, END))
edit.add_command(label='Find', image=find_icon, compound=LEFT, accelerator='Ctrl+F', command=find_file)

#View check button
show_statusbar=BooleanVar()
show_statusbar.set(True)
show_toolbar=BooleanVar()
show_toolbar.set(True)

def hide_toolbar():
    global show_toolbar
    if show_toolbar:
        tool_bar.pack_forget()
        show_toolbar=False
    else:
        text_editor.pack_forget()
        status_bar.pack_forget()
        tool_bar.pack(side=TOP, fill=X)
        text_editor.pack(fill=BOTH, expand=True)
        status_bar.pack(side=BOTTOM)
        show_toolbar=True

def hide_statusbar():
    global show_statusbar
    if show_statusbar:
        status_bar.pack_forget()
        show_statusbar=False
    else:
        status_bar.pack(side=BOTTOM)
        show_statusbar=True

#Code for adding view check boxes
view.add_checkbutton(label='Toolbar', onvalue=True, offvalue=0, variable=show_toolbar, image=toolbar_icon, compound=LEFT, command=hide_toolbar)
view.add_checkbutton(label='Satus Bar', onvalue=1, offvalue=False, variable=show_statusbar, image=statusbar_icon, compound=LEFT, command=hide_statusbar)

#Color theme
def change_theme():
    chosen_theme=theme_choice.get()
    color_tuple=color_dict.get(chosen_theme)
    fg_color, bg_color=color_tuple[0], color_tuple[1]
    text_editor.config(background=bg_color, fg=fg_color)

count=0
for i in color_dict:
    color_theme.add_radiobutton(label=i, image=color_icons[count], variable=theme_choice, compound=LEFT, command=change_theme)
    count+=1

#**********************Bind shortcut Keys*****************************
main_application.bind("<Control-n>", new_file)
main_application.bind("<Control-o>", open_file)
main_application.bind("<Control-s>", save_file)
main_application.bind("<Control-Alt-s>", save_as_file)
main_application.bind("<Control-r>", pdf_create)
main_application.bind("<Control-q>", exit_file)
main_application.bind("<Control-f>", find_file)

#*********************Main Menu Functionality End************************
main_application.config(menu=main_menu)
main_application.mainloop()
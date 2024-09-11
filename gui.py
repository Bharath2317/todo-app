import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in To-do")
input_box = sg.InputText(tooltip="Enter To-do")
add_button = sg.Button("Add")

window = sg.Window("My To-do List",layout = [[label],[input_box,add_button]])
window.read()
window.close()








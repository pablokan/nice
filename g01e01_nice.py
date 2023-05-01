from nicegui import ui
from nicegui.events import ValueChangeEventArguments

t = 0
def show(event: ValueChangeEventArguments):
    n = int(event.value)
    t += n
    print(t)    

for i in range(10):    
    ui.number(label='Number', value=3.1415927, format='%.2f', on_change=show)

ui.run()


#     ui.input(f'{n1*2}')
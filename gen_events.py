from nicegui import ui
from nicegui.events import ValueChangeEventArguments

def show(event: ValueChangeEventArguments):
    ui.notify(f'{event.value}')

with ui.row():
    ui.button('A', on_click=lambda: ui.notify('You clicked the button A.'))
    ui.button('B').on('click', lambda: ui.notify('You clicked the button B.'))
    ui.number(label='Number', value=3.1415927, format='%.2f').on('keydown.enter', show)
with ui.row():
    ui.button('C').on('mousemove', lambda: ui.notify('You moved on button C.'))
    ui.button('D').on('mousemove', lambda: ui.notify('You moved on button D.'), throttle=0.5)
with ui.row():
    ui.button('E').on('mousedown', lambda e: ui.notify(str(e)))
    ui.button('F').on('mousedown', lambda e: ui.notify(str(e)), ['ctrlKey', 'shiftKey'])
with ui.row():
    ui.input('G').classes('w-12').on('keydown.space', lambda: ui.notify('You pressed space.'))
    ui.input('H').classes('w-12').on('keydown.y.shift', lambda: ui.notify('You pressed Shift+Y'))
    ui.input('I').classes('w-12').on('keydown.once', lambda: ui.notify('You started typing.'))

ui.run()
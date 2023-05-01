from nicegui import ui

lista = []

def send() -> None:
        lista.append(int(n.value))
        print(lista)
        s.update('aaaa')
        n.clear()
                

s = ui.label('')
n = ui.number().on('keydown.tab', send)
ui.button('Suma', on_click=lambda: ui.notify(f'{sum(lista)}'))

ui.run()

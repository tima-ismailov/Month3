import flet as ft 
import datetime

def main(page: ft.Page):
    page.title = "мое первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    greeting = ft.Text("Привет, мир!")

    greeting_history = [] 
    history_text = ft.Text("история поздравлений:", style='bodyMedium')
    
    def get_greeting(name):
        current_hour = datetime.datetime.now().hour
        if 6 <= current_hour < 12:
            return f"Доброе утро, {name}!"
        elif 12 <= current_hour < 18:
            return f"Добрый день, {name}!"
        elif 18 <= current_hour < 24:
            return f"Добрый вечер, {name}!"
        else:
            return f"Доброй ночи, {name}!"
    
    def one_button_click(e):
        name = name_input.value.strip()

        if name: 
            greeting.value = get_greeting(name)
            greeting_button.text ='Приветствовать'
            name_input.value = ''

            greeting_time = datetime.datetime.now().strftime("%H:%M")
            greeting_history.append(f"{name} в {greeting_time}")
            history_text.value = f"история поздравлений: \n  {', '.join(greeting_history)}"
            
        else:
            greeting.value = "Пожалуйста, введите ваше имя"

        page.update() 

    name_input = ft.TextField(label="Введите имя: ", autofocus=True, on_submit=one_button_click)

    def clear_history(e):
        greeting_history.clear()
        history_text.value = "история поздравлений: \n"
        page.update()

    def toggle_theme(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    theme_button = ft.IconButton(ft.icons.BRIGHTNESS_6, tooltip="Сменить тему", on_click=toggle_theme)
    clear_button = ft.ElevatedButton("Очистить историю", on_click=clear_history)
    greeting_button = ft.ElevatedButton("Приветствовать", on_click=one_button_click)

    page.add(ft.Row([theme_button], alignment=ft.MainAxisAlignment.END), 
             greeting, 
             name_input, 
             greeting_button,
             clear_button,
             history_text)

ft.app(target=main)


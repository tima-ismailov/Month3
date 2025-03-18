import flet as ft 
import datetime

def main(page: ft.Page):
    page.title = "мое первое приложение"
    page.theme_mode = ft.ThemeMode.LIGHT

    greeting = ft.Text(
        "Привет, мир!",
        size=20,
        weight=ft.FontWeight.BOLD,
        opacity=1,
        animate_opacity=ft.Animation(600, 'ease_in_out'),
        animate_scale=ft.Animation(500, 'ease_in_out'),
        text_align=ft.TextAlign.CENTER
    )

    greeting_history = [] 
    history_text = ft.Text("История поздравлений:",
                           style='bodyMedium',
                           opacity=1,
                           animate_opacity=ft.Animation(700, 'ease_in_out'),
                           )

    history_visible = True  

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
            greeting_button.text = 'Приветствовать'
            name_input.value = ''

            greeting_time = datetime.datetime.now().strftime("%H:%M")
            greeting_history.append(f"{name} в {greeting_time}")
            history_text.value = f"История поздравлений: \n{', '.join(greeting_history)}"
            
        else:
            greeting.value = "Пожалуйста, введите ваше имя"

        page.update()

    name_input = ft.TextField(label="Введите имя: ", autofocus=True, on_submit=one_button_click)

    def clear_history(e):
        greeting_history.clear()
        history_text.value = "История поздравлений: \n"
        page.update()

    def toggle_theme(e):
        page.theme_mode = ft.ThemeMode.DARK if page.theme_mode == ft.ThemeMode.LIGHT else ft.ThemeMode.LIGHT
        page.update()

    def toggle_history(e):
        nonlocal history_visible
        history_visible = not history_visible
        history_text.visible = history_visible
        toggle_history_button.text = "Показать историю" if not history_visible else "Скрыть историю"
        page.update()

    theme_button = ft.IconButton(ft.icons.BRIGHTNESS_6, tooltip="Сменить тему", on_click=toggle_theme)
    clear_button = ft.ElevatedButton("Очистить историю", on_click=clear_history)
    greeting_button = ft.ElevatedButton("Приветствовать", on_click=one_button_click)
    toggle_history_button = ft.ElevatedButton("Скрыть историю", on_click=toggle_history)

    page.add(ft.Row([theme_button], alignment=ft.MainAxisAlignment.END), 
             greeting, 
             name_input, 
             greeting_button,
             clear_button,
             toggle_history_button,
             history_text)

ft.app(target=main)

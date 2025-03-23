import flet as ft
import datetime

def main(page: ft.Page):
    page.title = "Task Manager"
    page.theme_mode = ft.ThemeMode.LIGHT
    
    tasks = []  # Хранилище задач
    
    def add_task(e):
        if task_input.value.strip():
            tasks.append({
                "text": task_input.value.strip(),
                "date": datetime.datetime.now().strftime("%Y-%m-%d %H:%M"),
                "done": False
            })
            task_input.value = ""
            update_tasks()
    
    def toggle_task_status(e):
        index = int(e.control.data)
        tasks[index]["done"] = not tasks[index]["done"]
        update_tasks()
    
    def update_tasks():
        task_list.controls.clear()
        for index, task in enumerate(tasks):
            task_list.controls.append(
                ft.Row([
                    ft.Checkbox(value=task["done"], on_change=toggle_task_status, data=index),
                    ft.Text(f"{task['text']} ({task['date']})"),
                ])
            )
        page.update()
    
    def sort_by_date(e):
        tasks.sort(key=lambda x: x["date"], reverse=date_sort_button.text == "📅 Новые выше")
        date_sort_button.text = "📅 Старые выше" if date_sort_button.text == "📅 Новые выше" else "📅 Новые выше"
        update_tasks()
    
    def sort_by_status(e):
        tasks.sort(key=lambda x: x["done"], reverse=status_sort_button.text == "✅ Завершенные внизу")
        status_sort_button.text = "✅ Завершенные вверху" if status_sort_button.text == "✅ Завершенные внизу" else "✅ Завершенные внизу"
        update_tasks()
    
    task_input = ft.TextField(label="Новая задача")
    add_button = ft.ElevatedButton("Добавить", on_click=add_task)
    date_sort_button = ft.ElevatedButton("📅 Новые выше", on_click=sort_by_date)
    status_sort_button = ft.ElevatedButton("✅ Завершенные внизу", on_click=sort_by_status)
    task_list = ft.Column()
    
    page.add(
        ft.Row([task_input, add_button]),
        ft.Row([date_sort_button, status_sort_button]),
        task_list
    )
    
ft.app(target=main)

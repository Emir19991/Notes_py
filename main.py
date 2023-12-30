class Notes:
    def __init__(self):
        self.notes = {}

    def create_note(self, title, content):
        self.notes[title] = content

    def save_notes(self):
        with open('notes.txt', 'w') as file:
            for title, content in self.notes.items():
                file.write(f"{title}:\n{content}\n")

    def read_notes(self):
        with open('notes.txt', 'r') as file:
            for line in file:
                print(line)

    def edit_note(self, title, new_content):
        if title in self.notes:
            self.notes[title] = new_content
            print(f"Заметка '{title}' отредактирована")

    def delete_note(self, title):
        if title in self.notes:
            del self.notes[title]
            print(f"Заметка '{title}' удалена")


notes_manager = Notes()
notes_manager.create_note("Заметка 1", "Содержание заметки 1")
notes_manager.create_note("Заметка 2", "Содержание заметки 2")

notes_manager.save_notes()

print("Список заметок:")
notes_manager.read_notes()

notes_manager.edit_note("Заметка 1", "Отредактированное содержание заметки 1")
notes_manager.save_notes()

print("Обновленный список заметок:")
notes_manager.read_notes()

notes_manager.delete_note("Заметка 2")
notes_manager.save_notes()

print("Обновленный список заметок:")
notes_manager.read_notes()
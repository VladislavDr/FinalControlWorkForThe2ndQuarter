import sys
import json
import datetime
import uuid
import Note
Note
Note.Note
from Note import Note
from datetime import datetime
datetime.date



def main():
    global notes
    global count
    
    notes = read_notes()

    while True:
            mode = input("\nВыберет режим, в котором хотите работать: \n"+
                            "Введите add, если хотите создать новую заметку. " + 
                            "Введите list, если хотите увидеть все заметки. \n" +
                            "Введите filter, если хотите увидеть все заметки. " +
                            "Введите edit, если хотите отредактировать заметку. \n" + 
                            "Введите delete, если хотите удалить заметку. " +
                            "Введите exit, если хотите выйти из программы. \n" +
                            "Введите Ваш выбор: ")
            match mode:
                case "add":
                    add_note()
                case "list":
                    full_list_notes()
                case "edit":
                    edit_note()
                case "delete":
                    delete_note()
                case "filter":
                    filter_notes()
                case "exit":
                    print("До встречи!")
                    sys.exit()
                case _:
                    print("Не верно, попробуй еще разок \n")



def read_notes():
    try:
        with open("notes.json", "r") as file:
            data = json.load(file)
            notes = [Note(**note) for note in data]
    except (json.decoder.JSONDecodeError, FileExistsError):
        notes = []
    return notes


def save_notes(notes):
    with open("notes.json", "w") as file:
        json.dump([note.__dict__ for note in notes], file, indent=2, separators=(',', ': '))


def add_note():
    count = len(notes)
    id = count + 1
    title = input("Введите название заметки: ")
    body =  input("Введите основной текс заметки: ")
    date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
    note = Note(id, title, body, date)
    notes.append(note)
    save_notes(notes)
    print("Успешно добавлена новая заметка!")


def edit_note():
    id = int(input("Введите id заметки для последующего редактирвоания: "))
    note = next((note for note in notes if note.id == id), None)
    if note:
        title = input("Введите новое название заметки: ")
        body =  input("Введите основной текс новой заметки: ")
        date = datetime.now().strftime('%d.%m.%Y %H:%M:%S')
        if title:
            note.title = title
        if body:
            note.body = body
        if date:
            note.date = date
        save_notes(notes)
    else:
        print("Такой заметки не было найдено!")


def delete_note():
    id = int(input("Введите id заметки для последующего удаления: "))
    note = next((note for note in notes if note.id == id), None)
    if note:
        notes.remove(note)
        print("Успешно удалено!")
        for note in notes:
            print("note")
            print(note.id)
            print(id)
            if note.id == id+1:
                note.id = id
                id += 1
        save_notes(notes)
    else: print("Увы, такой заметки не найдено!")   



def full_list_notes():
    try:
        filter_notes = [note for note in notes]
    except ValueError:
        filter_notes = notes

    if filter_notes:
        for note in filter_notes:
            print(f'ID заметки: {note.id} \nЗаголовок: {note.title} \nТекст заметки: {note.body} \nВремя создания:{note.date} \n')
    else:
        print("Заметок не найдено")


def filter_notes():
    data = (input('Введите дату для фильтрации в заметках в формате дд.мм.гггг: '))
    try:
        filter_date = datetime.strptime(data, '%d.%m.%Y')
        filter_notes = [note for note in notes if datetime.strptime(note.date, '%d.%m.%Y %H:%M:%S').date()==filter_date.date()]
    except ValueError:
        filter_notes = notes

    if filter_notes:
        for note in filter_notes:
            print(f'ID заметки: {note.id} \nЗаголовок: {note.title} \nТекст заметки: {note.body} \nВремя создания:{note.date} \n')
    else:
        print("Заметок не найдено")


main()
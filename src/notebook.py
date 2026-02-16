import note

class Notebook:
    
    def __init__(self):
        self.notes: list[str] = []

    def add_note(self,title: str, text: str, importance: str) -> int:
       def add_note(self, title: str, text: str, importance: str) -> int:
        code = self._next_code
        self._next_code += 1

        note = Note(code, title, text, importance)
        self.notes.append(note)

        return code


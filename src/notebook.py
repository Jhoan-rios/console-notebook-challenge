import note

class Notebook:
    
    def __init__(self):
        self.notes: list[str] = []

    def add_note(self,title: str, text: str, importance: str) -> int:
        code = self._next_code
        self._next_code += 1

        Note = note(code, title, text, importance)
        self.notes.append(Note)

        return code
       
    def delete_note(self, code: int):
        self.notes = [i for i in self.notes if i.code != code]
    
    def important_notes(self) -> list[note.Note]:
        return [
            i for i in self.notes
            if i.importance in (note.HIGH, note.MEDIUM)
        ]
    
    def tag_with_most_notes(self) -> str | None:
        tag_count = {}

        for note in self.notes:
            for tag in note.tags:
                tag_count[tag] = tag_count.get(tag, 0) + 1

        if not tag_count:
            return None

        max_count = max(tag_count.values())
        candidates = [t for t, c in tag_count.items() if c == max_count]

        return sorted(candidates)[0]




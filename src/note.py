# TODO: Agrega el código de las clases del modelo aquí. Borra este comentario al terminar.

import datetime


class Note:

    HIGH = "HIGH"
    MEDIUM = "MEDIUM"
    LOW = "LOW"

    def __init__(self, code: str, title: str, text: str, importance: str):
        self.code = code
        self.title = title
        self.text = text
        self.importance = importance
        self.creation_date = datetime.now()
        self.tags: list[str] = []

        def add_tag(Self, tag: str):
            self.tags.append(tag)

            def __str__(str):
                return(f"Date: {self.creation_date}n\
                         {self.title}: {self.text}")
            
        
            
    
            
            
        

        


        
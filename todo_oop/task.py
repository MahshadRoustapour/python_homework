class Task:
    def __init__(self, title,  description, id_, start_time, statuse, end_time = None):
        self.title = title
        self.description = description
        Task.is_valide(id_)
        self.id_ = id_
        self.start_time = start_time
        self.end_time = end_time
        self.statuse = statuse

    def __str__(self):
        return f"""title---> {self.title}, description---> {self.description},
            id---> {self.id_}, start time---> {self.start_time}, end time---> {self.end_time},
            status---> {self.statuse}"""
        
    @staticmethod
    def is_valide(id_):
        try:
            num = int(id_)
        except Exception as e:
            print(e)

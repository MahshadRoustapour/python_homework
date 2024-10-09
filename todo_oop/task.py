class Task:
    def __init__(self, title,  description, id_, statuse, statrt_time = None, end_time = None):
        self.title = title
        self.description = description
        Task.is_valide(id_)
        self.id = id_
        self.start_time = statrt_time
        self.end_time = end_time
        self.statuse = statuse

    def __str__(self):
        return f"""title---> {self.title}, description---> {self.description},
            id---> {self.id}, start time---> {self.start_time}, end time---> {self.end_time},
            status---> {self.statuse}"""
        
    @staticmethod
    def is_valide(id_):
        try:
            num = int(id_)
        except Exception as e:
            print(e)

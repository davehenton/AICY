class Chat:
    def __init__(self, contact, message, isGroup, isImportant=False):
        self.contact = contact
        self.message = message
        self.isGroup = isGroup
        self.isImportant = isImportant

    def __str__(self):
        return '[{0}, {1}, {2}, {3}]'.format(str(self.contact), self.message, str(self.isGroup), str(self.isImportant))

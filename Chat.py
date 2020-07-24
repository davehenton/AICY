class Chat:
    def __init__(self, personId, message, isGroup, isImportant=False):
        self.personId = personId
        self.message = message
        self.isGroup = isGroup
        self.isImportant = isImportant

    def __str__(self):
        return '[{0}, {1}, {2}, {3}]'.format(str(self.personId), self.message, str(self.isGroup), str(self.isImportant))


I = 99
C = Chat(969692,"message", 0)
X = isinstance(C, Chat)
Y = isinstance(I, Chat)
print(X,Y)
print(C)

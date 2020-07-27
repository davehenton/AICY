from Chat import *
def test_chat():
    I = 99
    C = Chat(969692,"message", 0)
    assert True == isinstance(C, Chat)
    assert False == isinstance(I, Chat)
    assert "[969692, message, 0, False]" == str(C)

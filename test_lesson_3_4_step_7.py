import pytest


@pytest.fixture(scope="class")
# Область покрытия "class" означает,
# что фикстура будет вызвана один раз для ВСЕГО класса.
def prepare_faces():
    print("^_^", "\n")
    yield
    print(":3", "\n")  # Это выполняется только после прогона всех тестов.


@pytest.fixture()
def very_important_fixture():
    #  Выполниться столько раз сколько её вызвать.
    print(":)", "\n") 


@pytest.fixture(autouse=True)
# Параметр "autouse=True" указывает на то,
# что данная фикстура будет запускаться
# для каждого теста, даже без её явного вызова.
def print_smiling_faces():
    print(":-Р", "\n")


class TestPrintSmilingFaces():

    def test_first_smiling_faces(self, prepare_faces, very_important_fixture):
        # вызываем фикстуру prepare_faces в тесте, передав ее как параметр (выполнится сначала "^_^",
        # а потом после окончания второго теста ":3")
        # вызываем фикстуру very_important_fixture в тесте, передав ее как параметр.
        pass

    def test_second_smiling_faces(self, prepare_faces):
        #  Фикстура prepare_faces вызывается в данном тесте, но так как она задана для класса,
        #  то тут выполняться не будет.
        #  Не передаём как параметр фикстуру print_smiling_faces,
        #  но она все равно выполняется.
        pass

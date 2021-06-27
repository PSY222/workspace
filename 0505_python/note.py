class Note(object):
    def _init_(self,content = None):
        self.content = content
    def write_content(self,content):
        self.content = content
    def remove_all(self):
        self.content = ""
    def _str_(self):
        return self.content

class NoteBook(object):
    def _init_(self,title):
        self.title = title
        self.page_number = 1
        self.notes = {}

    def add_note(self, note, page=0):
        if self.page_number < 300:
            if page == 0 :
                self.notes[self.page_number] = note
                self.page_number += 1
            else:
                self.notes = {page : note}
                self.page_number += 1
        else:
            print("Page가 모두 채워졌습니다.")

    def remove_note(self,page_number):
        if page_number in self.notes.keys():
            return self.notes.pop(page_number)
        else:
            print("해당 페이지는 존재하지 않습니다")

    def get_number_of_pages(self):
        return len(self.notes.keys())


    class Person:
            def _init_(self,name,age,gender):
            self.name = name
            self.age = age
            self.gender = gender

            def about_me(self):
                print("저의 이름은 ", self.name, "이구요, 제 나이는",str(self.age), "살 입니다.")

    class Employee(Person):
        def _init_(self,name,age,gender,salary,hire_date):
            super()._init_(name,age,gender)
            self.salary = salrary
            self.hire_date = hire_date

        def do_work(self):
            print("열심히 일을 합니다.")

        def about_me(self):
            super().about_me()
            print("제 급여는 ",self.salary,"원 이구요, 제 입사일은 ",self.hire_date," 입니다.")

class Product(object):
    pass

class Inventory(object):
    def _init_(self):
        self._items = []

    def add_new_items(self,product):
        if type(product) == Product:
            self._items.append(product)
            print("new item added")
        else:
            raise ValueError("invalid item")

    def get_number_of_items(self):
        return len(self._items)

    @property
    def items(self):
        return self._items

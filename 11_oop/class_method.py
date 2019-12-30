# class method is a method that is bound to a class rather than its object.
# It doesn't require creation of a class instance

class ClassTest:
    def instance_method(self):
        print(f"called instance_method of {self}")
    
    @classmethod
    def class_method(cls):
        print(f"called class_method of {cls}")
    
    @staticmethod
    def static_method():
        print("called static_method")


ClassTest.class_method()
ClassTest.static_method()
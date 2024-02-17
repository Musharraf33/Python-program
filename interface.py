# Interface

#                                                |--------------------------------------------|
#                                                |    Interface                               |
#                                                |--------------------------------------------|
#                        |--------------------------------------------|---------------------------------------|
#                        |                                                                                    |
#                        |                                                                                    |
#  |------------------------------------------------|                                  |-------------------------------------------|
#  | contain only abstract method                   |                                  |OR any normal method                       |
#  |------------------------------------------------|                                  |-------------------------------------------|


from abc import ABC,abstractmethod


class Shape(ABC):                      #    +---------------------------------------------------------+ 
                                       #    +                                                         +
    @abstractmethod                    #    + interface (This class have no objaect beacuse           +
    def Show(self):                    #    +            it is pure abstract class or interface class +
        pass                           #    +---------------------------------------------------------+
    
class Square(Shape):
    def Show(self):
        print("Squre has 4 sides....")
        
class circle(Shape):
    def Show(self):
        print("Circle has circle shape.....")
        
o=Square()
o.Show()

c=circle()
c.Show()



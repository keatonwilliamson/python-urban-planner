# using System;

# namespace UrbanPlanner
# {
#     class Building
#     {
#         public Building(string address)
#         {
#             _address = address;
#         }
#         private string _designer = "Keaton Williamson";
#         private DateTime _dateConstructed;
#         private string _address;
#         private string _owner;
#         public int Stories { get; set; }
#         public double Width { get; set; }
#         public double Depth { get; set; }
#         public double Volume
#         {
#             get
#             {
#                 return Width * Depth * (3 * Stories);
#             }
#         }
#         public void Construct()
#         {
#              _dateConstructed = DateTime.Now;
#         }
#         public void Purchase(string owner)
#         {
#              _owner = owner;
#         }
#         public void Print()
#         {
#             Console.WriteLine(_address);
#             Console.WriteLine("----------------------");
#             Console.WriteLine("Designed by " + _designer);
#             Console.WriteLine("Constructed on " + _dateConstructed);
#             Console.WriteLine("Owned by " + _owner);
#             Console.WriteLine(Volume + " meters of space");
#             Console.WriteLine();

#         }
#     }
# }

import datetime


class Building:

    def __init__(self, address, stories):
        # Establish the properties of each book
        # with a default value

        self.address = address
        self.stories = 3

        self.designer = "Keaton Williamson"
        self.date_constructed = ""
        self.owner = ""

        self.width = 0
        self.depth = 0

    @property 
    def volume(self):
        try:
            return self.width * self.depth
        except AttributeError:
            return ""

    def construct(self):
        self.date_constructed = datetime.datetime.now() 

    def purchase(self, name):
        self.owner = name

    def __str__(self):
        return (f"{self.address} Designed by {self.designer}\n"
        f"Constructed on {self.date_constructed}\n"
        f"Owned by {self.owner}\n"
        f"{self.stories} stories\n"
        f"{self.depth} depth\n"
        f"{self.width} width\n"
        f"{self.volume} meters of space\n"
        )

# Remember, that the @decorator syntax is just syntactic sugar; the syntax:

# @property
# def foo(self): return self._foo
# really means the same thing as

# def foo(self): return self._foo
# foo = property(foo)
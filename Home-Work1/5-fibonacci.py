class Fibonachi:
    """
    This class handles Fibonacci series with different cases and permissions in Homework.
    I tried to write everything I learned in structured programming 
    -> (conditions, loops, simple data structures, recursion, etc...)
    and OOP 
    -> (inheritance, encapsulation, polymorphism, abstraction).

    Written by {Name: Youssif Medhate Esmail, ID: 812719542}
    """
    def __init__(self, end: int):
        self.__end = end

    
    #******************** Recursion ********************
    
    def __check_input_when_recursive(self) -> None:
        if self.__end >= 25 or self.__end <= 0:
            raise ValueError(
                f"Recursion can't handle end = {self.__end}\n"
                f"The end must be in range (1 -> 25) to avoid stack overflow.\n"
            )

    def __fibonacci_recursive_way(self, index: int) -> int:
        if index in (1, 2):
            return 1
        return self.__fibonacci_recursive_way(index - 1) + self.__fibonacci_recursive_way(index - 2)

    def fibonacci_recursive(self, index: int) -> int:
        """
        range(1 -> end) (1 ,end) are included in series.
        Time complexity = O(2^n)
        Space complexity = O(n) -> because of recursion stack.
        (This is not the best way to handle Fibonacci)
        """
        self.__check_input_when_recursive()
        return self.__fibonacci_recursive_way(index)
        
    def print_recursive_series(self, sep=',') -> None:
        """
        Print series without saving values.
        Time complexity = O(2^n * n)
        Prints as series with default separator ', ' 
        """
        for number in range(1, self.__end):
            print(self.fibonacci_recursive(number), end=sep + ' ')
        print(self.fibonacci_recursive(self.__end))

    def list_fibonacci_recursive_series(self) -> list:
        """
        Time complexity = O(2^n * n)
        Returns a list including the last index (end). 
        (This is not the best way to handle it)
        """
        return [self.fibonacci_recursive(x) for x in range(1, self.__end + 1)]

    #******************** Iterative ********************

    def __check_input_when_iterative(self) -> None:
        if self.__end >= 2000 or self.__end <= 0:
            raise ValueError(
                f"Iterative method can't handle end = {self.__end}\n"
                f"The end must be in range (1 -> 2000)\n"
            )
        
    def __fibonacci_iterative_way(self, index: int) -> int:
        if index in (1, 2):
            return 1
        a, b = 1, 1
        for _ in range(3, index + 1):
            a, b = b, a + b
        return b

    def fibonacci_iterative(self, index: int) -> int:
        """
        Iterative approach to compute nth Fibonacci number.
        Time complexity = O(n)
        Space complexity = O(1)
        """
        self.__check_input_when_iterative()
        return self.__fibonacci_iterative_way(index)

    def print_iterative_series(self, sep=',') -> None:
        """
        Print Fibonacci series using iterative way.
        Time complexity = O(n^2)
        """
        for number in range(1, self.__end):
            print(self.fibonacci_iterative(number), end=sep + ' ')
        print(self.fibonacci_iterative(self.__end))

    def list_fibonacci_iterative_series(self) -> list:
        """
        Returns a list of Fibonacci numbers using iterative way.
        Time complexity = O(n^2)
        """
        return [self.fibonacci_iterative(x) for x in range(1, self.__end + 1)]

    #************* Fastest Way (efficient) *************
    
    def __check_input_when_fasts_way(self) ->None:
         if self.__end <= 0:
             raise ValueError(
                f"end must > 0 , can't handle end = {self.__end}\n"
            )
             
    def print_fastes_way(self , sep =',') ->None:
        """
        Print Fibonacci series using fastes way.
        Time complexity = O(n)
        """
        
        self.__check_input_when_fasts_way()
        
        if self.__end >= 1:
            print(1, end= sep + ' ')
        
        if self.__end >= 2:
            print(1, end= sep + ' ')
        
        a , b = 1 , 1
        
        for _ in range(3 , self.__end):
            a ,b = b, a + b
            print(b , end= sep +' ')
        print(a + b)

    def list_fibonacci_fastes_way(self)-> list:
        """
        Returns a list of Fibonacci numbers using fastes way.
        Time complexity = O(n)
        """
        self.__check_input_when_fasts_way()
        
        if self.__end == 1:
            return [1]
        if self.__end == 2:
            return [1, 1]

        fibo_list = [1, 1]
        a, b = 1, 1

        for _ in range(3 , self.__end + 1):
            a, b = b, a + b
            fibo_list.append(b)

        return fibo_list 

    #To handel oop conceptes (over riding operatores)

    def __len__(self)-> int:
        return self.__end
    
    def __str__(self)-> str:
        return "Just class to handel fibonacci"
    
    def __iadd__(self , value: int)->object:
        self.__end += value
        return self

    def __isub__(self, value: int)->object:
        self.__end -= value
        return self

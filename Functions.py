#Functions

def sayHello(name = "Default Name"):
    print("Hello", name)

sayHello()

def loopFunction():
    userName = input("What is your name: ")
    userChoice = int(input("How many times wanna write your name?: "))
    for f in range(userChoice):
        print(userName)

loopFunction()

#Note:
# Parameter is optional.
# If your function have to parameter, then use it.


# return() Function
# if you wanna get a value from your function, use return()

def doIt(a, b, c):
    return a + b - c

ayye = doIt(1, 2, 3)
print("Result =", ayye) #0


#FLEXIBLE PARAMETERS AT FUNCTIONS

def exampleOne(*numbers):
  total = 0
  for f in numbers:
    total += f
  return total
  
a = exampleOne(2, 3, 4)
print(a)


def favMovies(*movies):
  favMoviesList = list()
  for f in movies:
    favMoviesList.append(f)
  return favMoviesList

listOfMovies = favMovies("Shawshank Redemption", "Fight Club", "Matrix")

print(type(listOfMovies)) # <class 'list'>

MovieOne = listOfMovies[0]
MovieTwo = listOfMovies[1]
MovieThre = listOfMovies[2]



for movies in MovieOne, MovieTwo, MovieThre:
    print(movies)
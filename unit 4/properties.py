class Dog:
    def __init__(self,name,breed,age,color):
       self.breed = breed
       self.age = age
       self.color = color
       self.name = name
    def say_age(self):
        words_to_say = "I am "+str(self.age)+"years old"
        print(words_to_say)
    def intro (self):
        say = 'I am of ' + str(self.breed)+" Breed"
        print(say)
    def my_name (self):
        print("i am " + self.name )
    

    def bark (self):
        print("woof! woof!")
    def sleep(self):
        print('Zzzzz')
    def eat(self):
        print("NOm NOm")
dog = Dog('LUNA','Bhutanese',20,'black')
petdog = Dog('puppy','pug',10,"white")
my_friend_dog = Dog( 'GAWA',"german shephard", 15,'brown')
dog.say_age()
petdog.say_age()
dog.intro()
dog.my_name()
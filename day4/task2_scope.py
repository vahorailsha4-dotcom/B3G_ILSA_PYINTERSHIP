def make_greeting(language):
    def greet(name):
        if language.lower()=="english":
            print("Hello",name)
        elif language.lower()=="hindi":
            print("Namaste",name)
        else:
            print("HII",name)
    return greet
english_greet=make_greeting("English")
hindi_greet=make_greeting("Hindi")

english_greet("Ilsa")
hindi_greet("Zeinab")


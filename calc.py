from speak import *
import speech_recognition as sr
import operator

def add(x, y):
    return x+y

def sub(x, y):
    return x - y

def mul(x, y):
    return x * y

def __truediv__(x,y):
    return x / y

def floordiv(x,y):
    return x // y

def calculate():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        speak("Say what you want to calculate, example: 3 plus 3")
        print("listening...")
        r.adjust_for_ambient_noise(source)
        audio = r.listen(source)
        my_string = r.recognize_google(audio)
        print(my_string)

        def get_operator_fn(op):
            return {
                '+': operator.add,
                '-': operator.sub,
                'x': operator.mul,
                '/': operator.__truediv__,
                '//': operator.floordiv,
            }[op]

        def eval_binary_expr(op1, oper, op2):
            op1, op2 = int(op1), int(op2)
            return get_operator_fn(oper)(op1, op2)

        speak("Your result is ")
        speak(eval_binary_expr(*(my_string.split())))

if __name__ == "__main__":
    calculate("5+3")

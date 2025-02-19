from data import Data


# muita sujeira fora do main

class Buttons: 
    @staticmethod   
    def b_one_press(callback):
        logic_value = "1" # valor pessoal de cada classe
        Data.v_string += "1"
        Data.l_string += logic_value
        callback()
        
    @staticmethod
    def b_two_press(callback):
        logic_value = "2"
        Data.v_string += "2"
        Data.l_string += logic_value
        callback()

    @staticmethod
    def b_three_press(callback):
        logic_value = "3"
        Data.v_string += "3"
        Data.l_string += logic_value
        callback()
        
    @staticmethod
    def b_four_press(callback):
        logic_value = "4"
        Data.v_string += "4"
        Data.l_string += logic_value
        callback()
        
    @staticmethod
    def b_five_press(callback):
        logic_value = "5"
        Data.v_string += "5"
        Data.l_string += logic_value
        callback()
        
    @staticmethod
    def b_six_press(callback):
        logic_value = "6"
        Data.v_string += "6"
        Data.l_string += logic_value
        callback()
        
    @staticmethod
    def b_seven_press(callback):
        logic_value = "7"
        Data.v_string += "7"
        Data.l_string += logic_value
        callback()
        
    @staticmethod
    def b_eight_press(callback):
        logic_value = "8"
        Data.v_string += "8"
        Data.l_string += logic_value
        callback()
        
    @staticmethod
    def b_nine_press(callback):
        logic_value = "9"
        Data.v_string += "9"
        Data.l_string += logic_value
        callback()
    
    @staticmethod
    def b_zero_press(callback):
        logic_value = "0"
        Data.v_string += "0"
        Data.l_string += logic_value
        callback()
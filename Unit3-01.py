# Created by: Mr. Coxall
# Change by:Gavin Zhou
# Created on: Oct 3 2017
# Created for: ICS3U
# This program shows how to use an if statement

import ui

NUMBER_COMPUTER_IS_THINKING_ABOUT = 5

def check_number_of_touch_up_inside(sender):
    # check the number of students entered verses the constant above
    
    # input
    number_entered = int(view['input_of_number_textbox'].text)
    
    # process
    if number_entered == NUMBER_COMPUTER_IS_THINKING_ABOUT:
        # output
        view['check_answer_label'].text = "Correct!!!"

view = ui.load_view()
view.present('sheet')

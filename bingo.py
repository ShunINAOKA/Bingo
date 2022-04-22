from session import _get_state
import streamlit as st
import numpy as np
import random
import re
import pandas as pd
from session import _get_state
# 状態を維持する
max_number = 15
remaining_numbers = []

state = _get_state()
if state.count == None:
    state.chosen_numbers = []
    state.count = 0
    state.remaining_numbers = []

    for number in range(max_number):
        state.remaining_numbers.append(number+1)
button1 = st.button("Button1", on_click=None)
button2 = st.button("Button2", on_click=None)
def press_start():
    if button2:
        chosen_number = 0
        # chosen_number_prev = 0
        index = 0
        return chosen_number, index

@st.cache(suppress_st_warning=True)
def press_button(index):
    if button1:
        if len(state.remaining_numbers) != 0:
            chosen_number = random.choice(state.remaining_numbers)
            state.remaining_numbers = list(set(state.remaining_numbers) - {chosen_number}) #remaining remaining_number
            state.chosen_numbers.append(chosen_number) 
            list_num = [s for s in state.chosen_numbers if isinstance(s,int) == True]
            count_num = len(list_num)
            for i in range(len(list_num)):
                list_num[i] = str(list_num[i])
            remainder = count_num%5
            if count_num%5 != 0:
                list_num.extend(['nan']*(5-remainder))   
            np_num = np.array(list_num)
            quotient = int(len(list_num)/5)
            np_num_array = np_num.reshape(quotient, 5)
            st.write(np_num_array)
            chosen_number_prev = chosen_number
            index += 1
            return chosen_number
            
        else:
            st.write("Game is over")

def input_name():
    name = st.text_input('The first place', 'Shun')
    st.write('The first place is', name)
    print('name',  name)
    return name

df = pd.DataFrame(
    np.random.randn(10, 3),
    columns=('Rank','Number','Name'))

st.table(df)

chosen_number, index = press_start()

chosen_number = press_button(index)
input_name()
print('chosen_number',chosen_number)
# print('chosen_number_prev',chosen_number_prev)
print('index',index)







#pandas
#game over  









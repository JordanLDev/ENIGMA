
"""
THIS WAS A CHALLENGE I SET MYSELF TO PROGRAM A ROTOR / WHEEL WITH NUMBERS BETWEEN 0 AND 25,
FIRSTLY, I NEEDED TO GET THE USER INPUT.
SECONDLY, I NEEDED TO GET ALL NUMBERS BEFORE THE USER INPUT.
THIRDLY, I NEEDED TO GET ALL THE NUMBERS AFTER THE USER INPUT.
LASTLY, I NEEDED TO ORGANISE THE LIST IN THE CORRECT ORDER TO SIMULATE A ROTOR / WHEEL.
"""

# USER INPUTS THE NUMBER FOR THE ROTOR
input_num = int(input("ENTER THE ROTOR NUMBER BETWEEN 0 AND 25: "))
# INITIALISES WITH THE NUMBER USERS INPUTTED AFTER THE PROMPT
index_rotor_input = [input_num]
# SETS THE ROTOR REMAINDER LIST DEFAULT TO 0
index_rotor_remainder = [0]

# THIS FOR LOOP WORKS OUT ALL NUMBERS AFTER THE USER INPUT NUMBER. 
# FOR EXAMPLE IF 19 IT WILL COUNT UP TO 25 AND APPEND EACH NUMBER IN ORDER.
# [19,20,21,22,23,24,25]
# ONCE MAXIMUM NUMBER IS REACHED IT WILL STOP THE FOR LOOP.

for i in index_rotor_input:
    max_num = 25
    if i < max_num:
        i += 1
        index_rotor_input.append(i)
    elif i > max_num: 
        i += 1
        index_rotor_input.append(i)

# THIS FOR LOOP WORKS OUT ALL NUMBERS BEFORE THE USER INPUT NUMBER. 
# FOR EXAMPLE IF 19 IT WILL COUNT FROM 0 AND APPEND EACH VALUE IN ORDER UP UNTIL THE USER INPUT VALUE - 1
# [19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18]
# ONCE MAXIMUM VALUE IS REACHED IT WILL STOP THE FOR LOOP.

for i in index_rotor_remainder:
    max_num = input_num - 1
    if i < max_num:
        i += 1
        index_rotor_remainder.append(i)
    elif i > max_num: 
        i += 1
        index_rotor_remainder.append(i)
# THIS APPENDS THE TWO LISTS TOGETHER IN THE CORRECT ORDER.

for i in index_rotor_remainder:
    index_rotor_input.append(i)

#print(index_rotor_remainder)

# THIS PRINTS THE RESULT AFTER THE LISTS HAVE BEEN COMBINED
print(index_rotor_input)

"""
--- FUTURE IMPLEMENTATION --
alphabet_rotor = [["A"],["B"], ["C"],["D"], ["E"], ["F"], ["G"], 
["H"], ["I"], ["J"], ["K"],["L"], ["M"], ["N"], ["O"], ["P"], ["Q"], ["R"], ["S"], ["T"], ["U"], ["V"], ["W"], ["X"], ["Y"], ["Z"]]
index_rotor = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25]
rotor_data = [*zip(alphabet_rotor,index_rotor)]
rotor_max_count = 0
#print(rotor_data[1])
selected_rotor_position = int(input())
print(selected_rotor_position)
rotor_modifier = 0
"""

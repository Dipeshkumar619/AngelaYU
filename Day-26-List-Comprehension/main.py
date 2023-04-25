# short_names=[name for name in names if len(item) < 5]
# short_names=[name for name in names if len(name) < 5]
# List comprehension
# numbers=[1,1,2,3,5,8,13,21,34,55]
# squared_num=[item*item for item in numbers]
# print(squared_num)
# even_num=[item for item in numbers if item%2==0]
# print(even_num)
#
# missing_states=[item for item in all_states if item not in guessed_states ]
# # Dictionary Comprehension
# new_dict={nk:nv for item in list}
# new_dict={nk:nv for (key,value) in dict.items()}
# new_dict={nk:nv for (key,value) in dict.items() if test}
# import random
# student_scores={key:random.randint(1,100) for key in names}
#
# passed_students={k:v for (k,v) in student_scores.items() if v > 33}
# sentence="What is the Airspeed velocity of an Unladen Swallow"
# import pandas
# list_sent=sentence.split(" ")
# print(list_sent)
# count_word1={k:len(k) for k in list_sent}
# count_word={k:len(k) for k in sentence.split()}
#
# print(count_word)

# weather_C={"Monday":12,"Tuesday": 14,"Wednesday": 15,"Thursday": 14,"Friday": 21,"Saturday": 22,"Sunday": 24}
# weather_F={k:(v*9/5+32) for (k,v) in weather_C.items()}
# print(weather_F)
import pandas
student_dict={
    "student":["Angela","James","Lily"],
    "score":[56, 57, 78]
}
student_data_frame=pandas.DataFrame(student_dict)
for (k,v) in student_data_frame.items():
    print(k,v)


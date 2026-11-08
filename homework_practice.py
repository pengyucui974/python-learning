# scores = [78, 92, 65, 88, 96, 73, 84]
# sum=0
# j=0
# num_90=0
# for i in scores:
#     sum+=i
#     if j==0:
#         max_num=i
#         min_num=i
#     else:
#         if i>max_num:
#             max_num=i
#         if i<min_num:
#             min_num=i
#     j+=1
#     if i>=90:
#         num_90+=1
#
# group_low=[]
# for k in scores:
#     if k<sum/len(scores):
#         group_low.append(k)
#
# print(f"平均分为{sum/len(scores):.2f}")
# print(f"最高分为{max_num}")
# print(f"最低分为{min_num}")
# print(f"90分及以上人数为{num_90}")
# print(f"低于平均分的成绩包括{group_low}")


#------------------------------

# temperatures = [28.3, 29.1, 31.5, 35.2, 39.8, 42.1, 38.6, 34.5]
# def analyze_temperature(data, threshold):
#     """
#     analyze the temperaure
#     :param data:list of temperatures
#     :param threshold:input
#     :return: dict
#     """
#     total = 0
#     num_threshold = []
#     max_temp = data[0]
#     min_temp = data[0]
#
#     for temp in data:
#         total += temp
#         if temp > max_temp:
#             max_temp = temp
#         if temp < min_temp:
#             min_temp = temp
#         if temp > threshold:
#             num_threshold.append(temp)
#
#     average = total / len(data)
#     return {"average": average, "maximum": max_temp, "minimum": min_temp,"above_threshold": num_threshold}
# result = analyze_temperature(temperatures, 35)
# print(result)


#-------------------

# text = "python git python comsol python git abaqus"
# def get_times(text:str):
#     """
#     get times from text
#     :param text: string
#     :return: dictionary
#     """
#     words_list = text.split()
#     exist_word={}
#     max_times=0
#     max_times_word=""
#     for word in words_list:
#         if word not in exist_word:
#             exist_word[word]=1
#         else:
#             exist_word[word]+=1
#
#     for keys  in exist_word.keys():
#         if exist_word[keys]>max_times:
#             max_times=exist_word[keys]
#             max_times_word=keys
#
#     return exist_word,max_times_word
#
# results,max_times_word=get_times(text)
# print(max_times_word)
# print(results)


#--------------------

# f=open("homework.txt","w",encoding="utf-8")
# content="28.5\n30.2\n31.8\nerror\n35.6\n40.1"
# f.write(content)
# f.close()
#
# f=open("homework.txt","r",encoding="utf-8")
# num_row=f.readlines()
#
# my_list=[]
# invalid_num=0
# for i in num_row:
#     try:
#         my_list.append(float(i.strip()))
#     except ValueError:
#         print("有非法字符")
#         invalid_num+=1
#
# average=sum(my_list)/len(my_list)
# print(f"有效数据有{len(my_list)}个，无效数据有{invalid_num}个，平均温度为{average:.2f}°C")


#-------------------------

class Experiment:
    def __init__(self,name,rock_temperature, air_velocity, power):
        self.name = name
        self.rock_temperature = rock_temperature
        self.air_velocity = air_velocity
        self.power = power

    def show_info(self):
        print(f"{self.name}: Rock_temperature: {self.rock_temperature} °C, Air_velocity: {self.air_velocity} m/s, Power: {self.power} mW")

    def is_high_power(self,threshold):
        if self.power > threshold:
            return True
        else:
            return False
        # return self.power > threshold

exp1 = Experiment("Case-1", 60, 2, 25.3)
exp2 = Experiment("Case-2", 80, 2, 67.8)
exp3 = Experiment("Case-3", 100, 2, 128.5)

exp1.show_info()
print(exp2.is_high_power(50))

exp_list=[exp1,exp2,exp3]
power=0
for exp in exp_list:
    if exp.power>power:
        best_exp = exp
        power = exp.power

best_exp.show_info()





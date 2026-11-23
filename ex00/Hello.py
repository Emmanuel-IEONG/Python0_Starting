ft_list = ["Hello", "tata!"]
ft_tuple = ("Hello", "toto!")
ft_set = {"Hello", "tutu!"}
ft_dict = {"Hello" : "titi!"}

ft_list.pop()
ft_list.append("World!")

temp_list = list(ft_tuple)
temp_list.pop()
temp_list.append("France!")
ft_tuple = tuple(temp_list)

ft_set.discard("tutu!")
ft_set.add("Paris!")

ft_dict["Hello"] = "42Paris!"

print(ft_list)
print(ft_tuple)
print(ft_set)
print(ft_dict)

# n = int(input())
# print(sum([i for i in range(1,n) if i%3 == 0 or i%5 == 0]))

# def totalpage(m,n):
#     page = m//n
#     if m%n != 0:
#         page += 1
#     return pag
#
# print(totalpage(11,10))

names = "이유덕,이재영,권종표,이재영,박민호,강상희,이재영,김지완,최승혁,이성연,박영서,박민호,전경헌,송정환,김재성,이유덕,전경헌"
indi_names = names.split(',')
last_name = [i[0] for i in indi_names]
print("김씨: ",last_name.count("김\n"),"이씨: ",last_name.count("이"))

print(indi_names.count("이재영"))


one_name = list(set(indi_names))
print(one_name)

one_name.sort()
print(one_name)

smart_phone = ['iphone','galaxy','xiaomi','essential','pixel']

#list comprension
i_name =[phone for phone in smart_phone if phone.startswith('i')]
print(i_name)
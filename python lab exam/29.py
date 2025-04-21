phone_no = {
    "aniket":1,
    "akif":2,
    "shreya":3
}
phone_no2 ={
    'unnati':6565
}

print(phone_no)

print(phone_no['akif'])

phone_no['shreya'] = [1111,2222]
print(phone_no)

phone_no['akif'] = {'akif_colg':1545,'akif_skl':2892}
print(phone_no)

print(phone_no.items())

print(phone_no.keys())

print(phone_no.pop('akif'))
print(phone_no)

phone_no.update(phone_no2)
print(phone_no)

phone_no['aniket']= 8975
print(phone_no)


get=input('Enter the phone number: ')
strings={
    '1':'one',
    '2':'two',
    '3':'three',
    '4':'four',
    '5':'five',
    '6':'six',
    '7':'seven',
    '8':'eight',
    '9':'nine',
    '0':'zero',
}
output=""
for ch in get:
    output+=strings.get(ch)+' '
print(output)
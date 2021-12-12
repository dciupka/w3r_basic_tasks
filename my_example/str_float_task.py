""". Mamy następujący kod Pythona, który przechowuje ciąg znaków:
text = 'X-DSPAM-Confidence: 0.8475'
Użyj find() i wycinków ciągów znaków, tak aby wyodrębnić część ciągu po znaku
dwukropka, a następnie użyj funkcji float(), żeby przekształcić wyodrębniony
ciąg znaków na liczbę zmiennoprzecinkową."""
text = 'X-DSPAM-Confidence: 0.8475'

positon_index = text.find(":")
value = text[(positon_index+1):]
new = value.strip()
print(new)
print(type(new))
new_value = float(new)
print(new_value)
print(type(new_value))

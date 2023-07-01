import languages

LANGUAGE_FAMILY = languages.living_indo_european

total_native_speakers = 0
total_total_speakers = 0
new_language_family = {}

for language, data in LANGUAGE_FAMILY.items():
    total_native_speakers += data["native_speakers"]
    total_total_speakers += data["total_speakers"]

# print(f"Total Native Speakers: {total_native_speakers:,}\
# \nTotal Total Speakers: {total_total_speakers:,}")

""" 
Total Native Speakers: 1,915,931,282
Total Total Speakers: 3,288,753,879
"""

for language, data in LANGUAGE_FAMILY.items():
    new_language_family[language] = data
    new_language_family[language]["native_weight"] = \
        (data["native_speakers"] / total_native_speakers) * 100
    new_language_family[language]["total_weight"] = \
        (data["total_speakers"] / total_total_speakers) * 100

print(f"new_language_family = \n\n{new_language_family}\n\n")
PLACE_HOLDER = "[name]"

with open('./Input/Names/invited_names.txt') as names_file:
    names = names_file.readlines()

with open('./Input/Letters/starting_letter.txt') as letter_file:
    letter_contents = letter_file.read()
    for name in names:
        stripped_name = name.strip()
        new_letter = letter_contents.replace(PLACE_HOLDER,stripped_name)
        with open(f'./Output/ReadyToSend/letter_for_{stripped_name}.txt', 'w') as compleated_letter:
            compleated_letter.write(new_letter)



favorite_languages = {
    'jen': ['python', 'ruby'],
    'sarah': ['c'],
    'edward': ['ruby', 'go'],
    'phil': ['python', 'haskell'],
}

for name, languages in favorite_languages.items():
    if len(languages) != 1:
        print("\t" + name.title() + "'s favorite languages are:")
        for language in languages:
          print("\t" + language.title())
    else:
        print("\t" + name.title() + "'s favorite languages is:")
        for language in languages:
            print("\t" + language.title())
#Krista Dockery hw 3
def locate_words(string, sub):
    matches = []
    index = 0
    while index < len(string):
        if string[index : index + len(sub)] == sub:
            matches.append(index)
            index += len(sub)
        else:
            index += 1
    return matches

a = ("""
A Proclomation.
Whereas, on the twentysecond day of September, in the year of our Lord one thousand
eight hundred and sixty two, a proclomation was issued by the President of the United
States, containing, among other things, the following, towit:
That on the first day of January, in the year of our Lord one thousand eight hundred and
sixty-three, all persons held as slaves within any State or designated part of a State, the
people wherof shall then be in rebellion against the United States, shall be then,
thenceforward, and forever free; and the Executive Government of the United States,
including the military and naval authority thereof, will recognize and maintain the freedom
of such persons, and will do no act or acts to repress such persons, or any of them, in any
effors they may make for their actual freedom.
""")

print(locate_words(a, "Lord"))
print(locate_words(a, "proclomation"))
print(locate_words(a, "State"))
print(locate_words(a, "hundred"))

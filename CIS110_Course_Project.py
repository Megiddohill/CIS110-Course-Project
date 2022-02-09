print("Hello.\n")
print("You are about to take a journey. \nSomewhere, right now, a dog is about to complete their time on this side of the grey veil. \nThat seperates us from this world... to the next. \nSee if you can't reach out to our friend. \nFeel yourself joining your spirit with this dog, see the world... through their eyes.... \n")
dog_name = input('Are you connected? Maybe you can tell me their name to make sure?:  ')
print()

print(dog_name, "? Really.... That's a good name for a .... a.... well.... hmmmm...\n")
dog_breed = input("Reach out again... what kind of breed is our friend?:  ")
print()

print('Ah! Of course! A"',dog_breed,'"A fine breed, with a fine name.',dog_name,'"the"',dog_breed,'.\n')
print("I think you're getting a stronger connection... maybe you feel a little scared, or uncomfortable? \nIt's probably because your friend  is feeling scared too. Try and think of calming thoughts.\n")
fav_smell = input('Try thinking of a really good smell, don\'t worry if its something a dog might like:  ')
print()

print("I think you found our friend\'s favorite smell, well done,\nIts a good smell...", fav_smell, ".\n")
fav_food = input('Can you taste that? Our friend is trying to remember their favorite meal. Mmm, it\'s... it\'s:  ')
print()

print("Yes! That\'s it!",fav_food,"! Our friend sure knows what\'s good.\n")
sec_breed = input('Our scared friend is thinking of a friend, another breed of dog... It\'s a:  ')
print()

print('That\'s right. Our friend\'s best friend, the',sec_breed,'from next door. \nIt\'s good to have friends.\n')
print('But, you still.... sense that scared feeling, don\'t you? Like something scary is watching you both?\n')
print('............\n')
scary_thing = input("What are they? .... I don\'t think I like it .... I think they are ... are:  ")
print()

print('A',scary_thing,'....You think so? Maybe it isn\'t. Our friend seems very scared now.\n')
print('You should try and be with your friend. Close your eyes for a few seconds... when you open them....\n')
print('You\'ll take the journey together..... through',dog_name,'\'s eyes, but both your spirits.\n')
print('Are you ready? It\'s starting....\n\n\n\n')
print("You lay on your side, grasping for breath. Your human is there, crying, you feel very scared, but you also \ndon't want them to be sad.\n")

x = int(input('Do you comfort your human or let them comfort you? Enter 1 for comfort them. 2 for accept their comfort:  '))
while x != 1 and x != 2:
    x = int(input("This can't happen. Try another choice:  "))
if x == 1:
    print("You're scared but you see your human crying and sad. And you don't want that. You take all your \nremaining strength and pick your head up to be able to reach their face. Your kisses seem to reassure \nthem and for the oddest moment you taste",fav_food,"and remember the last time your human and you shared \nthat most delicious of foods, content with the memory, you close your eyes, the next time you open them...\n")
else:
    print("Whimpering and scared you reach out for your human. They take you paw and nuzzle your face. \nSomehow you feel a little braver and calmer and their nearby face for some strange reason makes you \nremember",fav_smell,".The scent overwhelms you and you close your eyes, the next time you open them.\n")

print('You see that you are in a strange but wonderful place. Bright colors and exciting smells. You \ncan almost taste',fav_food,'as you gulp in the air. Young pups run around playing, but seem to not know \nbasic dog things, like how to smell for each other or howl or bark... very strange. You look behind \nyou and there is a small tunnel and in it you can see your human in your bedroom, they’re huddled over \nsomething and still sad. You want to go back, but you are also drawn to this place. As if you belong \nhere, or you will belong here. Before you make up your mind. A presence and voice is suddenly near you. \nIt’s a safe presence and a kind voice. You instinctively trust it. \n\nThe voice says, "Hello',dog_name,'of the',dog_breed,'clan." \n\nAnd starts saying what a good dog you were, and how important you were in your life, and it’s sad, but \nyour human must go on without you. It’s just the way it has to be. But the voice tells you to \nlook one more time. As you do your fur stands up and you growl without thinking, because behind \nyour human is several dark figures. They look like',scary_thing,'And they are whispering dark and bad sounding \nwords in the ear of your human.\n')
input('Are you ready to continue the journey? Press Enter:  ')
print()

print('The voice tells you to be calm. Humans and Dogs can’t see the dark ones on Earth. Only "Knights of the Order of \nthe First Hound" can see and do battle with such creatures, the voice explains, and that you must now \nmake a choice. More pups are being readied to go Earth. But they need training. Dogs on earth are as important \nto keep the dark ones at bay as much as the Order of the First Hound are. The voice invites you to stay and \nteach the young ones all they need to learn to be the best dogs they can be. But you can also choose to go \nback as a spirit and join the Order of the First Hound and fight against the dark ones. Both choices \nare good, and both choices are important. Which one do you choose?\n')
y = int(input("What do you feel is right? Choose '1' to stay and '2' to go back:  "))
while y != 1 and y != 2:
    y = int(input("This can't happen. Try another choice:  "))
if x == 1 and y == 2:
    print('The voice sounds impressed and moved. It says that this is not an easy path. But you were brave in life, \nthat bravery echoes into a dog’s afterlife. The next steps you take will be into the Order of the First Hound. \n“Are you ready? “ Is the voice’s last words and without a moment’s hesitation your howl fills the \nheavens around you, and they dissolve into a light so bright you have to close your eyes… when you open \nthem you know what comes next is something only a bark can describe.\n')
elif x != 1 and y == 2:
    print('The voice tells you it is a good choice, but you are not quite ready yet to join the order. You \nfeel ashamed and nervous now, but the voice reassures you that in order to face the dark ones, there can be \nno hesitating and no fear before doing what needs to be done. You are capable of being such a dog, but just a \nlittle more time is needed, instead you are to go back to earth as a new pup, perhaps a',sec_breed,'to \nrefine your bark and strengthen your nerves. You’ll be a good dog, the voice assures you and you feel a scratching \non your head so good you can’t help but close your eyes, when you open them again, the face of a young \nboy with a hug smile is greeting you.\n')
else:
    print('Choosing to stay, the voice senses your decision, “You’ve done a good service on Earth.”, says the \nvoice. “The young ones here need you to teach them to stay, to bark, to comfort and bring joy, to wag their \ntails, and to howl, because howling is a secret language that encourages the Knights of the Order and gives \nthem strength to face the darkness.” You look down and at your paws is the smallest',sec_breed,'you’ve \never seen, feebly moving its tail up, down, and sideways, scenting in the fresh air and seeing the golden sky. \nYou inhale deeply before giving your new pup its first lesson on how to be a proper dog.\n')
print("The connection breaks as our friend takes their rightful place in the universe. \nRemember that a dog's journey never really ends, anymore than our own journeys. \nIt's the choices that takes us along the path, so be careful with your own.\n" )
print('Are you ready to continue your journey?')
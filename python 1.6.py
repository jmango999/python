import webbrowser as wb
import pyautogui as pg
name=pg.prompt("What is your name")
points=0
show= pg.prompt("What is your favorite TV show?")

if show == "Hannah Montana":
    pg.alert ("OMG LOL xD")
    points+= 250
    wb.open('https://www.youtube.com/watch?v=uVjRe8QXFHY')
elif show == "Gossip Girl":
    wb.open('https://www.youtube.com/watch?v=ofm4Ag-HprM')
    pg.alert("Love that")

elif show == "greys anatomy":
    pg.alert("Great show!")
    wb.open ('https://www.google.com/search?rlz=1C1GCEA_enUS751US751&q=grey%27s+anatomy&spell=1&sa=X&ved=0ahUKEwjh7djrnZ_eAhXmmOAKHXznBoIQBQgpKAA&biw=1342&bih=616')
elif show == " Friends":
    pg.alert == (" no one told me life was going to be this way!" )
    wb.open('https://www.google.com/search?q=friends&rlz=1C1GCEA_enUS751US751&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjH0Z_wnp_eAhVGhuAKHU5LCmcQ_AUIDygC&biw=1342&bih=616#imgrc=nqAZ54yPmImSQM:')
elif show == " Riverdale":
    pg.alert("that show is great")
    wb.open ('https://www.google.com/search?q=riverdale&rlz=1C1GCEA_enUS751US751&oq=riverdale&aqs=chrome..69i57j0l5.1605j0j7&sourceid=chrome&ie=UTF-8')
elif show == " the office" :
    pg.alert(" Love that show! ")
    wb.open ()
    pg.alert(" Your favorite show is " + str(show))
else:
    pg.alert("your favorite show is " + str(show))
        



dessert= input (" What is your favorite dessert?")

if dessert == "Cookies":
    pg.alert ("I love cookies")
    points+= 250
    wb.open('https://www.google.com/search?q=cookies&rlz=1C1GCEA_enUS751US751&source=lnms&tbm=isch&sa=X&ved=0ahUKEwjVxe3c57DeAhXiRd8KHVe_D2kQ_AUIDigB&biw=1366&bih=626')
elif dessert == "Nuts":
     pg.alert("I'm allergic")

elif dessert == "Cake":
    pg.alert("Funfetti is the best")
    wb.open ('https://www.google.com/search?q=funfetti+cake&rlz=1C1GCEA_enUS751US751&source=lnms&tbm=isch&sa=X&ved=0ahUKEwiIo_ie6LDeAhUFheAKHUPHA8EQ_AUIDigB&biw=1366&bih=626#imgrc=dUt95rBHur0DVM:')
elif dessert == "Cupcakes":
    pg.alert == (" I love cupcakes" )
    wb.open('https://www.google.com/imgres?imgurl=https://truffle-assets.imgix.net/c8f35591-funfetti-freakshake-cupcakes-pc.jpg&imgrefurl=https://www.tastemade.com/videos/freakfetti-cupcakes&h=1920&w=1080&tbnid=YI2kCJRveEopoM:&q=cupcakes&tbnh=186&tbnw=104&usg=AI4_-kRzU-nkx6Dcxrsni3NR0KYMCCy0pw&vet=12ahUKEwitmYLX6LDeAhVkZN8KHYayAmgQ_B0wGnoECAUQBg..i&docid=12VajQhlVjrStM&itg=1&sa=X&ved=2ahUKEwitmYLX6LDeAhVkZN8KHYayAmgQ_B0wGnoECAUQBg')
elif dessert == " Brownies":
    pg.alert(" I don't like them ")
elif dessert == " Smore brownies" :
    pg.alert(" So good!")
  
    pg.alert(" Your favorite dessert is " + dessert)
else:
    pg.alert("your favorite dessert is " + dessert)
           

animal= input ("What is your favorite animal?")
if animal == "horses":
    pg.alert ("I also like horses")
    wb.open('https://greenwichfreepress.com/wp-content/uploads/2018/05/KFHS2018-046-771x1157.jpeg')

elif rider  == "Mclain Ward":
    wb.open('https://www.youtube.com/watch?v=ib5uqG-aTDE')
    pg.alert( " I like dogs too!")
else:
    pg.alert (" Your favorite animal is " + animal)
rider= input ("Who is your favorite rider?")
if rider == "Mclain Ward":
    pg.alert ("I love Mclain Ward!")
    wb.open('https://www.youtube.com/watch?v=ib5uqG-aTDE')
else:
    pg.alert("your favorite aniaml is " + animal)



games= input (" What is your favorite games?")

if games == "Fortnite":
    pg.alert ("The popular one")
    points+= 250
    wb.open('https://www.google.com/search?q=fortnite&rlz=1C1GCEA_enUS751US751&oq=fortnite&aqs=chrome..69i57j0l5.2777j0j9&sourceid=chrome&ie=UTF-8')
elif games == "Monopoly":
     pg.alert(" Ilove that game")

elif games == "Jenga":
    pg.alert(" Stack them!!")
elif games == "Chopsticks":
    pg.alert == ("Do you want to play?" )
elif games ==  "Legos":
    pg.alert("I would always play those!")
elif games == "Truth or dare" :
    pg.alert(" Dare?")
  
    pg.alert(" Your favorite games is " + games)
else:
    pg.alert("your favorite game is " + games)

ice_cream = pg.confirm("Which one of these flavors is your favorite?", "Choose one", ["chocolate", "cookie dough", "bluemonster","vanilla"])


    

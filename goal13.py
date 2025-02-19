import random  #import random
app.setMaxShapeCount(10000000000)  #max shapes set

#total amount of greenhouse gases (we want lower number)
app.greenhouse_gases = 1000   


#MAIN-GAME LOOP
def start_game():
    Label("Welcome To The Climate Action Game!", 200, 100, size = 20, bold = True)
    Label("In this game, you can gather materials", 200,150, size = 20, bold = True)
    Label("and build projects to reduce your total", 200,175,size = 20, bold = True)
    Label("amount of greenhouse", 200,200,size = 20, bold = True)
    Label("gases and help fight climate change!", 200,225, size = 20, bold = True)
    Label("Your goal is to create a sustainable,", 200,280, size = 20, bold = True)
    Label('low-carbon environment!', 200,305, size = 20, bold = True)
    Label('Press Space To Continue', 200, 355, size = 20, bold = True)
    

#Background for start
Earth = Group(
    Circle(200, 700, 550, fill='white'),
    Circle(200, -300, 550, fill='white'),
    Rect(0,0,400,400,fill = 'darkGreen'),
    Label('1',50,75,fill = 'white', bold = True, font = 'Museo Sans', size = 100),
    Label('3',95,75,fill = 'white', bold = True, font = 'Museo Sans', size = 100),
    Label('CLIMATE', 225,55,fill = 'white', bold = True, font = 'Museo Sans', size = 35),
    Label('ACTION', 215,90,fill = 'white', bold = True, font = 'Museo Sans', size = 35),
    Oval(200,250,301,201,fill = 'white'),
    Line(25,250,80,305,fill = 'white', lineWidth = 10),
    Line(25,255,80,195,fill = 'white', lineWidth = 10),
    Oval(80,250,100,50,fill = 'white'),
    Line(375,250,320,305,fill = 'white', lineWidth = 10),
    Line(375,255,320,195, fill = 'white', lineWidth = 10),
    Oval(320,250,100,50,fill = 'white'),
    Circle(200,250,80,fill = 'green'),
    Polygon(175,175,150,225,155,240,178,270,155,290,180,280,190,285,200,250,225,225,225,190,245,182, fill = 'white'),
    Oval(200,183,57,30,fill = 'white'),
    Oval(225,170,60,30,fill = 'white'),
    Polygon(155,330,190,295,215,285,235,260,275,250,320,250,320,305,fill = 'white'),
    Oval(200,310,50,10,fill = 'white'),
    Oval(230,320,120,30,fill = 'white'),
    Circle(200,250,80,fill = None, border  = 'black', borderWidth = 0.25),
    Label('Press Space To Skip To The Game', 200, 365, size = 20, bold = True, fill = 'white')
    )
#starting stuff
Starting = Rect(125,200,150,75, fill = 'blue')
Text = Label('START!', 200,237.5, size = 40)
Background = Rect(0,0,400,400, fill = 'cyan')
Background.visible = False



#mouse move - opacity change
def onMouseMove(mouseX, mouseY):
    if Starting.contains(mouseX, mouseY):
        Starting.opacity = 80
        Text.opacity = 80
    else:       #opacity
        Starting.opacity = 100
        Text.opacity = 100


 #when mouse hits 'start'       
def onMousePress(mouseX, mouseY):
    if Starting.hits(mouseX, mouseY):
        Background.visible = True
        Starting.visible = False
        Text.visible = False
        Earth.clear()
        start_game()

        

#materials the player has AKA resources
materials = {
    'solar_panels': 0,
    'recycled_plastic': 0,
    'renewable_wood': 0,
    'wind_turbines': 0,
    'trees': 0
}

#projects that the player can build with materials
projects = {
    'solar_farm': {
        'solar_panels': 10,
        'recycled_plastic': 5
    },
    'wind_turbine_farm': {
        'wind_turbines': 5,
        'renewable_wood': 3
    },
    'carbon_capturer': {
        'renewable_wood': 4,
        'recycled_plastic': 2
    },
    'reforestation': {
        'trees': 10,
        'renewable_wood': 2
    }
}

#key presses - different options
def onKeyPress(key):
    if 'space' in key:
        Rect(0,0,400,400,fill = 'cyan')
        game()
        Earth.clear()
    if '1' in key:
        Rect(0,0,400,400,fill = 'cyan')
        gather_materials()
        Earth.clear()
        Label('Press Space to Go Back', 300,75, bold = True, size = 15, fill = 'green')
        Label('Press One To Keep', 315, 150, bold = True, size = 15, fill = 'green')
        Label('Gathering Materials', 315, 175, bold = True, size = 15, fill = 'green')
    if '2' in key:
        Rect(0,0,400,400,fill = 'cyan')
        build_project()
        Earth.clear()
    if '3' in key:
        Rect(0,0,400,400,fill = 'cyan')
        Label("Thank You For Playing!", 200,150, size = 30,bold = True)
        Label("Keep Working On Fighting", 200,200,size = 30, bold = True)
        Label("Climate Change!", 200,250,size = 30,bold = True)
        Earth.clear()
        app.stop()
        
#game - main screen
def game():  
        Label(f"{app.greenhouse_gases}: Current Amount Of Greenhouse Gases", 175,30, size = 15, bold = True)
        Label("Options:", 100,75, size = 25, bold = True)
        OptionOne = Label("1. Gather Materials", 100,125, size = 20,bold = True)
        OptionTwo = Label("2. Build A Climate Action Project", 165,175, size = 20,bold = True)
        OptionThree = Label("3. Exit Game", 70,225, size = 20,bold = True)
        Label('Press One to Gather Materials', 165, 275,size = 15, bold = True, fill = 'green')
        Label('Press Two to Build A Project', 165, 300,size = 15, bold = True, fill = 'green')
        Label('Press Three to Exit Game', 165, 325, size = 15, bold = True, fill = 'green')


    #function to gather materials (set to random)
def gather_materials():
    gathered_solar_panels = random.randint(0,2)
    gathered_recycled_plastic = random.randint(0,3)
    gathered_renewable_wood = random.randint(0,3)
    gathered_wind_turbines = random.randint(0,1)
    gathered_trees = random.randint(0,2)
    
    #update materials after gathering and collecting
    materials['solar_panels'] += gathered_solar_panels
    materials['recycled_plastic'] += gathered_recycled_plastic
    materials['renewable_wood'] += gathered_renewable_wood
    materials['wind_turbines'] += gathered_wind_turbines
    materials['trees'] += gathered_trees
    
    #show gathered materials
    Label("You Gathered:", 125,75, size = 20, bold = True)
    if gathered_solar_panels >= 0:
        Label(f"{gathered_solar_panels} Solar Panels", 135,125, size = 20, bold = True)
    if gathered_recycled_plastic >= 0:
        Label(f'{gathered_recycled_plastic} Recycled Plastic', 135,150, size = 20, bold = True)
    if gathered_renewable_wood >= 0:
        Label(f'{gathered_renewable_wood} Renewable Wood', 135,175, size = 20, bold = True)
    if gathered_wind_turbines >= 0:
        Label(f'{gathered_wind_turbines} Wind Turbines', 135,200, size = 20, bold = True)
    if gathered_trees >= 0:
        Label(f'{gathered_trees} Trees', 135,225, size = 20, bold = True)
    
    Label("Current Materials After Gathering:", 165,260, size = 20, bold = True)
    show_materials()     #show updated materials
    
    
#function to show materials
def show_materials():
    y_position = 300
    for material, amount in materials.items():
        Label(f"{material}: {amount}", 135, y_position, size = 15, bold = True)
        y_position += 15


#feedback for projects
def evaluate_project(project_type):
    
    Label(f"{project_type} has been completed!", 200, 50, size = 15, bold = True, fill = 'green')
    #projects
    if project_type == 'solar_farm':
        app.greenhouse_gases -= 150
    elif project_type == 'wind_turbine_farm':
        app.greenhouse_gases -= 100
    elif project_type == 'carbon_capturer':
        app.greenhouse_gases -= 200
    elif project_type == 'reforestation':
        app.greenhouse_gases -= 50
    #show updated greehouse gas total amount
    Label(f"{app.greenhouse_gases}: Current Total Amount Of Greenhouse Gas", 200, 150, size = 15, bold = True)
    #WIN CHECK 
    if (app.greenhouse_gases <= 0):
        Rect(0,0,400,400,fill = 'green')
        Label('YOU WIN!', 200,200,fill = gradient('green', 'blue', 'purple'), size = 75, bold = True)
        app.stop



#Function to build projects
def build_project():
    Label('Press 2 to buy something!', 295,200,bold = True, fill = 'green', size = 15)
    Label('Solar farm', 80, 195, size = 20, bold = True)
    Label('Wind turbine farm', 100, 215,size = 20,bold = True)
    Label('Carbon capturer', 100,235, size = 20,bold = True)
    Label('Reforestation', 90,255,size = 20,bold = True)
    Label("Available Projects To Fight Climate Change:", 194,100, size = 18, bold = True)
    #ask user for what project they want to build
    choice = app.getTextInput("Which Project Would You Like To Build? ").strip().lower().replace(' ', '_')
    
    if choice not in projects:
        Label("Invalid Choice. Please Choose A Valid Project To Build.", 200,350, size = 15, bold = True, fill= 'red')
        return
    
    #check if sufficient materials
    can_build = True
    
    for material, amount_needed in projects[choice].items():
        if materials[material] < amount_needed:
            Label(f"Not Enough {material} To Build This Project.", 200,340, size = 15, bold = True, fill = 'crimson')
            can_build = False
            break
    if can_build:
        #deduct amount of materials needed to build project
        for material, amount_needed in projects[choice].items():
            materials[material] -= amount_needed
        evaluate_project(choice)  #evaluate impact to climate change
    else:
        Label("You Don't Have Enough Materials To Build This Project.", 200,365, fill = 'red')


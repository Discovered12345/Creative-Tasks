app.curent_question = False
app.score = 0
app.game_over = False
app.game_won = False
app.start_game = False

#questions
sdg_questions = [
    {"number": 1, "question": "What is SDG Goal 1?", "options": ["No Poverty", "Zero Hunger"], "answer": "No Poverty"},
    {"number": 2, "question": "What is SDG Goal 2?", "options": ["Clean Water", "Zero Hunger"], "answer": "Zero Hunger"},
    {"number": 3, "question": "What is SDG Goal 3?", "options": ["Quality Education", "Good Health"], "answer": "Good Health"},
    {"number": 4, "question": "What is SDG Goal 4?", "options": ["Quality Education", "Clean Water"], "answer": "Quality Education"},
    {"number": 5, "question": "What is SDG Goal 5?", "options": ["Clean Water", "Gender Equality"], "answer": "Gender Equality"},
    {"number": 6, "question": "What is SDG Goal 6?", "options": ["Clean Water", "Zero Hunger"], "answer": "Clean Water"},
    {"number": 7, "question": "What is SDG Goal 7?", "options": ["Clean Energy", "Quality Education"], "answer": "Clean Energy"},
    {"number": 8, "question": "What is SDG Goal 8?", "options": ["Decent Work", "Good Health"], "answer": "Decent Work"},
    {"number": 9, "question": "What is SDG Goal 9?", "options": ["Industry Innovation", "Reduced Inequalities"], "answer": "Industry Innovation"},
    {"number": 10, "question": "What is SDG Goal 10?", "options": ["Gender Equality", "Reduced Inequalities"], "answer": "Reduced Inequalities"},
    {"number": 11, "question": "What is SDG Goal 11?", "options": ["Sustainable Cities", "Life on Land"], "answer": "Sustainable Cities"},
    {"number": 12, "question": "What is SDG Goal 12?", "options": ["Climate Action", "Responsible Consumption"], "answer": "Responsible Consumption"},
    {"number": 13, "question": "What is SDG Goal 13?", "options": ["Climate Action", "Clean Water"], "answer": "Climate Action"},
    {"number": 14, "question": "What is SDG Goal 14?", "options": ["Quality Education", "Life below Water"], "answer": "Life below Water"},
    {"number": 15, "question": "What is SDG Goal 15?", "options": ["Decent Work", "Life on Land"], "answer": "Life on Land"},
    {"number": 16, "question": "What is SDG Goal 16?", "options": ["Peace and Justice", "Reduced Inequalities"], "answer": "Peace and Justice"},
    {"number": 17, "question": "What is SDG Goal 17?", "options": ["Gender Equality", "Partnerships"], "answer": "Partnerships"},

    ]
    
#courtroom
courtroom = Group(
    Rect(0,0,400,400,fill = rgb(173,216,230)),
    Rect(0,300,400,100,fill = rgb(139,69,19)),
    Rect(100,200,200,50,fill = rgb(101,67,33)),
    Rect(50,50,300,150,fill = rgb(101,67,33)),
    Line(60,60,340,60,fill = rgb(139,69,19), lineWidth = 5),
    Line(60,190,340,190,fill = rgb(139,69,19), lineWidth = 5),
    Line(60,60,60,190,fill = rgb(139,69,19), lineWidth = 5),
    Line(340,60,340,190,fill = rgb(139,69,19), lineWidth = 5),
    Label("Courtroom", 200,20,size = 30,bold = True)
)
#judge
judge = Group(
    Circle(200,150,20,fill = 'tan'),
    Rect(180,170,40,60, fill = 'black', border = 'black', borderWidth = 3),
    Line(180,190,160,210,fill = 'black', lineWidth = 5),
    Line(220,190,240,210,fill = 'black', lineWidth = 5),
    Circle(160,210,5,fill = 'tan'),
    Circle(240,210,5,fill = 'tan'),
    Line(240,210,260,190,fill = 'brown', lineWidth = 5),
    Polygon(255,180,265,180,265,200,255,200,fill = 'brown')
)
#user
user = Group(
    Circle(200,350,20,fill = 'tan'),
    Rect(180,370,40,60,fill = 'blue', border = 'blue', borderWidth = 3),
    Line(180,390,160,410,fill = 'tan', lineWidth = 5),
    Line(220,390,240,410,fill = 'tan', lineWidth = 5),
    Circle(160,410,5,fill = 'tan'),
    Circle(240,410,5,fill = 'tan'),
    Rect(180,370,40,22,fill = 'brown', border = 'black'),
    Rect(190,390,20,20,fill = 'brown', border = 'black')
)
#audience
audience = Group(
    Rect(85,110,30,40,fill = 'red', border = 'red', borderWidth = 3),
    Circle(100,100,15,fill = 'tan'),
    Rect(135,110,30,40,fill = 'green', border = 'green', borderWidth = 3),
    Circle(150,100,15,fill = 'tan'),
    Rect(235,110,30,40,fill = 'yellow', border = 'yellow', borderWidth = 3),
    Circle(250,100,15,fill = 'tan'),
    Rect(285,110,30,40,fill = 'purple', border = 'purple', borderWidth = 3),
    Circle(300,100,15,fill = 'tan')
)
#green start button
start_button = Group(
    Rect(150,180,100,40,fill = 'green'),
    Label("Start", 200,200,size = 20,fill = 'white'))

            #--- <> ---#

#boxes and score label
Option_one = Rect(25,200,150,100, fill = 'white', border = 'black', borderWidth = 7.5)
Option_one.visible = False
Option_two = Rect(225,200,150,100, fill = 'white', border = 'black', borderWidth = 7.5)
Option_two.visible = False
Question_one = Rect(125,60,150,75, fill = 'white', border = 'black', borderWidth = 7.5)
Question_one.visible = False
score_label = Label("Score: 0", 50,380,size = 16, fill = 'black')
score_label.visible = False

#function to display the questions
def display_question():
    randomQuestion = sdg_questions[randrange(1, 17)]   #generate the number that matches previous list of sdg question numbers
    question_label = Label(randomQuestion['question'], 200,95, size = 12)
    option_one_label = Label(randomQuestion['options'][0], 100,250,fill = 'black', size = 14)
    option_two_label = Label(randomQuestion['options'][1], 300,250, fill = 'black', size = 14)
    app.current_question = randomQuestion
    
#function to check the answers from the selected option that the use clicks
def check_answer(selected_option):
    if selected_option == app.current_question["answer"]:
        app.score += 1
        score_label.value = f"Score: {app.score}"
        if app.score >= 10:
            app.game_won = True
            end_game()
        else:
            Rect(25,200,150,100, fill = 'white', border = 'black', borderWidth = 7.5)
            Rect(225,200,150,100, fill = 'white', border = 'black', borderWidth = 7.5)
            Rect(125,60,150,75, fill = 'white', border = 'black', borderWidth = 7.5)
            display_question()
    else:
        app.game_over = True
        end_game()

#function to start the game
def start_game():
    courtroom.opacity = 50
    judge.opacity = 50
    user.opacity = 50
    audience.opacity = 50
    start_button.visible = False
    display_question()
    Option_one.visible = True
    Option_two.visible = True
    Question_one.visible = True
    score_label.visible = True
    
#end game (user wins or loses)
def end_game():
    if app.game_won == True:
        Rect(0,0,400,400,fill = 'green', opacity = 70)
        Label("YOU WIN!", 200,200,size = 30,fill = 'white', bold = True)
        drawConfetti()
    elif app.game_over == True:
        Rect(0,0,400,400,fill = 'red', opacity = 70)
        Label("GAME OVER", 200,200,size = 30,fill = 'black', bold = True)
        
#confetti for win animation
def drawConfetti():
    colors = ['red', 'blue', 'yellow', 'pink', 'purple', 'green']
    for i in range(200):
        x = randrange(0,400)
        y = randrange(0,400)
        size = randrange(3,7)
        color = colors[randrange(0, 6)]
        Oval(x,y,size, size, fill = color)

#mouse move
def onMouseMove(x,y):
    if start_button.contains(x,y):
        start_button.opacity = 80
    else:
        start_button.opacity = 100
        
#mouse move
def onMousePress(x,y):
    if start_button.hits(x,y):
        app.start_game = True
        start_game()
    elif app.start_game and not app.game_over and not app.game_won:
        if Option_one.hits(x,y):
            check_answer(app.current_question["options"][0])
        elif Option_two.hits(x,y):
            check_answer(app.current_question["options"][1])

















define qu = Character("คำถาม", color = "#ffff00")
define gm = Character("เกมมาสเตอร์")
define tu = Character("วิธีการเล่น")
define c = Character("ถูกต้องนะครับ!", color = "#00ff99")
define n = Character("ไม่ถูกต้องครับ", color = "#770000")


## Declaring BG Images and shit

image bg = "blackhole_re.jpg"

# Get Game question

init python:
    import json
    import os
    name = os.getcwd()
    qcount = 0
    dir = name + '\I\'nao The Quiz 2017\game\data.json'
    # os.path.expanduser('~')
    with open(dir) as dataraw:
        data = json.load(dataraw)
    print data
    dataq = data["question"]
    for q in dataq:
        qcount = qcount + 1

 
label start:
    python: 
        turncount = 0
        qno = "1"
        score1 = 0
        score2 = 0
        ## DEFINING MAIN SYS
        ## BOI
        def check(question, answer):
            ans = dataq[question]["answer"]
            teamname = team1_name if turncount % 2 == 0 else team2_name
            if answer == ans: 
                renpy.say(gm, "เป็นคำตอบที่...")
                renpy.say(c, "เยี่ยมมาก ทีม %s! คุณได้รับ %s คะแนน" % (teamname, dataq[question]["worth"]))
                if teamname == team1_name: 
                    globals()['score1'] += dataq[question]["worth"]
                else:
                    globals()['score2'] += dataq[question]["worth"]
            else:
                renpy.say(gm, "เป็นคำตอบที่...")
                renpy.say(n, "น่าเสียดาย ทีม %s!" % (teamname))
            

            


    # jump tutorial
    scene bg with fade
    ## TODO: Add image to greet players before playing.
    # "[qcount]"
    gm "ยินดัต้อนรับเข้าสู่ อิเหนา The Quiz 2017"
    gm "นี่เป็นระบบเกมอัตโนมัติ ที่คนเขียน (หัวหน้าทีม) ดันมาใช้ระบบของ Visual Novelทำซะนี่ ._."
    gm "ก่อนอื่น ขอให้ส่งตัวแทนมา 2 กลุ่ม หรือจะแบ่งกลุ่มแบ่งแยกฝั่งกันเลยก็ได้ จากนั้น ให้คลิกที่ปุ่ม พร้อมแล้ว! ได้เลย"

    menu:
        "พร้อมแล้ว! เข้าสู่ขั้นต่อไป...":
            jump ready
            
label ready:
    python:
        team1_name = renpy.input("กรุณาใส่ชื่อของทีมที่ 1 :")
        team1_name = team1_name.strip()
        team2_name = renpy.input("กรุณาใส่ชื่อของทีมที่ 2 : ")
        team2_name = team2_name.strip()

    jump tutorial
    
    
label tutorial:
    
    tu "คำถามจะมีทั้งหมด 20 คำถาม จะมีการผสมรวมกันระหว่าง ข้อช้อยส์ กับ เติมคำ"
    tu "แค่ละข้อจะมีคะแนนให้แตกต่างกันตั้งแต่ 1 - 10 คะแนน แบ่งตามลำดับความยาก"
    tu "ตัวอย่างเช่น..."

label fill(qno = "0"):
    $ que = dataq[qno]["question"]
    $ ans = renpy.input(que)
    $ check(qno, ans)

label choices(qno = "1"):
    python:
            choicearr = []
            for choice in dataq[qno]["choices"]:
                choicearr.append(dataq[qno]["choices"][choice])
        
            qno = "%s" % qno
            ques = dataq[qno]["question"]
            choice1 = choicearr[0]
            choice2 = choicearr[1]
            choice3 = choicearr[2]
            choice4 = choicearr[3]
        
    menu:
        "[ques]"
                
        "[choice1]":
            $ check(qno, choicearr[0])
        "[choice2]":
            $ check(qno, choicearr[1])
        "[choice3]":
            $ check(qno, choicearr[2])  
        "[choice4]":
            $ check(qno, choicearr[3])
        
label tets:
    c "k"
    

return

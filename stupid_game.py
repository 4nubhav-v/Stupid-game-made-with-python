print(
    "         ___    .                         +\n"
    "*  .      \  \     _ _       *        ,---------------------------,\n"
    "           \**\ ___\/ \...............|  Stupid Flying Jet Game   | .\n"
    "   .     X*######*+~\__\              `---------------------------'\n"
    "      +    o/\  \           .           *      .\n"
    "              \__\                     .                  .\n"
)
print("+++++++++++++++Welcome to My Stupid Flying Jet Game+++++++++++++++")
op1 = input(
    "Your engine's fuel is about to die, Type 'on' to ignore the warning or type 'off' to turn off the engine "
)
if op1 == "on":
    op2 = input(
        "Your jet ran out of fuel and it slowly starts to descends, Type 'par' to jump off the jet and use the parachute or Type 'Stfu' "
    )
    if op2 == "par":
        print("Congraulations You lived this ugly world again ;-)")
    else:
        print("Game Over Stupid, Your jet crashed and you f*ucking died their . . .")
elif op1 == "off":
    op3 = input("Good Choice , Now  type 'par' to open parachute")
    if op2 == "par":
        print("Congraulations You lived this ugly world again ;-)")
    else:
        print("Game Over Stupid, Your jet crashed and you f*ucking died their . . .")
else:
    print("Can't read this stupid instructions or what ? ")

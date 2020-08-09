#!python3
#pomodoro_timer.py is a simple script to set a pomodoro timer for yourself.

______ time
______ webbrowser

___ choose_time(
    print("How long would you like to set for your Pomodoro?")
    p_time = input("Please enter a time in minutes: ")
    r_ int(p_time)

___ timer(p_time
    time.sleep((p_time * 60))   
    alarm()
    
___ alarm(
    webbrowser.open("https://www.youtube.com/watch?v=vTVWGoQcn9Q")
    print("\n******** TIME UP ********\n")
    
__ __name__ __ "__main__":
    w___ True:
        p_time = choose_time()
        timer(p_time)
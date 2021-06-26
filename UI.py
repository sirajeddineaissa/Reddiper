import PySimpleGUI as sg
import run

def new_layout(i): 
    return [[sg.T("Subreddit:  "), sg.InputText(key=(i))]] 

def main():
    sg.theme("DarkAmber")
    
    column_layout = [
        [sg.T("Subreddit: "), sg.InputText(key=(0)), sg.Button(button_text="Add Subreddit", enable_events=True)]
    ]

    initial_layout = [
        [sg.Column(column_layout, key="-col-")],
        [sg.Submit(button_text="Scrape Now!"), sg.Cancel(button_text="Cancel")],
    ]
    #Load the initial layout into the main window
    window = sg.Window("Reddit Image Scraper", initial_layout)

    i = 1
    while True:
        event, values = window.read()
        #Do nothing and close the window in case the user exists or clicks on "Cancel"
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        
        elif event == "Add Subreddit":
            #Prevent adding an extra column when the user clicks on "Add Subreddit" until they fills the previous text area
            if list(values.values())[-1]:
                window.extend_layout(window["-col-"], new_layout(i))
                i += 1
        
        if event == "Scrape Now!":
            #Write the inserted subreddits into the subs.csv file and launch the run script
            f = open("subs.csv", "w")
            for str in values.values():
                f.write(str+"\n")
            f.close()
            run.main()
            window.close()

if __name__ == "__main__":
    main()
    

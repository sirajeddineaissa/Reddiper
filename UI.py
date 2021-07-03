import PySimpleGUI as sg
import run

def new_layout(i): 
    return [[sg.T("Subreddit:  "), sg.InputText(key=(i), size=(20,None)), sg.T("Max Quantity"), sg.InputText(key=(i+1), size=(5,None)), sg.T("Category"), sg.InputText(key=(i+2), size=(15,None))]] 

def main():
    sg.theme("DarkAmber")
    
    column_layout = [
        [sg.T("Subreddit:  "), sg.InputText(key=(0), size=(20,None)), sg.T("Max Quantity"), sg.InputText(key=(1), size=(5,None)), sg.T("Category"), sg.InputText(key=(2), size=(15,None))] 
    ]

    initial_layout = [
        [sg.Column(column_layout, key="-col-")],
        [sg.Submit(button_text="Scrape Now!"), sg.Button(button_text="Add Subreddit", enable_events=True), sg.Cancel(button_text="Cancel")],
    ]
    #Load the initial layout into the main window
    window = sg.Window("Reddiper", initial_layout)

    i = 3
    while True:
        event, values = window.read()
        #Do nothing and close the window in case the user exists or clicks on "Cancel"
        if event == sg.WIN_CLOSED or event == "Cancel" :
            break
        
        elif event == "Add Subreddit":
            #Prevent adding an extra column when the user clicks on "Add Subreddit" until they fill the previous text area
            if list(values.values())[-1]:
                window.extend_layout(window["-col-"], new_layout(i))
                i += 3
        
        if event == "Scrape Now!":
            #Write the inserted subreddits into the subs.csv file and launch the run script
            f = open("subs.csv", 'w')
            k = 1
            while(k <= len(values)):
                if k==len(values):
                    f.write(f"{list(values.values())[k-1]}")
                else:
                    f.write(f"{list(values.values())[k-1]},")
                if(k % 3 == 0 and k):
                   f.write("\n")
                k += 1
            f.close()
            run.main()
            window.close()
    
if __name__ == "__main__":
    main()
    

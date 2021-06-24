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
    
    window = sg.Window("Reddit Image Scraper", initial_layout)
    i = 1
    while True:
        event, values = window.read()
        if event == sg.WIN_CLOSED or event == "Cancel":
            break
        elif event == "Add Subreddit":
            if list(values.values())[-1]:
                window.extend_layout(window["-col-"], new_layout(i))
                i += 1
        
        if event == "Scrape Now!":
            
            f = open("subs.csv", "w")
            for str in values.values():
                f.write(str+"\n")
            f.close()
            run.main()
            window.close()

if __name__ == "__main__":
    main()
    

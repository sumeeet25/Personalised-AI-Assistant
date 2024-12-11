import subprocess

def open_app_or_website(query):
    query = query.lower()

    if "launch" in query:
        name_of_website = query.replace("launch", "").strip()
        if name_of_website:
            link = f"https://www.{name_of_website}.com"
            subprocess.run(["open", link])
            return f"Opening {name_of_website}..."
        else:
            return "Invalid website name."

    

    elif "open" in query or "start" in query:
        name_of_app = query.replace("open", "").replace("start", "").strip()
        if name_of_app:
            try:
                script = f'tell application "{name_of_app}" to activate'
                subprocess.run(["osascript", "-e", script])
                return f"Opening {name_of_app}..."
            except Exception as e:
                return f"Error: {e}"
        else:
            return "Invalid app name."

    else:
        return "Unknown command. Please use 'visit <website>' or 'open <app>'."

if __name__ == "__main__":
    user_input = input("Enter command: ")
    result = open_app_or_website(user_input)
    print(result)

import webbrowser
import os
import shutil

def print_header():
    columns, _ = shutil.get_terminal_size()
    with open("yt2inv.txt", 'r') as file:
        for line in file:
            line = line.rstrip('\n') # remove unneccessary crud
            print(f"{line.center(columns)}")

# print one line strings in the center with delay
def display_center_text(text):
    columns = shutil.get_terminal_size().columns
    centered_text = text.rstrip().center(columns)
    print(centered_text)

def convert_youtube_to_invidious(youtube_url):
    invidious_base_url = "https://yewtu.be"

    if "youtube.com" in youtube_url or "youtu.be" in youtube_url:
        if "watch?v=" in youtube_url:
            video_id = youtube_url.split("watch?v=")[-1]
        elif "youtu.be" in youtube_url:
            video_id = youtube_url.split("youtu.be/")[-1]
        else:
            return "Invalid YouTube URL."

        invidious_url = f"{invidious_base_url}/watch?v={video_id}"
        return invidious_url
    else:
        return "Invalid YouTube URL."

def main():
    os.system('clear')
    display_center_text("yt2inv")
    display_center_text("a youtube to invidious converter")

    history = []

    while True:
        youtube_url = input("\nEnter a YouTube link (or 'q' to quit)\nurl:").strip()

        if youtube_url.lower() in ['q', 'exit']:
            print("Exiting the program. Goodbye!")
            break
        elif youtube_url.lower() == 'history':
            print("\nConverted Links History:")
            for link in history:
                print(link)
            continue

        invidious_link = convert_youtube_to_invidious(youtube_url)

        if invidious_link != "Invalid YouTube URL.":
            history.append(invidious_link)
            print(f"Invidious Link: {invidious_link}")

            open_now = input("Do you want to open this link in your browser now? (y/n): ").strip().lower()
            if open_now == 'y':
                webbrowser.open(invidious_link)
        else:
            print("Invalid YouTube URL. Please make sure the URL is correct and try again.")

if __name__ == "__main__":
    main()

import webbrowser

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
    print("Welcome to YouTube to Invidious Link Converter!")
    print("Enter a YouTube URL to convert it to an Invidious link.")
    print("Type 'q' to quit or 'history' to view converted links.")

    history = []

    while True:
        youtube_url = input("\nEnter a YouTube link (or 'q' to quit): ").strip()

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

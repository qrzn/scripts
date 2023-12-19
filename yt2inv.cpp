#include <iostream>
#include <string>

std::string convert_youtube_to_invidious(const std::string& youtube_url) {
    const std::string invidious_base_url = "https://yewtu.be/watch?v=";
    std::size_t pos;
    std::string video_id;

    if ((pos = youtube_url.find("youtube.com")) != std::string::npos) {
        pos = youtube_url.find("watch?v=");
        if (pos != std::string::npos) {
            video_id = youtube_url.substr(pos + 8); // 8 is the length of "watch?v="
        }
    } else if ((pos = youtube_url.find("youtu.be")) != std::string::npos) {
        pos = youtube_url.find("youtu.be/");
        if (pos != std::string::npos) {
            video_id = youtube_url.substr(pos + 9); // 9 is the length of "youtu.be/"
        }
    }

    return (!video_id.empty()) ? invidious_base_url + video_id : "Invalid YouTube URL.";
}

int main() {
    std::string youtube_url, invidious_url;

    std::cout << "Welcome to YouTube to Invidious Link Converter!\n";
    std::cout << "Enter a YouTube URL to convert it to an Invidious link:\n";
    std::cout << "Type 'q' to quit.\n";

    while (true) {
        std::cout << "\nEnter a YouTube link: ";
        std::getline(std::cin, youtube_url);

        if (youtube_url == "q") {
            break;
        }

        invidious_url = convert_youtube_to_invidious(youtube_url);

        if (invidious_url != "Invalid YouTube URL.") {
            std::cout << "Invidious Link: " << invidious_url << std::endl;
            // Code to open the URL in a web browser could be added here
        } else {
            std::cout << invidious_url << std::endl;
        }
    }

    std::cout << "Exiting the program. Goodbye!\n";
    return 0;
}

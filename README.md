# YouTube Transcriber - SD Hacks 2019
YouTube Transcriber is a custom-made audio transcriber application that is capable of retrieving the full audio transcript of a YouTube video (if it has one). The YouTube video is specified with a URL provided by the user.

## Description
This transcriber implements functionality that scans the URL of a desired YouTube video and parses the file of timed text obtained from the video. The information is parsed, and the captions themselves are stored into an array of single sentences. The application also implements additional functionality that allows the user to obtain a summary of a YouTube video by providing any number of keywords. The program will then search every single sentence of the audio transcript that contains a significant number of occurrences of each keyword and of its synonyms. Each of these relevant sentences are then aggregated into a single text file in which they will be displayed as bullet points. The user can treat the bullet points as a textual synopsis of the YouTube video.

## Credits
The implementation of the prototype of YouTube Transcriber was initiated on by Andrew Wang Chen, Aaron Jaydip Shah, and Ming Wei Hung on Friday, October 25, 2019, 09:30 PM (Pacific Time), during the 2019 hackathon hosted at the Recreation, Intramural, and Athletic Complex (RIMAC Arena) at the University of California, San Diego (UCSD). The submission of the prototype application was due on Sunday, October 27, 2019, 10:00 AM (Pacific Time).

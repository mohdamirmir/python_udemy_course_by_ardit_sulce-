contents = [
    "This is the first long string content, containing detailed information about item number one in the list.",
    "Here is the second content entry, which consists of a much longer descriptive string to satisfy the requirement.",
    "Finally, this is the third and last long string in the contents list, also filled with enough words to make it suitably lengthy."
]



filenames = ["dragon_report.txt", "moon_cheese_log.txt", "summer_rain_data.txt"]

for content, filename in zip(contents,filenames):
    file = open(f"files/{filename}", "w")
    file.write(content)
    file.close()
    



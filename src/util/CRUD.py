"""
        title: "Feynman lectures on physics",
        description: "high quality up-to-date copy of Feynman's legendary lectures totallly free.",
        url: "https://www.feynmanlectures.caltech.edu/",
        img: './math2.png',
        type: TYPES[1],
        topic: TOPICS[0]
"""

def createEntry(title, description, url, img, typeOfEntry, topic):
    """
    this function create an entry for the API and print in console 
    the result.
    """
    
    print("{")
    print(f'title: {title},')
    print(f'description: {description},')
    print(f'url: {url},')
    print(f'img: {img},')
    print(f'type: {typeOfEntry},')
    print(f'topic: {topic}')
    print("}")

    
createEntry("Feynman lectures on physics", "high quality up-to-date copy of Feynman's legendary lectures totallly free.", "https://www.feynmanlectures.caltech.edu/", './math2.png', "1","2")
from bs4 import BeautifulSoup
import requests
import csv

with open("scraping/Daredevil Vol 1 (1964–1998) _ Marvel Database _ Fandom.html", "r", encoding="utf-8") as html_file:
    content = html_file.read()
    soup = BeautifulSoup(content, "lxml")
    title = soup.find_all("div", class_ = "md-volume__issue__info__link")
    story_title = soup.find_all("div", class_ = "md-volume__issue__info__story-title")
    dates = soup.find_all("div", class_ = "md-volume__issue__info__date")

    release_dates = []
    for date in dates:
        if "Release date:" in date.span.text:
            release_dates.append(date)

    with open("dd_scrape1.csv", "w", newline="", encoding="utf-8") as csv_file:

        writer = csv.writer(csv_file)

        writer.writerow(["Title", "Story Title", "Release Date", "Link"])

        for titles, story, date in zip(title, story_title, release_dates):

            writer.writerow([
                titles.a["title"].strip().replace("Vol 1 ", "#"),
                story.get_text(strip=True),
                date.get_text(strip=True).replace("Release date:", ""),
                "https://marvel.fandom.com" + titles.a["href"]
            ])
    

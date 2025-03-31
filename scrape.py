import requests
from bs4 import BeautifulSoup
from datetime import datetime, timezone

# URL to scrape
url = "https://blog.stremio.com/category/stremio-news/"
response = requests.get(url)
soup = BeautifulSoup(response.content, "html.parser")

# Start RSS structure
rss = """<?xml version="1.0" encoding="UTF-8"?>
<rss version="2.0">
  <channel>
    <title>Stremio News</title>
    <link>{}</link>
    <description>Latest news and updates from the Stremio Blog</description>
    <language>en-us</language>
    <lastBuildDate>{}</lastBuildDate>
""".format(url, datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT"))

# Find posts
posts = soup.find_all("article")

for post in posts:
    # Extract title and link
    title_element = post.find("h2", class_="entry-title")
    if title_element and title_element.find("a"):
        title = title_element.text.strip()
        link = title_element.find("a")["href"]
    else:
        continue

    # Extract description
    description_element = post.find("div", class_="entry-content").find("p") if post.find("div", class_="entry-content") else None
    description = description_element.text.strip() if description_element else "No description available."

    # Extract date
    date_element = post.find("time", class_="entry-date")
    if date_element and "datetime" in date_element.attrs:
        pub_date = datetime.strptime(date_element["datetime"], "%Y-%m-%dT%H:%M:%S%z").strftime("%a, %d %b %Y %H:%M:%S GMT")
    else:
        pub_date = datetime.now(timezone.utc).strftime("%a, %d %b %Y %H:%M:%S GMT")

    # Check for image
    image_element = post.find("img")
    image_tag = ""
    if image_element and "src" in image_element.attrs:
        image_url = image_element["src"]
        # Ensure the URL is absolute
        if not image_url.startswith("http"):
            image_url = "https://blog.stremio.com" + image_url
        # Placeholder length (RSS requires it, but we don’t have the actual size yet)
        image_length = "10000"  # Dummy value; ideally, fetch the image to get real size
        image_type = "image/jpeg"  # Assume JPEG; adjust if needed
        image_tag = f'<enclosure url="{image_url}" length="{image_length}" type="{image_type}" />'

    # Add item with image if present
    rss += f"""
    <item>
      <title>{title}</title>
      <link>{link}</link>
      <description><![CDATA[{description}]]></description>
      <pubDate>{pub_date}</pubDate>
      <guid>{link}</guid>
      {image_tag}
    </item>
    """

# Close RSS
rss += """
  </channel>
</rss>
"""

# Save as .rss file
with open("stremio_news.rss", "w", encoding="utf-8") as f:
    f.write(rss)
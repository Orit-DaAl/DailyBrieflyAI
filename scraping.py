from datetime import datetime, timedelta
import feedparser
import requests
import time
from bs4 import BeautifulSoup


def fetch_category_news(category_name, SOURCES):
    """
    Scans RSS urls for a specific category and filters for articles published within the last 12 hours.
    Performs initial cleaning by skipping promoted content and validating publication timestamps.
    """
    now = datetime.now()
    day_ago = now - timedelta(hours=12)
    articles = []
    PROMOTED_PATHS = ["/spotlight/", "/sponsored/"]


    for url in SOURCES[category_name]:
        print(f"Scanning: {url}")
        try:
            feed = feedparser.parse(url)

            for entry in feed.entries:
                link = entry.link.lower()
                if any(path in link for path in PROMOTED_PATHS):
                    continue  
                if hasattr(entry, 'published_parsed'):
                    published = datetime.fromtimestamp(time.mktime(entry.published_parsed))
                    if published > day_ago:
                        articles.append({
                            "title": entry.title,
                            "link": entry.link,
                            "source": url,
                            "published": published.strftime("%Y-%m-%d %H:%M"),
                            "summary": entry.get("summary", "")
                        })

        except Exception as e:
            print(f"Error scanning {url}: {e}")

    print(f"Total articles found: {len(articles)}")
    return articles




def fetch_article_body(url):
    """
    Extracts the main body text, title, and preview image (og:image) from a given URL.
    Strips HTML noise (scripts, nav, ads) and returns clean text capped at 2000 characters.
    """
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
    }
    
    try:
        response = requests.get(url, headers=headers, timeout=10)
        response.raise_for_status() 
        
        soup = BeautifulSoup(response.content, "html.parser")
        for tag in soup(["script", "style", "nav", "footer", "header", "aside", "form"]):
            tag.decompose() 
            
        title = soup.title.get_text(strip=True) if soup.title else "No Title"
        if soup.body:
            text = soup.body.get_text(separator="\n", strip=True)
        else:
            text = ""
            
        og_image = soup.find("meta", property="og:image")
        image_url = og_image["content"] if og_image else None

        full_content = f"TITLE: {title}\n\nCONTENT:\n{text}"       
        return full_content[:2000], image_url
        
    except Exception as e:
        return f"Error fetching {url}: {str(e)}", None

custom_css = """
.gradio-container {max-width: 850px !important; margin: auto; font-family: 'Segoe UI', sans-serif; background-color: #f7f9fc;}
.main-title {text-align: center; color: #1a202c; padding: 20px 0;}
#output-markdown { background: white; padding: 30px; border-radius: 15px; shadow: 0 4px 6px rgba(0,0,0,0.1); }
"""
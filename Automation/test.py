import webbrowser
from fuzzywuzzy import process

# Dictionary of websites
website_dict = {
    "google": "https://www.google.com",
    "youtube": "https://www.youtube.com",
    "github": "https://www.github.com",
    "facebook": "https://www.facebook.com",
    "twitter": "https://www.twitter.com",
    "linkedin": "https://www.linkedin.com",
    "instagram": "https://www.instagram.com",
    "reddit": "https://www.reddit.com",
    "wikipedia": "https://www.wikipedia.org",
    "amazon": "https://www.amazon.com",
    "netflix": "https://www.netflix.com",
    "stack overflow": "https://stackoverflow.com",
    "quora": "https://www.quora.com",
    "medium": "https://www.medium.com",
    "nytimes": "https://www.nytimes.com",
    "bbc": "https://www.bbc.com",
    "cnn": "https://www.cnn.com",
    "al jazeera": "https://www.aljazeera.com",
    "the guardian": "https://www.theguardian.com",
    "buzzfeed": "https://www.buzzfeed.com",
    "yahoo": "https://www.yahoo.com",
    "bing": "https://www.bing.com",
    "duckduckgo": "https://www.duckduckgo.com",
    "slack": "https://www.slack.com",
    "discord": "https://www.discord.com",
    "pinterest": "https://www.pinterest.com",
    "tumblr": "https://www.tumblr.com",
    "vimeo": "https://www.vimeo.com",
    "dailymotion": "https://www.dailymotion.com",
    "imgur": "https://www.imgur.com",
    "flickr": "https://www.flickr.com",
    "dropbox": "https://www.dropbox.com",
    "onedrive": "https://onedrive.live.com",
    "mega": "https://mega.nz",
    "icloud": "https://www.icloud.com",
    "spotify": "https://www.spotify.com",
    "soundcloud": "https://www.soundcloud.com",
    "apple": "https://www.apple.com",
    "microsoft": "https://www.microsoft.com",
    "adobe": "https://www.adobe.com",
    "udemy": "https://www.udemy.com",
    "coursera": "https://www.coursera.org",
    "edx": "https://www.edx.org",
    "khan academy": "https://www.khanacademy.org",
    "udacity": "https://www.udacity.com",
    "futurelearn": "https://www.futurelearn.com",
    "linkedin learning": "https://www.linkedin.com/learning",
    "pluralsight": "https://www.pluralsight.com",
    "codecademy": "https://www.codecademy.com",
    "freecodecamp": "https://www.freecodecamp.org",
    "hackerrank": "https://www.hackerrank.com",
    "leetcode": "https://www.leetcode.com",
    "geeks for geeks": "https://www.geeksforgeeks.org",
    "datacamp": "https://www.datacamp.com",
    "aws": "https://aws.amazon.com",
    "azure": "https://azure.microsoft.com",
    "google cloud": "https://cloud.google.com",
    "heroku": "https://www.heroku.com",
    "gitlab": "https://www.gitlab.com",
    "bitbucket": "https://bitbucket.org",
    "digitalocean": "https://www.digitalocean.com",
    "wordpress": "https://www.wordpress.com",
    "wix": "https://www.wix.com",
    "squarespace": "https://www.squarespace.com",
    "weebly": "https://www.weebly.com",
    "shopify": "https://www.shopify.com",
    "bigcommerce": "https://www.bigcommerce.com",
    "magento": "https://magento.com",
    "stripe": "https://www.stripe.com",
    "paypal": "https://www.paypal.com",
    "square": "https://squareup.com",
    "xero": "https://www.xero.com",
    "quickbooks": "https://quickbooks.intuit.com",
    "trello": "https://www.trello.com",
    "asana": "https://www.asana.com",
    "jira": "https://www.atlassian.com/software/jira",
    "notion": "https://www.notion.so",
    "monday": "https://www.monday.com",
    "airtable": "https://www.airtable.com",
    "clickup": "https://www.clickup.com",
    "todoist": "https://www.todoist.com",
    "evernote": "https://www.evernote.com",
    "google keep": "https://keep.google.com",
    "zoho": "https://www.zoho.com",
    "hubspot": "https://www.hubspot.com",
    "mailchimp": "https://www.mailchimp.com",
    "salesforce": "https://www.salesforce.com",
    "pipedrive": "https://www.pipedrive.com",
    "zendesk": "https://www.zendesk.com",
    "intercom": "https://www.intercom.com",
    "freshdesk": "https://www.freshdesk.com",
    "typeform": "https://www.typeform.com",
    "survey monkey": "https://www.surveymonkey.com",
    "google forms": "https://forms.google.com",
    "eventbrite": "https://www.eventbrite.com",
    "meetup": "https://www.meetup.com",
    "zoom": "https://www.zoom.us",
    "skype": "https://www.skype.com",
    "teams": "https://teams.microsoft.com",
    "webex": "https://www.webex.com",
    "gotomeeting": "https://www.gotomeeting.com",
    "bluejeans": "https://www.bluejeans.com",
    "join.me": "https://www.join.me",
    "google meet": "https://meet.google.com",
    "protonmail": "https://protonmail.com",
    "outlook": "https://outlook.live.com",
    "gmx": "https://www.gmx.com",
    "zoho mail": "https://www.zoho.com/mail/",
}


def find_closest_match(query, website_dict):
    # Find the closest match from the dictionary
    closest_match, score = process.extractOne(query, website_dict.keys())
    return closest_match if score > 70 else None  # Adjust the threshold as needed


def open_website(query):
    closest_match = find_closest_match(query, website_dict)
    if closest_match:
        url = website_dict[closest_match]
        print(f"Opening {closest_match}: {url}")
        webbrowser.open(url)
    else:
        print("No close match found for your query.")


# Example usage
query = input("Enter the website name to open: ")
open_website(query)

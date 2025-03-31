# Stremio RSS Feed

An automated RSS feed generator for Stremio news and updates. This repository scrapes the official Stremio blog and creates an up-to-date RSS feed that can be subscribed to with any RSS reader.

## How to Add This RSS Feed to Your RSS Reader

### Direct Link Method

To add this RSS feed to your RSS reader, use the raw GitHub URL for the RSS file:

```
https://raw.githubusercontent.com/owen-the-kid/stremio-rss-feed/main/stremio_news.rss
```

### Step-by-Step Instructions for Popular RSS Readers

#### Feedly

1. Log in to your Feedly account
2. Click on "Add Content" or the "+" button
3. Select "Add a source"
4. Paste the RSS feed URL and click "Add"

#### Inoreader

1. Log in to your Inoreader account
2. Click on "Subscribe" or the "+" button
3. Paste the RSS feed URL and click "Subscribe"

#### NewsBlur

1. Log in to your NewsBlur account
2. Click on "Add" or the "+" icon
3. Paste the RSS feed URL and click "Add"

#### Thunderbird

1. Open Mozilla Thunderbird
2. Right-click on "Feeds" in the sidebar
3. Select "Subscribe..."
4. Paste the RSS feed URL and click "Add"

#### NetNewsWire (Mac/iOS)

1. Open NetNewsWire
2. Click "File" > "New Feed Subscription..." (or press ⌘N)
3. Paste the RSS feed URL and click "Add"

## Feed Updates

This feed is automatically updated once every day using GitHub Actions. The workflow scrapes the latest content from the Stremio blog and updates the RSS file in this repository.

## Technical Details

- **Update Frequency**: Daily at midnight (UTC)
- **Content Source**: [Stremio Blog - News Category](https://blog.stremio.com/category/stremio-news/)
- **Feed Format**: Standard RSS 2.0

## Self-Hosting or Creating Your Own Version

If you want to create your own version of this RSS feed:

1. Fork this repository
2. Ensure GitHub Actions are enabled for your fork
3. The workflow will automatically run on schedule, or you can manually trigger it

## Troubleshooting

If the feed isn't updating:
- Check the Actions tab in the GitHub repository to see if the workflow is running successfully
- Ensure your RSS reader is properly refreshing the feed

## Contributing

Contributions are welcome! If you'd like to improve the scraper or add features, please submit a pull request.

## License

This project is available under the MIT License.

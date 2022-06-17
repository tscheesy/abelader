
def data_from_input(url, yt_object):
    thumbnail = yt_object.thumbnail_url
    title = yt_object.title
    description = yt_object.description
    publish_date = yt_object.publish_date
    length = str(yt_object.length)
    views = yt_object.views
    keywords = yt_object.keywords
    channel = yt_object.channel_id

    # extracting YT-Video ID from successful URL input
    try:
        video_id = url.split("=")[1]
    except:
        video_id = url.split("be/")[1]

    # extracting YT-Video ID from Youtube-Object returned by Pytube

    # function returns list of the extracted metadata & Sanitized Link e.g. the video ID as displayed in the youtube url
    return {
        "title": title,
        "description": description,
        # "publish_date": publish_date,
        "thumbnail": thumbnail,
        "length": length,
        "views": views,
        "keywords": keywords,
        "channel": channel,
        "url": url,
        "id": video_id,
        "object": str(yt_object),
    }

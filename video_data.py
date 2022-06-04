def data_from_input(url, yt_object):
    video_title = yt_object.title
    thumbnail = yt_object.thumbnail_url

    #extracting YT-Video ID from successful URL input
    try:
        video_id = url.split("=")[1]
    except:
        video_id = url.split("be/")[1]

    # function returns list of the extracted metadata & Sanitized Link e.g. the video ID as displayed in the youtube url
    return {
        "title": video_title,
        "thumbnail": thumbnail,
        "url": url,
        "video_id": video_id,
    }

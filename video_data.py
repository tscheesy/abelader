def data_from_input(url, yt_object):
    video_title = yt_object.title

    #extracting YT-Video ID from successful URL input
    try:
        video_id = url.split("=")[1]
    except:
        video_id = url.split("be/")[1]

    return video_title, video_id

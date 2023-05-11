from pytube import YouTube
defaultLink = 'https://www.youtube.com/watch?v=o4TbVaIk40Q'
def DownloadVidAndAudio(link = defaultLink, outputFilename = None):
    youtubeObject = YouTube(link)
    if outputFilename is None:
        outputFilename = 'VIDEO AND AUDIO ' + youtubeObject.streams[0].title
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    youtubeObject.download(filename=outputFilename, output_path='Downloads')
    print("Download is completed successfully")
def DownloadOnlyAudio(link = defaultLink, outputFilename = None):
    youtubeObject = YouTube(link)
    if outputFilename is None:
        outputFilename = 'AUDIO ONLY ' + youtubeObject.streams[0].title
    youtubeObject = youtubeObject.streams.filter(only_audio=True)
    youtubeObject[0].download(filename = outputFilename, output_path='Downloads')
    print("Download is completed successfully")
def DownloadOnlyVideo(link = defaultLink, outputFilename = None):
    youtubeObject = YouTube(link)
    if outputFilename is None:
        outputFilename = 'VIDEO ONLY ' + youtubeObject.streams[0].title
    elif outputFilename.split('.')[len(outputFilename.split('.'))-1] != 'mp4':
        outputFilename = outputFilename.split('.')[0] + '.mp4'
    youtubeObject = youtubeObject.streams.filter(only_video=True)
    youtubeObject[0].download(filename=outputFilename, output_path='Downloads')
    print("Download is completed successfully")
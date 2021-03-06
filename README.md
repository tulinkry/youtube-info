# Youtube video info

This utility lets you to download video information for selected video ids. The output goes to stdout and contains four columns: `id`, `title`, `publishedAt`, `viewCount` retrieved by the youtube api for every video id in the arguments.

## Installation

### Download recent release
```
curl -L 'https://github.com/tulinkry/youtube-info/releases/download/1.0.0/youtube-1.0.0.tar.gz' > youtube-latest.tar.gz
```

### Install it with python3
```
python3 -m pip install youtube-latest.tar.gz
```

## Running

You can now run the utility as a module with

```
python3 -m youtube
```

### The program usage

```
python3 -m youtube --help
Usage: __main__.py [OPTIONS] ID...

  Command line tool for querying details about youtube videos.

  <ID> ID of the video (can be repeated for more videos)

  The configuration file needs to have a youtube section with apikey in it:

  [youtube]
  apikey = xxx

Options:
  -c, --config TEXT  Configuration file with the youtube api token (by default
                     it looks in ~/.youtube.auth.cfg)
  --debug            print debugging information to stderr
  --help             Show this message and exit.
```

## Configuration

The utility needs a configuration file with an apikey for the youtube api. 
The file is by default searched at `~/.youtube.auth.cfg` or alternatively you can
set the path using the `--config` option.

The content example is:
```
[youtube]
apikey = xxx
```

You can obtain the api key at https://console.developers.google.com/apis/credentials when creating 
new projects and creating a new credentials in it.

## Uninstalling

You can uninstall the utility by doing
```
python3 -m pip uninstall youtube
```

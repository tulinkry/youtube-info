# Installation

## Download recent release
```
curl 'https://github.com/tulinkry/youtube-info/releases/download/0.0.1/youtube-0.0.1.tar.gz' > youtube-0.0.1.tar.gz
```

## Install it with python3
```
python3 -m pip install youtube-0.0.1.tar.gz
```

# Running

You can now run the utility as a module with

```
python3 -m youtube
```

## The program usage

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

# Configuration

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

# Uninstalling

You can uninstall the utility by doing
```
python3 -m pip uninstall youtube
```

# plugin.video.megacmd

Mega (stylized in uppercase as MEGA) is a cloud storage and file hosting service offered by Mega Limited, an
Auckland-based company.

This is a very minimal addon to stream videos from your MEGA account.

You need to have MEGAcmd command-line tool installed (from https://mega.nz/cmd) and must have logged into your
account via MEGAcmd before using this addon. This addon parses output from the then available `megacmd` command
which uses the webdav protocol. Based on my tests, this allows for streaming media with much faster download
speeds (3-4 MB/s limited by my ISP) than logging into MEGA via the addon itself and decrypting the files manually
or setting up a FUSE filesystem (I got 80-130 KB/s with both these).

This addon is not affiliated with MEGA or Mega Limited in any way.

## License

`The MIT License`

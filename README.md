# Blog-Note-Vim
Some simple scripts aim to make blog synchronization and notes management easier.

# Usage
1. blogSync: a script which makes blog sychronization steps of hexo easier
2. doctree: just a simple script containing 'tree ~/Documents'
3. notevim: a shell script to manage notes
# Get Started
1. Put these file in the same filefold(use `~/bin/` as example).
2. Add commands below to your `~/.profile`(change the path if needed)
```bash
export PATH=$PATH:~/bin/blogSync 
export PATH=$PATH:~/bin/doctree
export PATH=$PATH:~/bin/notevim
```
3. To use `doctree`, just execute the command `doctree`
4. To use `blogSync`, `cd` to the hexo blog filefold and just execute the command `blogSync`
5. To use `notevim`, which is the most complex one in this repository though it is simple for many 'linuxers', there are more steps:
	1. Add the note name and its dir path to the `notevimFileDir.json`. Here is an example.
		```json
		{
			"notename1":"path1",
			"notename2":"path2"
		}
		```
	2. Now you can edit the note by vim using `notevim -n notename1` instead of typing the full command of vim, which requires the full dir path. And use `notevim -l` to show all the notes defined in `notevimFileDir`.
	3. There is an additional feature for hexo blog(or you can make it custom by edit the source codes, which are annotated in detail).Use `notevim -u notename1` to synchronize the note1 in the original place and note1 in the hexo filefold,which will remove the older one and copy the other one to corresponding place.Before Using it, you need to add the hexo filefold path to the `notevimFileDir.json`, using the name `BlogDir`:
		```json
		{
			"BlogDir":"path"
		}
		```
# Postscript

They are just some exercise scripts used to practice the varibles sharement between scripts, may the fun be with you.

from fabric.api import local

def refresh():
	local('./manage.py flush --noinput')

refresh()
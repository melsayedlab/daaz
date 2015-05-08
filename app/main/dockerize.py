from docker import Client
from git import Repo
from urlparse import urlparse
import zipfile
import os
import os.path

DOCKER_SOCKET='unix://var/run/docker.sock'

def dockerize(file=None,url=None):
    basedir = "/tmp/.daaz/"
    cli = Client(version='1.15',base_url=DOCKER_SOCKET)

    if file:
        # Locate the file and decompress it
        zfile =zipfile.ZipFile(file)
        for name in zfile.namelist():
            filename = os.path.basename(name)
            dirname = basedir+"app-"+filename
            print "Decompressing " + filename
            if not os.path.exists(dirname):
                os.makedirs(dirname)
                zfile.extract(name, dirname)

  # Run a php Docker container
        container = cli.create_container(image='husseingalal/phpdkr')
        cli.start(container=container.get('Id'),  binds={
            dirname:
                {
                    'bind': '/var/www/app',
                    'ro': False
                }})
        return container.get('id')
    else:
        try:
            urlnew = urlparse(url).path
            k = urlnew.rfind('/')
            dest = urlnew[k+1:]
            dirname = basedir+"app-"+str(dest)
            Repo.clone_from(url, dirname)
            # Start the container
            container = cli.create_container(image='husseingalal/phpdkr')
            cli.start(container=container.get('Id'),  binds={
            dirname:
                {
                    'bind':'/var/www/app',
                    'ro': False
                }})
            return container.get('Id')
        except Exception, e:
            return e


from docker import Client
import zipfile
import os
import os.path

DOCKER_SOCKET='unix://var/run/docker.sock'

def dockerize(file):
  basedir = "/tmp/daaz/"
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
  cli = Client(version='1.15',base_url=DOCKER_SOCKET)
  container = cli.create_container(image='husseingalal/phpdkr')
  cli.start(container=container.get('Id'),  binds={
    dirname:
        {
            'bind': '/var/www/app',
            'ro': False
        }})
  return container.get('id')

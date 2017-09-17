from fabric.api import run, env

def runDeploy():
  print(env)
  sudo('apt-get install git')
  run('git clone git@github.com:CSester/dummy-repo2.git -b ' + env.source_commit)

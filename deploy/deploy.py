from fabric.api import run, env, sudo

def runDeploy():
  print(env)
  sudo('dnf install git -y')
  run('git clone git@github.com:CSester/dummy-repo2.git -b ' + env.source_commit)

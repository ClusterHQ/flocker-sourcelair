sourcelair-flocker
==================

Getting started with the demo web service
-----------------------------------------

## Using a SourceLair Blueprint

If you'd like to get started right away, just use the following SourceLair
Blueprint - https://www.sourcelair.com/blueprints/sourcelair/flocker-sourcelair

## Configuring the web service

1. Set up the database
Just run `./manage.py migrate` while on the `web` subdirectory to set up your
database. If you're on SourceLair, open Command Palette using
`Ctrl + Shift + P` or `Cmd` on a Mac and then run the Migrate command.

2. Point to a different cluster
If you'd like to point to a different cluster than the default one that we
have already set up, you can change the `DOCKER_HOST` setting in `settings.py`
file.

## Seeing everything in action

1. Point your browser to the `/` and register with a new account
  * If you're on SourceLair, access your public URL, accessible from the eye-like icon in the side-bar
2. You will be autimatically redirected to `/terminal/` and will see the terminal running
3. Create some files
4. Note the server that the terminal was spawned, just below it
5. Press `Ctrl + D` to close the terminal
6. Use the refresh terminal button to get a new one
7. Note the new server that was used this time
  * If it spawned in the same server as before, just repeat steps 5-7
8. Look for your files
9. They're there, waiting for you!

Cluster installation instructions
---------------------------------

Notes for installing the 5 node sourcelair cluster.

## pre-requisites

An SSH key on your local machine that allows root access to the machines in the cluster.

To test this, the following command should login with no prompts:

```bash
$ ssh root@node0.docker.gr
```

[install the flocker-cli](https://docs.clusterhq.com/en/0.3.2/indepth/installation.html#installing-flocker-cli) package on your local machine in order to be able to generate the TLS certs.

To test this installed correctly:

```bash
$ flocker-ca --version
```

[install the unofficial flocker tools](https://docs.clusterhq.com/en/1.0.1/labs/installer.html) package on your local machine which will provision Flocker for us.

To test this installed correctly:

```bash
$ flocker-volumes --help
```

## running the tools
Until the [install-zfs-with-ssh-keys](https://github.com/ClusterHQ/unofficial-flocker-tools/tree/install-zfs-with-ssh-keys) branch is merged - I have used the unofficial tools repo manually.

First - clone the tools repo and checkout the correct branch and export a variable pointing to where the python scripts live.

```bash
$ git clone https://github.com/clusterhq/unofficial-flocker-tools.git
$ cd unofficial-flocker-tools
$ git checkout install-zfs-with-ssh-keys
$ cd unofficial_flocker_tools
$ export TOOLSDIR=`pwd`
$ echo $TOOLSDIR
/Users/kai/projects/unofficial-flocker-tools/unofficial_flocker_tools
$ python $TOOLSDIR/flocker_volumes.py --help
```

## cluster.yml

This controls the cluster - it contains the list of the nodes, Flocker config and points to the SSH key we will use to access the nodes.

You should copy the `cluster.yml.sample` file into a blank `_certs` folder and run the tools.

Here is an example:

```bash
$ cd ~/projects/flocker-sourcelair
$ mkdir _certs
$ cp cluster.yml.sample _certs/cluster.yml
$ cd _certs
```

Now - edit the `cluster.yml` making sure you change the `private_key_path` to one that will be able to access the nodes.

For example - my default public key has been added to all servers and so I edited the `private_key_path` to be `/Users/kai/.ssh/id_rsa`

## manual preparation

I had to run the following commands on each of the nodes before running the tools:

```bash
$ sudo apt-get install -y software-properties-common python-software-properties linux-headers-generic build-essential
```

## running the tools

This assumes that you have exported a `$TOOLSDIR` variable pointing to the folder where the unofficial flocker tools have been cloned and the `install-zfs-with-ssh-keys` branch checked out.

Also - it assumes that `pwd` is a `_certs` folder containing a `cluster.yml`.

```bash
$ python $TOOLSDIR/install.py cluster.yml
$ python $TOOLSDIR/deploy.py cluster.yml
$ DOCKER_BINARY_URL=https://binaries.dockerproject.org/linux/amd64/docker-1.8.0-dev python $TOOLSDIR/plugin.py cluster.yml
```

## testing the installation

Once everything is installed, you can run the following commands to check that it has worked:

```bash
$ ssh root@node1.docker.gr
node1$ docker run -ti --rm -v testvol:/data --volume-driver flocker busybox sh -c "echo hello > /data/file.txt"
node1$ exit
$ ssh root@node2.docker.gr
node2$ docker run -ti --rm -v testvol:/data --volume-driver flocker busybox sh -c "cat /data/file.txt"
node2$ exit
```

This demonstrates data being written to node1 and then being read from node2 - all via a `docker run` command!

## Vagrant version for development

There is a Vagrant cluster that was used to test this setup against.  To get the cluster up and running:

```bash
$ cd vagrant
$ cp insecure_private_key /tmp/flocker-sourcelair-vagrant-private-key
$ mkdir _certs
$ cp cluster.yml.sample _certs/cluster.yml
$ vagrant up
$ cd _certs
```

Then run through the commands in the `running the tools` section.
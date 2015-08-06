sourcelair-flocker
==================

Notes for installing the 5 node sourcelair cluster.

## pre-requisites

An SSH key on your local machine that allows root access to the machines in the cluster.

To test this, the following command should login with no prompts:

```
$ ssh root@node0.docker.gr
```

[install the flocker-cli](https://docs.clusterhq.com/en/0.3.2/indepth/installation.html#installing-flocker-cli) package on your local machine in order to be able to generate the TLS certs.

To test this installed correctly:

```
$ flocker-ca --version
```

[install the unofficial flocker tools](https://docs.clusterhq.com/en/1.0.1/labs/installer.html) package on your local machine which will provision Flocker for us.

To test this installed correctly:

```
$ flocker-volumes --help
```

## running the tools
Until the `install-zfs-with-ssh-keys` branch is merged - I have used the unofficial tools repo manually.

First - clone the tools repo and checkout the correct branch and export a variable pointing to where the python scripts live.

```
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

```
$ cd ~/projects/flocker-sourcelair
$ mkdir _certs
$ cp cluster.yml.sample _certs/cluster.yml
$ cd _certs
```

Now - edit the `cluster.yml` making sure you change the `private_key_path` to one that will be able to access the nodes.

For example - my default public key has been added to all servers and so I edited the `private_key_path` to be `/Users/kai/.ssh/id_rsa`

## running the tools

This assumes that you have exported a `$TOOLSDIR` variable pointing to the folder where the unofficial flocker tools have been cloned and the `install-zfs-with-ssh-keys` branch checked out.

Also - it assumes that `pwd` is a `_certs` folder containing a `cluster.yml`.

```
$ python $TOOLSDIR/install.py cluster.yml
$ python $TOOLSDIR/deploy.py cluster.yml
$ DOCKER_BINARY_URL=https://binaries.dockerproject.org/linux/amd64/docker-1.8.0-dev python $TOOLSDIR/plugin.py cluster.yml
```

## testing with Vagrant

There is a Vagrant cluster that was used to test this setup against.  To get the cluster up and running:

```
$ cd vagrant
$ cp insecure_private_key /tmp/flocker-sourcelair-vagrant-private-key
$ mkdir _certs
$ cp cluster.yml.sample _certs/cluster.yml
$ vagrant up
$ cd _certs
```

Then run through the commands in the `running the tools` section.
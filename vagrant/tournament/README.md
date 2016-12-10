# Project: Tournament Results

## Setting Up Your Enviornment

### What You Need to Install

1. [Virtual Box](https://www.virtualbox.org/wiki/Downloads)
2. [Vagrant](https://www.vagrantup.com/)
3. [Python 2.7x](https://www.python.org/downloads/)

## After Installing / How To Run

1. Download/Clone the github repository.
2. In your terminal navigate to the downloaded repository
3. Turn on the virtual machine by typing `vagrant up`
4. Once virtual machine has been loaded log on by typing `vagrant ssh`
5. Once logged in, go to the `/vagrant/tournament` folder
6. Run psql by typing `psql`
7. Run the following sql command to create the tournament database.
    `\i tournament.sql`
8. Run the tournament_test python file. **(Make sure to do this in another terminal window/tab)**
    python tournament_test.py
